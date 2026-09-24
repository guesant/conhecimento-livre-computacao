# Filas de mensagens

Uma fila desacopla produtores e consumidores armazenando mensagens até que consumidores possam processá-las. Dependendo do sistema, acknowledgements, retries, ordering e delivery semantics variam.

## Casos de uso

Processamento assíncrono de jobs, absorção de picos e desacoplamento temporal são usos comuns.

## Boa prática

Projete consumidores idempotentes quando redelivery é possível, defina política de retry e dead-letter e monitore idade e profundidade da fila.

## Má prática

Assumir "exactly once" sem compreender as garantias de broker, consumidor e efeitos externos cria duplicação difícil de detectar. Retry infinito também transforma mensagens impossíveis em bloqueio operacional.

## Continue por aqui

[Event streaming](event-streaming.md) preserva eventos de forma que múltiplos consumidores possam manter posições independentes.
