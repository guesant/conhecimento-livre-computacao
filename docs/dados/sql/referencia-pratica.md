# Referência prática de funções

Uma função SQL é útil quando resolve uma transformação que aparece na consulta real: limpar uma entrada, tratar um valor ausente, calcular uma métrica, comparar datas ou desmontar um documento. Esta página agrupa as funções por tarefa, para consulta rápida. Ela não tenta substituir a documentação do SGBD nem listar funções internas ou raramente usadas.

## Limpar e normalizar texto

```sql
SELECT
    id,
    TRIM(name) AS name,
    LOWER(TRIM(email)) AS normalized_email,
    REPLACE(phone, '-', '') AS phone_digits,
    NULLIF(TRIM(notes), '') AS notes
FROM users;
```

Use `TRIM` para espaços nas extremidades, `LOWER` ou `UPPER` para uma normalização simples e `NULLIF` para transformar texto vazio em `NULL`. `LOWER` não substitui uma política de comparação internacionalizada; acentuação, idioma e collation devem ser testados no banco utilizado.

| Necessidade | PostgreSQL | MySQL |
| --- | --- | --- |
| Combinar texto | `CONCAT`, `concat_ws` | `CONCAT`, `CONCAT_WS` |
| Extrair trecho | `SUBSTRING`, `LEFT`, `RIGHT` | `SUBSTRING`, `LEFT`, `RIGHT` |
| Procurar trecho | `POSITION`, `STRPOS` | `POSITION`, `LOCATE`, `INSTR` |
| Substituir | `REPLACE`, `TRANSLATE` | `REPLACE` |
| Preencher | `LPAD`, `RPAD` | `LPAD`, `RPAD` |
| Agregar texto | `STRING_AGG` | `GROUP_CONCAT` |
| Regex | `~`, `regexp_replace` | `REGEXP_LIKE`, `REGEXP_REPLACE` |

## Evitar `NULL` inesperado

```sql
SELECT
    COALESCE(phone, mobile_phone, 'sem telefone') AS contact,
    total / NULLIF(item_count, 0) AS average_item_value
FROM orders;
```

`COALESCE` escolhe o primeiro valor não nulo. `NULLIF` é útil para impedir uma divisão por zero. Lembre que `NULL` não é uma string vazia nem zero, e que `= NULL` não encontra linhas. Use `IS NULL` e `IS NOT NULL`.

## Calcular valores com segurança

```sql
SELECT
    ROUND(total, 2) AS rounded_total,
    ABS(balance) AS absolute_balance,
    GREATEST(minimum_price, current_price) AS higher_price,
    LEAST(minimum_price, current_price) AS lower_price,
    total / NULLIF(quantity, 0) AS unit_value
FROM products;
```

Para dinheiro, prefira `numeric` ou `decimal` e escolha conscientemente o momento do arredondamento. Não use `float` apenas porque a coluna parece numérica. Divisão inteira também varia conforme os tipos dos operandos; use `CAST` quando o resultado decimal for necessário.

## Trabalhar com datas

```sql
SELECT
    created_at,
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month,
    CURRENT_DATE - CAST(created_at AS date) AS age_in_days
FROM orders;
```

As operações mais recorrentes são:

- obter o instante atual com `CURRENT_TIMESTAMP` ou `NOW`;
- extrair partes com `EXTRACT` ou `DATE_PART`;
- truncar uma data para mês, dia ou hora com `DATE_TRUNC`;
- calcular diferenças com `AGE`, `DATEDIFF` ou `TIMESTAMPDIFF`;
- somar intervalos com `INTERVAL`, `DATE_ADD` ou `DATE_SUB`;
- converter fusos com `AT TIME ZONE` ou `CONVERT_TZ`;
- formatar para apresentação somente na borda da aplicação ou relatório.

Exemplo portável para um dia inteiro:

```sql
SELECT *
FROM events
WHERE occurred_at >= TIMESTAMP '2025-01-01 00:00:00'
  AND occurred_at < TIMESTAMP '2025-01-02 00:00:00';
```

Esse intervalo costuma ser melhor para índices do que aplicar `DATE(occurred_at)` à coluna. Para intervalos que dependem de fuso horário, converta o limite para o fuso do banco antes de comparar.

## UUID v4 e v7

UUID v4 é aleatório. É uma boa escolha quando o identificador não deve revelar tempo ou sequência. UUID v7 combina um timestamp com aleatoriedade, mantendo unicidade distribuída e uma ordenação temporal aproximada. Isso costuma produzir inserções e paginação mais amigáveis a índices do que UUIDs completamente aleatórios, sem transformar o UUID em um relógio confiável ou em um campo de auditoria.

No PostgreSQL 18 ou posterior, a geração é nativa:

```sql
CREATE TABLE events (
    id uuid PRIMARY KEY DEFAULT uuidv7(),
    occurred_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payload jsonb NOT NULL
);

INSERT INTO events (payload)
VALUES ('{"kind": "signup"}')
RETURNING id;
```

Para v4, use `uuidv4()` ou `gen_random_uuid()`:

```sql
SELECT uuidv4();
SELECT gen_random_uuid();
```

`uuid_extract_version` ajuda a verificar o tipo recebido, e `uuid_extract_timestamp` pode extrair o timestamp de UUIDs v1 e v7. O timestamp de um UUID v7 não substitui `created_at`: mantenha uma coluna de data quando o horário do evento precisar ser consultado, auditado ou corrigido independentemente do identificador.

