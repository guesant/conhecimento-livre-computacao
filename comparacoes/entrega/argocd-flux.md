# Argo CD e Flux

Argo CD e Flux implementam reconciliação GitOps para Kubernetes. Ambos podem manter estado do cluster convergente com fontes declarativas, mas possuem modelos de recursos, experiência de usuário e ecossistemas diferentes.

## Argo CD

Argo CD oferece Application/AppProject, UI própria, API e padrões como app-of-apps/ApplicationSet. É atraente quando visualização e um modelo explícito de aplicações fazem parte da experiência operacional.

## Flux

Flux organiza capacidades em controllers e recursos Kubernetes, incluindo source, kustomize, helm e image automation. A experiência é fortemente Kubernetes-native e composável.

## Critérios

Compare modelo de tenancy, promoção entre ambientes, image automation, UX desejada, gestão de múltiplos clusters, integração com Helm/Kustomize, políticas de acesso e familiaridade operacional.

## Composição

Não é comum precisar dos dois reconciliando os mesmos recursos. Se coexistirem, separe ownership para impedir loops em que cada controller desfaz o outro.

## Anti-pattern

Escolher pelo número de estrelas ou pela existência de UI ignora o modelo de operação que será usado diariamente.

## Fontes

- Argo CD: https://argo-cd.readthedocs.io/
- Flux: https://fluxcd.io/flux/

## Continue por aqui

[Argo CD](../../argocd.md) aprofunda a ferramenta e [IaC, configuração e GitOps](../../composicoes/entrega/iac-configuracao-gitops.md) situa sua responsabilidade.