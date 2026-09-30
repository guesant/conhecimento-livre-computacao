# Finalizer

Finalizer é uma chave de metadata que impede a remoção completa de um objeto
até que um controller execute uma etapa de limpeza. Quando um objeto é
deletado, o API server registra `deletionTimestamp`; o controller observa esse
estado, remove dependências externas e só então remove seu finalizer.

## Por que existe

Recursos Kubernetes podem representar coisas fora do API server, como DNS,
discos, buckets ou objetos de um provedor. Excluir o objeto sem limpar o
recurso externo criaria vazamento ou conflito. Finalizer mantém o objeto visível
para que o controller tenha oportunidade de completar essa responsabilidade.

## Falha e intervenção

Se o controller desaparece, perde credencial ou não consegue alcançar o
backend, o objeto permanece `Terminating`. Remover o finalizer manualmente pode
liberar a exclusão, mas também pode deixar recursos externos órfãos. A ação é
segura apenas quando a limpeza foi confirmada ou quando preservar o recurso é
intencional.

## Relações

- [Controller](../control-plane/controller.md) implementa a limpeza.
- [Owner references](owner-references.md) tratam outra relação de lifecycle.
- [Namespace](../core/namespace.md) pode ficar preso por finalizers de objetos
  internos.

## Fonte primária

- [Finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/)
