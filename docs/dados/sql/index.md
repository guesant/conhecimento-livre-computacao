# SQL

SQL, ou Structured Query Language, é a linguagem usada para definir, consultar e manipular dados em bancos relacionais. Ela não é apenas uma lista de comandos: é uma forma de descrever conjuntos de dados, relações entre tabelas e transformações que o sistema de banco deve executar.

Esta seção ensina SQL do começo ao fim. Ela começa com tabelas, tipos e restrições, passa por inserção, atualização, exclusão e consultas, e chega a CTEs, consultas recursivas, funções de janela, operações de conjunto, subconsultas correlacionadas, JSON e particularidades de PostgreSQL e MySQL.

## O que você vai encontrar

- **Fundamentos e definição**: bancos, tabelas, colunas, tipos, chaves e restrições.
- **Manipulação de dados**: `INSERT`, `UPDATE`, `DELETE`, transações e cuidado com mutações.
- **Consultas**: `SELECT`, filtros, ordenação, agrupamento, joins, agregações e subconsultas.
- **SQL expressivo**: `CASE`, `COALESCE`, `NULLIF`, CTEs, consultas recursivas e funções de janela.
- **Recursos avançados**: `EXISTS`, `LATERAL`, `INTERSECT`, `EXCEPT`, `ROLLUP`, JSON e UPSERT.
- **Funções**: texto, números, datas, horários, agregação textual e expressões regulares.
- **Referência prática**: funções organizadas por tarefas comuns, como normalização, datas, agregações, JSON e diagnóstico.
- **Modelos de leitura e escrita**: `INSERT ... SELECT`, `MERGE`, views, materialized views, colunas geradas e relatórios pivotados.
- **Dados estruturados**: JSON, arrays, expansão de documentos e critérios para normalização.
- **Extensões úteis**: recursos práticos do PostgreSQL, plugins e componentes relevantes do MySQL e extensões populares do ecossistema.
- **Performance e segurança**: planos, índices, cardinalidade, permissões, RLS, parâmetros e auditoria.
- **Dialetos**: diferenças entre SQL padrão, PostgreSQL e MySQL.
- **Consulta rápida**: modelos curtos para lembrar a sintaxe mais usada.

## Uma trilha de aprendizagem

Se SQL for novidade, siga esta ordem:

1. leia [Fundamentos e definição](fundamentos.md);
2. pratique o [Tutorial de manipulação](manipulacao.md), sempre usando `WHERE` com cuidado;
3. estude [Consultas](consultas.md), principalmente joins, `GROUP BY` e `HAVING`;
4. use [SQL avançado](avancado.md) para aprender a decompor consultas maiores;
5. aprofunde [funções de janela](janelas-avancadas.md), [dados estruturados](json-arrays-e-dados-estruturados.md) e [DML avançado](dml-avancado-e-views.md);
6. estude [performance](performance-e-explain.md) e [segurança](seguranca-e-permissoes.md) antes de levar uma consulta para produção;
7. consulte [Dialetos e variáveis](dialetos.md) quando PostgreSQL e MySQL divergirem;
8. mantenha [Cheatsheet de SQL](cheatsheet.md) aberto durante os exercícios.

A sequência não é uma dependência rígida. A referência rápida serve para quem já sabe o que quer fazer; o tutorial serve para quem precisa construir um modelo mental antes de memorizar comandos.

## Um banco de exemplo

As páginas usam um pequeno domínio de usuários, pedidos e itens. Ele é suficiente para demonstrar chaves, joins, agregações, CTEs e funções de janela.

```sql
CREATE TABLE users (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(100) NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL REFERENCES users (id),
    status varchar(20) NOT NULL,
    total numeric(12, 2) NOT NULL CHECK (total >= 0),
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    order_id integer NOT NULL REFERENCES orders (id),
    product_id integer NOT NULL,
    quantity integer NOT NULL CHECK (quantity > 0),
    unit_price numeric(12, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id)
);
```

O exemplo usa sintaxe próxima do padrão SQL e do PostgreSQL. No MySQL, a declaração de identidade normalmente usa `AUTO_INCREMENT`; [Dialetos e variáveis](dialetos.md) explica essas diferenças sem misturá-las com os fundamentos.

## SQL é uma linguagem de conjuntos

Uma consulta não precisa ser pensada como um loop que visita uma linha por vez. Ela descreve um conjunto de linhas e as condições que esse conjunto deve satisfazer. O otimizador pode escolher outra ordem de execução, outro índice ou outro algoritmo de join, desde que preserve o resultado visível.

```sql
SELECT name, email
FROM users
WHERE created_at >= DATE '2025-01-01'
ORDER BY name;
```

Essa consulta diz quais colunas devem aparecer, de qual relação elas vêm, qual subconjunto interessa e como o resultado deve ser apresentado. Ela não determina se o banco fará uma varredura completa, usará um índice ou paralelizará a leitura.

## SQL padrão e dialetos

PostgreSQL, MySQL, MariaDB, SQLite, SQL Server e Oracle compartilham a estrutura central de SQL, mas divergem em tipos, funções, DDL, variáveis, paginação, UPSERT, JSON, transações e recursos procedurais. Aprender o conceito primeiro ajuda a reconhecer o que é portável e o que pertence ao dialeto.

Uma boa prática é marcar exemplos específicos. A sintaxe de uma CTE ou de um `JOIN` costuma ser portável; `DISTINCT ON`, `FILTER`, `RETURNING`, `ON CONFLICT`, `AUTO_INCREMENT` e variáveis `@nome` não são igualmente disponíveis em todos os sistemas.

## Próximas páginas

- [Fundamentos e definição](fundamentos.md)
- [Manipulação de dados](manipulacao.md)
- [Consultas](consultas.md)
- [SQL avançado](avancado.md)
- [Funções SQL](funcoes-texto-e-numericas.md)
- [Referência prática de funções](referencia-pratica.md)
- [Datas SQL](datas-e-horarios.md)
- [DML avançado](dml-avancado-e-views.md)
- [Dados estruturados](json-arrays-e-dados-estruturados.md)
- [Funções de janela](janelas-avancadas.md)
- [Performance SQL](performance-e-explain.md)
- [Segurança SQL](seguranca-e-permissoes.md)
- [Dialetos e variáveis](dialetos.md)
- [Mapa de extensões e recursos práticos](extensoes-praticas.md)
- [Cheatsheet de SQL](cheatsheet.md)
