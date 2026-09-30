# Gauge

Gauge representa um valor que pode aumentar ou diminuir, como temperatura,
memória usada, conexões ativas ou tamanho atual de uma fila.

## Modelagem

Um gauge descreve estado observado, não necessariamente eventos. Para calcular
taxa de mudança, use derivadas ou funções apropriadas e confirme que o valor
possui semântica contínua suficiente para isso.

Não use gauge para contagem acumulada de requisições ou erros. Reinícios e
scrapes ausentes tornam a interpretação diferente de um counter.

## Relações

- [Counter](counter.md) registra ocorrências acumuladas.
- [Histogram](histogram.md) registra distribuição.
- [Métricas](../metricas.md) trata labels e cardinalidade.

## Fonte primária

- [Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/)
