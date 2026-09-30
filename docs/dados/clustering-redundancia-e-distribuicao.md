# Mapa de clustering, redundância e distribuição de bancos

"Cluster de banco" pode descrever arquiteturas muito diferentes. Um conjunto de servidores pode manter uma cópia primária e réplicas para failover, compartilhar o mesmo estado com replicação síncrona, distribuir partições diferentes entre nós ou apenas oferecer um endpoint comum para clientes. Antes de escolher uma tecnologia, defina se o objetivo é continuidade, leitura, capacidade de escrita, isolamento de falhas, distribuição geográfica ou redução de custo.

## Termos que não são equivalentes

Alta disponibilidade mantém um serviço acessível depois de uma falha dentro do cenário previsto. Redundância fornece componentes ou dados adicionais para que uma falha não interrompa a função. Replicação mantém cópias do estado. Distribuição coloca processamento ou dados em mais de um failure domain. Sharding divide o conjunto de dados em partes que possuem donos diferentes.

Um cluster pode ter replicação sem escalar escrita. Pode distribuir réplicas por zonas sem dividir tabelas. Pode ter vários nós e continuar com um único escritor. O termo "cluster" não informa consistência, topologia, failover, partição, quorum ou escala.

## Modelos de distribuição

Na topologia primary-replica, o primary recebe escritas e as réplicas aplicam as mudanças. A replicação pode ser assíncrona, com possibilidade de atraso e perda das últimas confirmações durante uma falha, ou síncrona, aguardando confirmação de uma ou mais réplicas antes de confirmar a transação.

Na topologia active-passive, uma réplica assume após detecção e promoção. O cliente precisa de um endpoint estável, um mecanismo de eleição ou operador e uma forma de evitar dois primaries ativos. Na active-active, mais de um nó aceita escrita, o que exige resolver conflitos, ordenação, identidade de transações e efeitos de latência.

Em um cluster shared-nothing, cada nó possui CPU, memória e armazenamento próprios. O sistema pode replicar partições, direcionar consultas ao dono dos dados ou reconstruir uma partição perdida. Isso pode escalar capacidade, mas transforma joins, transações, rebalanço e operações de manutenção em problemas distribuídos.

## Consistência e quorum

Replicação síncrona reduz a janela de perda de dados, mas coloca a latência e a disponibilidade da confirmação sob influência da rede e do quorum. Replicação assíncrona responde mais rápido e tolera distância maior, mas o failover precisa lidar com lag e com transações que talvez não tenham chegado ao candidato.

Quorum define quantos membros precisam participar de uma decisão. Ele ajuda a impedir que duas partições se considerem primárias ao mesmo tempo, mas não corrige uma configuração de aplicação ou uma transação semanticamente inválida. Um cluster de dois nós sem testemunha ou terceiro voto pode perder a capacidade de decidir com segurança quando há uma partição.

Para entender por que três votantes costumam ser mais eficientes que dois ou quatro, veja
[Quorum, consenso e Raft](quorum-e-consenso.md). A página separa quorum de maioria,
consenso sobre um log e replicação primary-replica.

Replicação não é backup. Um `DELETE`, corrupção lógica, erro de migração ou ransomware pode ser replicado imediatamente. A arquitetura precisa de backup independente, retenção e teste de restauração.

## PostgreSQL

O PostgreSQL oferece replicação física por WAL para formar primary e standby, com modos síncrono e assíncrono. Hot standby permite consultas em uma réplica, mas leituras podem observar atraso. A promoção, o endpoint, o fencing e a eleição ficam a cargo da solução de operação, como um operador, Patroni ou outro controlador.

Replicação lógica usa publicações e subscrições baseadas na identidade das linhas. Ela pode replicar tabelas selecionadas, integrar versões ou plataformas diferentes e alimentar consumidores específicos, mas exige planejamento de schema, conflitos, sequences, DDL, ordem e reprocessamento.

Particionamento nativo do PostgreSQL divide uma tabela em partições por range, list ou hash dentro de uma instância lógica. Isso melhora poda de partições, manutenção e retenção quando a chave de acesso está alinhada, mas não coloca automaticamente cada partição em um servidor diferente. Para distribuição horizontal, considere extensões ou plataformas como Citus, sempre verificando compatibilidade de consultas, transações, joins e operações administrativas.

O CloudNativePG, operadores e ferramentas de failover podem automatizar ciclo de vida, backups, eleição e restauração. Eles não mudam a semântica do PostgreSQL nem transformam qualquer consulta em consulta distribuída. O desenho deve distinguir recurso do operador, mecanismo do banco e comportamento da aplicação.

## MySQL

O MySQL oferece replicação tradicional assíncrona e semissíncrona, além de Group Replication. InnoDB Cluster combina MySQL Server, Group Replication, MySQL Shell e MySQL Router. O modo single-primary mantém um escritor e secundárias; o modo multi-primary aceita mais de um escritor, com custo de conflitos, certificação, latência e restrições de workload.

