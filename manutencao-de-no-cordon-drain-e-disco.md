# Manutenção de nó: cordon, drain e disco

Um nó Kubernetes às vezes precisa sair de operação por um tempo sem deixar de pertencer ao cluster: reiniciar o host, aplicar uma atualização de kernel, trocar um componente físico. Kubernetes separa essa manutenção temporária em duas ações distintas, e confundi-las é o erro mais comum.

`cordon` marca o nó como `SchedulingDisabled`: nenhum Pod novo é agendado nele, mas os Pods que já estavam rodando continuam onde estão, sem interrupção.

`drain` vai além, ele evacua os Pods existentes, respeitando `PodDisruptionBudget` quando declarado, e implica um cordon como parte do processo.

A escolha entre os dois depende do que a manutenção exige: uma reinicialização do host precisa que nada esteja rodando nele, então precisa de drain; uma pausa apenas para impedir que mais carga seja agendada ali enquanto se investiga algo pode usar só cordon.

Um `drain` bem-sucedido em um cluster com vários nós é quase transparente, porque o scheduler reagenda os Pods evacuados em outro lugar antes que o usuário perceba qualquer coisa. Em um cluster de nó único essa transparência desaparece: drenar o único nó esvazia todos os workloads sem ter para onde reagendá-los, e eles ficam em `Pending` até o nó voltar e ser reintegrado.

Uma manutenção assim precisa ser tratada como indisponibilidade total planejada, não como uma operação de rotina que passa despercebida, e o motivo de valer a pena fazê-la de qualquer forma (em vez de reiniciar sem avisar o Kubernetes) é que os Pods saem de forma ordenada, respeitando o `terminationGracePeriodSeconds` de cada um, em vez de serem simplesmente mortos quando o host cai.

Terminada a manutenção, `uncordon` reabre o agendamento no nó, o que remove a marca SchedulingDisabled mas não força nada a acontecer imediatamente: o scheduler volta a considerar aquele nó como destino possível para Pods futuros, e Pods que já estavam pendentes por falta de nó tendem a ser agendados ali em pouco tempo, mas não instantaneamente e não por ação direta do uncordon.

Se isso não acontecer, a causa provável não está no cordon em si, mas em outro requisito do Pod que continua não satisfeito, como um taint residual ou uma condição de pressão de recursos ainda ativa no nó recém-reintegrado.

## Quantos nós drenar por vez, quando o control plane tem quorum

Num cluster com vários servidores de control plane (o mecanismo de quorum está descrito em [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md)), drenar um servidor para manutenção o retira temporariamente do consenso, exatamente como se ele tivesse falhado.

A regra prática decorre direto da aritmética de quorum: com três servidores, cujo quorum é dois, drenar um de cada vez é seguro, porque os dois restantes ainda formam maioria; drenar um segundo antes de reintegrar o primeiro derruba o cluster para escrita, porque sobra só um servidor vivo, minoria de três. Com cinco servidores, cujo quorum é três, é seguro drenar até dois ao mesmo tempo.

A manutenção de servidores de control plane, portanto, precisa ser sequencial, um de cada vez com reintegração confirmada antes do próximo, nunca em paralelo, ao contrário de agentes, cuja perda simultânea de vários nunca ameaça o quorum, só reduz a capacidade disponível para agendar workloads.

Dois erros de `drain` aparecem com frequência e têm causas específicas, não genéricas. Uma recusa por não haver um controlador de replicação por trás de um Pod significa que aquele Pod foi criado avulso, sem nenhum controlador (Deployment, StatefulSet ou DaemonSet) que o recrie depois; o drain recusa remover por padrão exatamente porque, sem um controlador, ninguém vai recolocá-lo em outro lugar.

Um drain que expira sem terminar normalmente indica que algum Pod não está respondendo ao período de graça dentro do tempo esperado, o que vale investigar antes de simplesmente forçar um tempo de graça menor, porque forçar esconde a causa em vez de resolvê-la.

## Pressão de disco e eviction

O disco de um nó cumpre pelo menos dois papéis que competem pelo mesmo espaço e merecem monitoramento separado: guardar as imagens de container baixadas e as camadas do runtime de containers, e, quando o nó também hospeda o datastore do cluster (como acontece num control plane que roda etcd localmente), guardar esse datastore.

Um disco cheio por um dos dois lados é frequentemente confundido com um problema no outro; verificar o consumo de cada caminho separadamente evita esse erro de atribuição.

Quando o espaço livre cai abaixo de um limiar, o kubelet reporta a condição `DiskPressure` no nó e começa a evictar Pods de prioridade mais baixa para liberar espaço, uma proteção automática contra um disco cheio travar o próprio nó.

Um nó em DiskPressure: True já está nesse estado de eviction ativa, o que é diferente de um alerta preventivo de espaço baixo, e merece tratamento de incidente e não de item de rotina para revisão depois.

O runtime de containers costuma remover imagens órfãs (sem container associado) automaticamente sob essa mesma pressão, mas depender exclusivamente dessa limpeza reativa significa operar sempre perto do limite; uma limpeza proativa e periódica de imagens não utilizadas evita chegar a esse ponto.

Um consumidor menos óbvio de espaço em disco é o log do sistema quando configurado para crescer sem limite de retenção, e snapshots do datastore acumulados sem uma política de expiração, ambos capazes de encher um disco sem que nenhum workload tenha crescido.

## Continue por aqui

[Diagnóstico de Pod, nó, certificado e Argo CD](diagnostico-de-pod-no-cluster-e-do-argocd.md) cobre o que fazer quando um nó já está `NotReady` em vez de em manutenção planejada. [Quorum, etcd e datastore do K3s](quorum-etcd-e-datastore-do-k3s.md) explica por que o datastore local de um nó é um dos dois consumidores de disco citados aqui.
