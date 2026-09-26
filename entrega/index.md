# Entrega e GitOps

Esta área separa princípios de entrega, estratégias de rollout e implementações concretas.

## GitOps

GitOps usa repositórios versionados como fonte declarativa e reconciliação contínua para aproximar estado desejado e estado observado. [Argo CD](../argocd.md) é uma implementação desse modelo para Kubernetes.

## Entrega progressiva

[Canary](progressiva/canary.md) expõe uma mudança gradualmente. [Blue-green](progressiva/blue-green.md) mantém ambientes ou revisões paralelas e troca o tráfego. [Argo Rollouts](progressiva/argo-rollouts.md) implementa estratégias avançadas no Kubernetes.

## Feature flags

Feature flags separam disponibilização de código de ativação de comportamento. Elas podem complementar rollout, mas não são sinônimo de canary.

## Versionamento e identificação

[Versionamento de releases e identificadores](versionamento-de-releases.md) compara SemVer, CalVer, numeração sequencial e hash Git. A página separa o significado de uma versão do contrato da identidade exata do artefato que foi produzido.

## Continue por aqui

Escolha a estratégia pelo tipo de risco que deseja controlar: infraestrutura/revisão, exposição de tráfego ou ativação de funcionalidade.
