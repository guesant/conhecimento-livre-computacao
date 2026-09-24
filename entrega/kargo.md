# Kargo

Kargo coordena promoção de versões entre ambientes GitOps. Ele observa
artefatos, valida etapas e atualiza a configuração que o reconciler de destino
deve aplicar.

Para um fluxo executável do primeiro projeto até autopromoção, consulte o
[tutorial completo de Kargo](kargo-tutorial.md).

## Fronteira

Kargo não substitui o reconciler Kubernetes. Argo CD ou Flux continua
responsável por aplicar a configuração ao cluster. Kargo atua na promoção,
sequenciamento e evidência de que uma revisão pode avançar.

## Failure modes

Uma promoção pode falhar por artefato ausente, credencial, policy, conflito no
repositório ou saúde insuficiente do ambiente anterior. O diagnóstico precisa
separar erro de promoção de erro de sincronização posterior.

## Relações

- [GitOps](gitops.md) fornece o modelo declarativo.
- [Reconciliação](reconciliation.md) aplica a revisão promovida.
- [Argo Rollouts](progressiva/argo-rollouts.md) trata tráfego e rollout dentro
  do cluster.

## Fonte primária

- [Kargo documentation](https://docs.kargo.io/)
