# DaemonSet

DaemonSet garante que um Pod esteja presente nos nós que correspondem ao seu
selector. Ele é adequado para agentes que precisam observar, configurar ou
servir cada nó, como coletores de logs, plugins de rede e componentes de
storage.

## Seleção de nós

O conjunto de nós pode ser limitado por node selector, affinity, taints e
tolerations. A afirmação "um por nó" significa um por nó elegível, não um por
nó indiscriminadamente. Alterar labels ou tolerations pode criar ou remover
Pods de forma legítima.

## Atualização

O DaemonSet pode atualizar Pods usando rollout gradual ou recriação. O ritmo
precisa considerar que o agente pode ser parte da rede, observabilidade ou
storage do próprio nó que está sendo atualizado. Uma falha no agente pode
reduzir a capacidade de diagnóstico do cluster e, em alguns casos, impedir
que workloads sejam iniciados.

## Limites

DaemonSet não é uma forma de replicar uma API para receber tráfego arbitrário.
Se o serviço precisa de uma quantidade independente de réplicas e de
scheduling por capacidade, Deployment é a abstração apropriada. Se cada
instância possui identidade e volume próprios, StatefulSet pode ser mais
adequado.

## Relações

- [Taints e tolerations](../scheduling/taints-tolerations.md) controlam
  elegibilidade.
- [Node affinity](../scheduling/affinity.md) refina a seleção.
- [Pod](pod.md) é a unidade criada pelo DaemonSet.

## Fonte primária

- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
