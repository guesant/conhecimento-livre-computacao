# Locks e transações no PostgreSQL

PostgreSQL combina MVCC, locks de tabela, locks de linha, locks de predicado e locks
consultivos. Esses mecanismos respondem a perguntas diferentes. MVCC permite que uma
leitura observe uma versão consistente sem bloquear toda a escrita; locks coordenam
operações incompatíveis; locks de predicado protegem uma decisão serializável mesmo
quando ainda não existe uma linha correspondente.

Uma transação não é apenas um bloco de SQL. Ela cria uma visão, adquire recursos, pode
ficar esperando outra sessão, pode ser abortada por deadlock ou conflito serializável e
mantém seus efeitos até `COMMIT` ou `ROLLBACK`. O tamanho e a duração da transação fazem
parte do comportamento de concorrência.

## O que o PostgreSQL bloqueia

O PostgreSQL pode registrar locks sobre relações, páginas, tuplas, transações, virtual
transactions, objetos e chaves consultivas. Nem todo lock exibido em `pg_locks` é um
recurso que a aplicação deve tentar controlar diretamente. Locks de página e vários locks
internos são mantidos por períodos curtos pelo mecanismo.

Os locks de tabela abaixo são os modos usados por `LOCK TABLE` e também adquiridos
implicitamente por comandos SQL. A ordem representa a força aproximada do lock, mas a
compatibilidade deve ser consultada pela matriz oficial, porque um modo pode conflitar
com vários outros.

| Modo | Uso típico | Característica |
| --- | --- | --- |
| `ACCESS SHARE` | `SELECT` | Permite leituras concorrentes e só conflita com `ACCESS EXCLUSIVE`. |
| `ROW SHARE` | `SELECT FOR UPDATE` e `SELECT FOR SHARE` | Marca intenção de bloquear linhas. |
| `ROW EXCLUSIVE` | `INSERT`, `UPDATE`, `DELETE` e `MERGE` | Usado por DML que modifica linhas. |
| `SHARE UPDATE EXCLUSIVE` | `VACUUM`, `ANALYZE`, `CREATE INDEX CONCURRENTLY` | Coordena manutenção e mudanças que não podem concorrer com certas operações de schema. |
| `SHARE` | `CREATE INDEX` | Permite leituras, mas impede modificações concorrentes específicas. |
| `SHARE ROW EXCLUSIVE` | Algumas alterações de integridade e schema | É exclusivo em relação a locks de escrita e não é obtido por toda alteração de schema. |
| `EXCLUSIVE` | Operações que precisam restringir mais concorrência | Ainda permite `ACCESS SHARE`, dependendo do conflito. |
| `ACCESS EXCLUSIVE` | `ALTER TABLE`, `DROP TABLE`, `TRUNCATE`, `VACUUM FULL`, `REINDEX` e `CLUSTER` | Conflita com todos os modos, inclusive leituras comuns. |

Os nomes são importantes porque uma sessão que executa apenas `SELECT` obtém
`ACCESS SHARE`, enquanto uma migração que solicita `ACCESS EXCLUSIVE` pode esperar por ela.
Se a leitura estiver dentro de uma transação longa, o problema persiste até o commit ou
rollback dessa transação.

## Locks de linha

Locks de linha protegem registros selecionados e não a tabela inteira. As quatro formas
explícitas são:

- `FOR UPDATE`, que bloqueia a linha para alterações concorrentes e é apropriado quando
  a aplicação vai modificá-la depois da leitura;
- `FOR NO KEY UPDATE`, que protege a linha contra alterações relevantes sem afirmar que
  uma chave referenciada será alterada;
- `FOR SHARE`, que permite que outras transações também mantenham share lock, mas impede
  alterações incompatíveis;
- `FOR KEY SHARE`, que protege a chave contra alterações que quebrariam uma referência,
  sem bloquear toda alteração não relacionada da linha.

Uma instrução pode usar `NOWAIT` para falhar imediatamente se não conseguir o lock, ou
`SKIP LOCKED` para ignorar linhas ocupadas. `SKIP LOCKED` é útil para workers que retiram
itens de uma fila, mas não representa uma leitura completa e pode deixar itens esperando
por muito tempo se o produtor do lock estiver quebrado.

