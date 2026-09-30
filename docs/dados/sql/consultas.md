# SQL: consultas

Uma consulta transforma relações de entrada em um resultado. A ordem em que você escreve as cláusulas não é exatamente a ordem conceitual em que o banco raciocina. Em geral, o conjunto é filtrado por `FROM` e `WHERE`, agrupado por `GROUP BY`, filtrado por `HAVING`, projetado por `SELECT` e ordenado por `ORDER BY`.

## Selecionar colunas

```sql
SELECT id, name, email
FROM users;
```

`SELECT *` é útil para explorar uma tabela, mas consultas de aplicação devem preferir colunas explícitas. Isso reduz dados transferidos, evita dependência acidental de colunas novas e deixa o contrato do resultado visível.

Use aliases para tornar a saída e as relações legíveis:

```sql
SELECT
    u.name AS customer_name,
    o.total AS order_total
FROM users AS u
JOIN orders AS o ON o.user_id = u.id;
```

## Filtrar com `WHERE`

```sql
SELECT id, name
FROM users
WHERE name LIKE 'Ana%'
  AND email IS NOT NULL;
```

Operadores comuns são `=`, `<>`, `>`, `>=`, `<`, `<=`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`, `IS NOT NULL`, `AND`, `OR` e `NOT`.

Parênteses tornam a intenção clara:

```sql
SELECT *
FROM orders
WHERE status = 'paid'
  AND (total >= 100 OR created_at >= DATE '2025-01-01');
```

Não compare com `NULL` usando `=`. A lógica de três valores pode fazer uma condição parecer falsa quando ela é desconhecida.

`BETWEEN` normalmente inclui os dois limites. `LIKE` usa `%` para zero ou mais caracteres e `_` para exatamente um caractere:

```sql
SELECT * FROM users WHERE name LIKE 'Ana%';
SELECT * FROM orders WHERE total BETWEEN 100 AND 500;
```

## Ordenar e limitar

```sql
SELECT id, name, created_at
FROM users
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

Inclua um critério estável de desempate. Sem `id` no exemplo, duas linhas com o mesmo `created_at` podem aparecer em ordem diferente entre execuções.

Paginação por offset é simples:

```sql
SELECT id, name
FROM users
ORDER BY id
LIMIT 20 OFFSET 40;
```

Para tabelas grandes ou dados que mudam enquanto o usuário pagina, keyset pagination costuma ser mais estável:

```sql
SELECT id, name
FROM users
WHERE id > 40
ORDER BY id
LIMIT 20;
```

## Distinção

`DISTINCT` elimina duplicidades do resultado projetado:

```sql
SELECT DISTINCT status
FROM orders;
```

Ele não substitui um join correto nem resolve uma relação que deveria ser modelada. Usar `DISTINCT` para esconder duplicação inesperada pode esconder um erro de cardinalidade.

## Joins

Um `JOIN` combina linhas de relações usando uma condição. O tipo do join define o que acontece quando não há correspondência.

```sql
SELECT
    u.name,
    o.id AS order_id,
    o.total
FROM users AS u
JOIN orders AS o
    ON o.user_id = u.id;
```

`INNER JOIN` retorna somente correspondências. `LEFT JOIN` mantém todas as linhas da esquerda:

```sql
SELECT
    u.id,
    u.name,
    COUNT(o.id) AS order_count
FROM users AS u
LEFT JOIN orders AS o
    ON o.user_id = u.id
GROUP BY u.id, u.name;
```

Esse padrão inclui usuários sem pedidos. Se você colocar uma condição de `orders` no `WHERE`, pode transformar o `LEFT JOIN` em um inner join acidental:

```sql
SELECT u.id, u.name
FROM users AS u
LEFT JOIN orders AS o ON o.user_id = u.id
WHERE o.status = 'paid';
```

Quando a condição deve preservar usuários sem pedidos, coloque-a no `ON`:

```sql
LEFT JOIN orders AS o
    ON o.user_id = u.id
   AND o.status = 'paid'
```

`RIGHT JOIN` é equivalente com a perspectiva invertida. `FULL OUTER JOIN`, quando disponível, preserva linhas sem correspondência dos dois lados. `CROSS JOIN` produz o produto cartesiano e deve ser intencional.

## Agregações

Funções agregadas reduzem várias linhas a um valor: `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`.

```sql
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(total) AS revenue,
    AVG(total) AS average_order
FROM orders
GROUP BY status;
```

`COUNT(*)` conta linhas. `COUNT(column)` ignora `NULL`. `COUNT(DISTINCT column)` conta valores distintos não nulos.

