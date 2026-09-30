# PostgreSQL GRANT

PostgreSQL GRANT concede privilégios sobre objetos do banco, como schemas,
tabelas, sequências, funções e colunas. É o mecanismo de ACL e RBAC básico do
PostgreSQL.

## Modelo

Privilégios podem ser concedidos a roles e herdados conforme a configuração.
Uma role de aplicação deve receber apenas as operações necessárias e não deve
ser proprietária de tudo que precisa consultar.

## Relação com RLS

GRANT decide se a operação sobre o objeto é permitida. RLS pode restringir as
linhas depois disso. Os dois mecanismos resolvem dimensões diferentes e devem
ser testados em conjunto.

## Fonte

- [PostgreSQL GRANT](https://www.postgresql.org/docs/current/sql-grant.html)
