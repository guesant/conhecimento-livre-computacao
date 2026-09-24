# Regras do Prometheus

Recording rules avaliam uma expressão recorrente e gravam seu resultado como
uma nova série. Alerting rules avaliam uma condição e produzem um alerta para
o caminho de roteamento.

## Recording rules

Materialize agregações caras ou usadas em vários dashboards e alertas. A regra
deve ter nome, unidade e labels estáveis. Gravar tudo prematuramente aumenta
cardinalidade e armazenamento.

## Alerting rules

Um alerta precisa representar uma condição acionável, com severidade, contexto,
for e documentação de resposta. Um threshold sem ação correspondente gera
ruído e alert fatigue.

## Failure modes

Erro de PromQL, target sem scrape ou regra não carregada pode deixar
observabilidade incompleta sem impedir a aplicação. Monitore o estado de
avaliação, o atraso e a presença das séries esperadas.

## Relações

- [Prometheus](../prometheus.md) executa e armazena as regras.
- [Alertmanager](alertmanager.md) roteia alertas.
- [Alertas acionáveis](../../alertas-acionaveis-e-distributed-tracing.md)
  trata resposta operacional.

## Fonte primária

- [Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)
- [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
