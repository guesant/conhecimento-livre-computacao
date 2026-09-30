# Cheatsheet de SQL

Folha de consulta rápida para sintaxe comum. Os exemplos usam nomes genéricos e podem precisar de ajustes para o dialeto do banco.

## Estrutura

```sql
CREATE TABLE table_name (
    id integer PRIMARY KEY,
    name varchar(100) NOT NULL,
    code varchar(40) UNIQUE,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP,
    CHECK (name <> '')
);

ALTER TABLE table_name ADD COLUMN active boolean DEFAULT true;
ALTER TABLE table_name DROP COLUMN active;
DROP TABLE table_name;
```

## Inserir, atualizar e remover

```sql
INSERT INTO table_name (name, code)
VALUES ('Example', 'EX-1');

UPDATE table_name
SET name = 'Updated'
WHERE id = 1;

DELETE FROM table_name
WHERE id = 1;
```

Antes de `UPDATE` ou `DELETE`, execute:

```sql
SELECT *
FROM table_name
WHERE id = 1;
```

## Consultar

```sql
SELECT column_a, column_b
FROM table_name
WHERE column_a IS NOT NULL
  AND column_b IN ('a', 'b')
ORDER BY column_a DESC
LIMIT 20;
```

```sql
SELECT category, COUNT(*) AS total, SUM(amount) AS amount
FROM sales
WHERE status = 'paid'
GROUP BY category
HAVING COUNT(*) > 1
ORDER BY amount DESC;
```

## Joins

```sql
SELECT a.id, a.name, b.value
FROM table_a AS a
JOIN table_b AS b ON b.a_id = a.id;

SELECT a.id, COUNT(b.id) AS total
FROM table_a AS a
LEFT JOIN table_b AS b ON b.a_id = a.id
GROUP BY a.id;
```

## Agregações e valores nulos

```sql
SELECT
    COUNT(*) AS rows_count,
    COUNT(DISTINCT user_id) AS users_count,
    SUM(amount) AS total,
    AVG(amount) AS average,
    MIN(amount) AS minimum,
    MAX(amount) AS maximum
FROM payments;
```

```sql
SELECT
    COALESCE(phone, 'no phone') AS phone,
    NULLIF(total, 0) AS nonzero_total,
    CASE WHEN active THEN 'yes' ELSE 'no' END AS label
FROM users;
```

## CTE e janela

```sql
WITH totals AS (
    SELECT user_id, SUM(amount) AS total
    FROM payments
    GROUP BY user_id
)
SELECT *
FROM totals
WHERE total > 100;
```

```sql
SELECT
    user_id,
    amount,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at) AS sequence,
    LAG(amount) OVER (PARTITION BY user_id ORDER BY created_at) AS previous_amount
FROM payments;
```

## Existência e conjuntos

```sql
SELECT u.*
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.user_id = u.id
);
```

```sql
SELECT email FROM customers
UNION ALL
SELECT email FROM subscribers;
```

## Transações

```sql
BEGIN;
SAVEPOINT before_change;
ROLLBACK TO SAVEPOINT before_change;
COMMIT;
```

Ou, em caso de erro:

```sql
ROLLBACK;
```

## Diagnóstico

```sql
EXPLAIN SELECT * FROM users WHERE email = 'ana@example.com';
```

No PostgreSQL, `EXPLAIN ANALYZE` executa a consulta para medir o plano real. Não use essa forma sem avaliar os efeitos quando a instrução modifica dados.
