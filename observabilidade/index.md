# Observabilidade

Observabilidade é a capacidade de inferir o estado interno de um sistema a partir dos sinais que ele produz. Métricas, logs, traces e profiles possuem modelos e custos diferentes; ferramentas concretas implementam partes dessa cadeia.

## Sinais

[Métricas](metricas.md) representam medições agregáveis e séries temporais. [Logs](logs.md) registram eventos. [Distributed tracing](tracing.md) relaciona operações ao longo de uma requisição distribuída.

## Implementações

[Prometheus](prometheus.md) coleta e consulta métricas. [Loki](loki.md) centraliza logs com um modelo de indexação orientado a labels. [Grafana](grafana.md) consulta e visualiza fontes de dados; não é, por si só, o coletor dos sinais.

## Princípio operacional

Escolha o sinal pela pergunta. Não transforme logs em métricas de cardinalidade ilimitada nem use métricas quando precisa investigar um evento individual com contexto.

## Continue por aqui

[Sinais de observabilidade e saúde](../sinais-de-observabilidade-e-saude-de-aplicacao.md) fornece a visão geral existente. As páginas desta seção aprofundam cada sinal e implementação.