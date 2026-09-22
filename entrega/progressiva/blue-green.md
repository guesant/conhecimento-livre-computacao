# Blue-green deployment

Blue-green mantém duas revisões ou ambientes equivalentes: um atende tráfego enquanto o outro recebe a nova versão. A promoção troca qual revisão é ativa.

## Casos de uso

É útil quando a troca precisa ser rápida e há capacidade para manter duas revisões simultaneamente.

## Boa prática

Garanta compatibilidade de dados entre as versões durante a janela de troca e teste o ambiente inativo antes da promoção.

## Má prática

Considerar rollback instantâneo quando uma migração destrutiva já tornou a versão anterior incompatível é uma falsa garantia. O custo de duplicar capacidade também precisa ser considerado.

## Continue por aqui

[Canary](canary.md) aumenta exposição gradualmente. [Argo Rollouts](argo-rollouts.md) oferece ambos os modelos.