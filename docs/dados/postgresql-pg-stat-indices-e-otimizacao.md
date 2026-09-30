# Mapa de diagnóstico e otimização do PostgreSQL

Otimizar PostgreSQL não significa adicionar índices até o plano deixar de mostrar `Seq Scan` ou aumentar parâmetros de memória sem medir. A pergunta correta é qual recurso está limitando a operação observada, em qual consulta, sob qual volume e com qual contrato de latência.

Uma requisição lenta pode estar esperando um lock, lendo páginas demais, usando um plano baseado em estatísticas antigas, fazendo sort ou hash que não cabe na memória, aguardando I/O, sofrendo com bloat, repetindo uma consulta por causa de N+1 ou esperando uma réplica. Um índice ausente é somente uma das hipóteses.

## O que observar primeiro

Separe o diagnóstico em quatro dimensões:

- **tempo de CPU:** parsing, planejamento, joins, agregações, funções e serialização;
- **I/O:** leituras físicas, cache, escrita de WAL, checkpoints, vacuum e storage;
- **concorrência:** locks, deadlocks, sessões longas, pool esgotado e filas;
- **plano:** cardinalidade estimada, seletividade, ordem dos joins, método de acesso e custo de sort ou hash.

O mesmo SQL pode ser rápido para dez linhas e caro para milhões. Também pode ser rápido em uma tabela uniforme e ruim quando os dados ficam concentrados em poucos valores. Toda conclusão deve registrar a consulta, parâmetros representativos, tamanho da tabela, versão do PostgreSQL, plano e ambiente.

## A família `pg_stat`

As views `pg_stat*` formam o primeiro ponto de observação nativo. Elas combinam informação dinâmica do que está acontecendo agora com contadores acumulados de acessos, I/O, vacuum, WAL e replicação.

Os contadores acumulados não são um stream instantâneo. Eles podem ser atualizados com atraso, ser observados por meio de um snapshot de estatísticas da transação e ser reiniciados após eventos como restart não limpo. Ao comparar períodos, registre quando os contadores foram zerados e use uma diferença temporal, em vez de interpretar um valor absoluto isolado como tendência.

### `pg_stat_activity`

`pg_stat_activity` mostra uma linha por processo do servidor. É a view para descobrir quem está ativo, quem está parado dentro de uma transação e qual sessão está esperando.

Uma consulta inicial pode ser:

```sql
SELECT
  pid,
  usename,
  datname,
  application_name,
  client_addr,
  state,
  wait_event_type,
  wait_event,
  clock_timestamp() - query_start AS query_age,
  clock_timestamp() - xact_start AS transaction_age,
  query
FROM pg_stat_activity
WHERE state IS DISTINCT FROM 'idle'
ORDER BY COALESCE(xact_start, query_start) NULLS LAST;
```

Os estados merecem interpretações diferentes:

- `active` significa que o backend está executando uma consulta, mas ele ainda pode estar esperando um evento;
- `idle` é uma conexão disponível aguardando o próximo comando;
- `idle in transaction` indica uma transação aberta sem consulta em execução, situação que pode reter locks e impedir vacuum;
- `idle in transaction (aborted)` exige rollback antes que a conexão possa continuar normalmente;
- `wait_event_type = 'Lock'` aponta para espera de lock pesado, mas I/O, IPC, buffer pin e outros eventos também podem explicar latência.

`query_start` mede a consulta atual ou a última consulta, enquanto `xact_start` ajuda a encontrar uma transação antiga que pode estar bloqueando a manutenção. O texto de `query` pode estar truncado e não substitui um identificador de consulta.

### Bloqueadores e `pg_locks`

Para investigar uma sessão esperando:

```sql
SELECT
  blocked.pid AS blocked_pid,
  blocked.query AS blocked_query,
  blocker.pid AS blocker_pid,
  blocker.state AS blocker_state,
  blocker.query AS blocker_query,
  clock_timestamp() - blocker.xact_start AS blocker_transaction_age
FROM pg_stat_activity AS blocked
JOIN LATERAL unnest(pg_blocking_pids(blocked.pid)) AS blocker_pid
  ON true
JOIN pg_stat_activity AS blocker
  ON blocker.pid = blocker_pid
WHERE blocked.wait_event_type = 'Lock';
```

