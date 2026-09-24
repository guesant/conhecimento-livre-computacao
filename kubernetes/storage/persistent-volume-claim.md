# PersistentVolumeClaim

PersistentVolumeClaim, PVC, é a solicitação de armazenamento feita por uma
aplicação. Ele descreve capacidade, modos de acesso, classe e às vezes um
selector, sem precisar conhecer o identificador físico do volume.

## Binding e montagem

O control plane procura ou provisiona um PV compatível e associa o claim a ele.
Um Pod referencia o PVC e o kubelet coordena attach e mount por meio do driver
de storage. `Bound` indica associação, não que o filesystem esteja montado e
pronto dentro do container.

## Modos e lifecycle

`ReadWriteOnce`, `ReadOnlyMany`, `ReadWriteMany` e `ReadWriteOncePod` possuem
semânticas diferentes e não são suportados por todos os backends. Escolher
RWX apenas por conveniência pode introduzir custo e complexidade desnecessários.

A exclusão de um PVC pode acionar a reclaim policy do PV. O operator deve
confirmar dados, backup e dependências antes de remover um claim de produção.

## Relações

- [PersistentVolume](persistent-volume.md) representa a capacidade vinculada.
- [StorageClass](storage-class.md) seleciona provisionamento.
- [StatefulSet](../core/statefulset.md) pode criar claims por réplica.

## Fonte primária

- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
