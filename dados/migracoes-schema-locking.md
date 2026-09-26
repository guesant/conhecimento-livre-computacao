# Migrações de schema, locks e transações

Uma migração de banco não é apenas uma alteração de arquivo. Ela é uma operação concorrente sobre um estado que está sendo usado por aplicações, workers, relatórios, réplicas e rotinas administrativas. Uma instrução curta pode esperar por uma transação antiga, manter outras sessões em fila e transformar uma alteração aparentemente simples em indisponibilidade.

O risco não depende somente de o `ALTER TABLE` ser rápido quando executado isoladamente. É preciso considerar o tempo para obter o lock, o trabalho que a alteração faz no armazenamento, a forma como o banco coordena DDL com DML e o comportamento dos clientes enquanto a mudança aguarda ou é aplicada.

## Como uma migração trava o sistema

Considere uma tabela grande e uma conexão que executou uma consulta dentro de uma transação, mas permaneceu aberta enquanto o cliente processava a resposta. A conexão pode continuar segurando locks de metadados ou uma visão transacional. Quando uma migração tenta alterar a tabela, ela entra em espera.

O problema pode piorar porque a migração normalmente precisa de um lock mais forte. Enquanto esse pedido está aguardando, novas consultas podem ser enfileiradas atrás dele, mesmo que fossem compatíveis com o lock que existia antes. O sintoma observado pela aplicação passa a ser uma fila de requisições, aumento de latência, esgotamento do pool de conexões e, por fim, erros em cascata.

O incidente pode acontecer mesmo sem uma sessão explicitamente usando `LOCK TABLES`. Uma transação comum, um cursor, uma consulta longa, uma conexão em estado `idle in transaction` ou uma sessão de manutenção esquecida podem ser suficientes.

## Coluna com default e constraint

Uma alteração como esta combina várias decisões:

```sql
ALTER TABLE accounts
  ADD COLUMN status text NOT NULL DEFAULT 'active';
```

Ela pode precisar:

- alterar o catálogo do banco;
- obter um lock de definição da tabela;
- materializar um valor para linhas já existentes;
- validar que nenhuma linha viola `NOT NULL` ou outra constraint;
- atualizar índices ou estruturas auxiliares;
- sincronizar o novo schema com réplicas ou nós de um cluster;
- manter compatibilidade com versões antigas e novas da aplicação.

Essas partes têm custos diferentes. Uma operação que é metadata-only em uma versão do PostgreSQL pode exigir reescrita em outra versão ou em outro banco. Uma operação online pode permitir DML durante a maior parte do trabalho e ainda precisar de um lock exclusivo curto no início ou no commit da definição.

### PostgreSQL

No PostgreSQL atual, adicionar uma coluna com default constante pode ser rápido porque o banco consegue armazenar o default no catálogo sem reescrever imediatamente todas as linhas. Isso não torna a operação livre de espera: ainda é necessário adquirir o lock apropriado, e uma transação longa pode impedir a alteração.

Defaults voláteis, como funções que produzem um valor diferente por linha, podem exigir atualização das linhas. Nessa situação, é mais seguro adicionar a coluna sem default, preenchê-la em lotes e só depois definir o default para novas inserções.

Adicionar uma constraint verifica os dados existentes. Para constraints `CHECK` e `FOREIGN KEY`, uma estratégia comum é criar a constraint como `NOT VALID`, corrigir ou validar os dados e executar `VALIDATE CONSTRAINT` em uma etapa separada. Isso reduz o período de bloqueio forte, mas não elimina o custo da validação nem dispensa o planejamento da compatibilidade.

Para unicidade em tabela grande, pode ser possível criar o índice com `CREATE UNIQUE INDEX CONCURRENTLY` e depois associá-lo ao contrato apropriado. A instrução concorrente possui restrições próprias e não deve ser colocada dentro de uma transação comum de migration sem verificar a documentação da versão usada.

### MySQL e MariaDB

InnoDB usa locks de metadados além dos locks de registros. Uma operação de DDL pode ser classificada como `INSTANT`, `INPLACE` ou `COPY`, conforme a operação, versão, engine e definição da tabela. `INSTANT` altera principalmente metadados; `INPLACE` pode trabalhar sem copiar toda a tabela, mas ainda consumir CPU, memória e I/O; `COPY` cria ou reconstrói uma cópia e pode ser muito mais pesada.

Mesmo com DDL online e `LOCK=NONE`, a operação pode esperar por uma transação que mantém metadata lock. Quando o DDL solicita o lock exclusivo final, consultas novas podem ficar esperando atrás dele. Por isso, "online" significa menor bloqueio durante parte da operação, não "impossível de bloquear".

