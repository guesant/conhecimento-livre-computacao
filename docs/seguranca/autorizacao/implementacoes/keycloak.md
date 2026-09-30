# Keycloak

Keycloak é uma plataforma de identidade que oferece login federado, OAuth 2.0,
OpenID Connect, SAML, usuários, grupos, roles e integração com diretórios.

## Autorização

Roles e claims podem participar de decisões nos consumidores. O recurso
Authorization Services acrescenta uma modelagem própria de recursos e policies,
mas autenticação no Keycloak não concede automaticamente acesso a uma operação
de negócio.

## Operação

Proteja o admin, use clientes separados, limite scopes e defina expiração de
tokens. A aplicação deve validar issuer, audience, assinatura e claims antes de
usar qualquer role.

## Fonte

- [Documentação do Keycloak](https://www.keycloak.org/documentation)