`pg_locks` mostra os locks concedidos e aguardados. A view precisa ser relacionada com `pg_stat_activity` pelo PID e, quando necessário, com a relação ou transação envolvida. Não mate a sessão mais antiga automaticamente: primeiro identifique se ela pertence a uma operação crítica, se a aplicação conseguirá repetir a transação e se o cancelamento é menos perigoso que manter a fila.

### `pg_stat_database`

`pg_stat_database` fornece uma visão por banco, incluindo sessões, transações, commits, rollbacks, blocos lidos, blocos encontrados no cache, conflitos em recovery, deadlocks e tempo de I/O quando a medição correspondente está habilitada.

A razão entre blocos encontrados e blocos lidos pode sugerir comportamento de cache, mas não deve ser tratada como uma nota de desempenho. A estatística não mostra sozinha se o conjunto quente cabe na memória, se há pressão no cache do sistema operacional ou se uma consulta está lendo dados desnecessários.

### `pg_stat_user_tables`

`pg_stat_user_tables` ajuda a encontrar tabelas com perfil de acesso problemático:

```sql
SELECT
  relname,
  seq_scan,
  seq_tup_read,
  idx_scan,
  idx_tup_fetch,
  n_live_tup,
  n_dead_tup,
  last_analyze,
  last_autoanalyze,
  last_vacuum,
  last_autovacuum
FROM pg_stat_user_tables
ORDER BY seq_tup_read DESC;
```

Muitos `seq_scan` não significam automaticamente falta de índice. Uma varredura sequencial pode ser a melhor escolha quando a consulta precisa de grande parte da tabela ou quando a tabela é pequena. O sinal mais útil é combinar o contador com o volume lido, a consulta real, o plano e a seletividade do predicado.

`n_dead_tup` alto pode indicar atualização ou exclusão intensa, autovacuum atrasado, transações longas ou bloat. O valor é estimado e não substitui uma medição específica, mas é suficiente para indicar onde investigar.

### `pg_stat_user_indexes` e `pg_statio_*`

`pg_stat_user_indexes` mostra acessos por índice, enquanto `pg_statio_user_tables` e `pg_statio_user_indexes` mostram estatísticas de blocos. Esses dados ajudam a localizar índices que nunca aparecem no workload observado e estruturas que causam mais I/O do que o esperado.

Um índice com `idx_scan = 0` não deve ser removido imediatamente. O contador pode ter sido zerado, a janela observada pode não incluir uma rotina mensal, o índice pode existir para uma constraint ou pode ser necessário somente em uma consulta rara e crítica. A remoção exige inventário de constraints, dependências, workload e janela de observação suficiente.

### `pg_stat_io`

Nas versões que o suportam, `pg_stat_io` detalha I/O por tipo de backend, contexto e objeto. Ele ajuda a diferenciar uma consulta que está consumindo CPU de uma que está produzindo leituras, escritas ou extensões de relação. Use-o com métricas do sistema operacional, porque a view não explica sozinha o comportamento do filesystem, do dispositivo, do cache do kernel ou do volume remoto.

### `pg_stat_statements`

`pg_stat_statements` agrega estatísticas por consulta normalizada. Ele é útil para descobrir as consultas que mais acumulam tempo, as que têm maior média, as que executam muitas vezes e as que produzem mais leituras ou escritas.

Exemplo de investigação:

```sql
SELECT
  calls,
  total_exec_time,
  mean_exec_time,
  rows,
  shared_blks_hit,
  shared_blks_read,
  temp_blks_read,
  temp_blks_written,
  query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;
```