Antes de executar, confirme o algoritmo e o nível de concorrência aceitos pela versão e pelo engine. Se o banco não puder cumprir `ALGORITHM=INSTANT` ou `LOCK=NONE`, prefira falhar antes a executar silenciosamente uma cópia da tabela em horário de tráfego.

### Galera

Em Galera, uma mudança de schema também é uma operação de cluster. No modo padrão de Total Order Isolation, o DDL é ordenado e aplicado nos nós, e transações podem ser bloqueadas enquanto a alteração é processada. Uma alteração tolerável em um servidor isolado pode, portanto, interromper a escrita no cluster inteiro.

Rolling Schema Upgrade pode reduzir o bloqueio, mas exige executar a alteração por nó, manter compatibilidade entre schemas durante a transição e entender o comportamento da aplicação enquanto os nós estão em estados diferentes. Não é uma opção automática nem uma justificativa para liberar uma mudança incompatível.

## Estratégia expand and contract

Para tabelas grandes ou sistemas sem janela de manutenção, prefira uma sequência compatível entre versões:

1. Expandir o schema com uma coluna ou índice opcional, sem exigir imediatamente a migração de todos os dados.
2. Publicar uma aplicação que tolere tanto o schema antigo quanto o novo.
3. Fazer backfill em lotes pequenos, ordenados por uma chave estável, com commits frequentes e limite de tempo.
4. Medir locks, lag, I/O, duração e erros; pausar o backfill quando os limites operacionais forem atingidos.
5. Verificar que todos os registros estão válidos e criar ou validar constraints em uma etapa separada.
6. Ativar a leitura do novo campo e, quando necessário, manter escrita dupla durante a transição.
7. Remover o caminho antigo somente depois de confirmar que nenhum consumidor, worker, relatório ou versão antiga ainda depende dele.
8. Fazer a contração em outra mudança, preferencialmente depois do período de observação e de um backup verificado.

O default do banco pode ser adicionado durante a expansão para proteger novas inserções, mas não deve ser confundido com o backfill. O backfill é uma operação de dados e precisa de seu próprio controle de volume, retry e observabilidade.

## Backfill seguro

Um backfill deve evitar uma única transação que percorra milhões de linhas. Use lotes limitados por uma chave indexada ou por uma faixa de identificadores, e não por `OFFSET` crescente em uma tabela que muda durante o processo.

Cada lote deve ser pequeno o bastante para liberar locks rapidamente e grande o bastante para não desperdiçar todo o tempo em overhead de commits. O tamanho correto depende do disco, da carga, do lag de replicação e da janela de latência aceita.

O processo precisa ser reiniciável. Grave progresso de forma idempotente, reavalie linhas antes de escrever, trate deadlocks e timeouts como sinais para retry com backoff e não assuma que uma conexão perdida significa que o lote não foi aplicado. Quando o resultado não for conhecido, consulte uma chave de negócio ou use uma operação idempotente antes de repetir.

## Tipos de locking

Os nomes e conflitos variam entre bancos, mas estes conceitos aparecem com frequência.

### Locks de tabela

Um lock de tabela protege a definição ou o acesso a uma tabela inteira. Pode permitir leituras e impedir escrita, permitir somente certos tipos de alteração ou bloquear qualquer acesso concorrente. DDL, `TRUNCATE`, reconstrução de índices e operações de manutenção costumam pedir locks mais fortes que um `SELECT` comum.

No PostgreSQL, `ACCESS SHARE` é obtido por uma leitura comum e `ACCESS EXCLUSIVE` conflita com todos os modos. `ALTER TABLE`, `DROP TABLE`, `TRUNCATE`, `VACUUM FULL` e outras operações podem adquirir esse lock forte, conforme a instrução. Os locks normalmente permanecem até o fim da transação.

### Locks de linha

Locks de linha coordenam alterações sobre registros específicos. No PostgreSQL, `FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE` e `FOR KEY SHARE` têm forças diferentes. Eles bloqueiam operações concorrentes sobre as mesmas linhas, mas não transformam a tabela inteira em uma seção crítica.

No InnoDB, locks de registro são associados à estrutura de índice. A consulta, o índice escolhido e o nível de isolamento influenciam quais registros e intervalos são bloqueados. Dois comandos que parecem tratar da mesma linha podem adquirir locks em registros de índice diferentes se não houver um caminho de acesso comum.

### Locks de metadados

Metadata locks protegem a definição de tabelas, views e objetos relacionados. Eles explicam por que um `ALTER TABLE` pode ficar esperando uma transação que apenas fez um `SELECT` e ainda não executou `COMMIT` ou `ROLLBACK`.

Esse lock é uma das causas mais comuns de incidentes durante DDL em MySQL e MariaDB. A migração precisa observar tanto a sessão que está executando o DDL quanto as sessões antigas que seguram o metadado.