O PostgreSQL mantém o lock de linha até o fim da transação, salvo regras específicas de
savepoint e rollback. Uma consulta que lê e mantém milhares de linhas bloqueadas pode
impedir atualizações por muito mais tempo do que o tempo de execução do `SELECT`.

## Locks de predicado e serialização

Em `SERIALIZABLE`, o PostgreSQL usa Serializable Snapshot Isolation e locks de predicado
para rastrear conflitos entre leituras e escritas. O objetivo não é bloquear previamente
toda linha possível, mas detectar quando a combinação de transações não poderia ter
ocorrido em uma ordem serial.

Uma transação pode terminar com `serialization_failure` mesmo sem esperar em um lock de
tabela ou de linha. O chamador precisa repetir a transação inteira, com limite de tentativas
e backoff. Repetir somente o statement que falhou pode quebrar a invariável que o nível
serializável deveria proteger.

## Locks consultivos

Advisory locks são chaves escolhidas pela aplicação. Eles podem ser adquiridos para a
sessão inteira ou somente para a transação:

```sql
SELECT pg_advisory_xact_lock(8472);
```

Um advisory lock é útil para impedir que dois workers executem a mesma tarefa ou para
serializar uma migração coordenada. Ele não impede que outro processo ignore o protocolo
e altere a tabela. Constraints, locks normais e regras de autorização continuam sendo
necessários.

Prefira a variante transacional quando o lock deve desaparecer automaticamente em
`COMMIT` ou `ROLLBACK`. Para locks de sessão, sempre defina como o processo detectará e
liberará uma sessão abandonada. Um lock consultivo sem proprietário identificável pode
virar uma indisponibilidade difícil de diagnosticar.

## Duração e fila de locks

Locks de tabela e de linha normalmente duram até o fim da transação. Isso significa que
`idle in transaction` é diferente de uma conexão simplesmente ociosa. A primeira mantém
snapshot e locks; a segunda não possui uma transação aberta, embora ainda possa manter
recursos de conexão.

Uma sessão esperando por lock pode criar uma fila. O problema não é apenas o primeiro
bloqueador: quando uma operação forte está esperando, outras sessões podem ficar atrás
dela mesmo que fossem compatíveis com o estado anterior. Por isso é importante observar
quem espera, quem bloqueia e há quanto tempo.

Uma consulta inicial de diagnóstico pode ser:

```sql
SELECT
  waiting.pid AS waiting_pid,
  waiting.query AS waiting_query,
  blocker.pid AS blocker_pid,
  blocker.state AS blocker_state,
  blocker.query AS blocker_query,
  now() - blocker.xact_start AS blocker_age
FROM pg_stat_activity AS waiting
JOIN pg_locks AS waiting_lock
  ON waiting_lock.pid = waiting.pid
  AND NOT waiting_lock.granted
JOIN pg_locks AS blocker_lock
  ON blocker_lock.locktype = waiting_lock.locktype
  AND blocker_lock.database IS NOT DISTINCT FROM waiting_lock.database
  AND blocker_lock.relation IS NOT DISTINCT FROM waiting_lock.relation
  AND blocker_lock.page IS NOT DISTINCT FROM waiting_lock.page
  AND blocker_lock.tuple IS NOT DISTINCT FROM waiting_lock.tuple
  AND blocker_lock.virtualxid IS NOT DISTINCT FROM waiting_lock.virtualxid
  AND blocker_lock.transactionid IS NOT DISTINCT FROM waiting_lock.transactionid
  AND blocker_lock.classid IS NOT DISTINCT FROM waiting_lock.classid
  AND blocker_lock.objid IS NOT DISTINCT FROM waiting_lock.objid
  AND blocker_lock.objsubid IS NOT DISTINCT FROM waiting_lock.objsubid
  AND blocker_lock.granted
JOIN pg_stat_activity AS blocker
  ON blocker.pid = blocker_lock.pid;
```

Em diagnósticos novos, `pg_blocking_pids(waiting.pid)` costuma ser mais simples e menos
sujeito a omissões do que reconstruir manualmente toda a relação de conflito.

