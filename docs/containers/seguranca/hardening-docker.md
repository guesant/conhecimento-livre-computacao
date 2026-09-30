# Hardening de containers Docker

Hardening de Docker é a redução deliberada da superfície de ataque do host, do
daemon, das imagens, do processo do container e das conexões entre serviços.
Não é uma opção única de linha de comando. É uma composição de controles que
devem continuar válidos quando a imagem for atualizada, quando um serviço for
reimplantado e quando um operador precisar investigar um incidente.

## O limite de segurança de um container

Um container é um processo ou conjunto de processos isolados por mecanismos do
kernel. Namespaces separam visões de processos, rede, mounts e outros recursos;
cgroups limitam e contabilizam consumo; capabilities dividem privilégios que
antes pertenciam ao UID 0; seccomp filtra system calls; e um LSM, como AppArmor
ou SELinux, acrescenta regras de acesso.

Essa composição é diferente de uma máquina virtual. O container compartilha o
kernel do host e não deve ser tratado como uma fronteira suficiente entre
tenants que não confiam uns nos outros. Um processo que consiga acessar o
socket do daemon, obter capacidades perigosas, montar o filesystem do host ou
usar um dispositivo sensível pode escapar do modelo esperado sem que a imagem
tenha um binário obviamente malicioso.

O modelo de ameaça precisa declarar o que será protegido. Isolar uma API de
outros serviços no mesmo host é diferente de executar código enviado por
terceiros. O segundo cenário exige mais rigor na seleção do runtime, no kernel,
na rede, nos mounts e, em alguns casos, uma máquina virtual ou um sandbox de
kernel mais forte.

## Camadas do hardening

Uma política útil separa os controles em camadas:

| Camada | Pergunta principal | Controles relevantes |
| --- | --- | --- |
| Host | O kernel e o sistema operacional reduzem o impacto de um processo comprometido? | Patches, LSM, seccomp, namespaces, cgroups, firewall e auditoria |
| Daemon | Quem pode controlar o engine e por qual transporte? | Rootless, socket protegido, SSH, TLS, mTLS e menor privilégio |
| Imagem | O que será executado foi construído e identificado de forma confiável? | Base mínima, digest, SBOM, proveniência, assinatura e scan |
| Processo | Quais privilégios, mounts, syscalls e recursos o serviço realmente precisa? | Usuário não root, capabilities, `no-new-privileges`, filesystem somente leitura e limites |
| Rede | Quais serviços podem conversar e quais portas ficam expostas? | Redes separadas, portas mínimas, TLS, firewall e egress controlado |
| Operação | Como alterações, logs e incidentes serão controlados? | Atualização, rotação, observabilidade, limpeza, backup e resposta a incidentes |

Nenhuma dessas camadas corrige uma configuração insegura em outra. Uma imagem
assinada ainda pode ser executada com `--privileged`; um container sem
capabilities ainda pode expor todo o Docker Engine pelo socket; e um daemon
rootless ainda precisa de imagens, dependências e rede tratados com cuidado.

## Proteção do host

O host deve receber atualizações de segurança do kernel, do Docker Engine, do
runtime OCI, do sistema de arquivos e das ferramentas usadas para construir as
imagens. A superfície do host deve ser pequena: remova serviços não usados,
restrinja SSH, aplique firewall e evite executar workloads não relacionados no
mesmo usuário ou no mesmo diretório de dados.

O diretório de dados do Docker contém camadas, metadados, volumes e, em alguns
casos, credenciais operacionais. Ele deve ter permissões restritas, backup
planejado e armazenamento separado quando o impacto de preencher o disco for
relevante. Não se deve tratar `/var/lib/docker` como um diretório de troca de
arquivos entre containers.

Ative cgroups e defina limites de CPU, memória, processos e armazenamento. Um
serviço que consome toda a memória do host pode provocar uma negação de serviço
mesmo que não consiga acessar outro container. Limites não substituem
dimensionamento, mas fazem a falha de um workload ser mais contida.

