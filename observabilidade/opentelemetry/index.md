# OpenTelemetry

OpenTelemetry é um conjunto de APIs, SDKs, protocolos e componentes para
instrumentar, coletar e exportar telemetria. Ele cobre traces, métricas e logs
sem ser um backend de armazenamento ou visualização.

## Modelo

A aplicação produz sinais por APIs e SDKs. Exporters enviam os dados para um
backend ou para o Collector. Recursos, atributos e contexto de trace conectam
observações de serviços diferentes.

A padronização do transporte não define retenção, consulta, dashboard ou
política de alertas. Essas responsabilidades continuam nos backends e
ferramentas de operação.

## Relações

- [OpenTelemetry Collector](collector.md) recebe e encaminha sinais.
- [Instrumentação](instrumentation.md) cria dados na aplicação.
- [Tracing](../tracing.md) explica o sinal distribuído.
- [Exemplars](../metric-types/exemplars.md) ligam métricas a traces.

## Fonte primária

- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
