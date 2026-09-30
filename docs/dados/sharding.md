# Sharding

Sharding é a distribuição horizontal de um conjunto de dados em partes chamadas shards. Cada shard é responsável por uma faixa ou subconjunto das chaves. O objetivo é aumentar capacidade de armazenamento, throughput ou isolamento quando uma única instância não atende ao requisito. O custo é espalhar estado, roteamento, operações administrativas e parte da consistência.

Sharding não é o mesmo que particionamento local. Particionamento divide uma tabela dentro de uma instância lógica; sharding coloca dados em servidores, processos ou grupos independentes. Também não é o mesmo que replicação: replicação cria cópias do mesmo dado, enquanto sharding divide o conjunto. Um shard normalmente pode ter suas próprias réplicas para tolerância a falhas.

## Chave de shard

A chave precisa distribuir carga e permitir que a maioria das consultas encontre um shard sem consultar todos. Uma chave de tenant é adequada quando o tenant é a unidade de isolamento e a carga é relativamente equilibrada. Uma chave temporal pode facilitar retenção, mas concentrar todas as escritas no período atual. Uma chave incremental pode criar hotspot no shard que recebe os maiores valores.

Uma chave ruim produz shards desiguais, consultas scatter-gather e migrações frequentes. A escolha deve considerar cardinalidade, distribuição real, consultas, crescimento, privacidade, localização e possibilidade de mover um tenant ou faixa sem reescrever toda a aplicação.

## Estratégias

Sharding por range associa intervalos a shards. Ele favorece consultas por intervalo e arquivamento, mas pode concentrar escritas em uma faixa quente. Sharding por hash distribui melhor uma chave uniforme, mas dificulta consultas ordenadas e movimentação de intervalos. Sharding por diretório usa um catálogo que mapeia cada chave para um shard, oferecendo flexibilidade ao custo de uma dependência adicional.

Consistent hashing reduz a quantidade de chaves remapeadas ao adicionar um nó, mas não resolve por si só tamanho desigual, hotspots, réplicas, transações ou consultas por múltiplas chaves. Hashing composto, buckets virtuais e divisão de tenants grandes são técnicas para controlar esses problemas.

## Roteamento

O roteador pode viver na aplicação, em um proxy, no driver, em um middleware ou no próprio produto. Ele precisa conhecer o mapa de shards, lidar com mudanças, renovar cache de topologia e reagir a um shard indisponível. Um cache de roteamento stale pode enviar uma escrita ao lugar errado; por isso, a aplicação precisa de versionamento, fencing ou uma resposta segura durante o rebalanceamento.

Consultas que incluem a chave podem ser direcionadas. Consultas sem a chave podem precisar consultar todos os shards, agregar resultados e ordenar globalmente. O custo cresce com a quantidade de shards e com o maior tempo de resposta. Índices locais não produzem automaticamente um índice global.

## Transações e integridade

Uma transação local em um shard pode preservar ACID naquele shard. Uma transação que atravessa shards exige coordenação, 2PC, saga, uma restrição de modelo ou uma aceitação explícita de consistência eventual. Foreign keys entre shards são difíceis de manter e podem impedir rebalanço ou disponibilidade independente.

Modelos distribuídos devem declarar onde vivem IDs, sequences, locks, unicidade e outbox. Um ID global precisa tolerar geração concorrente e migração. Uma unicidade global precisa de um dono ou de coordenação. Uma exclusão em um shard que publica evento para outro precisa de idempotência e de um mecanismo para não perder a mensagem.

## Rebalanço

Adicionar ou remover shards exige copiar dados, mudar roteamento, manter leituras e escritas coerentes e lidar com falha durante a migração. O processo precisa de estado de progresso, checkpoints, throttling, validação, dupla leitura ou escrita quando necessário e uma forma de rollback.

Não faça rebalanço sem medir impacto em I/O, locks, cache, replicação e latência. Uma migração que copia dados corretamente ainda pode causar indisponibilidade se monopolizar recursos do banco. Shards grandes devem ser divididos em unidades menores ou buckets para permitir movimentos graduais.

## PostgreSQL, MySQL e MariaDB

PostgreSQL possui particionamento nativo e replicação, mas sharding entre servidores é uma decisão adicional. Citus é uma extensão e plataforma que distribui tabelas por workers usando uma chave de distribuição e coordenação de consultas. A compatibilidade depende de funções, joins, transações, constraints, tipo de tabela e da versão.

MySQL InnoDB Cluster fornece alta disponibilidade e roteamento, mas não transforma automaticamente uma tabela InnoDB em vários shards. MySQL NDB Cluster possui um modelo de dados e particionamento distribuído próprios. Produtos ou camadas como Vitess podem oferecer sharding para workloads MySQL, com regras específicas de schema, chaves e consultas.

MariaDB Spider distribui tabelas por servidores backend e oferece uma forma de proxy e storage engine para sharding e federação. O desenho precisa considerar limitações de joins, transações XA, monitoramento e compatibilidade da versão. Galera pode replicar cada shard para alta disponibilidade, mas o cluster Galera isolado não é um mecanismo de sharding.

## Quando usar

Sharding faz sentido quando a capacidade ou o isolamento de uma única instância foi medido como insuficiente e a chave de distribuição é estável. Antes dele, considere índices, particionamento local, arquivamento, réplicas de leitura, pool de conexões, otimização de consultas, aumento vertical e separação de workloads.

Não use sharding apenas porque a aplicação tem muitos registros ou porque "horizontal" parece mais moderno. O custo de rebalanço, diagnóstico, operações cross-shard, backups e desenvolvimento pode superar o ganho. Um banco único com backups e réplica bem operados pode ser mais confiável para um workload pequeno ou médio.

## Checklist

- Qual é o limite medido da instância atual?
- Qual chave permite roteamento da maioria das consultas?
- Como serão tratados hotspots e tenants grandes?
- Quais operações exigem transação ou unicidade global?
- Como funcionam backup, restauração e disaster recovery por shard?
- Como ocorre adição, remoção e rebalanço?
- Como detectar topologia stale e impedir escrita no shard errado?
- Como consultar dados sem a chave?
- Como migrar uma versão de schema em todos os shards?
- Qual é o plano de teste e rollback?

## Relações

- [Clustering, redundância e distribuição](clustering-redundancia-e-distribuicao.md)
- [Particionamento de ferramentas](../comparacoes/ferramentas/particionamento-linux.md)
- [Replicação](replicacao.md)
- [Transações e ACID](transacoes-acid.md)

## Fontes

- [PostgreSQL, particionamento](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- [Citus, documentação](https://docs.citusdata.com/en/stable/)
- [MySQL NDB Cluster](https://dev.mysql.com/doc/refman/8.4/en/mysql-cluster.html)
- [Vitess, documentação](https://vitess.io/docs/)
- [MariaDB Spider](https://mariadb.com/docs/server/server-usage/storage-engines/spider)
