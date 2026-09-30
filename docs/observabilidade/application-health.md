# Saúde de aplicação

Um Pod em estado `Running` apenas indica que o processo iniciou e não terminou.
Um Pod `Ready` passou a `readinessProbe`, mas uma probe mal desenhada pode não
verificar uma operação relevante. A disponibilidade percebida pelo consumidor
é uma camada adicional que precisa observar o serviço de fora da aplicação.

Uma `livenessProbe` deve detectar um processo travado que só se recupera com
reinício. Uma `readinessProbe` deve retirar temporariamente o Pod dos endpoints
de um Service quando ele não pode receber tráfego, sem reiniciar o processo. A
liveness não deve depender de uma falha momentânea do banco ou de outra
dependência externa, porque reiniciar o processo não corrige essa dependência.

Monitoramento de caixa-branca usa métricas, logs e traces internos. Ele explica
causas, mas pode falhar junto com o sistema observado. Monitoramento de
caixa-preta testa DNS, TLS ou HTTP a partir de fora e confirma a disponibilidade
percebida, embora não explique sua causa.

## Relações

- [Liveness probe](../kubernetes/recursos/liveness-probe.md) trata de reinício.
- [Readiness probe](../kubernetes/recursos/readiness-probe.md) trata de
  elegibilidade para tráfego.
- [Sinais de observabilidade](../sinais-de-observabilidade-e-saude-de-aplicacao.md)
  apresenta métricas, logs e traces.
