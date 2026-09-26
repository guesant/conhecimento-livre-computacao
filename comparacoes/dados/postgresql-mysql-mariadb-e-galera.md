# PostgreSQL, MySQL, MariaDB e Galera

PostgreSQL, MySQL e MariaDB são servidores de banco relacionais com mecanismos, extensões e ecossistemas diferentes. Galera não é um servidor SQL concorrente a todos eles: é uma tecnologia de replicação e clustering usada principalmente com MariaDB e também disponível em ecossistemas MySQL compatíveis. A comparação correta precisa separar o banco, o mecanismo de armazenamento, a solução de alta disponibilidade e a camada de distribuição.

## Comparação por capacidade

| Tecnologia | Alta disponibilidade | Distribuição de dados | Escrita típica | Observação |
| --- | --- | --- | --- | --- |
| PostgreSQL | primary/standby, replicação física, operadores | particionamento local; Citus e outras extensões | um primary por topologia comum | forte ecossistema SQL e extensões |
| MySQL InnoDB | primary/replica, Group Replication, InnoDB Cluster | particionamento local; NDB ou camadas como Vitess | single-primary comum; multi-primary específico | Router e Shell integram operação do cluster |
| MariaDB InnoDB | primary/replica e soluções de cluster | Spider, ColumnStore e outras topologias | depende da topologia | ecossistema próprio, apesar da origem comum com MySQL |
| Galera | quorum e replicação virtualmente síncrona | não faz sharding por si só | multi-primary com certificação | todos os nós normalmente aplicam todas as escritas |

## PostgreSQL

Escolha PostgreSQL quando o modelo relacional, consultas expressivas, extensões, integridade e recursos de transação forem prioritários. Para alta disponibilidade, a composição usual é um primary, standbys, armazenamento e uma camada de eleição ou operador. Para leitura, réplicas podem aliviar o primary, desde que a aplicação aceite lag e roteie escritas ao primary.

Para distribuição horizontal, o particionamento nativo não basta. Citus e soluções semelhantes adicionam uma camada com chave de distribuição, workers e coordenação. A escolha exige conferir quais tabelas são distribuídas, quais joins podem ser locais, como funcionam transações e como o rebalanço será operado.

## MySQL

MySQL com InnoDB possui replicação tradicional e Group Replication. InnoDB Cluster acrescenta MySQL Shell e Router para formar e encaminhar um conjunto de instâncias. O modo single-primary costuma simplificar o modelo de escrita; multi-primary pode ser útil em cenários específicos, mas não elimina conflitos nem torna qualquer transação adequada para escrita em vários nós.

MySQL NDB Cluster é uma plataforma distinta, com particionamento automático e requisitos próprios. Ela não deve ser inferida a partir do comportamento de uma instalação comum de MySQL com InnoDB. Para workloads MySQL que precisam de sharding com compatibilidade específica, Vitess é uma camada adicional com seu próprio modelo de schema, roteamento e operações.

## MariaDB

MariaDB possui replicação e topologias próprias para primary/replica, failover e leitura. Galera oferece um cluster multi-primary virtualmente síncrono para tabelas InnoDB, com quorum e certificação de write sets. Spider fornece uma forma de distribuir tabelas por backends, mas introduz uma camada de roteamento e transações distribuídas.

O fato de MariaDB e MySQL compartilharem ancestrais não significa que seus operadores, versões, engines, defaults ou recursos de cluster sejam intercambiáveis. Compatibilidade SQL também não garante compatibilidade de replicação, ferramentas de failover ou comportamento de schema.

## Galera em detalhes

Galera mantém cópias do mesmo conjunto de dados nos nós do cluster. Uma transação gera um write set e passa por certificação nos membros. Se houver conflito, uma transação pode ser abortada e precisar de retry no nível da aplicação. Se o cluster perder quorum, os nós restantes podem deixar de aceitar escrita para evitar split brain.

Galera é atraente quando o objetivo é disponibilidade com cópias consistentes e a latência entre os nós é controlada. Ele não é uma solução de escrita horizontal para qualquer workload, porque todas as réplicas precisam processar os write sets. Hotspots, transações grandes, conflitos e distância entre regiões podem consumir a capacidade que se pretendia ganhar.

Uma composição comum é Galera por shard. Cada grupo mantém uma cópia redundante de um subconjunto e um roteador envia a chave ao grupo correto. Isso separa dois problemas: Galera trata alta disponibilidade dentro do shard; a camada de sharding trata distribuição. A composição exige mais operação, backups e testes do que qualquer mecanismo isolado.

## Como escolher

Comece pelo objetivo principal. Se ele é recuperação rápida de um escritor, primary/standby pode ser suficiente. Se é leitura, réplicas e cache podem resolver sem sharding. Se é capacidade de escrita e armazenamento além de um único nó, analise sharding, NDB, Citus, Vitess ou uma plataforma distribuída. Se é multi-primary, meça conflitos e latência antes de assumir que o ganho de disponibilidade compensa.

Considere também o ecossistema da equipe, backup, restore, observabilidade, migração, suporte da aplicação, requisitos de consistência, custo de quorum, localização dos nós e capacidade de testar falhas. A tecnologia mais distribuída não é automaticamente a mais resiliente.

## Relações

- [Clustering, redundância e distribuição](../../dados/clustering-redundancia-e-distribuicao.md)
- [Sharding](../../dados/sharding.md)
- [Replicação](../../dados/replicacao.md)
- [Transações e ACID](../../dados/transacoes-acid.md)

## Fontes

- [PostgreSQL, alta disponibilidade e replicação](https://www.postgresql.org/docs/current/high-availability.html)
- [PostgreSQL, replicação lógica](https://www.postgresql.org/docs/current/logical-replication.html)
- [MySQL InnoDB Cluster](https://dev.mysql.com/doc/refman/8.4/en/mysql-innodb-cluster-introduction.html)
- [MySQL Group Replication](https://dev.mysql.com/doc/refman/8.4/en/group-replication.html)
- [MariaDB, topologias](https://mariadb.com/docs/server/architecture/topologies/topologies-overview)
- [MariaDB Galera Cluster](https://mariadb.com/docs/galera-cluster)
- [Galera Cluster, documentação](https://galeracluster.com/library/galera-documentation.pdf)
