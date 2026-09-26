# Taints

Um taint marca um nó com uma condição que impede ou expulsa Pods que não
possuem uma toleration correspondente. Ele é controlado no nó e afeta a
elegibilidade de workloads.

`NoSchedule` impede novas colocações incompatíveis. `PreferNoSchedule` expressa
uma preferência. `NoExecute` pode remover Pods existentes que não toleram o
taint, com possibilidade de permanência temporária quando a toleration declara
`tolerationSeconds`.

Taints são úteis para reservar hardware, separar nós de control plane e marcar
manutenção. Uma regra ampla que aceita qualquer chave precisa de justificativa,
porque pode permitir que um workload atravesse um domínio de confiança ou de
falha que deveria permanecer isolado.

## Relações

- [Tolerations](tolerations.md) expressa a permissão correspondente no Pod.
- [Scheduler](../control-plane/scheduler.md) aplica a elegibilidade.
- [Cordon e drain](../../../operacional/manutencao-de-no-cordon-drain-e-disco.md) tratam de
  manutenção voluntária.

## Fonte primária

- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
