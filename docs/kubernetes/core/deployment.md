# Deployment

Deployment declara o estado desejado de um workload stateless e coordena a
criação de ReplicaSets e Pods para alcançá-lo. Ele acrescenta rollout,
rollback, pausa e histórico de revisão ao mecanismo básico de replicação.

## Rollout

Uma alteração no Pod template cria uma nova revisão. Conforme a estratégia
configurada, o Deployment cria Pods da nova revisão e remove Pods antigos,
respeitando limites de disponibilidade e de sobreposição. `RollingUpdate`
permite transição gradual; `Recreate` encerra a revisão anterior antes de
criar a nova.

Readiness não é apenas uma indicação visual. O Deployment usa a condição dos
Pods para decidir quando uma revisão está disponível, enquanto o Service usa
Endpoints ou EndpointSlices para decidir se um Pod recebe tráfego. Uma probe
mal definida pode fazer o rollout travar ou enviar tráfego cedo demais.

## Rollback e histórico

O histórico é formado pelos ReplicaSets que representam revisões do template.
Rollback escolhe uma revisão anterior, mas não desfaz efeitos externos como
migrações de banco ou dados escritos por uma versão nova. Compatibilidade de
schema e ordem de mudança continuam sendo responsabilidades da aplicação.

## Quando não usar

Deployment não fornece identidade ordinal, armazenamento exclusivo por réplica
ou bootstrap ordenado. Para essas propriedades, considere [StatefulSet](statefulset.md).
Para um Pod por nó, considere [DaemonSet](daemonset.md).

## Relações

- [Service](service.md) fornece endereço estável para os Pods.
- [PodDisruptionBudget](../recursos/pdb.md) limita disrupções voluntárias.
- [Graceful shutdown](../recursos/graceful-shutdown.md) trata encerramento.

## Fonte primária

- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