AppArmor e SELinux devem ser mantidos ativos quando a distribuição os fornece.
Use perfis específicos para serviços sensíveis quando o perfil padrão não
expressar a política necessária. LSM, capabilities e seccomp cobrem dimensões
diferentes, portanto desabilitar um deles para corrigir uma incompatibilidade
deve ser uma exceção registrada, testada e temporária.

Quando o host executa workloads com níveis de confiança diferentes, separar
hosts ou usar máquinas virtuais costuma ser mais seguro do que tentar resolver
toda a diferença com flags de `docker run`. A redução de privilégios melhora a
contenção, mas não transforma um kernel compartilhado em um hypervisor.

## Docker daemon e API

O daemon tradicional do Docker executa com privilégios elevados. Por isso, o
socket Unix, normalmente `/var/run/docker.sock`, deve ser considerado uma
interface administrativa equivalente a acesso privilegiado ao host. Pertencer
ao grupo que pode escrever nesse socket não é uma permissão comum de execução
de containers.

Não monte o socket dentro de um container sem uma justificativa excepcional.
Ferramentas que precisam criar imagens ou containers devem usar um builder
isolado, uma API intermediária com escopo limitado ou uma estratégia rootless.
O padrão abaixo transforma um container em um operador do engine e deve ser
tratado como uma concessão de alto risco:

```yaml
services:
  docker-control:
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

Não exponha a API TCP sem autenticação e criptografia. Quando o controle remoto
é necessário, prefira um transporte SSH com usuários e chaves controlados ou
TLS com autenticação mútua, firewall e uma rede administrativa separada. O
endpoint deve aceitar conexões apenas de operadores e automações que realmente
precisam dele. Um certificado válido sem autorização de rede e sem controle de
identidade não resolve o problema.

Rootless Docker executa o daemon e os containers sem UID 0 no host. Ele reduz o
impacto de uma falha do daemon, mas possui requisitos e limites próprios, como
faixas de UID e GID subsidiárias, restrições de networking e incompatibilidade
com algumas operações que dependem de privilégios do kernel. `userns-remap`
mantém o daemon rootful e mapeia o root do container para um UID não privilegiado
no host. Os dois modelos não são equivalentes e devem ser escolhidos conforme o
workload e o nível de isolamento necessário.

Proteja também o acesso administrativo ao host. A combinação de SSH restrito,
MFA quando disponível, chaves protegidas, logs de auditoria, menor número de
operadores e separação entre usuários humanos e contas de automação reduz o
risco de o daemon ser usado como atalho para o host.

## Imagens e cadeia de build

Prefira imagens base pequenas, mantidas e adequadas ao workload. Uma imagem
pequena não é automaticamente segura, mas reduz pacotes, executáveis e
vulnerabilidades desnecessárias. Remova compiladores, shells auxiliares e
gerenciadores de pacotes da imagem final quando eles não forem necessários em
runtime. Use builds multi-stage para separar ferramentas de compilação do
artefato de execução.

Tags são convenientes para desenvolvimento, mas não identificam um artefato de
forma imutável. Em implantações controladas, registre a imagem pelo digest:

```text
registry.example/app@sha256:0123456789abcdef...
```

O digest deve ser resolvido, revisado e atualizado como parte do processo de
dependências. Isso não elimina a necessidade de atualizar a base. Apenas torna
explícito qual conteúdo foi aprovado.

O contexto de build deve ser mínimo e conter um `.dockerignore` revisado. Não
envie chaves SSH, diretórios `.git`, dumps, arquivos `.env`, caches ou artefatos
locais para o builder sem necessidade. `ARG` e `ENV` usados durante o build
podem acabar no histórico, nos metadados ou na inspeção da imagem. Segredos de
build devem usar os mounts de segredo ou SSH do BuildKit e não uma instrução
`COPY`, `ARG` ou `ENV`.

O pipeline deve produzir, quando aplicável:

- SBOM do artefato final e das dependências;
- proveniência que identifique o repositório, o commit e o builder;
- assinatura ou atestação verificável;
- resultado de scan de vulnerabilidades com política de severidade;
- registro do digest promovido para cada ambiente.

Verifique esses metadados antes da promoção. Um scan feito apenas na imagem
intermediária pode não encontrar pacotes adicionados no estágio final. Da mesma
forma, assinar uma tag sem verificar o digest consumido não garante que o
deploy recebeu o artefato revisado.

O processo de build deve ser reproduzível na medida possível. Fixe fontes e
versões importantes, evite scripts remotos não auditados, valide checksums e
não use `curl | sh` como mecanismo normal de instalação. Atualizações precisam
ser aplicadas continuamente, porque um digest antigo pode continuar vulnerável
mesmo quando o runtime está configurado de forma correta.

## Usuário, capabilities e privilégios

Defina um usuário não root na imagem ou no runtime. O UID e o GID devem possuir
somente as permissões necessárias sobre os diretórios usados pelo serviço. Não
confie apenas no nome `app`: o kernel aplica números de UID e GID, e um usuário
mal definido pode continuar sendo UID 0.

Comece removendo todas as capabilities e adicione somente as estritamente
necessárias:

```sh
docker run --rm \
  --cap-drop=ALL \
  --cap-add=NET_BIND_SERVICE \
  --user 65532:65532 \
  example/app@sha256:0123456789abcdef
