# Apache Shiro

Apache Shiro é um framework Java para autenticação, autorização, criptografia
e gerenciamento de sessão. Seu módulo de autorização trabalha com subjects,
roles e permissions.

## Uso

Shiro pode proteger endpoints e operações de aplicações Java. O projeto deve
definir uma fonte de realms, a semântica de roles e o comportamento em caso de
falha dessa fonte.

## Limites

Shiro não elimina a necessidade de políticas de domínio nem garante que uma
consulta filtre recursos por tenant. A camada de autorização deve acompanhar o
fluxo real do dado.

## Fonte

- [Apache Shiro Authorization](https://shiro.apache.org/authorization.html)
