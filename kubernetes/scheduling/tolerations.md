# Tolerations

Uma toleration é uma permissão declarada pelo Pod para permanecer ou ser
agendado em um nó que possui um taint. Ela não força o scheduler a escolher o
nó e não substitui affinity.

A correspondência considera chave, operador, valor e efeito. `Exists` pode
aceitar qualquer valor para uma chave; uma toleration sem chave pode ser ampla
demais e deve ser tratada como uma decisão de segurança. O efeito `NoExecute`
também pode ser tolerado por tempo limitado.

Tolerations são comuns em DaemonSets que precisam executar em nós reservados ou
em agentes de infraestrutura. A toleration deve ser tão específica quanto o
workload permite, para não remover a proteção que o taint deveria oferecer.

## Relações

- [Taints](taints.md) define a marca aplicada ao nó.
- [DaemonSet](../core/daemonset.md) é um consumidor frequente de tolerations.
- [Affinity](affinity.md) seleciona ou separa nós por labels.

## Fonte primária

- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
