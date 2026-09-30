# SQL avançado

SQL avançado não é escrever uma linha ilegível. É decompor uma pergunta em relações intermediárias, declarar regras com clareza e escolher a ferramenta que representa melhor o problema.

## `CASE`

`CASE` é uma expressão que produz um valor:

```sql
SELECT
    id,
    total,
    CASE
        WHEN total = 0 THEN 'free'
        WHEN total < 100 THEN 'small'
        WHEN total < 1000 THEN 'medium'
        ELSE 'large'
    END AS order_size
FROM orders;
```

Ele também pode ser usado dentro de agregações:

```sql
SELECT
    SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) AS paid_count,
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled_count
FROM orders;
```

## `COALESCE` e `NULLIF`

`COALESCE` retorna o primeiro valor não nulo:

```sql
SELECT id, COALESCE(phone, mobile_phone, 'sem telefone') AS contact
FROM users;
```

`NULLIF(a, b)` retorna `NULL` quando `a` e `b` são iguais. É útil para evitar divisão por zero:

```sql
SELECT
    COALESCE(confirmed / NULLIF(total, 0), 0) AS confirmation_rate
FROM stats;
```

## CTEs

CTEs, ou Common Table Expressions, criam relações nomeadas durante uma instrução:

```sql
WITH
orders_per_user AS (
    SELECT user_id, COUNT(*) AS total
    FROM orders
    GROUP BY user_id
),
active_users AS (
    SELECT id, name
    FROM users
    WHERE active = true
)
SELECT a.name, o.total
FROM active_users AS a
JOIN orders_per_user AS o ON o.user_id = a.id;
```

CTEs podem referenciar CTEs anteriores. Use nomes que expressem o conjunto e não a implementação.

## `WITH RECURSIVE`

Uma CTE recursiva possui uma parte inicial e uma parte que acrescenta novos resultados. Ela permite percorrer hierarquias, grafos com limites e sequências.

```sql
WITH RECURSIVE hierarchy AS (
    SELECT id, manager_id, name, 0 AS depth
    FROM employees
    WHERE id = 1

    UNION ALL

    SELECT e.id, e.manager_id, e.name, h.depth + 1
    FROM employees AS e
    JOIN hierarchy AS h ON e.manager_id = h.id
)
SELECT *
FROM hierarchy
ORDER BY depth, id;
```

Uma consulta recursiva precisa de uma condição que termine. Em grafos, proteja-se contra ciclos e imponha um limite de profundidade ou mantenha um caminho visitado.

## Funções de janela

Uma função de janela calcula sobre um conjunto relacionado sem colapsar as linhas como `GROUP BY` faz. `OVER` define a janela.

```sql
SELECT
    user_id,
    created_at,
    total,
    SUM(total) OVER (
        PARTITION BY user_id
        ORDER BY created_at, id
    ) AS running_total
FROM orders;
```

`PARTITION BY` separa grupos independentes. Sem ele, a janela considera o conjunto inteiro.

### Ranking

```sql
SELECT
    user_id,
    total,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY total DESC, id) AS row_number,
    RANK() OVER (PARTITION BY user_id ORDER BY total DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY user_id ORDER BY total DESC) AS dense_rank
FROM orders;
```

- `ROW_NUMBER()` sempre gera posições diferentes.
- `RANK()` dá a mesma posição para empates e deixa lacunas.
- `DENSE_RANK()` dá a mesma posição para empates sem deixar lacunas.

### Linha anterior e seguinte

```sql
SELECT
    user_id,
    created_at,
    total,
    LAG(total) OVER (PARTITION BY user_id ORDER BY created_at, id) AS previous_total,
    LEAD(total) OVER (PARTITION BY user_id ORDER BY created_at, id) AS next_total
FROM orders;
```

`FIRST_VALUE` e `LAST_VALUE` dependem da definição da moldura da janela. A moldura padrão nem sempre inclui a última linha que o leitor imagina; declare `ROWS BETWEEN ...` quando essa distinção importar.

```sql
SELECT
    user_id,
    created_at,
    total,
    AVG(total) OVER (
        PARTITION BY user_id
        ORDER BY created_at
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_average
FROM orders;
```

```sql
SELECT
    user_id,
    created_at,
    total,
    FIRST_VALUE(total) OVER (
        PARTITION BY user_id
        ORDER BY created_at, id
    ) AS first_total,
    LAST_VALUE(total) OVER (
        PARTITION BY user_id
        ORDER BY created_at, id
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_total
FROM orders;
```

Quando várias funções usam a mesma janela, um nome reduz repetição:

```sql
SELECT
    user_id,
    total,
    ROW_NUMBER() OVER user_window AS position,
    AVG(total) OVER user_window AS average_total
FROM orders
WINDOW user_window AS (
    PARTITION BY user_id
    ORDER BY created_at, id
);
```

## Operações de conjunto

As consultas precisam ter o mesmo número de colunas e tipos compatíveis:

```sql
SELECT email FROM newsletter_subscribers
UNION
SELECT email FROM customers;
```

