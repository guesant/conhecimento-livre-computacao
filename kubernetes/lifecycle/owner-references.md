# Owner references

Owner reference relaciona um objeto dependente ao objeto que controla seu
lifecycle. Controllers usam essa metadata para descobrir ownership e o garbage
collector pode remover dependentes quando o proprietário desaparece, conforme
as regras de propagação escolhidas.

## Ownership e controle

Ser apontado como owner não significa que um objeto terá seu conteúdo
reconciliado automaticamente. O controller precisa observar e agir. Também é
possível que um recurso tenha um owner lógico diferente do controller que o
criou, por isso a leitura das referências precisa ser combinada com labels,
annotations e comportamento do operator.

Cross-namespace owner references não são permitidas como uma forma geral de
ownership namespaced. Recursos cluster-scoped e namespaced possuem regras
próprias. Uma referência inválida pode impedir garbage collection ou gerar uma
falsa impressão de dependência.

## Garbage collection

Exclusão em cascata pode ser foreground, background ou orphan, conforme o
pedido. A escolha influencia disponibilidade e ordem de limpeza. Antes de
excluir um owner, confirme que os dependentes podem ser removidos e que dados
persistentes possuem outra proteção.

## Relações

- [Controller](../control-plane/controller.md) cria e observa dependentes.
- [Finalizer](finalizers.md) executa limpeza que o garbage collector não
  consegue inferir.
- [ReplicaSet](../core/replicaset.md) mantém ownership dos Pods.

## Fonte primária

- [Garbage Collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/)