### Locks de intervalo, gap e predicate

Alguns mecanismos bloqueiam não só registros existentes, mas também intervalos nos quais uma nova linha poderia aparecer. InnoDB pode usar gap locks e next-key locks, especialmente em níveis de isolamento mais fortes e em leituras de faixa. PostgreSQL usa MVCC e, em `SERIALIZABLE`, mecanismos de conflito serializável que podem abortar transações, em vez de simplesmente manter o mesmo tipo de gap lock do InnoDB.

O efeito prático é que uma consulta por faixa pode interferir em um `INSERT` que aparentemente não atualiza nenhuma linha existente. O plano de execução, os índices e o isolamento fazem parte do comportamento de concorrência.

### Locks de intenção

Locks de intenção indicam que uma transação pretende adquirir locks de granularidade menor. Eles permitem que o mecanismo detecte conflitos entre uma operação que quer a tabela inteira e operações que mantêm locks em linhas. InnoDB usa locks de intenção para coordenar locks de tabela e de registro.

### Locks consultivos ou advisory

Um advisory lock representa uma chave definida pela aplicação, como "apenas um deploy de schema por vez". O banco pode coordenar processos que respeitam a mesma chave, mas não impede sozinho que outro processo ignore o protocolo e escreva na tabela.

Esse mecanismo pode ser útil para serializar jobs ou migrations, mas não substitui constraints, locks normais ou controle de concorrência sobre os dados. Sempre defina timeout e comportamento de recuperação.

## Modos de transação

### Autocommit

Em autocommit, cada statement confirmado forma sua própria transação. É conveniente para operações curtas, mas perigoso quando duas ou mais alterações precisam ser atômicas. Um backfill em autocommit pode liberar locks a cada lote; uma atualização de negócio que exige várias tabelas precisa de uma transação explícita.

### Transação explícita

`BEGIN`, `COMMIT` e `ROLLBACK` delimitam o conjunto de operações. A transação deve ser curta, previsível e livre de chamadas externas desnecessárias. Uma sessão que fica parada depois de `BEGIN` continua mantendo recursos e pode bloquear migrations, vacuum, DDL ou outras transações.

### Savepoints

`SAVEPOINT` e `ROLLBACK TO SAVEPOINT` permitem desfazer uma parte da transação sem cancelar todo o trabalho. Eles são úteis para processar itens independentes em uma transação maior, mas não tornam uma operação grande automaticamente segura. Em particular, voltar a um savepoint não é uma estratégia universal para liberar metadata locks.

### Somente leitura e somente escrita

Uma transação read-only pode proteger uma leitura contra alterações incompatíveis sem permitir DML local. Uma transação read-write pode modificar o estado. O suporte e as restrições exatas variam entre bancos, réplicas e níveis de isolamento.

### Níveis de isolamento

Os níveis mais comuns são:

- `READ UNCOMMITTED`: permite a menor proteção conceitual, embora alguns bancos implementem esse modo com semântica mais forte;
- `READ COMMITTED`: cada statement observa os commits válidos para o início daquele statement;
- `REPEATABLE READ`: a transação mantém uma visão mais estável, mas pode precisar abortar diante de conflitos;
- `SERIALIZABLE`: tenta produzir resultado equivalente a uma ordem serial e pode abortar transações concorrentes para preservar essa propriedade.

O nome do nível não garante comportamento idêntico entre PostgreSQL, MySQL e MariaDB. Compare anomalias permitidas, locks, snapshots, deadlocks, erros de serialização e política de retry do driver.

### DDL dentro de transações

PostgreSQL permite que muitas operações de DDL participem de transações e sejam revertidas, mas os locks continuam relevantes até o fim da transação. Em MySQL e MariaDB, muitas operações DDL produzem commits implícitos ou não têm a mesma reversibilidade de DML. Em Galera, o DDL também precisa obedecer ao método de atualização de schema do cluster.

Não envolva uma migration em uma transação apenas por hábito. Confirme se a engine suporta a operação como esperado, qual lock será adquirido e se o framework de migration não está mantendo o lock por mais tempo que a instrução exige.

## Como prevenir indisponibilidade

Antes de uma migration relevante:

- reproduza o schema e o volume aproximado em um ambiente de teste;
- confirme a versão do servidor, engine, extensão e topologia;
- verifique o plano de execução e o algoritmo de DDL;
- liste transações longas e sessões `idle in transaction`;
- defina `lock_timeout` ou equivalente para falhar sem esperar indefinidamente;
- defina `statement_timeout` ou um limite operacional para trabalho pesado;
- execute primeiro uma operação que não altere dados para validar permissões e compatibilidade;
- faça backup verificável e confirme o plano de rollback;
- monitore fila de locks, pool de conexões, CPU, I/O, espaço, lag e erros;
- use uma janela de baixo tráfego quando a alteração não puder ser expandida de forma compatível.

