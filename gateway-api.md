# Gateway API

Gateway API separa a infraestrutura de borda das regras de roteamento da
aplicação. O modelo evita concentrar controlador, listeners, certificados,
hostnames e backends em um único recurso `Ingress` com anotações específicas de
cada implementação.

## Recursos do modelo

- [GatewayClass](rede/gateway-api/gateway-class.md) identifica o controlador
  escolhido pela plataforma.
- [Gateway](rede/gateway-api/gateway.md) declara listeners, portas, protocolos
  e certificados.
- [HTTPRoute](rede/gateway-api/http-route.md) associa hostnames e caminhos a
  Services da aplicação.

Essa separação distribui a posse dos recursos. A equipe de infraestrutura
administra a classe e o gateway; a equipe da aplicação administra suas rotas,
respeitando as associações permitidas por `allowedRoutes`.

## Relações

[Ingress](kubernetes/networking/ingress.md) continua sendo uma API válida e
mais simples para cenários que não precisam dessa separação. [Ingress: os
nomes internos pela tailnet](../arquitetura/ingress.md) mostra como o
hl-infrastructure configura a entrada do próprio ambiente.

## Fontes primárias

- [Gateway API](https://gateway-api.sigs.k8s.io/)
- [Gateway API concepts](https://gateway-api.sigs.k8s.io/concepts/)
