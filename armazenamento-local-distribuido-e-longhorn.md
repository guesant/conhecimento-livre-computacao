# Estratégias de armazenamento no Kubernetes

As páginas de [armazenamento local e distribuído](kubernetes/storage/local-distributed.md)
e [Longhorn](kubernetes/storage/longhorn.md) tratam cada decisão de forma
canônica. Este texto mantém somente a comparação necessária para escolher
entre elas no contexto de um cluster Kubernetes.

**Armazenamento local** vincula os dados ao disco de um nó específico: rápido,
sem rede envolvida, mas o Pod que o usa só pode ser agendado no nó que o
contém. **Armazenamento distribuído** replica os dados entre múltiplos nós e
permite reagendar o Pod enquanto houver réplicas saudáveis. Em um cluster de
nó único, não há outro nó para receber uma réplica, e a perda do host afeta os
dois modelos igualmente.

Longhorn é um sistema de armazenamento em blocos distribuído para Kubernetes, funcionando como provisionador CSI, sem depender de SAN ou storage externo dedicado. Para cada volume, cria um **engine** (um processo associado ao Pod que usa o volume) e um conjunto de **réplicas**, preferencialmente distribuídas em nós e discos diferentes; o engine escreve de forma síncrona em todas as réplicas ativas, e se uma falha, reconstrói em outro disco elegível a partir de uma réplica saudável. O **armazenamento secundário** (backupstore) é um destino externo, tipicamente compatível com S3 ou NFS, para onde o Longhorn copia backups de volumes, distinto das réplicas primárias; um backup no backupstore sobrevive à perda de todos os nós do cluster, réplicas não. Ceph oferece um modelo mais maduro e flexível (blocos, objetos e arquivos), com maior complexidade operacional; para um cluster pequeno ou de nó único, Longhorn tem curva de operação mais simples.

Um banco de dados escreve de forma muito mais sensível a latência e ordem do que a maioria das aplicações stateless: um relacional como PostgreSQL usa um log de escrita antecipada (WAL), e uma transação só é confirmada depois que sua entrada é gravada de forma síncrona em disco, então armazenamento distribuído com latência de escrita alta ou variável aumenta proporcionalmente o tempo de confirmação de cada transação. Réplicas síncronas de armazenamento e réplicas de banco de dados (streaming replication) resolvem problemas em camadas diferentes: a primeira protege o volume contra perda de disco, a segunda protege o serviço contra perda do processo ou nó primário e permite failover mais rápido; um cluster PostgreSQL gerenciado por um operator normalmente usa réplicas de banco como mecanismo primário de disponibilidade, com armazenamento distribuído como proteção adicional de durabilidade do disco. Medir a latência de escrita real do ambiente, em vez de presumir que o overhead é aceitável ou inaceitável, é o que deveria decidir entre disco local dedicado e armazenamento distribuído para um workload sensível a latência.

## Replicação não é backup

Uma réplica de armazenamento copia cada escrita em tempo real para outro disco ou nó, protegendo contra a perda física de um componente, mas não contra um erro lógico: se uma aplicação corrompe seus próprios dados, apaga um registro por engano ou é atingida por ransomware, a escrita destrutiva é replicada com a mesma velocidade e confiabilidade que qualquer outra escrita legítima, e todas as réplicas ficam corrompidas ou vazias ao mesmo tempo. Um backup, por definição, é um ponto no tempo isolado da escrita corrente; só um snapshot anterior ao erro, copiado para fora do sistema de produção, permite voltar a um estado consistente. Snapshots do próprio volume ajudam contra erros lógicos recentes, mas normalmente permanecem no mesmo storage e domínio de falha do volume original, não substituindo uma cópia externa. Essa distinção importa mais para bancos de dados e qualquer dado sujeito a erro de aplicação, bug de migração ou ataque direcionado; importa menos para dados reconstruíveis a partir de outra fonte confiável, onde a réplica já cumpre disponibilidade e a fonte externa já cumpre o papel de backup.

## Continue por aqui

[Modelo de armazenamento do Kubernetes](modelo-de-armazenamento-do-kubernetes.md) cobre PVC, StorageClass e PV, as peças que qualquer provisionador aqui descrito atende.