O ranking precisa ser escolhido pela pergunta. `total_exec_time` encontra impacto agregado; `mean_exec_time` encontra latência média; `calls` encontra hot paths; blocos lidos e temporários ajudam a localizar pressão de I/O e operações que derramam para disco. Uma consulta lenta executada uma única vez pode merecer atenção operacional mesmo que não apareça no topo do impacto total.

Não compare consultas apenas pelo texto. Parâmetros, cardinalidade, plano genérico, plano customizado, cache e concorrência podem mudar o custo. Adicione tags ou `application_name` quando precisar distinguir chamadas legítimas com o mesmo SQL.

## `EXPLAIN` e evidência do plano

`EXPLAIN` mostra o plano estimado. `EXPLAIN ANALYZE` executa a consulta e compara estimativas com valores reais. Para leitura, uma forma comum de investigação é:

```sql
EXPLAIN (ANALYZE, BUFFERS, SETTINGS, VERBOSE)
SELECT id, title
FROM findings
WHERE locale = 'pt-BR'
  AND published_at IS NOT NULL
ORDER BY published_at DESC, id DESC
LIMIT 20;
```

`ANALYZE` realmente executa a instrução. Não o use casualmente em `UPDATE`, `DELETE`, `INSERT`, funções com efeitos colaterais ou consultas que publiquem eventos. Para esses casos, prefira um ambiente representativo, uma cópia controlada ou uma estratégia de teste que não altere dados reais.

Ao ler o plano, procure:

- diferença grande entre `rows` estimado e `actual rows`;
- nós que processam muito mais linhas do que entregam ao próximo estágio;
- `Seq Scan` em tabelas grandes quando o predicado deveria ser seletivo;
- `Index Scan` que visita muitas páginas aleatórias e acaba sendo pior que uma varredura sequencial;
- `Sort` ou `Hash` com `Disk` ou `temp read/write` elevados;
- loops internos executando milhares de vezes por causa de um Nested Loop mal estimado;
- `Buffers: read` alto em uma consulta que deveria estar quente;
- espera ou variação de tempo que não aparece no plano isolado.

Um `Seq Scan` não é um erro. Um índice também não é uma melhoria garantida. O plano deve ser avaliado com a cardinalidade e o workload reais.

## Falhas de performance relacionadas a índices

### Índice ausente

Um índice pode ser necessário quando uma consulta filtra ou faz join repetidamente por uma coluna seletiva, ordena por um conjunto estável ou valida uma existência sem precisar ler toda a tabela. A existência do índice deve corresponder ao formato da consulta:

```sql
CREATE INDEX CONCURRENTLY findings_locale_published_idx
  ON findings (locale, published_at DESC, id DESC);
```

O exemplo atende a uma consulta que filtra por `locale`, ordena por `published_at` e `id` e limita o resultado. O índice correto para outra consulta pode ter outra ordem, outro predicado ou nenhuma relação com essas colunas.

### Ordem incorreta em índice composto

Em um índice B-tree composto, a ordem das colunas influencia quais predicados podem restringir a busca e quais partes podem atender à ordenação. Uma regra simplificada é colocar primeiro as colunas usadas em igualdade, depois as colunas de faixa e, quando fizer sentido, as colunas que completam a ordenação. Isso não é uma fórmula universal: seletividade, distribuição, custo de sort e diferentes consultas precisam ser medidos.

Um índice `(status, created_at)` pode ajudar uma consulta que filtra por `status` e ordena por `created_at`. Ele pode ser pouco útil para filtrar somente por `created_at`, dependendo da distribuição e do tamanho da tabela. Não crie a ordem apenas copiando a ordem visual do `WHERE` sem olhar o plano.

### Índice com baixa seletividade

Colunas booleanas, estados com poucos valores e flags presentes na maioria das linhas podem não reduzir o trabalho o suficiente para justificar um índice completo. O PostgreSQL pode preferir uma varredura sequencial porque visitar o índice e depois muitas páginas da tabela custa mais.

Um índice parcial pode ser melhor quando o workload acessa uma pequena parte estável dos dados:

