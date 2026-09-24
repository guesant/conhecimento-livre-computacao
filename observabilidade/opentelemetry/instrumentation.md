# Instrumentação OpenTelemetry

Instrumentação adiciona APIs e SDKs para produzir telemetria com contexto,
atributos e exportação configurados. Ela pode ser manual, automática ou uma
combinação das duas.

## Decisões

Instrumente bordas de entrada e saída, operações de banco, filas e jobs com
nomes estáveis. Não inclua segredos, tokens, dados pessoais ou identificadores
de cardinalidade ilimitada como atributos.

Instrumentação automática reduz esforço inicial, mas pode capturar mais
detalhes do que a política permite ou produzir spans de baixo valor. Manual
permite semântica melhor nos limites de negócio.

## Relações

- [OpenTelemetry](index.md) define APIs e SDKs.
- [Collector](collector.md) processa e exporta.
- [Tracing](../tracing.md) usa contexto propagado.

## Fonte primária

- [OpenTelemetry instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/)
