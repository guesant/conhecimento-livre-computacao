# Row-Level Security

Row-Level Security, RLS, restringe quais linhas uma role pode ler ou alterar.
É um mecanismo de autorização no armazenamento, útil para isolamento de
tenants e defesa em profundidade.

## PostgreSQL

No PostgreSQL, policies definem condições para SELECT, INSERT, UPDATE e DELETE.
O resultado também depende de owner, superuser, BYPASSRLS, functions e views.

## Relações

RLS protege linhas. Não substitui autorização por campo, por objeto fora do
banco ou por operação de negócio.