## Deadlocks e timeouts

Deadlock ocorre quando duas ou mais transações esperam umas pelas outras. Por exemplo,
uma transação pode bloquear a linha A e esperar a linha B, enquanto outra bloqueia B e
espera A. O PostgreSQL detecta o ciclo e aborta uma das transações.

A aplicação deve:

1. atualizar recursos em uma ordem determinística;
2. manter a transação curta;
3. evitar chamadas externas enquanto locks estiverem mantidos;
4. tratar `deadlock detected` como erro de retry da transação inteira;
5. definir `lock_timeout` quando esperar indefinidamente for pior que falhar;
6. registrar duração, relação, operação e identificador da transação.

`statement_timeout` limita a duração de uma instrução. `lock_timeout` limita somente o
tempo gasto esperando locks. Eles respondem a riscos diferentes e não devem ser usados
como substitutos de uma modelagem de concorrência.

## Transação e autocommit

No autocommit, cada statement forma sua própria transação. Isso é adequado para uma
leitura isolada ou uma atualização realmente independente. Não é suficiente quando várias
tabelas precisam mudar juntas.

Uma transação explícita usa `BEGIN`, `COMMIT` e `ROLLBACK`:

```sql
BEGIN;
UPDATE accounts SET balance = balance - 10 WHERE id = 1;
UPDATE accounts SET balance = balance + 10 WHERE id = 2;
COMMIT;
```

O limite deve conter a invariável inteira, mas não espera de usuário, chamada HTTP ou
processamento que possa ocorrer fora do banco. Uma transação aberta durante uma chamada
externa conserva snapshot e locks sem produzir valor transacional adicional.

## Níveis de isolamento no PostgreSQL

O nível é escolhido por transação ou por sessão. Os nomes são padronizados, mas a
implementação de cada banco pode permitir anomalias diferentes.

| Nível | Semântica no PostgreSQL |
| --- | --- |
| `READ UNCOMMITTED` | Aceito pela sintaxe, mas se comporta como `READ COMMITTED`. PostgreSQL não permite dirty reads. |
| `READ COMMITTED` | Cada statement recebe um snapshot próprio. Dois statements da mesma transação podem ver commits diferentes. |
| `REPEATABLE READ` | A transação mantém o snapshot da primeira operação relevante. Conflitos podem causar abortos. |
| `SERIALIZABLE` | O resultado precisa ser equivalente a uma execução serial. Conflitos podem gerar `serialization_failure`, que exige retry da transação completa. |

`READ COMMITTED` costuma ser adequado para operações curtas. `REPEATABLE READ` é útil
quando várias leituras precisam observar uma mesma visão. `SERIALIZABLE` protege
invariantes complexas, mas exige que a aplicação aceite abortos e repita a transação.

O nível mais forte não corrige uma transação que chama um serviço externo, não garante
atomicidade entre bancos e não substitui constraints. Ele define o que o banco fará com
a concorrência dentro do seu próprio limite.

## Modos read only, read write e deferrable

Uma transação pode ser `READ ONLY` quando não deve modificar dados. Isso documenta a
intenção e permite que o banco rejeite DML acidental. `READ WRITE` é o modo normal para
operações que alteram estado.

`DEFERRABLE` só é útil com uma transação `SERIALIZABLE READ ONLY`. O banco pode esperar
antes de liberar a execução para obter um snapshot que não precise ser abortado por
conflitos serializáveis. É uma troca entre latência inicial e menos retries em leituras
longas, como relatórios consistentes.

Exemplo:

```sql
BEGIN ISOLATION LEVEL SERIALIZABLE READ ONLY DEFERRABLE;
SELECT count(*) FROM ledger_entries;
COMMIT;
```

## Savepoints

Savepoints permitem desfazer parte da transação:

```sql
BEGIN;
SAVEPOINT item;
UPDATE inventory SET quantity = quantity - 1 WHERE id = 10;
ROLLBACK TO SAVEPOINT item;
COMMIT;
```

Eles não são transações aninhadas independentes. A transação externa continua mantendo
seu snapshot e seus recursos. Use savepoints para tratar uma unidade opcional dentro de
um limite menor, não para esconder uma operação enorme ou prolongar locks.