No MySQL 8.4, `UUID()` gera UUID v1, e `UUID_TO_BIN` e `BIN_TO_UUID` convertem entre texto e `BINARY(16)`. O UUID v7 normalmente deve ser gerado pela aplicação ou por uma biblioteca compatível com RFC 9562:

```sql
CREATE TABLE events (
    id BINARY(16) PRIMARY KEY,
    occurred_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    payload JSON NOT NULL
);

INSERT INTO events (id, payload)
VALUES (UUID_TO_BIN(:uuid_v7), JSON_OBJECT('kind', 'signup'));

SELECT BIN_TO_UUID(id) AS id, occurred_at
FROM events;
```

O segundo argumento de `UUID_TO_BIN` foi projetado para reorganizar partes temporais de UUID v1. Não o aplique automaticamente a UUID v7. Use a mesma convenção de armazenamento e conversão em todas as aplicações, migrações e ferramentas.

### Escolha rápida

| Necessidade | Escolha |
| --- | --- |
| ID distribuído e sem ordenação temporal | UUID v4 |
| ID distribuído com melhor localidade temporal | UUID v7 |
| Ordenação e auditoria exatas | UUID v4 ou v7 mais uma coluna de tempo |
| Compatibilidade com instalações PostgreSQL antigas | gerar na aplicação ou usar `pgcrypto` |
| MySQL 8.4 | gerar v4 ou v7 fora do banco e armazenar em `BINARY(16)` |

Não exponha o UUID v7 como mecanismo de autorização nem dependa dele para descobrir o instante exato de criação. Ele é um identificador ordenável, não uma política de segurança nem um registro de auditoria.

## Agregar sem perder linhas

```sql
SELECT
    user_id,
    COUNT(*) AS order_count,
    SUM(total) AS order_total,
    AVG(total) AS average_order,
    MIN(created_at) AS first_order,
    MAX(created_at) AS last_order
FROM orders
GROUP BY user_id;
```

Para agregações condicionais, PostgreSQL permite `FILTER`:

```sql
SELECT
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE status = 'paid') AS paid,
    COUNT(*) FILTER (WHERE status = 'cancelled') AS cancelled
FROM orders;
```

Em MySQL e em bancos sem `FILTER`, use `SUM(CASE ...)`:

```sql
SELECT
    COUNT(*) AS total,
    SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) AS paid
FROM orders;
```

## Escolher a última linha de cada grupo

A solução mais portável usa uma função de janela:

```sql
WITH ranked AS (
    SELECT
        orders.*,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY created_at DESC, id DESC
        ) AS position
    FROM orders
)
SELECT *
FROM ranked
WHERE position = 1;
```

PostgreSQL também possui `DISTINCT ON`:

```sql
SELECT DISTINCT ON (user_id) *
FROM orders
ORDER BY user_id, created_at DESC, id DESC;
```

O `ORDER BY` precisa definir qual é a primeira linha. Sem uma ordenação determinística, a consulta pode escolher outra linha em execuções diferentes.

## JSON e dados semiestruturados

PostgreSQL:

```sql
SELECT
    payload->>'kind' AS kind,
    payload->'user'->>'email' AS email
FROM events
WHERE payload @> '{"kind": "signup"}';
```

MySQL:

```sql
SELECT
    JSON_VALUE(payload, '$.kind') AS kind,
    JSON_VALUE(payload, '$.user.email') AS email
FROM events
WHERE JSON_VALUE(payload, '$.kind') = 'signup';
```

Use JSON para documentos externos, configurações e atributos cujo formato realmente varia. Se um valor tem identidade, relacionamento, permissão, restrição ou consulta frequente, uma tabela normalizada costuma ser mais útil.

## Consultar existência

```sql
SELECT u.id, u.email
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.user_id = u.id
      AND o.status = 'paid'
);
```

`EXISTS` expressa que basta encontrar uma linha. Ele evita a multiplicação de resultados que um `JOIN` pode produzir quando a consulta só precisa testar existência. Para ausência, use `NOT EXISTS` e cuide do comportamento diferente de `NOT IN` quando há `NULL`.

## Diagnosticar antes de otimizar

Funções e recursos que mais ajudam no dia a dia:

- `EXPLAIN` para entender o plano escolhido;
- `EXPLAIN ANALYZE` para comparar estimativas com a execução real;
- `EXPLAIN (ANALYZE, BUFFERS)` no PostgreSQL para observar leituras;
- `pg_stat_statements` no PostgreSQL para localizar consultas caras;
- Performance Schema e schema `sys` no MySQL para investigar consultas e esperas;
- estatísticas atualizadas antes de concluir que um índice está sendo ignorado.

Não copie um plano de um banco para outro. A mesma consulta pode ter índices, estatísticas, tipos e algoritmos de join diferentes.

## Referência rápida de decisão

| Pergunta | Recurso recomendado |
| --- | --- |
| O valor pode estar ausente? | `COALESCE`, `NULLIF`, `IS NULL` |
| Preciso de uma linha por grupo? | `ROW_NUMBER`, `DISTINCT ON` no PostgreSQL |
| Preciso comparar com a linha anterior? | `LAG` |
| Preciso de acumulado ou média móvel? | `SUM` ou `AVG` com `OVER` |
| Só preciso saber se existe uma relação? | `EXISTS` |
| Preciso de vários níveis de resumo? | `ROLLUP`, `GROUPING SETS` |
| O filtro ficou lento após aplicar função? | intervalo, índice funcional ou coluna gerada |
| O dado é um documento variável? | JSON, com limites e validação |
| A busca textual é recorrente? | índice de texto, `pg_trgm` ou `FULLTEXT` |
| A consulta ficou lenta? | `EXPLAIN`, estatísticas e medição |