Durante a execução, interromper uma migration que está esperando por lock costuma ser mais seguro que deixar a fila crescer. Depois de cancelar, investigue o bloqueador; não mate sessões aleatoriamente sem verificar a transação e seu proprietário.

## Alternativas para tabelas grandes

Quando o DDL nativo não oferece risco aceitável, existem alternativas:

**Expand and contract** mantém versões antigas e novas do código compatíveis enquanto o dado é migrado gradualmente.

**Índice online ou concorrente** reduz o bloqueio de leitura e escrita quando o banco oferece essa operação, com restrições específicas de transação e falha parcial.

**Tabela sombra** cria uma tabela nova, copia ou replica os dados, acompanha alterações durante o backfill e faz uma troca curta. É poderosa, mas exige cuidado com triggers, chaves estrangeiras, sequences, grants, views, CDC, storage e rollback.

**Ferramenta de online schema change** automatiza uma variação de tabela sombra e pode usar triggers ou log de mudanças. Ela adiciona componentes e pontos de falha, portanto deve ser testada contra o modelo de escrita e a topologia do banco.

**Janela de manutenção** continua sendo uma opção válida quando a mudança realmente precisa de lock exclusivo, o sistema aceita indisponibilidade e a duração foi medida. Não é uma falha de arquitetura usar uma janela; é uma decisão explícita sobre disponibilidade.

## Diagnóstico

No PostgreSQL, investigue `pg_stat_activity`, `pg_locks` e `pg_blocking_pids`. Observe quem espera, quem bloqueia, há quanto tempo a transação está aberta e qual consulta criou o bloqueio.

No MySQL, use `SHOW FULL PROCESSLIST`, o Performance Schema, `metadata_locks`, `innodb_trx` e as tabelas de espera de locks. Estados como `Waiting for table metadata lock` apontam para uma fila de definição, mas o bloqueador pode ser uma conexão aparentemente inativa.

Em MariaDB, verifique os instrumentos disponíveis para metadata locks, `lock_wait_timeout`, estado do InnoDB e a situação do Galera. Em Galera, observe também o método de atualização de schema, estado do nó, flow control e filas de aplicação.

O diagnóstico deve ser feito antes e depois da migration. Uma migration "concluída" que deixou lag, transações abortadas, conexões presas ou sessões ociosas ainda pode ter causado um incidente.

## Checklist de revisão

Uma migration pronta para produção deve responder:

1. Qual é o lock mais forte que ela pode solicitar?
2. O que acontece se existir uma transação longa?
3. O trabalho lê ou reescreve todos os registros?
4. Qual algoritmo a versão real do banco escolherá?
5. A aplicação antiga continua funcionando durante a alteração?
6. O backfill pode ser pausado e retomado?
7. Como são tratados timeout, deadlock, retry e conexão perdida?
8. Como a mudança se comporta em réplicas, clusters e backups?
9. Qual é o critério de sucesso e qual é o plano de reversão?
10. Como saberemos que o sistema voltou ao estado saudável?

## Relações

- [Locks e transações no PostgreSQL](postgresql-locks-e-transacoes.md) é a referência
  específica sobre MVCC, modos de lock, isolamento, deadlocks e retries.
- [Transações e ACID](transacoes-acid.md) explica atomicidade, isolamento, durabilidade e limites transacionais.
- [Replicação](replicacao.md) explica lag, failover e por que cópias não são backups.
- [Clustering, redundância e distribuição](clustering-redundancia-e-distribuicao.md) compara topologias e domínios de falha.
- [Exclusão, edição, revisões e WAL](revisoes-exclusao-e-wal.md) relaciona mutações destrutivas, histórico e recuperação.

## Fontes

- [PostgreSQL, alteração de tabelas](https://www.postgresql.org/docs/current/ddl-alter.html)
- [PostgreSQL, locks explícitos](https://www.postgresql.org/docs/current/explicit-locking.html)
- [PostgreSQL, isolamento de transações](https://www.postgresql.org/docs/current/transaction-iso.html)
- [MySQL, metadata locking](https://dev.mysql.com/doc/refman/8.4/en/metadata-locking.html)
- [MySQL, performance e concorrência de DDL online](https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-performance.html)
- [MySQL, locks do InnoDB](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking.html)
- [MariaDB, metadata locking](https://mariadb.com/docs/server/reference/sql-statements/transactions/metadata-locking)
- [MariaDB, modos de lock do InnoDB](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-lock-modes)
- [MariaDB Galera, atualização de schema](https://mariadb.com/docs/galera-cluster/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster)
