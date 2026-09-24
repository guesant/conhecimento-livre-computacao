# Topology spread constraints

Topology spread constraints controlam como réplicas de Pods se distribuem
entre domínios de topologia, como nós, zonas ou regiões. Elas tornam explícito
um objetivo de equilíbrio e informam o que fazer quando a distribuição perfeita
é impossível.

## Modelo

`topologyKey` identifica o domínio e `labelSelector` define quais Pods entram
na contagem. `maxSkew` limita a diferença aceitável entre domínios. A regra
`DoNotSchedule` bloqueia uma colocação que ultrapasse o limite; `ScheduleAnyway`
permite a colocação, mas penaliza o candidato no score.

## Failure domain

Espalhar por nós protege contra falha de um nó. Espalhar por zonas protege
contra uma falha de domínio maior, mas só funciona se os nós estiverem
corretamente rotulados e houver capacidade em cada domínio. A constraint não
cria capacidade, não replica volumes e não substitui a estratégia de
disponibilidade da aplicação.

## Relações

- [Affinity](affinity.md) expressa relações e preferências.
- [PodDisruptionBudget](../recursos/pdb.md) limita disrupções voluntárias.
- [Scheduler](../control-plane/scheduler.md) aplica a regra.

## Fonte primária

- [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