`UNION` elimina duplicatas; `UNION ALL` preserva todas as linhas e costuma ser mais barato. `INTERSECT` retorna o que aparece nos dois conjuntos. `EXCEPT` retorna o que aparece no primeiro e não no segundo. O suporte e a precedência podem variar; use parênteses quando houver várias operações.

## `HAVING` e `FILTER`

`HAVING` filtra grupos. PostgreSQL também oferece `FILTER` para agregações condicionais:

```sql
SELECT
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE status = 'paid') AS paid,
    COUNT(*) FILTER (WHERE status = 'cancelled') AS cancelled
FROM orders;
```

Em bancos que não têm `FILTER`, use `SUM(CASE ...)` ou `COUNT(CASE ...)`.

Alguns bancos também oferecem `GROUPING SETS`, que permite escolher vários níveis de agrupamento na mesma consulta:

```sql
SELECT
    user_id,
    status,
    SUM(total) AS amount
FROM orders
GROUP BY GROUPING SETS ((user_id, status), (user_id), ());
```

`ROLLUP` é uma forma hierárquica comum de produzir parte desses subtotais; `GROUPING SETS` é mais explícito quando os níveis não formam uma simples hierarquia.

## `DISTINCT ON`

PostgreSQL oferece `DISTINCT ON` para escolher a primeira linha de cada grupo conforme uma ordenação:

```sql
SELECT DISTINCT ON (user_id)
    user_id, id, total, created_at
FROM orders
ORDER BY user_id, created_at DESC, id DESC;
```

Uma alternativa mais portável usa `ROW_NUMBER()` e filtra `row_number = 1`.

## `VALUES` como relação

`VALUES` pode representar dados pequenos dentro de uma consulta:

```sql
WITH priorities(code, weight) AS (
    VALUES ('urgent', 1), ('normal', 2), ('low', 3)
)
SELECT o.id, o.status, p.weight
FROM orders AS o
JOIN priorities AS p ON p.code = o.status;
```

Isso é útil para tabelas de mapeamento pequenas, testes e parâmetros estruturados.

## Conversão de tipo

`CAST` torna a conversão explícita:

```sql
SELECT CAST(total AS numeric(12, 2))
FROM orders;
```

Alguns bancos também aceitam `total::numeric`, mas essa forma é específica do PostgreSQL. Conversões podem falhar ou perder precisão; valide o domínio antes de converter.

## JSON

JSON pode ser uma boa forma de guardar atributos realmente variáveis, mas não deve substituir relações estáveis que precisam de integridade, índices e joins frequentes.

```sql
SELECT payload->>'plan' AS plan
FROM events
WHERE payload->>'kind' = 'signup';
```

A sintaxe de operadores, tipos e índices JSON diverge bastante. PostgreSQL diferencia `json` e `jsonb`; MySQL possui funções JSON próprias. Consulte [JSON](../bancos/documentos.md) e a documentação do banco antes de transportar a consulta.

## Colunas geradas

Uma coluna gerada deriva seu valor de outras colunas e pode evitar que a mesma fórmula seja repetida em várias escritas:

```sql
CREATE TABLE order_totals (
    quantity integer NOT NULL,
    unit_price numeric(12, 2) NOT NULL,
    total numeric(12, 2)
        GENERATED ALWAYS AS (quantity * unit_price) STORED
);
```

O suporte, a sintaxe e a possibilidade de indexar o resultado variam. Use uma coluna gerada quando a derivação for determinística e fizer parte do modelo; não a use para esconder uma regra de negócio que precisa de dados de outras linhas.

## ROLLUP

`ROLLUP` produz subtotais e total geral em bancos que oferecem agrupamento hierárquico:

```sql
SELECT
    user_id,
    status,
    SUM(total) AS amount
FROM orders
GROUP BY ROLLUP (user_id, status);
```

As linhas de subtotal usam `NULL` nas colunas que foram removidas do nível de agrupamento. Use `GROUPING` quando precisar distinguir esse subtotal de um valor originalmente nulo.

## `GREATEST` e `LEAST`

Essas funções comparam vários valores na mesma linha:

```sql
SELECT
    GREATEST(minimum_price, current_price) AS higher_price,
    LEAST(minimum_price, current_price) AS lower_price
FROM products;
```

O tratamento de `NULL` pode variar entre bancos. Se um valor ausente tiver significado, defina antes se ele deve ser ignorado ou tornar o resultado desconhecido.

## `EXPLAIN ANALYZE`

`EXPLAIN` mostra o plano estimado. PostgreSQL oferece `EXPLAIN ANALYZE` para executar a consulta e comparar estimativas com tempos e quantidades observados:

```sql
EXPLAIN ANALYZE
SELECT id, name
FROM users
WHERE email = 'ana@example.com';
```

Como essa forma executa a instrução, use-a com cuidado em `INSERT`, `UPDATE` e `DELETE`. Em consultas de leitura, ainda considere o custo real e o efeito de cache antes de concluir que um plano é bom ou ruim.
