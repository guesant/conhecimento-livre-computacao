# Fundamentos de SQL

Antes de escrever consultas, é preciso entender o que o banco está guardando. Um banco relacional organiza dados em relações, normalmente representadas como tabelas. Uma tabela possui colunas com significado definido e linhas que representam ocorrências desse modelo.

## DDL, DML, DQL, TCL e DCL

As classificações são convenções didáticas, não fronteiras universais da linguagem:

| Categoria | Objetivo | Exemplos |
| --- | --- | --- |
| DDL, Data Definition Language | definir ou alterar estruturas | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| DML, Data Manipulation Language | inserir ou alterar linhas | `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DQL, Data Query Language | consultar dados | `SELECT` |
| TCL, Transaction Control Language | controlar transações | `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT` |
| DCL, Data Control Language | controlar permissões | `GRANT`, `REVOKE` |

`SELECT` às vezes é agrupado em DML. O mais importante é entender a operação, não decorar uma classificação.

## Banco e schema

Alguns sistemas permitem criar bancos explicitamente; outros trabalham com um banco criado pelo administrador e organizam objetos em schemas. PostgreSQL separa banco e schema. MySQL costuma usar “database” e “schema” como termos equivalentes.

```sql
CREATE DATABASE loja;
```

No MySQL, é comum selecionar o banco com:

```sql
USE loja;
```

No PostgreSQL, a conexão normalmente já escolhe o banco; o schema pode ser selecionado com `SET search_path` ou referenciado pelo nome:

```sql
SET search_path TO public;

SELECT *
FROM public.users;
```

Criar um banco é uma operação administrativa. Em aplicações, migrações costumam criar tabelas e índices dentro de um banco que já foi provisionado.

## Tipos de dados

O tipo da coluna é parte do contrato do modelo. Escolha o tipo que representa o domínio, não apenas o tipo que aceita qualquer valor.

| Família | Exemplos | Uso |
| --- | --- | --- |
| Inteiros | `smallint`, `integer`, `bigint` | contagens, identificadores e valores discretos |
| Decimais exatos | `numeric(12, 2)`, `decimal` | dinheiro e medidas que exigem precisão |
| Ponto flutuante | `real`, `double precision`, `float` | cálculos aproximados e científicos |
| Texto | `varchar(n)`, `text`, `char(n)` | nomes, descrições e códigos |
| Data e hora | `date`, `time`, `timestamp` | instantes e calendários |
| Booleano | `boolean` | estados verdadeiro/falso |
| Binário | `blob`, `bytea`, `varbinary` | bytes, quando armazená-los no banco fizer sentido |
| Estruturado | `json`, `jsonb` | dados semiestruturados e extensões controladas |

Não use `float` para valores monetários sem entender o erro de representação. `numeric` representa casas decimais de forma exata, embora possa custar mais processamento.

## Chaves e restrições

Restrições protegem invariantes no limite do banco. A aplicação pode validar entradas para oferecer mensagens melhores, mas não deve ser a única barreira para regras que o banco consegue garantir.

```sql
CREATE TABLE addresses (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    street varchar(200) NOT NULL,
    number integer,
    postal_code varchar(20),
    UNIQUE (street, number, postal_code)
);

CREATE TABLE customers (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(100) NOT NULL,
    address_id integer REFERENCES addresses (id)
);
```

- `PRIMARY KEY` identifica uma linha e não aceita `NULL`.
- `FOREIGN KEY` exige que uma referência exista na tabela relacionada, conforme a ação definida para exclusão ou atualização.
- `NOT NULL` exige um valor.
- `UNIQUE` impede duplicidade na combinação indicada.
- `CHECK` expressa uma condição que cada linha deve satisfazer.
- `DEFAULT` fornece um valor quando a coluna não aparece no `INSERT`.

## Criar uma tabela

Uma definição de tabela combina nome, colunas, tipos e restrições:

```sql
CREATE TABLE products (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(120) NOT NULL,
    sku varchar(40) NOT NULL UNIQUE,
    price numeric(12, 2) NOT NULL CHECK (price >= 0),
    active boolean NOT NULL DEFAULT true
);
```

Prefira nomes claros e consistentes. A chave estrangeira deve expressar o relacionamento, e não apenas repetir o nome da tabela sem indicar sua função.

## Inspecionar e alterar uma estrutura

`DESCRIBE` ou `DESC` é uma forma comum de inspecionar uma tabela no MySQL:

```sql
DESC products;
```

No PostgreSQL, o cliente `psql` oferece comandos próprios, como `\d products`, e também é possível consultar o catálogo do sistema. Essas formas não são SQL portável.

Alterações de schema devem ser tratadas como migrações revisáveis:

```sql
ALTER TABLE products
ADD COLUMN description text;

ALTER TABLE products
ADD CONSTRAINT products_price_check CHECK (price >= 0);
```

MySQL também possui `CHANGE`, que pode renomear uma coluna e declarar novamente seu tipo. A forma exige repetir o nome e o tipo:

```sql
ALTER TABLE products
CHANGE description product_description varchar(500);
```

Para apenas renomear, alguns bancos oferecem `RENAME COLUMN`:

```sql
ALTER TABLE products
RENAME COLUMN product_description TO description;
```

MySQL pode aceitar `FIRST` e `AFTER` para controlar a posição visual da coluna:

```sql
ALTER TABLE products
ADD COLUMN sku_alias varchar(40) AFTER sku;
```

A posição não muda o significado relacional nem deve ser usada como requisito da aplicação. Se a ordem importar apenas para leitura humana, prefira a ordem explícita no `SELECT`.

Remover uma coluna ou tabela é destrutivo:

```sql
ALTER TABLE products DROP COLUMN description;
DROP TABLE products;
```

Antes de usar `DROP`, verifique dependências, backups e o plano de reversão. `CASCADE` pode remover objetos relacionados e deve ser usado apenas quando esse efeito for intencional e compreendido.

## Identificadores automáticos

Identificadores gerados não substituem a modelagem da identidade. PostgreSQL oferece `GENERATED ... AS IDENTITY` e também possui o legado `SERIAL`, baseado em sequence. MySQL usa `AUTO_INCREMENT`. O conceito é semelhante, mas a sintaxe e alguns comportamentos diferem; a comparação está em [Dialetos e variáveis](dialetos.md).

## `NULL` não é zero nem texto vazio

`NULL` significa ausência ou desconhecimento de valor. Comparações comuns não retornam verdadeiro:

```sql
SELECT *
FROM users
WHERE email = NULL;
```

Use `IS NULL` e `IS NOT NULL`:

```sql
SELECT *
FROM users
WHERE email IS NOT NULL;
```

Operações com `NULL` seguem a lógica de três valores. `COALESCE` e `NULLIF` ajudam a expressar substituições e divisões seguras; elas aparecem em [SQL avançado](avancado.md).

## O modelo mental

Uma tabela não é apenas um arquivo com colunas. O schema expressa entidades, relacionamentos e invariantes. Antes de acrescentar uma coluna ou guardar um objeto JSON, pergunte qual consulta precisa ser respondida, qual regra deve ser garantida e qual parte do modelo deve ser independente.

## Ferramentas de administração

Clientes gráficos como MySQL Workbench podem ativar um modo de segurança que impede `UPDATE` e `DELETE` sem uma condição que use uma chave ou limite. Desativar essa proteção pode ser necessário para uma operação deliberada, mas aumenta o risco de uma mutação ampla. A ferramenta não substitui escrever, revisar e testar o `WHERE`.
