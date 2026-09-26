# Rollouts

Um rollout controla como uma nova versão passa a receber tráfego. A entrega progressiva limita o impacto de uma mudança e usa sinais de saúde, métricas ou aprovação para avançar, pausar ou reverter.

## Estratégias

- [Canary](../progressiva/canary.md) envia uma parcela do tráfego para a revisão nova.
- [Blue-green](../progressiva/blue-green.md) mantém duas revisões e alterna o ambiente ativo.
- [Argo Rollouts](../progressiva/argo-rollouts.md) implementa estratégias progressivas no Kubernetes.

Canary e blue-green são estratégias, não garantias de segurança. Elas precisam de métricas representativas, uma forma de interromper o avanço, compatibilidade entre versões e rollback que também funcione para dados. Um deploy gradual não desfaz uma migration destrutiva já aplicada.

## Relações

[Feature flags](../../feature-flags.md) controlam ativação de comportamento,
não necessariamente a versão que está implantada. [GitOps](../gitops/index.md)
trata a reconciliação do estado declarativo. [Testes de capacidade](../../confiabilidade/testes/index.md)
ajudam a validar o impacto operacional antes da promoção.