```

`NET_BIND_SERVICE` pode ser necessário para abrir uma porta abaixo de 1024,
mas muitas aplicações podem escutar uma porta alta e evitar a capability. Não
adicione `SYS_ADMIN`, `SYS_PTRACE`, `SYS_MODULE`, `SYS_RAWIO`, `NET_ADMIN` ou
`DAC_READ_SEARCH` como tentativa genérica de corrigir erros. Cada uma pode
ampliar muito a superfície de ataque. `SYS_ADMIN`, em particular, reúne
operações que frequentemente se aproximam de privilégios administrativos.

Ative `no-new-privileges` para impedir que o processo adquira novos privilégios
por meio de set-user-ID, set-group-ID ou mecanismos equivalentes:

```sh
docker run --rm \
  --security-opt no-new-privileges=true \
  --user 65532:65532 \
  example/app@sha256:0123456789abcdef
```

Esse controle não remove privilégios que o processo já possui. Ele deve ser
combinado com capabilities reduzidas, filesystem somente leitura e um usuário
não root.

## Seccomp no Docker

Seccomp é um filtro de system calls aplicado pelo kernel. Ele não é uma lista
de arquivos permitidos, não substitui um LSM e não decide sozinho se uma
operação sobre um recurso será autorizada. O filtro pode avaliar a chamada,
seus argumentos e a ação a tomar, como permitir, retornar erro ou encerrar o
processo.

O Docker aplica um perfil seccomp padrão que funciona como uma allowlist com
ação padrão de erro. Ele bloqueia chamadas de alto risco e usa filtros de
argumentos em parte da política, preservando compatibilidade para workloads
comuns. O perfil padrão é uma boa base e não deve ser substituído por
`seccomp=unconfined` somente porque uma aplicação encontrou uma chamada
bloqueada.

Use um perfil customizado somente quando houver um motivo claro e testes que
exercitem inicialização, caminhos de erro, DNS, TLS, threads, subprocessos,
JIT, acesso a arquivos e desligamento. Perfis são sensíveis à arquitetura, ao
kernel, ao runtime e à versão da aplicação. Um perfil derivado de uma única
execução pode bloquear uma funcionalidade rara e produzir uma falha que só
aparece em produção.

Para aplicar um perfil explicitamente:

```sh
docker run --rm \
  --security-opt seccomp=/etc/docker/seccomp/app.json \
  --security-opt no-new-privileges=true \
  --cap-drop=ALL \
  example/app@sha256:0123456789abcdef
