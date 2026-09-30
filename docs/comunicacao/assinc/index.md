# Comunicação assíncrona

Comunicação assíncrona separa o momento em que uma operação é solicitada do momento em que ela é processada. O produtor pode continuar sem aguardar o trabalho completo, enquanto uma fila, um log ou um consumidor preserva e processa a mensagem.

## Modelos

[Comunicação assíncrona](../comunicacao-assincrona.md) explica filas, pub/sub, eventos, streaming, retries, idempotência, backpressure e entrega. [Event bus](../event-bus.md) trata a distribuição de eventos entre consumidores. [RPC e comunicação assíncrona](../rpc-e-comunicacao-assincrona.md) compara resposta imediata com trabalho desacoplado.

O produtor precisa saber se a mensagem representa um comando, um evento ou uma notificação. O sistema também precisa definir confirmação, visibilidade, reentrega, ordenação, deduplicação, dead letter e retenção. "Fire and forget" sem persistência e observabilidade é apenas perda silenciosa de trabalho.

## Critérios

Escolha o modelo considerando tempo máximo, volume, ordenação, consistência, replay, fan-out, concorrência e custo de operar consumidores. Um job interno persistente pode ser suficiente para uma aplicação. Um log particionado pode fazer sentido quando vários consumidores precisam reconstruir seu próprio estado.

## Relações

[Filas](../../dados/mensageria/filas.md) aprofunda a unidade de trabalho. [Event streaming](../../dados/mensageria/event-streaming.md) trata logs duráveis e posições de consumidores. [Outbox](../../dados/mensageria/outbox.md) trata a escrita atômica da intenção de publicar junto com a transação de negócio.