## `GROUP BY` e `HAVING`

`WHERE` filtra linhas antes do agrupamento. `HAVING` filtra grupos depois da agregação:

```sql
SELECT
    user_id,
    COUNT(*) AS total_orders
FROM orders
WHERE status <> 'cancelled'
GROUP BY user_id
HAVING COUNT(*) >= 3;
```

Uma coluna selecionada que não é agregada normalmente precisa aparecer no `GROUP BY`. Alguns bancos aceitam exceções quando conseguem inferir dependência funcional, mas não dependa dessa variação em SQL portável.

## Subconsultas

Uma subconsulta pode produzir um valor, uma relação ou uma condição:

```sql
SELECT *
FROM orders
WHERE total > (
    SELECT AVG(total)
    FROM orders
);
```

Use `EXISTS` quando a pergunta for “existe uma linha relacionada?”:

```sql
SELECT u.id, u.name
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.user_id = u.id
      AND o.status = 'paid'
);
```

`EXISTS` pode ser melhor que um `JOIN` quando você não quer multiplicar linhas. Para a pergunta oposta, use `NOT EXISTS` e tenha cuidado com `NOT IN` quando o conjunto puder conter `NULL`.

## Consultas com várias etapas

Uma CTE dá nome a uma relação lógica durante a consulta:

```sql
WITH order_counts AS (
    SELECT user_id, COUNT(*) AS total
    FROM orders
    GROUP BY user_id
)
SELECT u.name, c.total
FROM users AS u
JOIN order_counts AS c ON c.user_id = u.id
WHERE c.total >= 3;
```

CTE melhora a leitura, mas não é automaticamente uma tabela temporária nem sempre melhora desempenho. Leia o plano e considere a quantidade de dados.

## Subconsultas escalares

Uma subconsulta pode produzir um único valor e ser usada numa condição ou projeção:

```sql
SELECT name, total
FROM orders
WHERE total = (SELECT MAX(total) FROM orders);
```

Se houver empate, a consulta retorna todas as linhas empatadas. Se a subconsulta puder retornar várias linhas, use `IN`, `EXISTS` ou transforme-a numa relação com `JOIN` ou CTE.

## Funções de data e número

Funções de data variam bastante por banco, mas as perguntas são recorrentes:

```sql
SELECT CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP;

SELECT
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month
FROM users;

SELECT ROUND(total, 2)
FROM orders;
```

MySQL possui funções como `CURDATE()`, `CURTIME()` e `DATE_FORMAT()`. PostgreSQL usa `CURRENT_DATE`, `CURRENT_TIME`, `to_char()` e `EXTRACT()` com sintaxe própria. Não confunda formatação para exibição com transformação do tipo de data: uma data formatada como texto deixa de ser uma data para ordenação e cálculo.

Exemplos específicos do MySQL:

```sql
SELECT CURDATE(), CURTIME();
SELECT DATE_FORMAT(created_at, '%d/%m/%Y') AS displayed_date
FROM users;
SELECT WEEKDAY(created_at) AS weekday_number
FROM users;
```

No MySQL, `WEEKDAY()` retorna zero para segunda-feira e seis para domingo. Para aplicações portáveis, prefira operações de data comuns e coloque a formatação na camada de apresentação.

## Consultar uma linha relacionada por vez

`LATERAL`, disponível com variações por banco, permite que uma subconsulta use colunas da linha anterior:

```sql
SELECT u.id, u.name, recent.total
FROM users AS u
LEFT JOIN LATERAL (
    SELECT COUNT(*) AS total
    FROM orders AS o
    WHERE o.user_id = u.id
      AND o.created_at >= CURRENT_DATE - INTERVAL '30 days'
) AS recent ON true;
```

Ele é útil para top-N por grupo, funções que recebem colunas da linha externa e consultas que seriam difíceis de expressar com um join comum. A sintaxe de intervalos e o suporte variam por dialeto.

## Verificar o plano

Quando uma consulta é lenta, não comece adicionando `DISTINCT` ou índices aleatórios. Primeiro meça e veja o plano:

```sql
EXPLAIN
SELECT id, name
FROM users
WHERE email = 'ana@example.com';
```

PostgreSQL possui `EXPLAIN ANALYZE`, que executa a consulta e inclui tempos reais. Use com cuidado em comandos que modificam dados. [PostgreSQL: pg_stat, índices e otimização](../postgresql-pg-stat-indices-e-otimizacao.md) aprofunda diagnóstico, estatísticas e índices.