```

O perfil não deve ser usado para mascarar um processo que exige privilégios
excessivos. Primeiro investigue a syscall rejeitada e determine se a operação
é realmente necessária. Depois permita o menor conjunto possível, com filtros
por argumento quando o perfil suportar essa distinção. Se a aplicação requer
carregamento de módulo, montagem, alteração de namespaces, acesso ao kernel ou
outra operação de alto risco, a conclusão correta pode ser mudar a arquitetura
ou executar o workload em uma VM, e não liberar a syscall.

Seccomp é mais eficaz em conjunto com:

- capabilities reduzidas, para limitar o que uma syscall permitida pode fazer;
- AppArmor ou SELinux, para aplicar regras sobre objetos e operações;
- user namespaces, para evitar que UID 0 do container seja UID 0 no host;
- cgroups, para conter consumo e negação de serviço;
- filesystem e mounts mínimos, para reduzir os dados acessíveis.

O perfil pode ser desabilitado com `--security-opt seccomp=unconfined`, mas
isso deve ser uma exceção explícita, monitorada e justificada. Não coloque essa
opção em uma imagem ou Compose compartilhado para resolver incompatibilidades
sem identificar a causa.

## Filesystem, mounts e dispositivos

Use um root filesystem somente leitura quando o serviço não precisar escrever
na imagem:

```sh
docker run --rm \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  --user 65532:65532 \
  example/app@sha256:0123456789abcdef
```

Diretórios que precisam persistir devem ser volumes com finalidade definida e
permissões restritas. Mounts do host devem ser somente leitura quando possível
e devem apontar para caminhos específicos. Evite `/`, `/etc`, `/proc`, `/sys`,
`/dev` ou o diretório do daemon como bind mounts. Um mount de `/` em
`/host` pode transformar uma falha de aplicação em alteração do sistema
operacional.

Não use `--privileged` como configuração padrão. A opção altera várias
dimensões ao mesmo tempo, concede capabilities amplas, relaxa o acesso a
dispositivos e enfraquece a separação esperada. Se um serviço precisa de um
dispositivo, use `--device` para o dispositivo exato, avalie a capability
necessária e restrinja o mount.

Evite também `--pid=host`, `--network=host`, `--ipc=host`, `--uts=host` e
`--userns=host` salvo quando a necessidade for comprovada. Cada namespace do
host compartilhado expõe informações ou poderes que normalmente ficariam
isolados. Mesmo quando a opção é inevitável, compense com usuário, capabilities,
LSM, seccomp, mounts e rede mais restritos.

Reduza setuid e setgid desnecessários na imagem, mantenha ownership explícito
e não coloque segredos em camadas ou arquivos que serão copiados para a imagem
final. Acesso a `/proc` e `/sys` também pode revelar metadados sensíveis, então
o serviço deve receber apenas o que sua função requer.

## Rede

Crie redes definidas pelo usuário e separe frontend, backend, workers e banco.
Publique somente as portas necessárias e, quando o serviço for local ao host,
prefira um bind em `127.0.0.1` ou em uma interface administrativa específica.
Não use `--network=host` para evitar configurar uma porta.

Uma rede Docker não substitui autenticação nem autorização. Serviços devem usar
TLS quando trafegarem dados sensíveis, validar identidade do peer e aplicar
timeouts. Restringir a comunicação por rede reduz exposição, mas não impede
que um serviço comprometido use uma credencial válida contra outro serviço.

O egress também merece uma política. Use firewall do host, proxy ou controles
da plataforma para impedir que um workload comprometido alcance qualquer
destino da rede interna. Restrinja DNS, metadata endpoints de cloud e redes de
administração. A regra deve ser explícita para workloads que processam entrada
não confiável.

## Limites de recursos e disponibilidade

Defina limites de memória, CPU e processos para cada serviço. Um exemplo de
baseline, que precisa ser ajustado por medição, é:

```sh
docker run --rm \
  --memory=256m \
  --memory-swap=256m \
  --cpus=0.5 \
  --pids-limit=128 \
  --ulimit nofile=4096:4096 \
  example/app@sha256:0123456789abcdef
