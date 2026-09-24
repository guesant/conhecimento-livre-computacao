# Topologias, rede e falhas num K3s multinó

Escolher entre um cluster de nó único e um cluster multinó de verdade não é uma escala contínua: existem três arranjos distintos, cada um com uma resposta diferente para a mesma pergunta, quanto vale a alta disponibilidade do control plane frente à complexidade operacional que ela exige.

A primeira opção mantém um único servidor com um ou mais agentes. Ela distribui workloads entre vários hosts, mas o control plane continua sendo um ponto único de falha exatamente como no nó único, e a complexidade operacional adicional é mínima, essencialmente o mesmo bootstrap de sempre com agentes se juntando depois.

A segunda opção usa três servidores com etcd embarcado replicado entre eles, o mecanismo de quorum descrito em [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md). É o ponto de equilíbrio mais comum: alta disponibilidade completa do control plane com uma operação ainda relativamente simples, ao custo de coordenar backup de etcd e atualizações entre três máquinas em vez de uma.

A terceira opção desacopla o control plane de um datastore externo, Postgres ou um etcd dedicado fora do K3s. Isso permite qualquer número de servidores, sem a restrição de número ímpar que o etcd embarcado impõe, mas transfere a responsabilidade operacional de alta disponibilidade e backup para quem quer que administre esse datastore externo, uma camada operacional inteira a mais.

| Critério | Um servidor + agentes | Três servidores, etcd embarcado | N servidores, datastore externo |
| --- | --- | --- | --- |
| HA do control plane | Não | Sim | Sim |
| Complexidade operacional | Baixa | Média | Alta |
| O que fazer backup | etcd de um servidor só | etcd replicado entre servidores | o datastore externo |
| Quando faz sentido | Ambiente de teste, ou infraestrutura limitada a um host bom | Produção pequena a média, quando três máquinas decentes já existem | Produção com muitos dados, quando já existe um datastore externo gerenciado |

## Requisitos de rede entre papéis

Um cluster multinó exige portas específicas abertas entre os papéis, e confundir qual porta serve a qual comunicação é uma fonte comum de firewall mal configurado. A porta da API do Kubernetes carrega tráfego de agentes e de qualquer cliente administrativo até os servidores. As portas do consenso do etcd carregam o "peer traffic" do Raft descrito em [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md) exclusivamente entre servidores; agentes nunca precisam alcançá-las, porque não participam do consenso.

A porta do kubelet carrega comunicação entre qualquer par de nós, servidor ou agente. A porta da rede overlay carrega o tráfego VXLAN, no caso do Flannel, a implementação padrão do K3s, entre todos os nós, o mecanismo que faz Pods em hosts diferentes se enxergarem como se estivessem na mesma rede local.

Uma porta adicional só entra em cena se a rede overlay estiver configurada no modo BGP em vez do VXLAN padrão, uma escolha rara; a tabela abaixo reúne os números exatos de cada uma dessas portas.

Testar cada porta individualmente depois de configurar o firewall vale a pena, porque uma porta aberta não garante que as demais também estejam. Confirmar só a porta da API e assumir que o resto funciona é como confirmar que a porta da frente está destrancada e presumir que as janelas também estão.

## Tabela de portas

A prosa acima já nomeia cada porta no contexto de para que ela serve; a tabela reúne os mesmos valores lado a lado, para consulta rápida ao configurar um firewall.

| Porta | Protocolo | Entre quem | Finalidade |
| --- | --- | --- | --- |
| `6443` | TCP | agentes e clientes administrativos até servidores | API do Kubernetes |
| `2379`-`2380` | TCP | servidor até servidor | consenso do etcd embarcado (peer traffic) |
| `10250` | TCP | qualquer nó até qualquer nó | comunicação do kubelet |
| `8472` | UDP | qualquer nó até qualquer nó | rede overlay VXLAN (Flannel) |
| `179` | TCP | qualquer nó até qualquer nó | BGP, só se a overlay estiver nesse modo em vez de VXLAN |

## Adicionar e remover nós

Um agente se registra contra qualquer servidor existente através de duas variáveis, o endereço do servidor e o token do cluster. A instalação padrão do K3s aceita as duas como `K3S_URL` e `K3S_TOKEN` no momento em que o agente sobe pela primeira vez.

