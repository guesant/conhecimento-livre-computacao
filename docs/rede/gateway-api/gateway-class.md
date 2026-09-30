# GatewayClass

`GatewayClass` é um recurso de escopo de cluster que identifica qual
controlador implementa uma classe de gateway. Ele descreve uma capacidade de
plataforma, não uma porta pública individual. Uma classe pode ser atendida por
Traefik, Cilium ou outro controlador compatível com Gateway API.

A existência de uma `GatewayClass` não publica tráfego. Ela oferece o ponto de
ligação que um recurso `Gateway` usa para declarar listeners e certificados.
Essa separação permite que a equipe de infraestrutura escolha ou troque o
controlador sem reescrever cada regra de aplicação.

## Relações

- [Gateway](gateway.md) declara os pontos de entrada reais.
- [HTTPRoute](http-route.md) declara as regras de encaminhamento.
- [Gateway API](../../gateway-api.md) apresenta o modelo completo.

## Fonte primária

- [Gateway API, GatewayClass](https://gateway-api.sigs.k8s.io/api-types/gatewayclass/)
