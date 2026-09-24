# Reclaim policy

Reclaim policy define o que acontece com um PersistentVolume depois que o PVC
associado deixa de existir. Ela é uma decisão de retenção e risco de dados.

## Políticas

`Delete` remove o volume provisionado quando a reclamação é excluída.
`Retain` preserva o PV e exige intervenção para revisar, limpar ou reutilizar
o volume. `Recycle` é legado e não deve ser tratado como estratégia moderna
de retenção.

Delete simplifica limpeza, mas transforma uma exclusão de PVC em possível perda
de dados. Retain reduz esse risco, mas cria volumes Released que precisam de
inventário e procedimento de recuperação.

## Diagnóstico

Antes de excluir PVC, confirme backup, owner, StorageClass, policy e impacto do
workload. Depois, verifique o estado do PV e os eventos do controller. Não
confunda réplica com backup.

## Relações

- [PersistentVolume](persistent-volume.md) representa o volume.
- [PersistentVolumeClaim](persistent-volume-claim.md) solicita a capacidade.
- [Armazenamento local e distribuído](local-distributed.md) discute failure
  domains.

## Fonte primária

- [Kubernetes reclaim policy](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reclaim-policy)
