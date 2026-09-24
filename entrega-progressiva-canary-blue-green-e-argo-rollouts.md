# Entrega progressiva

Esta página foi descompactada para separar estratégias de sua implementação.

- [Canary](entrega/progressiva/canary.md) aumenta exposição gradualmente.
- [Blue-green](entrega/progressiva/blue-green.md) mantém revisões paralelas e troca a ativa.
- [Argo Rollouts](entrega/progressiva/argo-rollouts.md) implementa essas e outras estratégias no Kubernetes.
- [Feature flags](feature-flags.md) controlam ativação de comportamento e podem complementar rollout.

Escolha primeiro o modelo de redução de risco; só depois a ferramenta que o automatiza.
