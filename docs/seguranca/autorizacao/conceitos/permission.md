# Permission

Permission é uma autorização derivada para executar uma action sobre um
resource. Ela pode vir de uma role, de um atributo, de uma relação ou de uma
policy explícita.

## Diferença

Uma permission não é necessariamente um registro persistido. Em RBAC ela pode
ser herdada de uma role; em ReBAC pode ser calculada a partir de tuples; em
ABAC pode resultar de uma expressão.

## Operação

Nomeie permissions com verbos do domínio e evite usar uma permission genérica
como substituto de decisões diferentes, por exemplo ler metadados e baixar
conteúdo.
