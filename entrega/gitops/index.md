# GitOps

GitOps usa estado declarativo versionado, agentes de reconciliação e observação contínua para aproximar o ambiente do estado desejado. A categoria trata o modelo operacional, não uma ferramenta específica.

## Conceitos

- [GitOps](../gitops.md) explica a fonte declarativa e o modelo pull-based.
- [Reconciliação](../reconciliation.md) explica a repetição segura que compara estado desejado e observado.
- [Entrega pull-based](../pull-based-delivery.md) e [entrega push-based](../push-based-delivery.md) comparam quem inicia a aplicação.
- [Drift](../drift.md) trata divergência entre declaração e ambiente.
- [Sync, prune e self-heal](../sync-prune-self-heal.md) trata ações de convergência.

## Implementações

[Argo CD](../../argocd.md), [Flux](../flux.md) e [Kargo](../kargo/index.md) participam de partes diferentes do ciclo. Argo CD e Flux reconciliam aplicações. Kargo coordena promoção de artefatos e estados entre ambientes. A composição pode usar mais de uma ferramenta, mas as responsabilidades e os donos do estado precisam estar explícitos.

## Relações

[Rollouts](../rollouts/index.md) trata exposição progressiva. [CI/CD](../../ci-cd.md) trata construção, teste e publicação. GitOps não substitui o pipeline de build nem transforma um artefato não verificado em artefato confiável.
