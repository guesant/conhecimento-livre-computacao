# API gateway plugin

Plugin é uma extensão que intercepta fases do processamento para aplicar
autenticação, rate limiting, transformação, logging ou outra política.

## Escopo

Um plugin pode ser configurado globalmente, por service, route ou consumer.
Quanto mais amplo o escopo, maior o blast radius de uma configuração errada.
Prefira o escopo mínimo que atende ao contrato.

Ordem de plugins importa quando uma política depende de outra, por exemplo
identificar o consumer antes de aplicar sua quota.

## Failure modes

Um plugin pode rejeitar tráfego válido por credencial, schema, limite ou ordem.
Ele também pode acrescentar latência e depender de armazenamento externo.
Observe logs, métricas e status do gateway separadamente do upstream.

## Relações

- [Route](route.md) define a superfície.
- [Consumer](consumer.md) fornece identidade.
- [Rate limiting](../rate-limiting/index.md) é uma política comum.

## Fonte primária

- [Kong plugins](https://docs.konghq.com/gateway/latest/plugins/)
