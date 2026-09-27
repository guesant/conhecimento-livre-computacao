# Casbin Node

Casbin Node é a implementação do Casbin para aplicações JavaScript e
TypeScript. O pacote também é conhecido no ecossistema como node-casbin.

## Modelo

O enforcer carrega um model e uma policy, recebe subject, object e action e
retorna uma decisão. O adapter pode persistir regras em banco, mas a aplicação
continua responsável por autenticar e aplicar a resposta.

## Fonte

- [Casbin Node](https://casbin.org/docs/overview)
