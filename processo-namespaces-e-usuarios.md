# Processo, namespaces e usuários num container

Um container não é uma máquina pequena rodando dentro de outra. É um processo comum, listado na mesma tabela de processos do kernel do host que qualquer outro processo, ao qual o kernel aplica um conjunto de restrições de visibilidade e de recursos antes de deixá-lo rodar.

Rode `docker run -d nginx` e depois `ps aux` no host: o processo nginx aparece na lista, com um PID normal do host, ao lado de qualquer outro processo do sistema, com uma entrada real no diretório proc daquele PID, incluindo a quais namespaces ele pertence e a qual cgroup está associado.

Nenhuma chamada de sistema feita dentro do container passa por um kernel diferente: é o mesmo kernel do host que atende, na mesma velocidade, com a mesma versão e os mesmos módulos carregados que qualquer outro processo do host usa.

É essa ausência de um segundo kernel que explica por que iniciar um container é quase instantâneo, e por que uma vulnerabilidade no kernel do host é, em princípio, uma superfície de ataque compartilhada por todos os containers rodando sobre ele.

A comparação completa com uma máquina virtual, que roda seu próprio kernel sobre um hypervisor, está em [máquinas virtuais e hipervisores](vms-e-hipervisores.md); a distinção essencial é só esta: container isola visão e recursos dentro de um kernel único, VM isola executando um kernel próprio sobre outro.

O que faz esse processo parecer isolado não é rodar em outro lugar, é o kernel restringir o que ele enxerga através de namespaces: dentro do seu próprio PID namespace, esse mesmo processo do host aparece como PID 1, sem visibilidade de nenhum outro processo do sistema.

O kernel Linux trata o processo com PID 1 de um namespace de forma diferente dos demais: sinais que teriam ação padrão de terminar o processo, como `SIGTERM`, são ignorados pelo PID 1 a menos que o próprio processo instale um manipulador explícito para eles, um comportamento documentado em `man 7 pid_namespaces`.

Isso explica um sintoma comum: um `docker stop` que demora o tempo total do período de graça e termina em SIGKILL, porque a aplicação nunca foi escrita para rodar como PID 1 e não implementa esse tratamento de sinal, algo que ela nunca precisaria fazer fora de um container.

É por isso que existem processos como tini ou dumb-init, usados como ENTRYPOINT de uma imagem: eles assumem o papel de PID 1 no lugar da aplicação, encaminham sinais corretamente para o processo real (que passa a rodar como PID 2, com comportamento normal de sinal) e reaproveitam processos zumbis, responsabilidade que todo PID 1 tem no Linux.

Quando o PID 1 de um namespace termina, por qualquer motivo, o kernel encerra à força, via SIGKILL, todos os demais processos que ainda existirem dentro do mesmo PID namespace; "o container parou" e "o processo principal saiu" são, na prática, a mesma coisa, porque não existe um container rodando sem o seu PID 1 ativo.

## Os oito tipos de namespace

Um namespace envolve um recurso global do kernel, como a árvore de processos, a pilha de rede ou o conjunto de pontos de montagem, de forma que os processos dentro dele enxerguem sua própria instância isolada desse recurso, sem ver nem afetar a instância que existe em outro namespace.

Namespaces respondem à pergunta "o que este processo consegue ver?"; eles não limitam quanto de CPU ou memória um processo pode consumir, isso é papel dos cgroups, cobertos em [cgroups, capabilities e isolamento de filesystem](cgroups-capabilities-e-filesystem.md).

O kernel Linux implementa oito tipos, documentados em `man 7 namespaces`: PID (a árvore de processos), Network (interfaces, rotas, regras de firewall, portas), Mount (a árvore de pontos de montagem visível ao processo), UTS (hostname e domainname), IPC (System V IPC e POSIX message queues), User (mapeamento de UID/GID, detalhado abaixo), Cgroup (a visão da própria hierarquia de cgroups) e Time (os relógios monotônico e de boot, não o relógio de parede).

Cada processo pertence a exatamente um namespace de cada tipo; por padrão, todo processo do host pertence aos namespaces raiz, criados no boot, e um container substitui a associação a um ou mais desses tipos por um namespace novo. Rede, mount e UTS são os mais imediatamente visíveis no uso comum: são eles que fazem `ip addr` mostrar interfaces diferentes do host, mount/df mostrarem um filesystem diferente, e hostname retornar um nome diferente.

Um container tipicamente cria um namespace novo para cada um dos oito tipos, mas isso não é obrigatório: `--network host` no Docker reutiliza o namespace de rede do host em vez de criar um novo, abrindo mão desse isolamento específico por um motivo pontual, como performance de rede.

Três utilitários inspecionam esse mecanismo diretamente, listados na tabela abaixo.

