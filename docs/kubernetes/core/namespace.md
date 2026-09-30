# Namespace

Namespace é um escopo lógico para nomes e políticas de objetos Kubernetes.
Ele permite separar workloads, aplicar quotas e organizar ownership sem criar
um cluster diferente para cada grupo.

## O que isola

A maioria dos recursos namespaced possui nome único dentro de um Namespace,
mas não globalmente. ResourceQuota, LimitRange, Role e NetworkPolicy costumam
usar esse escopo. Nodes, PersistentVolumes e alguns recursos de control plane
são cluster-scoped e não ficam contidos em um Namespace.

Namespace não é uma fronteira de segurança suficiente por si só. RBAC,
NetworkPolicy, admission policy, quotas e identidade de workload precisam ser
configurados conforme a ameaça. Um usuário com permissão ampla no cluster pode
continuar acessando vários Namespaces.

## Lifecycle

Excluir um Namespace inicia a exclusão dos objetos namespaced. Recursos com
finalizers podem manter o Namespace em `Terminating`, e dependências externas
podem exigir limpeza antes de remover o finalizer. A exclusão deve ser tratada
como mudança destrutiva, não como simples reorganização visual.

## Relações

- [RBAC](../access/rbac.md) define autorização por Namespace.
- [ResourceQuota](../recursos/requests.md) e [LimitRange](../recursos/limits.md)
  controlam consumo.
- [NetworkPolicy](../networking/network-policy.md) pode limitar tráfego entre
  namespaces.

## Fonte primária

- [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
