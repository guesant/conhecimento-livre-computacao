# HTTPRoute

`HTTPRoute` declara as regras de roteamento de uma aplicação. Ela associa
hostnames e caminhos a um `Service` de backend e pode restringir a associação a
um listener específico por meio de `sectionName`.

O recurso pode viver no namespace da aplicação, enquanto o `Gateway` permanece
sob controle da plataforma. Essa divisão evita editar um objeto de borda
compartilhado sempre que uma aplicação nova precisa publicar uma rota.

Funcionalidades específicas do controlador continuam sendo extensões. A
portabilidade cobre o modelo comum da especificação, não transforma toda
capacidade proprietária em campo padrão.

## Relações

- [GatewayClass](gateway-class.md) escolhe o controlador.
- [Gateway](gateway.md) expõe listeners e controla associações.
- [Service](../../kubernetes/core/service.md) é o backend Kubernetes da rota.
- [Gateway API](../../gateway-api.md) apresenta a arquitetura completa.

## Fonte primária

- [Gateway API, HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/)
