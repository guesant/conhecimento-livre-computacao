# OpenTelemetry Collector

O OpenTelemetry Collector recebe, processa e exporta telemetria entre
instrumentação e backends. Ele permite centralizar batching, filtros,
enriquecimento, retry e roteamento sem embutir toda a lógica em cada serviço.

## Pipeline

Uma pipeline define receivers, processors e exporters para um tipo de sinal.
Receivers aceitam dados; processors transformam ou filtram; exporters enviam.
A configuração precisa separar pipelines de traces, métricas e logs quando
suas garantias e destinos diferem.

## Failure modes

Fila, retry e backpressure podem proteger um backend lento, mas consomem
memória e podem descartar dados quando o limite é atingido. Um Collector
indisponível pode bloquear uma aplicação se a exportação for síncrona ou perder
telemetria se a política for best effort.

## Relações

- [OpenTelemetry](index.md) define o ecossistema.
- [Instrumentação](instrumentation.md) produz sinais.
- [Grafana Alloy](../alloy.md) é uma distribuição que pode executar funções
  semelhantes.

## Fonte primária

- [Collector](https://opentelemetry.io/docs/collector/)
