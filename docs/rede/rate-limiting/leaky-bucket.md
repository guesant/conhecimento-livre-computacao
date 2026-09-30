# Leaky bucket

Leaky bucket processa ou libera eventos em uma taxa controlada, como um balde
que drena por uma abertura de tamanho fixo. Ele suaviza picos e pode modelar
uma fila de saída.

## Trade-off

A fila precisa de capacidade e política para overflow. Quando o producer é mais
rápido que a drenagem por tempo suficiente, o sistema precisa rejeitar,
bloquear ou descartar. A suavidade pode aumentar latência mesmo quando o
upstream está saudável.

## Relações

- [Token bucket](token-bucket.md) permite burst explícito.
- [Filas](../../dados/mensageria/filas.md) tratam buffering e consumidores.
- [Rate limiting](index.md) define a garantia desejada.
