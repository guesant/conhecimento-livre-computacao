# Counter

Counter é uma métrica monotônica que aumenta ao registrar ocorrências e pode
voltar a zero quando o processo reinicia. Ela representa eventos acumulados,
não um valor instantâneo.

## Consulta

A taxa é calculada a partir da variação em uma janela, usando funções como
rate ou increase em PromQL. Um reset esperado de processo não deve ser
interpretado como redução de tráfego.

Não use counter para representar estado atual, como número de conexões abertas.
Esse caso pertence a gauge.

## Relações

- [Gauge](gauge.md) representa valores que sobem e descem.
- [Histogram](histogram.md) representa distribuição.
- [Métricas](../metricas.md) cobre cardinalidade e modelagem.

## Fonte primária

- [Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/)
