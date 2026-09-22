# Grafana

Grafana é uma plataforma de consulta e visualização que se conecta a data sources. Ele não substitui Prometheus, Loki ou um backend de tracing: consulta esses sistemas e apresenta seus dados em dashboards, explorações e alertas conforme a configuração.

## Casos de uso

Dashboards operacionais, exploração ad hoc e correlação visual entre fontes diferentes são usos comuns.

## Boa prática

Crie dashboards a partir de perguntas operacionais concretas. Mantenha unidades, escalas e labels consistentes. Evite painéis que só demonstram que "há dados" sem apoiar uma decisão.

## Má prática

Dashboards com dezenas de gráficos sem hipótese ou ação correspondente produzem ruído. Outra má prática é considerar o dashboard a fonte de verdade quando a definição da métrica e sua semântica vivem no sistema produtor.

## Fontes

- Grafana documentation: <https://grafana.com/docs/grafana/latest/>

## Continue por aqui

[Prometheus](prometheus.md) e [Loki](loki.md) são dois data sources comuns com modelos diferentes.
