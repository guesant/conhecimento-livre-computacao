# Sliding window

Sliding window avalia o volume numa janela que se move com o instante atual.
Ela reduz a rajada artificial da fronteira do fixed window.

## Custo

Uma implementação precisa manter eventos, buckets menores ou contadores
ponderados. Mais precisão exige mais estado e trabalho. Uma aproximação por
subjanelas pode ser suficiente quando o limite não é uma quota financeira.

Em múltiplas réplicas, a janela precisa de estado compartilhado para representar
o total agregado.

## Relações

- [Fixed window](fixed-window.md) é mais simples.
- [Token bucket](token-bucket.md) separa taxa média e burst.
- [Rate limiting local e compartilhado](../../rate-limiting-politica-local-e-compartilhada.md)
  trata distribuição de estado.
