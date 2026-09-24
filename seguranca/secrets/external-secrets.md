# External Secrets Operator

External Secrets Operator sincroniza valores de backends externos para Secrets
Kubernetes. SecretStore ou ClusterSecretStore define o backend e
ExternalSecret declara quais valores buscar.

## Modelo

O operator precisa de uma identidade para consultar o backend. Autenticação
nativa por ServiceAccount reduz credenciais estáticas, mas não elimina
permissões, bootstrap ou disponibilidade do backend.

O Secret materializado pode ser lido pela API conforme RBAC. Se essa superfície
não é desejada, um driver CSI pode montar o valor diretamente no Pod.

## Failure modes

Indisponibilidade do backend, credencial expirada, caminho errado, policy
insuficiente ou reconciliação atrasada podem deixar o Secret antigo ou ausente.
Observe status, eventos e timestamp de sincronização sem imprimir o conteúdo.

## Relações

- [Secret store externo](../../secret-store-externo.md) compara backends.
- [RBAC Kubernetes](../../kubernetes/access/rbac.md) limita a API.
- [Bootstrap](bootstrap.md) entrega a primeira identidade.

## Fonte primária

- [External Secrets Operator](https://external-secrets.io/latest/)
