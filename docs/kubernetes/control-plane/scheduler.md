# Kubernetes scheduler

O scheduler escolhe um nó para Pods que ainda não possuem binding. Ele observa
Pods pendentes, elimina nós incompatíveis com as restrições declaradas e
seleciona uma colocação conforme recursos, afinidade, topology spread, taints e
outras prioridades.

## Filter e score

A decisão tem duas ideias diferentes. Filtros removem nós que não podem
executar o Pod, por exemplo por falta de requests disponíveis, volume
incompatível ou taint sem toleration. Scoring ordena os candidatos restantes
segundo preferências como distribuição, afinidade e balanceamento.

O scheduler não inicia o container e não verifica se a aplicação está pronta.
Depois do binding, o kubelet do nó cria o Pod e reporta seu estado. Um Pod
agendado pode continuar pendente por imagem, volume, CNI ou erro do runtime.

## Diagnóstico

Um Pod pendente deve ser analisado pelos eventos e pelas condições, não apenas
por uma tentativa de alterar o nó manualmente. Requests exagerados, taints,
affinity obrigatória, topology constraints e falta de capacidade são causas
diferentes e exigem correções diferentes.

## Relações

- [Requests](../recursos/requests.md) informam a capacidade exigida.
- [Taints e tolerations](../scheduling/taints-tolerations.md) controlam
  elegibilidade.
- [Affinity](../scheduling/affinity.md) e [topology spread](../scheduling/topology-spread.md)
  expressam preferências e distribuição.

## Fonte primária

- [Kubernetes scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
