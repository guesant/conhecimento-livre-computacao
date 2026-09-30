# Dialetos SQL

A linguagem central é compartilhada, mas cada SGBD acrescenta tipos, funções, comandos administrativos e uma linguagem procedural. Esta página usa PostgreSQL e MySQL para mostrar onde o conceito continua igual e onde a sintaxe deixa de ser portável.

## Variáveis não são parâmetros

Uma variável guarda um valor durante uma sessão ou dentro de um programa armazenado. Um parâmetro de consulta, por outro lado, é fornecido pela aplicação:

```sql
SELECT *
FROM users
WHERE id = ?;
```

Use parâmetros preparados para valores fornecidos por usuários. Não monte SQL concatenando strings. Uma variável do banco não é uma solução genérica para injeção de SQL.

## Variáveis no MySQL

Variáveis de usuário começam com `@` e pertencem à sessão atual:

```sql
SET @min_age = 18;

SELECT *
FROM users
WHERE age >= @min_age;
```

Também é possível guardar o resultado de uma consulta:

```sql
SELECT MAX(price)
INTO @max_price
FROM products;

SELECT @max_price;
```

Dentro de procedures e functions MySQL, variáveis locais são declaradas em blocos `BEGIN ... END`:

```sql
BEGIN
    DECLARE total integer DEFAULT 0;

    SELECT COUNT(*)
    INTO total
    FROM users;

    SELECT total;
END;
```

A variável local precisa ser declarada no início do bloco. Variáveis de sessão, variáveis locais e variáveis de sistema são categorias diferentes.

## Variáveis no PostgreSQL

SQL comum não possui um equivalente geral ao `@nome` do MySQL. Variáveis normais aparecem principalmente em PL/pgSQL, dentro de uma function ou bloco `DO`:

```sql
DO $$
DECLARE
    total integer := 0;
BEGIN
    SELECT COUNT(*)
    INTO total
    FROM users;

    RAISE NOTICE 'Total: %', total;
END;
$$;
```

`DEFAULT` e `=` também podem inicializar uma variável PL/pgSQL. `%TYPE` acompanha o tipo de uma coluna e `%ROWTYPE` representa uma linha inteira:

```sql
DECLARE
    v_email users.email%TYPE;
    v_user users%ROWTYPE;
BEGIN
    SELECT * INTO v_user
    FROM users
    WHERE id = 10;

    v_email := v_user.email;
END;
```

`RECORD` oferece uma estrutura flexível quando o formato da linha não é conhecido na declaração. `CONSTANT` impede reatribuição:

```sql
DECLARE
    tax CONSTANT numeric := 0.15;
BEGIN
    RAISE NOTICE 'Taxa: %', tax;
END;
```

Para uma consulta comum, uma CTE ou uma subconsulta costuma expressar melhor um valor intermediário do que criar uma variável procedural.

## Identidade: `IDENTITY`, `SERIAL` e `AUTO_INCREMENT`

PostgreSQL moderno:

```sql
CREATE TABLE users (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name text NOT NULL
);
```

`SERIAL` é uma conveniência histórica que cria uma sequence e um default. Ele continua aparecendo em projetos existentes, mas `IDENTITY` deixa a relação entre coluna e geração mais explícita.

MySQL:

```sql
CREATE TABLE users (
    id bigint AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL
);
```

Esses mecanismos geram identificadores, mas não garantem que uma operação de negócio seja idempotente. Para evitar duplicidade de um evento, crie também uma chave única que represente a identidade do evento.

## Sequences no PostgreSQL

Uma sequence pode ser usada diretamente:

```sql
CREATE SEQUENCE invoice_number START WITH 1000 INCREMENT BY 1;

SELECT nextval('invoice_number');
```

Sequences não são contadores sem lacunas. Rollbacks e concorrência podem consumir valores. Se a exigência for numeração sem lacunas, trate isso como um problema de negócio separado e entenda o custo de serializar a emissão.

## UPSERT

PostgreSQL:

```sql
INSERT INTO users (email, name)
VALUES ('ana@example.com', 'Ana')
ON CONFLICT (email)
DO UPDATE SET name = EXCLUDED.name;
```

MySQL:

```sql
INSERT INTO users (email, name)
VALUES ('ana@example.com', 'Ana')
ON DUPLICATE KEY UPDATE name = VALUES(name);
```

As versões e formas recomendadas podem evoluir. O conceito comum é uma inserção que reage a uma violação de chave única; a coluna que define a identidade precisa existir no schema.

## `RETURNING`

PostgreSQL pode devolver as linhas afetadas por uma mutação:

```sql
INSERT INTO users (name, email)
VALUES ('Ana', 'ana@example.com')
RETURNING id, created_at;
```

Isso evita uma segunda consulta para recuperar o identificador gerado e reduz uma janela de concorrência. O suporte em MySQL depende da versão e do tipo de operação; não assuma portabilidade.

## Recursos que não são igualmente portáveis

| Recurso | PostgreSQL | MySQL | Alternativa conceitual |
| --- | --- | --- |
| `FILTER` em agregação | sim | não da mesma forma | `SUM(CASE ...)` |
| `DISTINCT ON` | sim | não | `ROW_NUMBER()` |
| `ON CONFLICT` | sim | `ON DUPLICATE KEY UPDATE` | UPSERT do dialeto |
| `RETURNING` | sim | suporte varia | nova consulta ou recurso equivalente |
| `SERIAL` | legado | não é a forma usual | `IDENTITY` ou `AUTO_INCREMENT` |
| `@variavel` | não como variável SQL geral | variável de sessão | CTE, parâmetro ou PL/pgSQL |
| `LATERAL` | sim | suporte e sintaxe variam | subconsulta, join ou janela |

## Como escrever SQL mais portável

- prefira `JOIN`, `CASE`, CTEs, agregações e funções de janela quando elas cobrirem a necessidade;
- isole SQL específico do banco em módulos ou repositórios claros;
- marque exemplos por dialeto em vez de apresentar uma extensão como se fosse padrão;
- teste tipos de data, intervalos, booleanos, strings e `NULL` no SGBD real;
- leia o plano no banco que executará a consulta, pois o otimizador não é portável.
