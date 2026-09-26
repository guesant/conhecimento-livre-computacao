# Scheduling por taints

As páginas de [taints](taints.md) e [tolerations](tolerations.md) separam a
marca aplicada ao nó da permissão declarada pelo Pod. Esta página preserva o
mapa relacional para quem precisa entender o mecanismo completo. Uma
toleration não força scheduling e não substitui affinity.

## Efeitos

`NoSchedule` impede novas colocações incompatíveis. `PreferNoSchedule` é uma
preferência. `NoExecute` pode remover Pods existentes que não toleram o taint,
com possibilidade de tolerar por tempo limitado. A toleration precisa
corresponder à chave, operador, valor e efeito conforme a regra declarada.

## Uso

Taints são úteis para reservar nós, separar hardware, marcar condições de
manutenção e proteger nós de control plane. Tolerations amplas como uma regra
que aceita qualquer chave devem ser justificadas, porque podem permitir que um
workload seja colocado em um domínio onde não deveria executar.

## Relações

- [Scheduler](../control-plane/scheduler.md) aplica a elegibilidade.
- [DaemonSet](../core/daemonset.md) frequentemente usa tolerations para
  agentes de nó.
- [Cordon e drain](../../../operacional/manutencao-de-no-cordon-drain-e-disco.md) usam outro
  mecanismo para manutenção voluntária.

## Fonte primária

- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
