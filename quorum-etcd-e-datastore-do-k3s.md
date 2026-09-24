# Quorum, etcd e datastore do K3s

Um quorum é um consenso entre a maioria: num grupo de N participantes, o quorum é `floor(N/2) + 1`, e nada é decidido sem ele. Servidores num cluster precisam concordar sobre o estado, qual é a configuração atual, qual Pod roda onde. Se um servidor decidisse sozinho e depois falhasse, o cluster inteiro pararia; o quorum evita isso, porque a maioria viva pode seguir decidindo mesmo com alguns servidores fora, e a minoria sincroniza de volta quando retorna.

Servidores com etcd embarcado usam Raft para chegar a esse consenso: um líder é eleito, propõe mudanças, os seguidores votam, e assim que a maioria confirma, a mudança é commitada. Com 3 servidores o quorum é 2, tolerando a perda de 1; com 5, o quorum é 3, tolerando 2. Números pares não adicionam tolerância e só gastam recurso: 2 servidores também têm quorum 2, então perder 1 já trava o cluster tanto quanto perder 1 de 1.

Perder o quorum, 2 de 3, por exemplo, trava decisões novas. O servidor isolado não consegue convencer os demais de nada, e mesmo que volte a falar com eles depois, não há garantia de que as verdades coincidam nesse meio-tempo. É por isso que perder quorum exige backup e restauração de etcd; o problema não se resolve sozinho, só com o retorno da conectividade.

Em K3s, o estado do cluster fica num datastore, com dois caminhos possíveis. **etcd embarcado** roda dentro de cada servidor, coordenando por Raft; a vantagem é não haver componente externo para operar, mas isso exige número ímpar de servidores e trava o cluster inteiro se a maioria cair ao mesmo tempo, sem outro caminho de recuperação além de restaurar um snapshot.

**Datastore externo** (PostgreSQL, MySQL, ou um etcd dedicado separado) torna os servidores K3s stateless, removendo a exigência de número ímpar e transferindo quorum e replicação para o banco externo, que tipicamente já tem sua própria estratégia de HA madura. O custo é uma segunda superfície de operação: se o datastore cai, todos os servidores K3s caem com ele, mesmo saudáveis individualmente.

**Kine** ocupa um meio-termo: um proxy que traduz a API que o K3s espera de um etcd em consultas SQL, rodando dentro de cada servidor. Isso permite usar PostgreSQL, MySQL ou até SQLite como backend; para a API Server, continua parecendo etcd, mas os dados residem num banco relacional comum, útil quando já existe um banco disponível para reaproveitar ou quando o objetivo é um ambiente leve com SQLite, um único arquivo sem processo separado.

O custo do Kine é desempenho, a sobrecarga de traduzir cada operação em SQL, já que etcd continua otimizado especificamente para a carga do Kubernetes. Um cluster já rodando etcd embarcado sem problemas não tem motivo para migrar.

Um único servidor é a escolha certa para laboratórios e ambientes onde a perda é aceitável, ou quando o orçamento não comporta as múltiplas máquinas que HA exige; fora desses casos, se a aplicação precisa rodar sem janelas de indisponibilidade, quorum deixa de ser opcional.

## Servidores, agentes e o endpoint de API

Um cluster K3s com mais de um nó distingue dois papéis: um **servidor** roda o control plane completo (API, scheduler, o datastore descrito acima) e pode agendar workloads comuns também, a menos que seja explicitamente marcado para não fazer isso. Um **agente** roda só o kubelet e o proxy de rede, executando workloads sem participar do control plane nem do quorum.

Essa distinção significa que nem todo nó adicional aumenta a tolerância a falha do control plane, só servidores adicionais fazem isso. Adicionar agentes aumenta a capacidade de executar workloads sem tocar em quorum, a forma mais simples de escalar capacidade horizontal.

Com mais de um servidor, outro problema aparece: um kubeconfig ou um agente que se junta ao cluster precisa de um único endereço de API para se conectar, mas existem vários servidores igualmente válidos para atendê-lo. Nenhum deles individualmente deveria ser tratado como o endereço permanente, porque perder justamente aquele servidor derrubaria a capacidade de qualquer cliente novo se conectar, mesmo com quorum saudável nos demais.

Um balanceador de carga na frente dos servidores resolve isso apresentando um único endereço estável, mas as duas formas mais comuns de implementá-lo têm uma diferença que importa na prática. Um DNS round-robin, um registro com múltiplos endereços A apontando para cada servidor, é a opção mais simples de configurar, sem infraestrutura adicional.

Essa simplicidade tem um custo: o DNS round-robin não tem verificação de saúde nenhuma embutida. Se um servidor cair, o DNS continua devolvendo o endereço dele como qualquer outro, e um cliente pode precisar de uma segunda tentativa contra outro endereço da lista para conseguir se conectar.

Um balanceador de carga dedicado (Nginx, HAProxy, ou um LB gerenciado de nuvem) fecha exatamente essa lacuna, monitorando a saúde de cada servidor e removendo automaticamente da rotação qualquer um que pare de responder. O custo é mais um componente próprio para manter, que por sua vez pode virar um ponto único de falha se não tiver redundância própria.

Sem algum desses dois mecanismos, a alta disponibilidade do datastore fica sem efeito prático, porque a camada de conexão continua apontando para uma máquina só.

