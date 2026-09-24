# Modos de acesso de volume

Modos de acesso descrevem como um volume pode ser montado pelos nós ou Pods.
Eles são uma capacidade do provisionador, não uma garantia de que a aplicação
coordena escrita corretamente.

## Modos

| Modo | Semântica |
| --- | --- |
| ReadWriteOnce | leitura e escrita por um nó |
| ReadOnlyMany | leitura por vários nós |
| ReadWriteMany | leitura e escrita por vários nós |
| ReadWriteOncePod | leitura e escrita por um único Pod |

O suporte varia por driver CSI. ReadWriteOnce não significa necessariamente um
único Pod; vários Pods no mesmo nó podem compartilhar o volume conforme o
driver. ReadWriteOncePod restringe essa condição.

## Escolha

Use o modo mínimo que atende ao workload. RWX pode exigir filesystem ou
backend distribuído e introduzir latência e locking adicionais. O modo não
substitui locking da aplicação, transações ou desenho de concorrência.

## Relações

- [PersistentVolumeClaim](persistent-volume-claim.md) solicita o modo.
- [CSI](csi.md) implementa a capacidade.
- [Política de reclamação](reclaim-policy.md) define o destino após exclusão.

## Fonte primária

- [Kubernetes access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)
