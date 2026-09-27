# PostgreSQL RLS

PostgreSQL Row-Level Security, RLS, restringe quais linhas podem ser lidas ou
alteradas por uma role. O banco avalia policies junto da operação SQL.

## Uso

RLS é útil para isolamento de tenants e proteção de dados mesmo quando várias
camadas acessam as mesmas tabelas. A policy deve cobrir SELECT, INSERT, UPDATE
e DELETE conforme a semântica do domínio.

## Cuidados

Owners, superusers, roles com BYPASSRLS, funções SECURITY DEFINER e views podem
alterar o resultado esperado. O desenho deve incluir testes de autorização no
banco e no serviço.

## Fonte

- [Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
