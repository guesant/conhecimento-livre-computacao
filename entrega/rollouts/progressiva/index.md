# Entrega progressiva

Entrega progressiva limita o impacto de uma versão nova enquanto sinais de
saúde, métricas ou aprovação são observados. O processo precisa definir como
avançar, pausar e retornar, inclusive quando uma alteração de schema não pode
ser revertida junto com o binário.

[Rollouts](../index.md) organiza as estratégias. [Canary](../../progressiva/canary.md),
[blue-green](../../progressiva/blue-green.md) e [Argo Rollouts](../../progressiva/argo-rollouts.md)
implementam escolhas diferentes de tráfego e ambiente.
