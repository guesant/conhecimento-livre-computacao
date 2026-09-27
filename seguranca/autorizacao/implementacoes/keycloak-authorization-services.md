# Keycloak Authorization Services

Keycloak Authorization Services fornece recursos para modelar recursos,
escopos, permissões e políticas em um servidor Keycloak. Ele pode atuar como
um ponto de administração e decisão para aplicações protegidas.

## Modelo

Uma aplicação registra recursos e escopos. Políticas podem combinar papéis,
grupos, atributos e contextos. O resultado pode ser aplicado por um resource
server integrado ou por uma camada de enforcement da própria aplicação.

## Limites

Keycloak também é um provedor de identidade. Autenticar um usuário não concede
automaticamente acesso a todos os recursos. As policies precisam ser avaliadas
no contexto correto e os tokens devem conter apenas claims necessários.

## Fonte

- [Keycloak Authorization Services](https://www.keycloak.org/docs/latest/authorization_services/)
