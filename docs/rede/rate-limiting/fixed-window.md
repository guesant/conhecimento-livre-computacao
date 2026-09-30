# Fixed window

Fixed window conta eventos em intervalos discretos, como cada minuto. Quando a
contagem alcança o limite, novas requisições são rejeitadas até a próxima
janela.

## Trade-off

O algoritmo é simples e barato, mas permite uma rajada no fim de uma janela e
outra no começo da seguinte. O limite efetivo em uma fronteira pode ser quase
o dobro do valor declarado.

É adequado quando simplicidade e custo importam mais que suavidade, ou quando
uma camada posterior absorve a variação.

## Relações

- [Rate limiting](index.md) define a política.
- [Sliding window](sliding-window.md) reduz a descontinuidade.
- [Token bucket](token-bucket.md) modela burst explicitamente.