| Utilitário | Faz o quê |
| --- | --- |
| `lsns` | lista todos os namespaces do host, com tipo, número de processos e comando associado |
| `nsenter` | entra no namespace de um processo já em execução, emprestando as ferramentas do host |
| `unshare` | cria um processo novo já dentro de um namespace novo, sem precisar de um runtime de container |

`lsns` lê `/proc` sem exigir privilégio especial para ver os namespaces do próprio usuário, e a coluna NPROCS mostra quantos processos compartilham cada um; filtrar por tipo, como só os de rede, é uma flag comum.

`unshare` precisa da flag de criar um processo filho, porque o processo que o chama já existe fora do novo namespace, e da flag de remontar o diretório proc, sem o que ferramentas de listagem de processos continuariam lendo o proc do namespace pai.

Aplicados a um container real em vez de a uma demonstração, o procedimento é o mesmo: descobrir o PID do processo principal e usar `lsns` ou `nsenter` a partir daí, útil para diagnosticar uma imagem mínima sem ferramentas de rede instaladas.

## User namespaces: o que "root dentro do container" significa

Um user namespace mapeia um intervalo de UIDs e GIDs de dentro do namespace para um intervalo, possivelmente diferente, de UIDs e GIDs no host. Esse mapeamento decide se o UID 0 dentro de um container corresponde ao UID 0 real do host, com todos os privilégios que isso implica, ou a um UID comum, sem privilégio nenhum fora do próprio namespace.

O mapeamento é declarado em arquivos como `/etc/subuid` e `/etc/subgid`, que reservam a cada usuário do host um intervalo de UIDs/GIDs subordinados que ele tem permissão de mapear para dentro de um namespace que criar; ferramentas como newuidmap/newgidmap, ou o próprio runtime internamente, aplicam esse mapeamento.

Uma vez mapeado, um processo com UID 0 dentro do namespace é, do ponto de vista do host, apenas mais um processo rodando com o UID subordinado correspondente, sem privilégio adicional sobre nada que pertença a esse UID fora do namespace.

No modo **rootful**, tradicionalmente o padrão do Docker Engine, o daemon roda como root e um container, salvo configuração explícita em contrário, não tem nenhum user namespace remapeado: o UID 0 dentro dele é o UID 0 real do host.

Qualquer processo com acesso ao socket do Docker consegue, na prática, pedir ao daemon um container montando qualquer caminho do host e rodando como root dentro dele, o que equivale a acesso root ao host inteiro; é por isso que montar esse socket em qualquer execução automatizada é uma decisão que exige a mesma cautela de conceder acesso root direto, nunca um detalhe operacional trivial.

No modo **rootless**, o padrão do Podman, que não depende de nenhum daemon rodando como root, cada usuário cria seus próprios containers usando o próprio user namespace, com UID 0 dentro do container mapeado para um UID comum, sem privilégio, no host. Um processo que escapasse do isolamento de namespace encontraria, do outro lado, apenas os privilégios desse UID comum, não os de root, uma redução real da superfície de dano de um comprometimento bem-sucedido.

No rootful, "root dentro do container" é literalmente root, contido apenas pelo que capabilities e seccomp ainda restringem; no rootless, já nasce sem privilégio nenhum fora do próprio namespace, independentemente de qualquer capability estar habilitada, porque para o kernel do host esse UID mapeado nunca foi root de verdade. Rootless não substitui capabilities e seccomp, soma uma camada de contenção adicional e independente delas, tratadas em [cgroups, capabilities e isolamento de filesystem](cgroups-capabilities-e-filesystem.md).

`podman run --userns=keep-id --volume "$(pwd):/workspace" imagem comando` cria um user namespace de verdade, mas mapeia o UID do usuário do host especificamente para o mesmo número dentro do container, resolvendo um problema prático comum de bind mount: arquivos criados dentro do container, num diretório montado do host, ficam com o dono correto no host em vez de pertencerem a um UID subordinado estranho ao editor de código ou ao Git.

`docker run --user "$(id -u):$(id -g)" --volume "$(pwd):/workspace" imagem comando` resolve um problema parecido de um jeito mais limitado: sem `userns-remap` configurado no daemon, essa flag só escolhe qual UID o processo roda dentro do container, sem criar um namespace remapeado.

O processo não roda como root, mas o UID usado é o UID real do host no mesmo espaço de identificadores, não um UID isolado por mapeamento, e a contenção real continua vindo do daemon em si e de flags adicionais de segurança.

## Continue por aqui

[Cgroups, capabilities e isolamento de filesystem](cgroups-capabilities-e-filesystem.md) cobre os outros dois eixos de confinamento, quanto um processo pode consumir e o que ele pode fazer mesmo dentro do próprio namespace; [especificações OCI e a pilha de runtimes](especificacoes-oci-e-pilha-de-runtimes.md) mostra como esses mecanismos chegam a ser aplicados de fato, entre `docker run` e o processo confinado em execução.
