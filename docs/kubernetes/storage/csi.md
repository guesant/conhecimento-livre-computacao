# CSI

Container Storage Interface, CSI, é um padrão para que orquestradores
conversem com plugins de storage. No Kubernetes, componentes CSI podem
provisionar volumes, anexá-los a nós, montá-los em Pods, expandi-los e
desanexá-los conforme o suporte do driver.

## Separação de responsabilidades

O controller do driver trata operações que podem ocorrer fora do nó, como
provisionamento e attach. O node plugin executa operações locais, como mount e
unmount. Sidecars conectam essas funções ao control plane, enquanto o kubelet
coordena o uso do volume pelo Pod.

CSI não define replicação, backup ou semântica transacional da aplicação. Um
driver pode oferecer snapshots ou clones, mas esses recursos não substituem
teste de restauração e consistência do banco.

## Failure modes

Um PVC pode estar Bound enquanto o attach, mount ou filesystem falha. O
diagnóstico deve separar provisionamento, binding, attach, mount, permissões,
capacidade e saúde do backend. A exclusão de um PVC também pode acionar a
reclaim policy da StorageClass e ser destrutiva.

## Relações

- [PersistentVolume](persistent-volume.md), [PersistentVolumeClaim](persistent-volume-claim.md)
  e [StorageClass](storage-class.md) formam a API Kubernetes.
- [Modelo de armazenamento](../../modelo-de-armazenamento-do-kubernetes.md)
  explica a indireção entre aplicação e backend.

## Fontes primárias

- [Container Storage Interface](https://github.com/container-storage-interface/spec)
- [Kubernetes storage](https://kubernetes.io/docs/concepts/storage/)
