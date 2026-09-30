# Gateway

`Gateway` referencia uma `GatewayClass` e declara os pontos de entrada de uma
plataforma de rede. Cada listener informa porta, protocolo, hostname e, quando
necessário, o certificado TLS que termina a conexão.

O recurso pertence à equipe que administra a infraestrutura de borda. A
permissão para que `HTTPRoute` de outros namespaces se associem ao gateway é
controlada por `allowedRoutes`. Permitir todos os namespaces favorece a
conveniência; restringir por namespace ou label reduz o raio de publicação
acidental.

## Relações

- [GatewayClass](gateway-class.md) identifica o controlador.
- [HTTPRoute](http-route.md) pertence à aplicação e encaminha para um Service.
- [Gateway API](../../gateway-api.md) explica a separação de responsabilidades.

## Fonte primária

- [Gateway API, Gateway](https://gateway-api.sigs.k8s.io/api-types/gateway/)