```

O limite de memória deve considerar heap, threads, buffers e bibliotecas. O
limite de PIDs reduz fork bombs, mas pode quebrar runtimes que criam muitos
workers. `ulimit` deve refletir o protocolo e o número de conexões esperadas.

Configure rotação e limite de logs para impedir que o daemon ou o filesystem
sejam consumidos. Métricas de CPU, memória, PIDs, I/O, reinícios e espaço livre
devem alimentar alertas. Health checks ajudam o orquestrador a reconhecer um
processo que não está funcional, mas não são uma fronteira de segurança e não
substituem readiness, timeouts ou circuit breakers.

## Segredos

Segredos não devem ser gravados na imagem, no histórico do Dockerfile, em
argumentos de build, em repositórios ou em arquivos de log. Durante o build,
use os mecanismos de segredo do BuildKit. Em runtime, prefira um gerenciador de
segredos ou a integração de secrets da plataforma, com escopo por serviço,
permissões mínimas e rotação.

Variáveis de ambiente são práticas, mas podem aparecer em inspeções, dumps,
diagnósticos ou processos com permissão suficiente. Para credenciais de maior
impacto, prefira arquivos temporários com ownership e mode restritos, injeção
por agente ou um cliente que obtenha credenciais de curta duração. Não monte
um diretório inteiro de credenciais quando o processo precisa de um único
arquivo.

A rotação deve invalidar o segredo anterior de forma controlada. O deploy deve
ser capaz de receber a nova credencial sem registrar seu valor e sem deixar
camadas antigas ou backups acessíveis para qualquer operador do runtime.

## Observabilidade e auditoria

Registre quem alterou o daemon, quem iniciou workloads privilegiados, quais
imagens foram executadas, qual digest estava ativo e quais containers acessaram
volumes ou dispositivos especiais. Eventos do daemon, logs do host, auditoria
do kernel e registros do pipeline devem possuir retenção compatível com o risco.

Monitore sinais de desvio de configuração:

- containers novos com `--privileged` ou capabilities perigosas;
- acesso ao socket do daemon;
- uso de `seccomp=unconfined`;
- mounts do host fora da allowlist;
- namespaces do host compartilhados;
- imagens executadas por tag mutável;
- aumento anormal de syscalls, processos, conexões ou escrita em disco;
- alterações no diretório de dados do Docker.

Logs não devem vazar tokens, cookies, chaves ou payloads sensíveis. O objetivo
da auditoria é permitir reconstruir a decisão e o impacto sem transformar a
observabilidade em outra fonte de segredos.

## Baseline de execução

O seguinte exemplo combina controles razoáveis para um serviço HTTP simples.
Ele não é universal: a aplicação pode precisar de uma porta, diretório,
capability ou syscall diferente, e cada exceção deve ser avaliada:

```sh
docker run --rm \
  --name app \
  --user 65532:65532 \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  --cap-drop=ALL \
  --security-opt no-new-privileges=true \
  --pids-limit=128 \
  --memory=256m \
  --memory-swap=256m \
  --cpus=0.5 \
  --network app-net \
  --publish 127.0.0.1:8080:8080 \
  registry.example/app@sha256:0123456789abcdef
```

O exemplo omite deliberadamente `--privileged`, o socket do Docker, o modo de
rede do host e `seccomp=unconfined`. O perfil seccomp padrão do Docker continua
ativo. Um perfil customizado só deve ser adicionado depois de testar a
aplicação e identificar quais syscalls precisam ser permitidas.

Em Compose, os mesmos princípios podem ser representados na definição do
serviço:

```yaml
services:
  app:
    image: registry.example/app@sha256:0123456789abcdef
    read_only: true
    user: "65532:65532"
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    tmpfs:
      - /tmp:rw,noexec,nosuid,nodev,size=64m
    pids_limit: 128
    mem_limit: 256m
    cpus: 0.5
    networks:
      - app
    ports:
      - 127.0.0.1:8080:8080

networks:
  app:
    driver: bridge
