# Dados

Esta área organiza persistência, consistência, mensageria, armazenamento e colaboração distribuída. Produtos concretos devem ser entendidos como implementações desses modelos, não como a definição da categoria.

## Categorias

- [Bancos e persistência](bancos/index.md) trata modelos de consulta e estado persistido.
- [Consistência e distribuição](consistencia/index.md) trata replicação, quorum, sharding e consenso.
- [Mensageria](mensageria/index.md) trata filas, jobs, workers e event streaming.
- [Armazenamento](armazenamento/index.md) trata objetos, cache e expiração.
- [Colaboração distribuída](colaboracao/index.md) trata sincronização local-first, CRDTs e resolução de conflitos.

[Exclusão, edição, revisões e WAL](revisoes-exclusao-e-wal.md) compara exclusão lógica, purga física, atualização destrutiva, versionamento editorial e o log de recuperação do PostgreSQL.

[Clustering, redundância e distribuição](clustering-redundancia-e-distribuicao.md) separa alta disponibilidade, replicação, distribuição de dados e sharding em bancos relacionais. [Quorum e consenso](quorum-e-consenso.md) explica maiorias, Raft e decisões sob falha. [Sharding](sharding.md) detalha chaves, roteamento, rebalanço e transações entre shards.

[Migrações de schema, locks e transações](migracoes-schema-locking.md) explica como uma alteração de estrutura pode bloquear um sistema inteiro, como os bancos coordenam DDL e DML e como usar expand and contract, backfill e online schema change com segurança.

[Locks e transações no PostgreSQL](postgresql-locks-e-transacoes.md) detalha MVCC, locks de tabela e linha, locks de predicado, advisory locks, isolamento, savepoints, two-phase commit, deadlocks e diferenças entre PostgreSQL, InnoDB, Galera, SQL Server, Oracle e SQLite.

[PostgreSQL: pg_stat, índices e otimização](postgresql-pg-stat-indices-e-otimizacao.md) organiza o diagnóstico por atividade, locks, I/O, consultas, planos, estatísticas, índices, vacuum e medição antes e depois da mudança.

[PostgreSQL: WAL e capacidade](postgresql-wal-e-capacidade.md) explica arquivamento, slots, réplicas atrasadas, pgBackRest e os cuidados para o `pg_wal` não preencher o volume.

[Checkpoints no PostgreSQL](postgresql-checkpoints.md) explica páginas sujas, WAL, checkpoints, restartpoints, parâmetros de controle, picos de I/O e recuperação após crash.

## Bancos não relacionais

[Key-value](bancos/key-value.md) modela acesso principalmente por chave. [Document databases](bancos/documentos.md) armazenam documentos estruturados e permitem consultas sobre sua estrutura.
[Bancos de dados em tempo real](bancos/realtime-database.md) combinam estado persistido,
listeners e sincronização contínua, com garantias de consistência, conflito e reconexão
que precisam ser definidas explicitamente.

## Colaboração distribuída

[Colaboração distribuída e local-first](colaboracao/index.md) reúne modelos para edição
concorrente, sincronização offline, CRDT, Operational Transformation, diff e resolução de
conflitos.

## Mensageria

[Filas](mensageria/filas.md) distribuem unidades de trabalho ou mensagens entre produtores e consumidores. [Event streaming](mensageria/event-streaming.md) mantém um log ordenado de eventos que pode ser lido por consumidores com posições próprias.

[Jobs e workers](mensageria/jobs-e-workers.md) explicam como persistir trabalho, agendar
execuções e processar filas com concorrência controlada. O job é o trabalho; o worker é o
processo que o executa; o storage é o componente que preserva estado e recuperação.

## Cópias e consistência

[Cache](cache.md) é uma cópia derivada, normalmente temporária e invalidável. [Replicação](replicacao.md)
mantém uma ou mais cópias de um estado primário e pode ser síncrona ou assíncrona. Cache,
réplica, backup e snapshot possuem objetivos diferentes e não devem ser tratados como
sinônimos.

[Replicação em cascata](replicacao-em-cascata.md) usa uma réplica como origem de outras
réplicas para reduzir fan-out direto e aproximar dados de determinados sites ou redes.

[TTL e expiração](ttl.md) explica validade temporal em cache, mensagens, leases, DNS,
sessões e retenção. [Fila de prioridade](mensageria/fila-de-prioridade.md) diferencia
escolha por urgência de uma fila FIFO.

## Armazenamento Kubernetes

O modelo de PV/PVC, storage classes e soluções locais ou distribuídas permanece na área de plataforma Kubernetes, porque ali a pergunta principal é integração com workloads do cluster.
