# Grafana Alloy

Grafana Alloy é uma distribuição de coleta e processamento que pode combinar
pipelines de métricas, logs e traces. Ele atua como agente ou gateway e pode
integrar protocolos e backends diferentes.

## Escolha

Alloy faz sentido quando a operação quer um agente unificado e a integração
com o ecossistema Grafana pesa. OpenTelemetry Collector pode ser preferível
quando a prioridade é uma distribuição upstream e neutra em relação ao
backend.

A escolha não elimina decisões de retenção, cardinalidade, segurança ou
backpressure. Um agente local ainda precisa de limites e observabilidade
própria.

## Relações

- [OpenTelemetry Collector](opentelemetry/collector.md) trata o componente
  upstream.
- [Prometheus](prometheus.md) armazena métricas.
- [Loki](loki.md) armazena logs.

## Fonte primária

- [Grafana Alloy](https://grafana.com/docs/alloy/latest/)
