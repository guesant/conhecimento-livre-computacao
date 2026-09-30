# DML avançado

Depois de dominar `INSERT`, `UPDATE` e `DELETE`, o próximo passo é combinar mutações com consultas, representar operações idempotentes e criar abstrações de leitura sem esconder regras importantes.

## `INSERT ... SELECT`

```sql
INSERT INTO order_archive (id, user_id, status, total, created_at)
SELECT id, user_id, status, total, created_at
FROM orders
WHERE created_at < TIMESTAMP '2024-01-01';
```

O `SELECT` deve ser revisado antes da mutação. Se o processo puder ser repetido, a tabela de destino precisa de uma chave ou condição que impeça duplicatas.

## `UPDATE ... FROM`

PostgreSQL permite atualizar uma tabela usando outra relação:

```sql
UPDATE users AS u
SET last_order_at = recent.created_at
FROM (
    SELECT user_id, MAX(created_at) AS created_at
    FROM orders
    GROUP BY user_id
) AS recent
WHERE recent.user_id = u.id;
```

Se a relação usada no `FROM` tiver mais de uma linha para o mesmo destino, o resultado pode ser surpreendente. Garanta uma linha por alvo ou agregue antes.

## `DELETE ... USING`

No PostgreSQL, uma remoção relacionada pode ser escrita assim:

```sql
DELETE FROM orders AS o
USING users AS u
WHERE o.user_id = u.id
  AND u.deleted_at IS NOT NULL;
```

Em outros bancos, use `DELETE` com `JOIN`, `EXISTS` ou uma subconsulta equivalente. A regra de segurança é a mesma: pré-visualize o conjunto e confirme as relações.

## `MERGE`

`MERGE` combina inserção, atualização e, em alguns bancos, exclusão conforme a correspondência entre origem e destino:

```sql
MERGE INTO customer_summary AS target
USING daily_customers AS source
ON target.customer_id = source.customer_id
WHEN MATCHED THEN
    UPDATE SET total_orders = source.total_orders
WHEN NOT MATCHED THEN
    INSERT (customer_id, total_orders)
    VALUES (source.customer_id, source.total_orders);
```

O suporte e as garantias variam por SGBD. Não trate `MERGE` como automaticamente atômico ou livre de condições de corrida: entenda as restrições, índices e isolamento do banco utilizado.

## UPSERT idempotente

Uma operação repetível precisa de uma chave que represente o evento:

```sql
INSERT INTO payments (external_id, user_id, amount)
VALUES ('payment-123', 10, 50.00)
ON CONFLICT (external_id) DO NOTHING;
```

A chave `external_id` é o que transforma uma repetição em uma confirmação do mesmo evento. Um `SELECT` seguido de `INSERT` sem proteção concorrente não oferece a mesma garantia.

## `RETURNING`

PostgreSQL pode devolver as linhas afetadas:

```sql
UPDATE orders
SET status = 'paid'
WHERE id = 42
RETURNING id, status, updated_at;
```

Isso evita uma leitura posterior e permite que a aplicação observe exatamente o resultado da mutação. Em outros bancos, verifique o suporte e o equivalente disponível.

## Views

Uma view dá nome a uma consulta:

```sql
CREATE VIEW active_users AS
SELECT id, name, email
FROM users
WHERE active = true;
```

Views são úteis para contratos de leitura, simplificação, compatibilidade e segurança. Elas não são automaticamente snapshots: normalmente executam a consulta quando são lidas.

```sql
SELECT *
FROM active_users
WHERE email LIKE '%@example.com';
```

Uma view pode esconder joins e filtros importantes. Documente a semântica, teste o plano e evite criar camadas tão profundas que ninguém consiga explicar o custo da consulta.

## Materialized views

Uma materialized view armazena o resultado e precisa ser atualizada:

```sql
CREATE MATERIALIZED VIEW monthly_sales AS
SELECT DATE_TRUNC('month', created_at) AS month,
       SUM(total) AS revenue
FROM orders
GROUP BY 1;

REFRESH MATERIALIZED VIEW monthly_sales;
```

Ela troca custo de leitura por custo de atualização e pode ficar desatualizada. Avalie frequência de refresh, concorrência, índices sobre o resultado e comportamento durante a atualização.

## Colunas geradas

Uma coluna gerada é calculada a partir de outras colunas:

```sql
CREATE TABLE order_totals (
    quantity integer NOT NULL,
    unit_price numeric(12, 2) NOT NULL,
    total numeric(12, 2)
        GENERATED ALWAYS AS (quantity * unit_price) STORED
);
```

O suporte e a sintaxe variam. Colunas geradas devem usar expressões determinísticas e não podem substituir uma regra que depende de outras linhas ou tabelas.

## `PIVOT` e relatórios cruzados

Quando o banco não possui `PIVOT`, agregações condicionais são uma forma portátil:

```sql
SELECT
    user_id,
    SUM(CASE WHEN status = 'paid' THEN total ELSE 0 END) AS paid,
    SUM(CASE WHEN status = 'pending' THEN total ELSE 0 END) AS pending,
    SUM(CASE WHEN status = 'cancelled' THEN total ELSE 0 END) AS cancelled
FROM orders
GROUP BY user_id;
```

O formato é útil para relatórios, mas valores dinâmicos não viram colunas automaticamente. Quando as categorias mudam com frequência, mantenha o resultado normalizado e deixe a pivotagem para a ferramenta de apresentação.
