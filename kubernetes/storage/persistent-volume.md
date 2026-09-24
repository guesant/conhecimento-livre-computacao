# PersistentVolume

PersistentVolume, PV, representa uma capacidade de armazenamento disponível ao
cluster. Ele pode ser criado estaticamente ou provisionado por um driver CSI e
possui lifecycle independente de um Pod.

## Binding

Um PersistentVolumeClaim solicita capacidade, modos de acesso e, opcionalmente,
uma StorageClass. O control plane vincula o PVC a um PV compatível. Esse
binding não é apenas um ponteiro textual: o volume precisa atender capacidade,
classe, selector e modos solicitados.

## Reclaim policy

`Delete` pode remover o backend quando o claim é excluído, conforme o
provisioner. `Retain` preserva o volume e exige recuperação ou limpeza manual.
Para dados importantes, a política deve ser avaliada junto com backup,
restauração e risco de exclusão acidental.

## Limites

PV não é backup, réplica de banco ou garantia de disponibilidade. Ele apenas
representa um volume que pode ser montado. O backend pode falhar, corromper
dados ou ficar indisponível mesmo quando o objeto PV está `Bound`.

## Relações

- [PersistentVolumeClaim](persistent-volume-claim.md) é a solicitação da
  aplicação.
- [StorageClass](storage-class.md) define provisionamento.
- [CSI](csi.md) implementa operações do backend.

## Fonte primária

- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
