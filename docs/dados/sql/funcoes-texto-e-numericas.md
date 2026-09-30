# Funções SQL

Funções de texto e números aparecem em quase toda consulta real. Elas podem normalizar valores, preparar uma apresentação, calcular métricas ou transformar a entrada antes de uma comparação. Quando uma transformação for usada em filtros ou joins frequentemente, avalie se um índice funcional, uma coluna gerada ou uma normalização no modelo é mais apropriado.

## Texto

```sql
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    LOWER(email) AS normalized_email,
    UPPER(country_code) AS country_code,
    TRIM(display_name) AS clean_name,
    LENGTH(description) AS description_length
FROM users;
```

Funções comuns:

| Função | Uso |
| --- | --- |
| `CONCAT` | combinar valores |
| `LOWER`, `UPPER` | normalizar caixa |
| `TRIM`, `LTRIM`, `RTRIM` | remover espaços |
| `LENGTH`, `CHAR_LENGTH` | medir tamanho |
| `REPLACE` | substituir trecho |
| `SUBSTRING` | extrair parte |
| `POSITION`, `STRPOS` | encontrar posição |
| `LPAD`, `RPAD` | preencher até um tamanho |

```sql
SELECT
    REPLACE(phone, '-', '') AS digits_only,
    SUBSTRING(order_code FROM 1 FOR 3) AS prefix
FROM orders;
```

`LENGTH` pode medir bytes em alguns bancos, enquanto `CHAR_LENGTH` mede caracteres. Essa diferença aparece com Unicode. Também há divergências em collation, acentuação, maiúsculas e comparações sem distinção de caixa.

## Agregação de texto

PostgreSQL usa `STRING_AGG`:

```sql
SELECT
    user_id,
    STRING_AGG(status, ', ' ORDER BY created_at) AS statuses
FROM orders
GROUP BY user_id;
```

MySQL usa `GROUP_CONCAT`:

```sql
SELECT
    user_id,
    GROUP_CONCAT(status ORDER BY created_at SEPARATOR ', ') AS statuses
FROM orders
GROUP BY user_id;
```

Essas funções produzem uma representação textual. Não use uma string concatenada como substituto de uma relação quando os itens precisarem ser consultados individualmente.

## Expressões regulares

PostgreSQL oferece operadores como `~` e `~*`:

```sql
SELECT email
FROM users
WHERE email ~* '^[^@]+@example\\.com$';
```

MySQL possui funções como `REGEXP_LIKE`:

```sql
SELECT email
FROM users
WHERE REGEXP_LIKE(email, '^[^@]+@example\\.com$');
```

Expressões regulares são úteis para validações e extrações pontuais, mas podem ser caras em grandes volumes. Para buscas recorrentes, considere índices, colunas normalizadas e uma política clara para entradas inválidas.

## Números

```sql
SELECT
    ABS(balance) AS distance_from_zero,
    ROUND(price, 2) AS rounded_price,
    CEIL(score) AS upper_integer,
    FLOOR(score) AS lower_integer,
    POWER(quantity, 2) AS squared_quantity,
    MOD(sequence_number, 2) AS parity
FROM measurements;
```

`ROUND`, `CEIL`, `FLOOR`, `ABS`, `POWER`, `SQRT`, `MOD`, `SIGN` e `RANDOM` possuem variações de nome, tipo de retorno e comportamento por banco. Para dinheiro, prefira `numeric` ou `decimal` e defina em que momento o arredondamento acontece.

Divisão inteira pode surpreender:

```sql
SELECT 5 / 2;
```

Dependendo dos tipos e do banco, o resultado pode ser `2` ou `2.5`. Force o tipo quando a intenção for explícita:

```sql
SELECT CAST(5 AS numeric) / 2;
```

## `GREATEST` e `LEAST`

```sql
SELECT
    GREATEST(minimum_price, current_price) AS higher,
    LEAST(minimum_price, current_price) AS lower
FROM products;
```

O tratamento de `NULL` diverge entre SGBDs. Teste esse caso quando uma coluna puder estar ausente.

## Formatação não é modelagem

Formatar um preço ou uma data para exibição dentro do banco pode ser conveniente para um relatório, mas transforma o resultado em texto. Ordenar `10`, `2` e `9` como texto produz uma ordem diferente da ordem numérica. Sempre que possível, devolva tipos sem formatar e deixe a apresentação para a camada responsável por idioma, moeda e fuso horário.
