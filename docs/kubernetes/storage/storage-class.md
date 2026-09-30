# StorageClass

StorageClass descreve uma classe de provisionamento dinâmico. Ela identifica o
provisioner, parâmetros do backend, política de reclaim, binding e expansão,
conforme as capacidades do driver.

## Provisionamento

Quando um PVC referencia uma StorageClass, o provisioner pode criar um PV sob
demanda. Uma classe padrão pode ser usada quando o claim não declara outra,
mas depender implicitamente da classe padrão torna o manifesto menos explícito
e pode causar mudanças de backend quando a configuração do cluster muda.

`volumeBindingMode` pode adiar o provisionamento até o scheduler conhecer o
nó que executará o Pod. Isso é importante para storage local ou topologias em
que o volume só existe em determinados nós.

## Trade-offs

Parâmetros como réplica, tipo de disco, filesystem e localização afetam
desempenho, custo e disponibilidade. Uma StorageClass que oferece mais cópias
não substitui backup lógico nem teste de restore. A escolha deve considerar o
failure domain que o backend consegue realmente suportar.

## Relações

- [PersistentVolumeClaim](persistent-volume-claim.md) solicita a classe.
- [CSI](csi.md) fornece o provisioner.
- [Armazenamento local, distribuído e Longhorn](../../armazenamento-local-distribuido-e-longhorn.md)
  compara backends do cenário.

## Fonte primária

- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
