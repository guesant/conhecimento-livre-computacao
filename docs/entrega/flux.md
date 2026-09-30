# Flux

Flux é uma plataforma GitOps baseada em controllers Kubernetes que reconcilia
fontes e recursos declarativos. Ele oferece APIs e controllers para fontes
Git, artefatos, Kustomize e Helm.

## Comparação

Flux e Argo CD usam reconciliação pull-based. As diferenças aparecem no modelo
de recursos, na interface operacional, na composição dos controllers e no
fluxo de promoção de artefatos. A escolha deve considerar ownership,
observabilidade, integração e experiência da equipe.

## Relações

- [Argo CD](../argocd.md) é a alternativa adotada ou avaliada.
- [Argo CD e Flux](../comparacoes/entrega/argocd-flux.md) compara dimensões.
- [GitOps](gitops.md) explica o modelo comum.

## Fonte primária

- [Flux documentation](https://fluxcd.io/flux/)
