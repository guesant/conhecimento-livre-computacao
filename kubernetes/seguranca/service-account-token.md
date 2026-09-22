# ServiceAccount token

ServiceAccount tokens permitem que workloads se autentiquem perante a API Kubernetes conforme a identidade da ServiceAccount.

Workloads que não precisam da API não precisam carregar essa credencial. Desabilitar automount reduz exposição.

Quando acesso é necessário, use ServiceAccount dedicada e [RBAC](../../rbac-do-kubernetes.md) mínimo.