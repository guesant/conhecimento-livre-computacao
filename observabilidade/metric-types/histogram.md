# Histogram

Histogram agrupa observações em buckets cumulativos e registra count e sum.
Ele permite estimar quantis e proporções de observações abaixo de um limite
sem armazenar cada evento individual como uma série.

## Latência

Buckets devem refletir a distribuição e as decisões operacionais. Buckets
muito estreitos aumentam séries e custo; buckets inadequados perdem resolução
na região em que o SLO precisa ser avaliado.

Em Prometheus, `histogram_quantile` usa buckets identificados pelo label `le`. A métrica deve
expor o bucket infinito e labels com cardinalidade controlada.

## Relações

- [Counter](counter.md) registra contagens de eventos.
- [Gauge](gauge.md) registra estado atual.
- [Exemplars](exemplars.md) conectam observação a trace.

## Fonte primária

- [Histograms and summaries](https://prometheus.io/docs/practices/histograms/)