## Two-phase commit

PostgreSQL suporta transações preparadas com `PREPARE TRANSACTION`, `COMMIT PREPARED` e
`ROLLBACK PREPARED`. O coordenador pode preparar vários participantes e depois decidir o
resultado global.

O custo é significativo: uma transação preparada conserva locks e estado até a decisão
final. Falhas do coordenador podem deixar transações órfãs, bloquear vacuum e consumir
espaço. Só use 2PC com inventário, timeout operacional e processo de recuperação para
transações preparadas abandonadas. Em muitos sistemas, outbox, saga e compensação são
mais simples.

## DDL e transações

Muitas operações DDL do PostgreSQL participam de transações e podem ser revertidas, mas
o lock continua mantido até o commit. Colocar `ALTER TABLE` e um backfill pesado na mesma
transação mantém a definição bloqueada durante todo o backfill.

`CREATE INDEX CONCURRENTLY` reduz a interferência com DML, mas possui fases, exige uma
transação própria e pode deixar um índice inválido após uma falha. Uma migration precisa
respeitar essas restrições em vez de envolver automaticamente tudo em uma transação.

## Comparação com outros bancos

| Sistema | Modelo relevante | Diferença operacional |
| --- | --- | --- |
| PostgreSQL | MVCC, locks de tabela e linha, predicate locking em serializável | `READ UNCOMMITTED` se comporta como `READ COMMITTED`; DDL frequentemente é transacional. |
| MySQL InnoDB | MVCC, locks de registro, gap e next-key, metadata locks | `REPEATABLE READ` é comum por padrão; DDL pode fazer commit implícito e o caminho de índice altera o conjunto bloqueado. |
| MariaDB InnoDB | Modelo semelhante ao InnoDB, com diferenças por versão e configuração | Não presuma equivalência completa com MySQL; valide isolation, DDL online e metadata locks na versão implantada. |
| MariaDB Galera | Transações locais combinadas com certificação e ordenação de grupo | Uma transação pode ser abortada na certificação mesmo sem um lock local tradicional; DDL precisa ser compatível com a operação do cluster. |
| SQL Server | Locks e row versioning configuráveis | Lock escalation, hints e níveis de isolamento alteram a quantidade de linhas ou páginas bloqueadas. |
| Oracle | MVCC, locks de linha e locks de tabela | DDL e controle de transação têm regras próprias, inclusive commits implícitos em operações DDL. |
| SQLite | Um escritor por arquivo, com modos rollback journal ou WAL | Não oferece a mesma concorrência de escritores de um servidor PostgreSQL; a escolha do journal muda leitores e bloqueios. |

Os nomes `READ COMMITTED`, `REPEATABLE READ` e `SERIALIZABLE` não são uma garantia de
comportamento idêntico. Compare snapshots, dirty reads, phantoms, gap locks, conflitos de
escrita, commits implícitos e erros que podem ser repetidos.

## Relações

- [Migrações de schema, locks e transações](migracoes-schema-locking.md) trata o risco de
  migrations, backfills e DDL em produção.
- [Transações e ACID](transacoes-acid.md) explica atomicidade, consistência, isolamento e
  durabilidade como propriedades do limite transacional.
- [PostgreSQL: `pg_stat`, índices e otimização](postgresql-pg-stat-indices-e-otimizacao.md)
  cobre investigação de atividade, planos, I/O e vacuum.
- [PostgreSQL: checkpoints](postgresql-checkpoints.md) explica a relação entre páginas
  sujas, WAL, recuperação e picos de I/O.

## Fontes

- [PostgreSQL, explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- [PostgreSQL, transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [PostgreSQL, monitoring locks](https://www.postgresql.org/docs/current/monitoring-locks.html)
- [PostgreSQL, transaction management](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [MySQL, InnoDB locking](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking.html)
- [MySQL, transaction isolation](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html)
- [MariaDB, InnoDB lock modes](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-lock-modes)
- [MariaDB Galera, schema upgrades](https://mariadb.com/docs/galera-cluster/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster)
