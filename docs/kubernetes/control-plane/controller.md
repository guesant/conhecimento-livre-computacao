# Controller Kubernetes

Controller é um loop que observa recursos, compara estado observado com estado
desejado e executa ações para reduzir a diferença. Essa reconciliação é a
abstração comum por trás de Deployments, StatefulSets, Jobs, Services e muitos
operadores de terceiros.

## Loop de reconciliação

Um controller recebe eventos de watch, consulta o estado atual, calcula uma
ação idempotente e escreve alterações na API. Ele não deve depender de um
único evento, porque eventos podem ser perdidos ou agrupados. Uma nova
reconciliação precisa produzir o mesmo resultado quando o estado já estiver
correto.

Controllers podem criar recursos filhos e usar owner references para que o
garbage collector acompanhe o lifecycle. Finalizers permitem executar limpeza
antes da remoção, mas um finalizer que não consegue completar pode bloquear o
objeto indefinidamente.

## Operators

Um operator combina um CRD com um controller que conhece um domínio específico.
Ele não é simplesmente um script que aplica YAML: precisa tratar versões,
status, retries, concorrência, ownership, upgrades e falhas parciais.

## Relações

- [CRD](../extensibility/crd.md) adiciona tipos à API.
- [Finalizer](../lifecycle/finalizers.md) controla limpeza antes da remoção.
- [Owner reference](../lifecycle/owner-references.md) liga recursos filhos ao
  proprietário.

## Fonte primária

- [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)
