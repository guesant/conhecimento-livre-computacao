# Exemplars

Exemplars associam uma observação de métrica a identificadores de uma execução
específica, normalmente um trace. Eles criam uma ponte entre a visão agregada
da métrica e a investigação de uma ocorrência.

## Limites

Exemplar não transforma cada request em label e não deve receber cardinalidade
ilimitada no conjunto principal de séries. Ele é um apontador opcional para
detalhe, não o armazenamento do evento inteiro.

## Uso

Uma métrica de latência pode mostrar que um bucket viola o objetivo e oferecer
um exemplar para abrir um trace representativo. O trace precisa existir no
backend correspondente e preservar sua própria política de retenção.

## Relações

- [Histogram](histogram.md) produz a distribuição agregada.
- [Tracing](../tracing.md) armazena a investigação detalhada.
- [OpenTelemetry](../opentelemetry/index.md) pode transportar ambos.

## Fonte primária

- [Prometheus exemplars](https://prometheus.io/docs/prometheus/latest/feature_flags/#exemplars-storage)
