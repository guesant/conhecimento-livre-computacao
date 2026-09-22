# Prometheus

Prometheus é um sistema de monitoramento e banco de séries temporais. Seu modelo comum de coleta é pull: o servidor descobre targets e faz scrape de endpoints que expõem métricas.

## Casos de uso

Monitoramento de aplicações e infraestrutura, alertas derivados de séries temporais e recording rules para pré-computar consultas são usos centrais. Em Kubernetes, o Prometheus Operator fornece recursos como ServiceMonitor, PodMonitor e PrometheusRule.

## Boa prática

Controle cardinalidade, defina retenção com base em capacidade e necessidade, use recording rules para consultas caras recorrentes e monitore o próprio pipeline de monitoramento.

## Má prática

Usar labels ilimitados, assumir que scrape bem-sucedido significa aplicação saudável ou hospedar toda observabilidade no mesmo failure domain sem reconhecer que a perda dele elimina também a evidência são problemas comuns.

## Limites

Prometheus não é um banco genérico de eventos. Logs e traces possuem modelos mais adequados para dados de alta dimensionalidade por evento.

## Fontes

- Prometheus documentation: https://prometheus.io/docs/
- Prometheus data model: https://prometheus.io/docs/concepts/data_model/

## Continue por aqui

[Métricas](metricas.md) explica o modelo. [Grafana](grafana.md) pode consultar Prometheus como data source.