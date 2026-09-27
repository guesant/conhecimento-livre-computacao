# Casbin Go

Casbin Go é a implementação principal do Casbin para Go. Ela fornece um
enforcer local que combina um modelo de autorização, uma policy e os valores
da requisição.

## Uso

O modelo pode representar RBAC, ABAC, ACL e outras relações. Adapters podem
persistir policies, mas não devem ser confundidos com a fonte de identidade ou
com o enforcement do endpoint.

## Fonte

- [Casbin para Go](https://casbin.org/docs/overview)
