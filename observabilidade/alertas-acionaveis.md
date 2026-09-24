# Alertas acionáveis

Um alerta acionável liga uma condição mensurável a uma resposta esperada. A
severidade deve representar a resposta necessária, não apenas a importância
técnica do componente: `critical` significa acionar alguém imediatamente com
uma ação possível, `warning` significa revisar antes que vire impacto, e
`info` não deveria acordar ninguém.

Um alerta precisa ter uma condição ligada a impacto real, um responsável e um
runbook acessível durante a indisponibilidade. Para uma condição puramente
informativa, o lugar adequado é um dashboard. Alertas sem critério de ação
treinam a equipe a ignorar notificações e escondem os eventos relevantes.

## Duração e custo da avaliação

O campo `for` exige que a condição permaneça verdadeira antes de disparar. Ele
reduz ruído causado por flutuações curtas, mas deve ser compatível com o tempo
de impacto tolerável. Um valor longo demais atrasa a detecção de um incidente
real.

*Recording rules* pré-computam expressões caras. Isso reduz a carga de
avaliação repetida, mas não substitui uma regra de alerta. É uma otimização da
consulta, não uma estratégia de notificação.

## Roteamento e agrupamento

O Alertmanager resolve um problema diferente: como consolidar e distribuir
alertas já disparados. Um nó indisponível pode gerar um alerta para cada Pod
que estava nele. Agrupar por rótulos comuns transforma esses eventos em uma
notificação sobre um incidente, em vez de uma sequência de mensagens
duplicadas.

O atraso inicial de um grupo permite que eventos correlacionados cheguem antes
do primeiro envio. O intervalo entre atualizações controla a frequência de
novas notificações enquanto o grupo continua ativo. O intervalo de repetição
lembra um alerta que ainda não foi resolvido mesmo sem mudança no grupo.

## Relações

- [Alertmanager](prometheus/alertmanager.md) documenta o roteamento,
  agrupamento, inibição e silenciamento.
- [Regras do Prometheus](prometheus/rules.md) explica recording rules e regras
  de alerta.
- [Sinais de observabilidade](../sinais-de-observabilidade-e-saude-de-aplicacao.md)
  situa alertas entre métricas, logs e traces.

## Fonte primária

- [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
- [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/)
