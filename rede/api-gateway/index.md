# API gateway

API gateway é um ponto de entrada que combina roteamento, autenticação,
políticas, transformação e observabilidade para APIs. Ele conhece contratos de
aplicação além de encaminhar conexões, mas não deve absorver toda lógica de
negócio.

## Fronteira

Reverse proxy pode encaminhar tráfego sem entender a API. Gateway normalmente
adiciona identidade, rate limiting, transformação, catálogo e política por
rota. A fronteira não é absoluta: produtos podem oferecer ambos os conjuntos
de recursos.

Um gateway torna o caminho de entrada centralizado, mas também concentra
latência, disponibilidade, configuração e blast radius de uma regra incorreta.

## Relações

- [Kong e catálogo](../../kong-e-o-catalogo-de-um-api-gateway.md) compara
  modelos de configuração.
- [Service](service.md) representa o upstream lógico.
- [Route](route.md) seleciona o tráfego.
- [Rate limiting](../rate-limiting/index.md) controla consumo.

## Fonte primária

- [Kong Gateway concepts](https://docs.konghq.com/gateway/latest/)