```sql
CREATE INDEX CONCURRENTLY findings_published_idx
  ON findings (published_at DESC, id DESC)
  WHERE published_at IS NOT NULL;
```

O predicado da consulta precisa ser reconhecível como compatível com o predicado do índice. Um índice parcial não é um índice universal para a coluna e não deve ser criado sem confirmar os filtros reais.

### Funções, casts e expressões

Aplicar uma função ao lado indexado pode impedir o uso do índice comum:

```sql
WHERE lower(email) = 'user@example.com'
```

Se essa busca é necessária, avalie um índice de expressão e uma política de normalização:

```sql
CREATE INDEX users_lower_email_idx
  ON users (lower(email));
```

Também investigue casts implícitos, comparação de tipos diferentes, operadores que não pertencem à classe de operador esperada, `LIKE` com wildcard inicial e expressões que transformam uma condição indexável em cálculo por linha. Um índice de expressão resolve um padrão conhecido, mas aumenta o custo de escrita e precisa respeitar a imutabilidade exigida pelo PostgreSQL.

### Índices em joins e foreign keys

A coluna referenciada por uma foreign key normalmente possui uma primary key ou unique index. A coluna que referencia não recebe automaticamente o mesmo índice em todos os modelos de banco. Sem um índice no lado filho, exclusões ou atualizações do pai e joins por essa relação podem exigir varreduras grandes.

Verifique as queries de join e as operações de manutenção antes de adicionar índices indiscriminadamente. Um índice no lado filho costuma ser útil, mas a ordem de colunas e a necessidade de incluir filtros adicionais ainda dependem do workload.

### Cobertura e index-only scan

Um índice que contém as colunas necessárias pode permitir um index-only scan, reduzindo acessos à heap quando o visibility map permite. Adicionar colunas com `INCLUDE` pode reduzir I/O de leitura, mas aumenta o tamanho do índice, o custo de escrita e o tempo de vacuum. Cobertura não é sinônimo de colocar todas as colunas em todos os índices.

### Índices demais ou redundantes

Cada índice é mantido durante `INSERT`, `UPDATE` e `DELETE`, ocupa storage, aumenta WAL e pode sofrer bloat. Índices quase iguais também complicam o planner e a operação.

Antes de criar mais um índice:

1. procure um índice existente que cubra a consulta;
2. confirme se a ordem das colunas e o predicado são compatíveis;
3. meça o plano antes e depois;
4. observe o custo de escrita e o tamanho da estrutura;
5. documente qual consulta e qual SLO justificam a mudança.

## Estatísticas ruins também parecem falta de índice

O planner escolhe o plano com base em estimativas. Estatísticas antigas, amostras inadequadas, distribuição muito assimétrica, colunas correlacionadas e combinações que o planner não consegue estimar podem levar a um plano ruim mesmo quando o índice correto existe.

Depois de uma grande carga, atualização ou mudança de distribuição, execute `ANALYZE` ou deixe o autovacuum analisar a tabela. Aumentar a estatística de uma coluna pode melhorar a estimativa para valores muito variados, mas também eleva o custo e o tamanho das estatísticas. Faça isso para uma hipótese específica, não como ajuste genérico.

Se duas colunas são fortemente relacionadas, estatísticas estendidas podem ajudar o planner. Ainda assim, a medição precisa usar os valores e os predicados reais da aplicação.

## Vacuum, bloat e visibilidade

PostgreSQL usa MVCC. Atualizações e exclusões deixam versões antigas que precisam ser recuperadas pelo vacuum quando não há transações antigas impedindo a remoção. Uma transação aberta por muito tempo pode manter o horizonte de visibilidade antigo, aumentar a tabela, reduzir a efetividade do vacuum e gerar consultas cada vez mais pesadas.

Observe `n_dead_tup`, `last_autovacuum`, `last_autoanalyze`, duração de transações e crescimento do storage juntos. Não trate `VACUUM FULL` como manutenção de rotina: ele reescreve a tabela e exige lock forte. Ajustar autovacuum por tabela pode ser adequado para uma tabela de alta mutabilidade, mas os parâmetros devem ser baseados em taxa de mudança e não apenas em tamanho absoluto.

