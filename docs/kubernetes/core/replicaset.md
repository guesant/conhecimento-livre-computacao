# ReplicaSet

ReplicaSet é um controller que mantém um número desejado de Pods equivalentes.
Ele compara os Pods que correspondem ao selector com a quantidade declarada e
cria ou remove Pods para aproximar o estado atual do desejado.

## Responsabilidade

O ReplicaSet identifica seus Pods por labels e selector. Se um Pod compatível
desaparece, ele cria outro usando o Pod template. Se existem Pods demais, ele
remove o excedente conforme as regras do controller. O ReplicaSet não faz
rollout entre versões e não oferece identidade estável para cada réplica.

Na prática, um Deployment administra ReplicaSets para associar versões do
template a revisões e controlar a transição entre elas. Criar ReplicaSets
manualmente é útil para entender o mecanismo, mas geralmente perde as
garantias de rollout e rollback que justificam um Deployment.

## Selector e ownership

O selector deve identificar apenas os Pods que o ReplicaSet possui. Labels
compartilhadas por workloads diferentes podem fazer um controller contar Pods
que não criou. Owner references permitem que o garbage collector relacione o
ReplicaSet aos Pods dependentes.

## Relações

- [Pod](pod.md) é a unidade que o ReplicaSet cria.
- [Deployment](deployment.md) é a abstração recomendada para workloads
  stateless com rollout.
- [Owner references](../lifecycle/owner-references.md) explicam a relação de
  ownership entre objetos.

## Fonte primária

- [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
