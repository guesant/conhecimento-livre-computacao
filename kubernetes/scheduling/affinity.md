# Affinity e anti-affinity

Affinity expressa preferências ou restrições de scheduling baseadas em labels
de nós ou de outros Pods. Anti-affinity expressa separação. As regras podem
ser obrigatórias, bloqueando nós incompatíveis, ou preferenciais, influenciando
o score sem tornar a colocação impossível.

## Node affinity

Node affinity escolhe nós por labels como zona, arquitetura, hardware ou papel.
Labels de nó precisam ser protegidas contra alteração por workloads não
confiáveis, porque uma regra de affinity só é tão confiável quanto a identidade
que controla essas labels.

## Pod affinity

Pod affinity e anti-affinity relacionam a localização de um Pod à presença de
outros Pods. Elas podem aumentar localidade ou espalhar réplicas por domínio.
Uma regra obrigatória ampla pode não ter solução em um cluster pequeno, deixando
Pods pendentes.

Topology keys, namespaces e selectors fazem parte da semântica. Uma policy
precisa dizer qual failure domain está sendo preservado, nó, zona, rack ou
outro domínio reconhecido pelo cluster.

## Relações

- [Scheduler](../control-plane/scheduler.md) filtra e pontua candidatos.
- [Topology spread](topology-spread.md) oferece uma forma explícita de
  distribuição.
- [Taints e tolerations](taints-tolerations.md) controlam elegibilidade.

## Fonte primária

- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