```

Valide a compatibilidade do Compose usado, porque nem todas as propriedades
possuem exatamente a mesma semântica em todo engine ou ambiente. Configuração
de segurança deve ser testada no mesmo runtime que executará o serviço.

## O que deve reprovar uma revisão

Os seguintes sinais exigem justificativa técnica e aprovação explícita:

| Sinal | Risco principal |
| --- | --- |
| `--privileged` | Remove várias barreiras simultaneamente |
| Socket do Docker montado | Permite controlar o daemon e normalmente o host |
| `seccomp=unconfined` | Remove o filtro padrão de system calls |
| `--cap-add` amplo | Expõe operações administrativas do kernel |
| `--pid=host` ou `--network=host` | Compartilha visão ou superfície do host |
| Bind mount de `/`, `/etc`, `/var/run` ou `/dev` | Permite observar ou alterar recursos sensíveis |
| Container root sem `no-new-privileges` | Aumenta o impacto de vulnerabilidades locais |
| Imagem apenas por tag mutável | O conteúdo executado pode mudar sem revisão |
| Segredo em `ARG`, `ENV` ou camada | Pode permanecer acessível no artefato ou diagnóstico |
| Ausência de limites | Falha de um processo pode consumir o host |

Não basta substituir esses sinais por uma configuração que passe em um scanner.
O revisor deve confirmar se a política é coerente com o processo, com o
filesystem e com a rede que ele recebe.

## Operação e resposta a incidentes

Mantenha um inventário de imagens, digests, responsáveis, volumes, redes e
permissões do daemon. Remova artefatos não usados conforme uma política de
retenção, mas não apague volumes ou dados de produção sem backup verificado e
procedimento de recuperação.

Quando houver suspeita de comprometimento, preserve logs e metadados antes de
reiniciar ou limpar o container. Identifique o digest executado, os mounts,
capabilities, namespaces, conexões, secrets acessíveis e comandos do daemon.
Depois isole a rede, revogue credenciais, substitua a imagem por um artefato
reconstruído e investigue o host. Recriar apenas o container não é suficiente
se o atacante teve acesso ao socket, ao host filesystem ou a uma credencial de
longa duração.

O CIS Docker Benchmark pode ser usado como checklist de verificação, mas uma
recomendação deve ser interpretada dentro do modelo de ameaça, da versão do
Docker e dos requisitos do serviço. Conformidade mecânica não substitui análise
de risco.

## Relação com Kubernetes

Em Kubernetes, parte desses controles é expressa no `securityContext`, em
políticas de admission, no runtime class, em NetworkPolicies, em limites de
recursos e na configuração do node. O princípio permanece o mesmo, mas o
objeto de controle muda: o administrador não deve presumir que uma opção de
`docker run` seja aplicada automaticamente pelo kubelet ou pelo runtime OCI.

Para containers Docker usados como artefatos de build ou execução local, esta
página é o ponto de partida. Para a camada do cluster, consulte [segurança do
cluster Kubernetes](../../kubernetes/index.md) e as páginas de
namespaces, capabilities, seccomp, AppArmor e NetworkPolicy relacionadas.

## Fontes primárias

- [Docker Engine security](https://docs.docker.com/engine/security/)
- [Docker seccomp profile](https://docs.docker.com/engine/security/seccomp/)
- [Docker rootless mode](https://docs.docker.com/engine/security/rootless/)
- [Protect the Docker daemon socket](https://docs.docker.com/engine/security/protect-access/)
- [Docker build best practices](https://docs.docker.com/build/building/best-practices/)
- [Docker run reference](https://docs.docker.com/reference/cli/docker/container/run/)
- [Linux seccomp filter](https://docs.kernel.org/userspace-api/seccomp_filter.html)
- [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)
- [Linux user namespaces](https://man7.org/linux/man-pages/man7/user_namespaces.7.html)
- [Linux cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)

## Continue por aqui

[seccomp](../../sistemas/linux/seccomp.md) explica o conceito de filtragem de
system calls. [Capabilities](../../sistemas/linux/capabilities.md) explica a
divisão de privilégios do kernel. [User namespaces](../../sistemas/linux/user-namespaces.md)
trata do mapeamento de identidades. [Imagem de container](../image.md) e
[OCI Runtime Specification](../oci/runtime-spec.md) explicam os artefatos e o
contrato de execução que esta política protege.
