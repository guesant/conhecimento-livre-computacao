# Canary deployment

Canary expõe uma nova versão a uma fração controlada do tráfego ou dos usuários antes de ampliar a exposição.

## Casos de uso

É adequado quando sinais de produção são necessários para validar uma versão e existe capacidade de segmentar tráfego e comparar comportamento.

## Boa prática

Defina métricas de sucesso e rollback antes do rollout. Aumente exposição em etapas e preserve uma versão estável para reversão.

## Má prática

Enviar 5% do tráfego sem observar nenhum indicador não é validação canary, apenas implantação lenta. Também é perigoso usar canary para mudanças de banco irreversíveis sem estratégia de compatibilidade.

## Continue por aqui

[Blue-green](blue-green.md) usa paralelismo e troca de tráfego de outra forma. [Argo Rollouts](argo-rollouts.md) automatiza estratégias no Kubernetes.