# ServiceAccount

ServiceAccount é uma identidade namespaced para workloads e controllers. Um
Pod pode usar essa identidade para autenticar na API Kubernetes ou para ser
reconhecido por integrações que atribuem permissões a workloads.

## Identidade e credenciais

O token projetado para um Pod é obtido por meio da API de TokenRequest e pode
ter audiência, expiração e escopo definidos. Montar automaticamente uma
credencial em todo Pod aumenta a superfície de ataque, por isso workloads que
não falam com a API devem desabilitar essa montagem.

ServiceAccount não concede permissão por si só. [RBAC](../access/rbac.md)
associa a identidade a Roles ou ClusterRoles. A conta deve ter somente as
ações necessárias para a aplicação, e o uso de uma conta compartilhada dificulta
atribuição e revogação.

## Relações

- [Secret](secret.md) pode armazenar material associado, mas não deve ser
  tratado como token eterno por padrão.
- [RBAC](../access/rbac.md) autoriza operações.
- [Pod SecurityContext](../seguranca/security-context.md) define outras
  propriedades de execução, independentes da identidade da API.

## Fonte primária

- [Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
