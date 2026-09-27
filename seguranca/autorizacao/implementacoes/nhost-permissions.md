# Nhost permissions

Nhost permissions protegem operações GraphQL e dados PostgreSQL por roles,
claims e regras de linha. A autorização é avaliada no acesso aos dados e não
apenas no cliente GraphQL.

## Modelo

O role da sessão e as claims selecionam permissões para tabelas, colunas e
linhas. O modelo precisa ser testado com usuários de cada tenant e com claims
ausentes ou inválidas.

## Fonte

- [Nhost permissions](https://docs.nhost.io/products/graphql/permissions)