## Otimizações fora do índice

Quando a consulta já usa um acesso adequado, investigue outras fontes de trabalho:

- selecione somente as colunas necessárias;
- evite N+1 no código da aplicação;
- substitua `OFFSET` profundo por paginação por cursor ou keyset quando a ordenação permitir;
- filtre cedo e reduza a cardinalidade antes de joins e agregações;
- evite ordenar um conjunto muito maior que o resultado solicitado;
- use `EXISTS` quando a pergunta for somente se existe uma linha;
- mova cálculos repetidos para uma projeção, cache ou materialized view quando o contrato aceitar atraso;
- não faça chamadas HTTP dentro da consulta ou da transação;
- separe leitura crítica de relatório pesado;
- limite concorrência em jobs que competem pelo mesmo I/O.

Uma mudança que reduz o tempo de banco mas aumenta a quantidade de chamadas da aplicação pode piorar a latência total. Meça o caminho completo, incluindo pool, serialização, rede e cache.

## Processo de otimização

Use um ciclo controlado:

1. Defina o sintoma e o SLO, por exemplo p95 de uma consulta ou tempo total de uma rota.
2. Encontre as consultas de maior impacto em `pg_stat_statements` e confirme a janela observada.
3. Verifique `pg_stat_activity`, locks, I/O, vacuum, pool e replicação para eliminar causas externas ao plano.
4. Capture `EXPLAIN` com parâmetros representativos e compare estimativas com valores reais.
5. Formule uma hipótese, como estatística velha, índice incompatível, sort em disco ou lock.
6. Faça uma alteração por vez em ambiente representativo.
7. Meça latência, CPU, I/O, WAL, bloat, throughput e efeito nas escritas.
8. Promova somente se a melhoria persistir sob concorrência e não degradar outros workloads.
9. Mantenha observabilidade pós-deploy e um plano de reversão.

Não use uma execução isolada como prova. Um plano pode mudar por cache, parâmetro, estatística, concorrência, tamanho da tabela ou versão do PostgreSQL.

## Operação segura de índices

Em tabelas acessadas por produção, `CREATE INDEX CONCURRENTLY` pode reduzir bloqueios de escrita, mas executa mais trabalho, demora mais e não pode ser usado da mesma forma que um `CREATE INDEX` dentro de uma transação comum. Ele também pode deixar um índice inválido após falha, que deve ser identificado e tratado.

`REINDEX CONCURRENTLY` e outras formas concorrentes têm trade-offs semelhantes. Antes de remover ou reconstruir um índice, verifique locks, espaço temporário, WAL, réplicas, janela e possibilidade de rollback.

## Relações

- [Migrações de schema, locks e transações](migracoes-schema-locking.md) explica como DDL e transações podem bloquear a aplicação.
- [Transações e ACID](transacoes-acid.md) define isolamento, atomicidade e limites transacionais.
- [Replicação](replicacao.md) explica lag, failover e o impacto de carga de I/O nas cópias.
- [Clustering, redundância e distribuição](clustering-redundancia-e-distribuicao.md) relaciona performance com topologia e domínio de falha.

## Fontes

- [PostgreSQL, cumulative statistics system](https://www.postgresql.org/docs/current/monitoring-stats.html)
- [PostgreSQL, `pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html)
- [PostgreSQL, `EXPLAIN`](https://www.postgresql.org/docs/current/using-explain.html)
- [PostgreSQL, tipos de índice](https://www.postgresql.org/docs/current/indexes-types.html)
- [PostgreSQL, índices multicoluna](https://www.postgresql.org/docs/current/indexes-multicolumn.html)
- [PostgreSQL, índices parciais](https://www.postgresql.org/docs/current/indexes-partial.html)
- [PostgreSQL, índices de expressão](https://www.postgresql.org/docs/current/indexes-expressional.html)
- [PostgreSQL, vacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html)
