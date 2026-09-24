# Alertmanager

Alertmanager recebe alertas do Prometheus, agrupa eventos, aplica silences e
inhibition e encaminha notificações para destinos configurados.

## Roteamento

Grouping combina alertas relacionados para evitar uma mensagem por série.
Routing escolhe destino e severidade. Inhibition suprime alertas derivados
quando uma causa maior já está ativa. Silence suspende uma condição conhecida
por uma janela explícita.

## Alertas acionáveis

Um alerta deve indicar impacto, labels úteis, janela e caminho de resposta.
Silenciar sem prazo ou agrupar por labels instáveis apenas esconde falhas.
O Alertmanager não substitui investigação da métrica ou correção do serviço.

## Failure modes

Falha de configuração, destino indisponível, silences amplos e perda de estado
podem impedir notificação. Monitore o próprio Alertmanager e teste o caminho
até o receptor, não apenas a existência da regra.

## Relações

- [Regras do Prometheus](rules.md) produz alertas.
- [Alertas acionáveis](../../alertas-acionaveis-e-distributed-tracing.md) trata
  a operação.
- [Prometheus](../prometheus.md) é a fonte usual.

## Fonte primária

- [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/)