InnoDB Cluster é principalmente uma solução de alta disponibilidade e roteamento, não um particionador automático de qualquer tabela InnoDB. O MySQL NDB Cluster é uma família diferente, com engine e modelo de distribuição próprios, incluindo particionamento automático. Não confunda NDB com um cluster comum de servidores MySQL usando InnoDB.

O particionamento do MySQL divide dados de uma tabela em partições administradas pela mesma instância lógica. Ele pode ajudar poda e manutenção, mas não equivale a sharding entre servidores. Para sharding, a chave, o roteamento, o rebalanço e as transações entre shards precisam ser fornecidos por uma camada ou produto específico.

## MariaDB

MariaDB suporta topologias primary-replica e outras formas de replicação para leitura, continuidade e distribuição operacional. Galera Cluster, integrado ao ecossistema MariaDB por `wsrep`, oferece replicação virtualmente síncrona e multi-primary para workloads transacionais.

O MariaDB Spider é um storage engine e proxy de tabelas remotas que pode distribuir tabelas entre nós MariaDB ou MySQL. Ele representa uma abordagem shared-nothing e pode coordenar operações distribuídas, mas consultas, joins, transações, monitoramento e rebalanço ficam mais complexos. A própria documentação diferencia Spider de soluções de alta disponibilidade e registra mudanças de suporte de recursos ao longo das versões.

MariaDB ColumnStore é outro modelo, voltado a cargas analíticas e armazenamento colunar. Não deve ser tratado como uma alternativa transparente ao InnoDB ou ao Galera para OLTP.

## Galera

Galera usa write sets, certificação e um grupo de processos para replicar transações entre nós. A confirmação é virtualmente síncrona: os nós certificam a transação antes de o cliente receber sucesso, embora a aplicação física em cada tablespace tenha etapas próprias.

O modelo pode oferecer leitura e escrita em qualquer nó, mas isso não significa escala linear de escrita. Cada nó precisa certificar e aplicar as mudanças. Workloads com conflitos frequentes, transações grandes, chaves quentes ou latência entre regiões podem sofrer aumento de aborts, flow control e tempo de commit.

Galera precisa de quorum e de uma visão primária do componente de grupo. Uma rede particionada pode deixar um conjunto sem quorum e impedir escritas para evitar split brain. Um número ímpar de votos ou um arbitrator bem projetado pode ajudar a decisão, mas não elimina falhas de rede, de causa comum ou de configuração.

Galera não é sharding. Todos os nós normalmente mantêm o mesmo conjunto de dados. Também não é backup e não deve ser estendido entre regiões distantes sem avaliar latência, perda de quorum, recuperação de estado e comportamento durante a partição.

## Comparação resumida

| Modelo | Dados em cada nó | Escala de leitura | Escala de escrita | Falha principal |
| --- | --- | --- | --- | --- |
| Primary e réplicas | cópia no primary e réplicas | possível | limitada ao primary | lag e promoção |
| Replicação síncrona | cópia confirmada por quorum | possível | limitada pela coordenação | latência e quorum |
| Galera multi-primary | cópia em cada nó | possível | limitada por certificação e aplicação em todos | conflitos e flow control |
| Sharding | subconjunto por shard | por roteamento e réplicas | horizontal, se a chave distribuir | joins, rebalanço e hotspots |
| NDB ou banco distribuído | fragmentos e réplicas gerenciados pelo sistema | conforme o produto | conforme o modelo de partição | restrições do modelo e operação |

## Relações

- [Replicação](replicacao.md) explica primary, réplica, atraso, failover e por que replicação não é backup.
- [Replicação em cascata](replicacao-em-cascata.md) explica como uma réplica pode atuar
  como relay de outras réplicas.
- [Quorum e consenso](quorum-e-consenso.md) explica maioria, tolerância a falhas e Raft.
- [Sharding](sharding.md) explica partições distribuídas, roteamento, rebalanço e transações entre shards.
- [Transações e ACID](transacoes-acid.md) trata o que muda quando a transação atravessa processos ou nós.
- [Revisões, exclusão e WAL](revisoes-exclusao-e-wal.md) explica WAL, MVCC, recuperação e limites do histórico.
- [PostgreSQL compartilhado](https://guesant.github.io/hl-infrastructure/arquitetura/postgresql-compartilhado/) registra uma decisão específica deste repositório.

## Fontes

- [PostgreSQL, alta disponibilidade e replicação](https://www.postgresql.org/docs/current/high-availability.html)
- [PostgreSQL, replicação lógica](https://www.postgresql.org/docs/current/logical-replication.html)
- [PostgreSQL, particionamento](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- [MySQL InnoDB Cluster](https://dev.mysql.com/doc/refman/8.4/en/mysql-innodb-cluster-introduction.html)
- [MySQL Group Replication](https://dev.mysql.com/doc/refman/8.4/en/group-replication.html)
- [MySQL NDB Cluster](https://dev.mysql.com/doc/refman/8.4/en/mysql-cluster.html)
- [MariaDB, topologias](https://mariadb.com/docs/server/architecture/topologies/topologies-overview)
- [MariaDB Galera Cluster](https://mariadb.com/docs/galera-cluster)
- [Galera Cluster, documentação](https://galeracluster.com/library/galera-documentation.pdf)
