# Argo CD AppProject

AppProject agrupa Applications sob políticas comuns. Ele restringe de quais
repositórios uma aplicação pode ler, para quais destinos pode entregar e quais
recursos Kubernetes pode criar.

## Fronteiras

Permitir qualquer repositório, cluster, Namespace ou recurso de escopo de
cluster transforma o projeto em uma credencial administrativa indireta.
Restrições devem ser pequenas e coerentes com a responsabilidade do grupo.

AppProject também pode definir papéis para operações na API do Argo CD. Esses
papéis não substituem RBAC do Kubernetes.

## Relações

- [Application](application.md) consome a política.
- [RBAC Kubernetes](../kubernetes/access/rbac.md) autoriza API do cluster.
- [App of apps](app-of-apps.md) precisa de permissões para criar filhas.

## Fonte primária

- [Argo CD AppProjects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/)