Um servidor adicional usa o par equivalente, `--server` e `--token`, descrito em [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md#bootstrap-do-quorum-do-primeiro-servidor-ao-terceiro). A diferença entre os dois papéis nesse momento de ingresso é a mesma de sempre: um entra no quorum, o outro só passa a executar workloads.

Remover um nó, servidor ou agente, segue a mesma ordem em qualquer dos dois casos: primeiro esvaziar os workloads que rodam nele, só depois apagar o registro dele na API. `kubectl cordon` impede novos Pods de serem agendados ali; `kubectl drain`, em seguida, remove os Pods existentes respeitando qualquer PodDisruptionBudget configurado.

Só depois que o drain termina sem Pods restantes é que `kubectl delete node` remove o registro. Fazer isso antes de esvaziar derruba os Pods sem controle, em vez de deixar o scheduler recriá-los em outro nó primeiro; esse comando apaga apenas o registro na API, não desinstala o K3s da máquina removida.

Se o serviço K3s continuar ativo na máquina removida, o nó tende a se re-registrar sozinho pouco depois, como se a remoção nunca tivesse acontecido. Reintroduzir um nó removido de propósito não tem atalho: ele reingressa do zero, pelo mesmo processo de um nó novo, com um token e um endereço de servidor válidos no momento do ingresso.

## Manutenção sem downtime

A técnica para atualizar ou corrigir um nó sem derrubar as aplicações que ele hospeda repete o cordon e o drain descritos acima, mas com um destino diferente ao final: em vez de apagar o registro, `kubectl uncordon` libera o nó de volta para receber Pods assim que a manutenção termina.

Três flags do drain aparecem quase sempre juntas nesse fluxo, reunidas na tabela abaixo em vez de citadas uma a uma em prosa.

| Flag | Efeito |
| --- | --- |
| `--ignore-daemonsets` | não falha por causa de Pods de DaemonSet, que não são drenáveis e continuam recriando-se sozinhos |
| `--delete-emptydir-data` | remove Pods com volumes `emptyDir` sem aviso, já que esse conteúdo não sobrevive à saída do Pod de qualquer forma |
| `--grace-period` | tempo de espera para cada Pod terminar graciosamente antes do encerramento forçado |

Drenar um agente nunca ameaça o quorum, porque agentes não participam dele; drenar um servidor, sim, ameaça, e a regra prática decorre direto da aritmética de quorum já explicada em [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md): num cluster de três servidores, só um pode estar drenado por vez, porque tirar um segundo deixaria só um sobrevivente, sem maioria nenhuma. Num cluster de cinco, dois podem ser drenados ao mesmo tempo, pela mesma conta, três sobreviventes ainda formam quorum.

## Validar que o cluster está saudável

Depois de montar um cluster multinode, o primeiro sinal a conferir é `kubectl get nodes`: todo servidor deve aparecer pronto com os papéis de control plane, e todo agente pronto sem esses papéis. Em seguida, os componentes internos do próprio Kubernetes (CoreDNS, o provisionador de armazenamento local, o servidor de métricas) devem aparecer em execução no namespace de sistema, porque um cluster com nós prontos mas componentes internos falhando ainda não está utilizável.

A verificação de quorum de verdade, porém, não vem dessa lista de nós sozinha: o status de um nó no Kubernetes e o estado do consenso Raft são reportados por mecanismos diferentes, como [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md#verificar-e-restaurar-o-quorum) detalha com o comando de listar membros do etcd.

Fechar a validação testando o agendamento de um Pod novo, e conferindo em qual nó ele caiu, confirma que o scheduler está de fato distribuindo carga entre os nós disponíveis, não só que eles existem.

## Como cada cenário de falha se comporta

O que determina a gravidade real de uma falha não é quantos nós caíram, é se os servidores sobreviventes ainda formam quorum. Perder um agente nunca afeta o quorum, porque agentes não participam do consenso Raft; o cluster continua operacional, os Pods que estavam naquele agente são recriados nos demais depois que o scheduler percebe a perda, e o tempo de indisponibilidade é o tempo de recriação mais o tempo de inicialização da própria aplicação, não mais que isso.

Perder um único servidor, num cluster de três, ainda deixa dois sobreviventes formando maioria, dois de três, então o cluster continua operacional. Se o servidor perdido era o líder do Raft no momento da falha, os dois sobreviventes elegem um líder novo entre si em questão de segundos, e a API pode ficar brevemente indisponível durante essa eleição, mas nada além disso.

Perder servidores suficientes para os sobreviventes deixarem de formar maioria, dois de três, por exemplo, é o cenário grave de verdade: o etcd para de confirmar qualquer escrita nova, então criar, atualizar ou apagar qualquer recurso passa a falhar. Pods já agendados continuam rodando normalmente, porque o kubelet não depende do etcd para manter um container já em execução; o que trava é só a criação de estado novo, não a execução do que já existia.

A única recuperação possível nesse cenário é restaurar de um snapshot de etcd feito antes da falha, com o comando descrito em [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md#verificar-e-restaurar-o-quorum). Sem um backup utilizável, a única saída é reconstruir o cluster do zero, com perda total do estado anterior; testar uma restauração de verdade, antes de precisar dela, é por isso a etapa mais importante de qualquer estratégia de recuperação.

Um datastore externo, a terceira topologia, muda o perfil de risco de um jeito específico. Como nenhum servidor guarda uma réplica local do estado, a perda desse datastore externo derruba todos os servidores ao mesmo tempo, sem quorum nenhum para absorver o golpe, porque a redundância inteira passou a depender de como esse datastore foi projetado, não mais do K3s.

Uma partição de rede que isola um servidor dos demais se comporta como uma perda de servidor do ponto de vista do quorum. O lado que ainda forma maioria continua operando normalmente; o lado isolado, mesmo com o processo continuando a rodar, fica efetivamente parado do ponto de vista do consenso, incapaz de confirmar qualquer escrita sozinho, até a partição ser reparada e a reconexão acontecer.

## Continue por aqui

[Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md) cobre o mecanismo de consenso e os três tipos de datastore que essas topologias pressupõem. [Backup do etcd, do CloudNativePG e da chave age](backup-do-etcd-cnpg-e-chave-age.md) detalha o snapshot que a recuperação de perda de quorum depende de já existir.