Esse endereço de API precisa ser decidido antes da instalação do primeiro servidor, não depois. Ele não é só uma configuração de rede: é um valor gravado dentro do próprio certificado TLS que o servidor apresenta, no campo Subject Alternative Name (SAN).

O certificado só é válido para os nomes e endereços declarados nele no momento da emissão. Adicionar um endereço de API novo depois que o cluster já existe, seja por uma reinstalação de rede, seja por um balanceador de carga introduzido tardiamente, exige reemitir esse certificado incluindo o endereço novo; não é uma mudança de configuração comum.

Decidir esse endereço com folga antes do primeiro `k3s server`, mesmo sem um balanceador de carga de verdade por trás no dia da instalação, evita esse retrabalho específico. A flag `--tls-san`, detalhada na tabela da próxima seção, é o mecanismo que adiciona esses nomes e IPs extras ao certificado.

## Bootstrap do quorum: do primeiro servidor ao terceiro

O primeiro servidor de um cluster multinode não recebe nenhuma flag além da que ativa o etcd embarcado: `k3s server --cluster-init` inicia esse etcd sozinho, sem outros membros para sincronizar, e deixa o servidor pronto para aceitar ingressos futuros. Esse comando ocupa o lugar da instalação single-node no momento da inicialização, e a tabela ao final desta seção reúne as demais flags do bootstrap multinode, para não repetir cada identificador em prosa.

Depois que o primeiro servidor sobe, ele grava um token de ingresso em `/var/lib/rancher/k3s/server/node-token`, e qualquer servidor ou agente que queira entrar no cluster precisa apresentar esse token para se autenticar. Perder o arquivo não é grave enquanto esse mesmo servidor continuar de pé, já que o conteúdo pode ser lido de novo a qualquer momento; o problema só aparece se esse servidor específico for perdido antes de qualquer outro nó ter copiado o token.

Cada servidor adicional se junta apontando para o endereço de um servidor já existente e apresentando o token lido no passo anterior. Nenhuma das duas informações muda para o terceiro servidor em diante: ambos continuam apontando para o mesmo primeiro servidor, não para o último que entrou.

Não existe atalho para o estado intermediário de dois servidores. Com um só, ainda não há quorum formado; com dois, o quorum passa a exigir os dois ativos ao mesmo tempo, o que é mais frágil que o servidor único original, não mais seguro. Só a partir do terceiro servidor o cluster atinge o quorum de dois em três, capaz de tolerar a perda de qualquer um deles.

Um datastore externo dispensa esse token de servidor: em vez de `--cluster-init`, o primeiro e os demais servidores apontam para o mesmo `--datastore-endpoint`, e a autenticação entre eles passa a ser a do próprio banco, não a do K3s. Um agente nunca usa nenhuma dessas duas flags: ele se registra contra qualquer servidor existente com o mesmo token, mas nunca participa do quorum, então o número de agentes não tem restrição de paridade nenhuma.

| Flag | Papel no bootstrap |
| --- | --- |
| `--cluster-init` | ativa o etcd embarcado no primeiro servidor |
| `--server` | aponta um novo servidor para o endereço de um servidor já existente |
| `--token` | autentica o novo servidor ou agente contra o cluster existente |
| `--datastore-endpoint` | usa um datastore externo em vez de etcd embarcado |
| `--tls-san` | adiciona nomes ou IPs extras ao certificado da API, além do já discutido acima |

## Verificar e restaurar o quorum

O etcd embarcado roda dentro do próprio processo `k3s`, sem um pod separado para inspecionar com as ferramentas usuais de Kubernetes; o sinal indireto mais confiável de quorum saudável é todo servidor aparecer como pronto ao mesmo tempo, já que um servidor fora do quorum não sustenta esse estado por muito tempo. Para uma verificação direta do Raft, o binário `etcdctl`, instalado separadamente no host, conecta ao endpoint local do etcd usando os certificados que o próprio K3s já gera.

| Certificado | Caminho |
| --- | --- |
| CA | `/var/lib/rancher/k3s/server/tls/etcd/server-ca.crt` |
| Certificado de cliente | `/var/lib/rancher/k3s/server/tls/etcd/server-client.crt` |
| Chave de cliente | `/var/lib/rancher/k3s/server/tls/etcd/server-client.key` |

Com esses três arquivos e o endpoint `https://localhost:2379`, o comando `etcdctl member list` lista uma linha por servidor do control plane, com exatamente um membro marcado como líder. Um número de membros menor que o esperado indica quorum degradado mesmo que a lista de nós do Kubernetes ainda mostre todos como prontos, porque o status do nó e o estado do Raft são reportados por caminhos diferentes dentro do K3s.

Quando os sobreviventes deixam de formar maioria, a única recuperação é restaurar um snapshot de etcd anterior à falha, com `k3s server --cluster-reset --cluster-reset-restore-path=<arquivo>` executado num único servidor sobrevivente. Rodar esse comando em mais de um servidor ao mesmo tempo não acelera a recuperação, cria dois clusters diferentes a partir do mesmo snapshot, sem reconciliação automática entre eles depois; os demais servidores só devem ser reiniciados depois que o primeiro concluir o reset com sucesso.

## Continue por aqui

[k3s](k3s.md) descreve o binário único e o kubeconfig deste cluster, que roda hoje como nó único, sem a exigência de quorum tratada aqui; esse é o ponto em que os dois textos se encontram e se separam, um cobre o mecanismo geral, o outro a escolha real deste cluster.
