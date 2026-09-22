# Distributed tracing

Distributed tracing representa uma operação como um trace composto por spans relacionados. Cada span descreve uma unidade de trabalho e relações de causalidade ou parentesco permitem acompanhar uma requisição através de múltiplos serviços.

## Casos de uso

Tracing é especialmente útil para investigar latência distribuída, localizar qual dependência domina o tempo de resposta e compreender caminhos que atravessam vários serviços.

## Boa prática

Propague contexto de trace de forma padronizada, defina sampling conscientemente e evite colocar dados sensíveis em atributos. Instrumente fronteiras relevantes em vez de criar spans para cada função trivial.

## Má prática

Amostragem agressiva sem considerar traces raros pode esconder exatamente os casos problemáticos. O extremo oposto, capturar tudo indefinidamente, pode ser economicamente inviável.

## Fontes

- W3C Trace Context: https://www.w3.org/TR/trace-context/
- OpenTelemetry tracing: https://opentelemetry.io/docs/concepts/signals/traces/

## Continue por aqui

[Métricas](metricas.md) mostram comportamento agregado; [logs](logs.md) preservam eventos; tracing conecta operações distribuídas.