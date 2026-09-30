# Funções de janela

Funções de janela calculam informações sobre linhas relacionadas sem reduzir o resultado a uma linha por grupo. Elas são a ferramenta certa para ranking, comparação com a linha anterior, acumulados, percentis e seleção do primeiro registro de cada grupo.

## `NTILE`

`NTILE` divide cada partição em grupos aproximadamente iguais:

```sql
SELECT
    id,
    total,
    NTILE(4) OVER (ORDER BY total DESC) AS quartile
FROM orders;
```

Isso cria quatro faixas de posição, não quatro faixas de valor com a mesma amplitude.

## Distribuição e percentis

```sql
SELECT
    id,
    total,
    PERCENT_RANK() OVER (ORDER BY total) AS relative_rank,
    CUME_DIST() OVER (ORDER BY total) AS cumulative_distribution
FROM orders;
```

`PERCENT_RANK` varia de zero a um conforme a posição relativa. `CUME_DIST` indica a fração de linhas com valor menor ou igual ao atual. Empates e `NULL` precisam ser tratados conforme a regra do relatório.

Alguns bancos oferecem `PERCENTILE_CONT` e `PERCENTILE_DISC`:

```sql
SELECT
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total) AS median
FROM orders;
```

`PERCENTILE_CONT` pode interpolar um valor; `PERCENTILE_DISC` escolhe um valor observado. O suporte é específico do banco.

## `NTH_VALUE`

```sql
SELECT
    user_id,
    total,
    NTH_VALUE(total, 2) OVER (
        PARTITION BY user_id
        ORDER BY created_at, id
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS second_order_total
FROM orders;
```

A moldura completa é importante para que a segunda linha permaneça visível em todas as linhas da partição.

## Top-N por grupo

```sql
WITH ranked AS (
    SELECT
        user_id,
        id,
        total,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY total DESC, id
        ) AS position
    FROM orders
)
SELECT *
FROM ranked
WHERE position <= 3;
```

Use `RANK` quando empates devem compartilhar a posição e `ROW_NUMBER` quando o resultado precisa ter exatamente N linhas por grupo.

## Diferença entre linhas

```sql
SELECT
    created_at,
    total,
    total - LAG(total) OVER (
        PARTITION BY user_id
        ORDER BY created_at, id
    ) AS change_from_previous
FROM orders;
```

O primeiro valor da partição será `NULL`. `COALESCE` pode fornecer um valor padrão, mas só depois de decidir se “não existe linha anterior” é semanticamente igual a zero.

## Lacunas e ilhas

Uma técnica comum identifica sequências consecutivas:

```sql
WITH numbered AS (
    SELECT
        user_id,
        activity_date,
        activity_date - ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY activity_date
        ) * INTERVAL '1 day' AS island_key
    FROM daily_activity
)
SELECT user_id, MIN(activity_date), MAX(activity_date), COUNT(*)
FROM numbered
GROUP BY user_id, island_key;
```

A expressão de data varia por dialeto. A ideia é criar uma chave que permaneça constante dentro de uma sequência sem lacunas.

## Sessões

Uma sessão pode começar quando o intervalo desde o evento anterior ultrapassar um limite:

```sql
WITH marked AS (
    SELECT
        user_id,
        occurred_at,
        CASE
            WHEN occurred_at - LAG(occurred_at) OVER (
                PARTITION BY user_id
                ORDER BY occurred_at
            ) > INTERVAL '30 minutes'
            OR LAG(occurred_at) OVER (
                PARTITION BY user_id
                ORDER BY occurred_at
            ) IS NULL
            THEN 1 ELSE 0
        END AS starts_session
    FROM events
),
numbered AS (
    SELECT *, SUM(starts_session) OVER (
        PARTITION BY user_id
        ORDER BY occurred_at
    ) AS session_number
    FROM marked
)
SELECT user_id, session_number, MIN(occurred_at), MAX(occurred_at), COUNT(*)
FROM numbered
GROUP BY user_id, session_number;
```

Para consultas grandes, evite repetir a mesma janela sem necessidade. Dê nome à janela ou materialize uma etapa intermediária quando isso melhorar leitura e plano.
