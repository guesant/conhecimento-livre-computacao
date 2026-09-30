# Token bucket

Token bucket acumula tokens até uma capacidade máxima e consome um token por
operação. A taxa de reposição define o consumo médio e a capacidade define o
burst permitido.

## Comportamento

Quando há tokens, a requisição passa e o bucket diminui. Quando não há, a
requisição espera ou é rejeitada conforme a política. A capacidade precisa
representar o que o upstream suporta em uma rajada, não apenas a taxa média.

## Relações

- [Rate limiting](index.md) define identidade e resposta.
- [Leaky bucket](leaky-bucket.md) drena em ritmo mais constante.
- [API gateway](../api-gateway/index.md) pode aplicar o bucket por route ou
  consumer.
