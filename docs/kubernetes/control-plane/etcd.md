# etcd

etcd é um datastore distribuído consistente usado pelo Kubernetes para
persistir o estado do control plane. Recursos da API, leases e metadata de
controllers dependem da disponibilidade e da integridade dessa camada.

## Consistência e quorum

etcd usa um protocolo de consenso para escolher um líder e replicar entradas.
Uma maioria de membros precisa estar disponível para confirmar escritas. Um
cluster de três membros tolera uma falha; aumentar a quantidade de membros não
melhora disponibilidade indefinidamente, porque aumenta tráfego e custo de
coordenação.

Quorum é diferente de número de Pods saudáveis. Um API server vivo pode falhar
ao ler ou persistir objetos se o etcd não tiver quorum. Da mesma forma, uma
réplica de dados que não participa do consenso não substitui um membro saudável.

## Backup e recuperação

Snapshot do etcd precisa ser consistente e restaurável na versão e topologia
pretendidas. Backup de um arquivo sem preservar metadata, encryption keys e
procedimento de restore não é uma recuperação completa. Em K3s single-node, a
escolha do datastore muda o procedimento, mas não elimina a necessidade de
backup testado.

## Relações

- [Quorum](quorum.md) trata a maioria e a tolerância a falhas.
- [Datastore do K3s](datastore.md) trata a escolha de backend e topologia.
- [Backup do etcd](../../backup-do-etcd-cnpg-e-chave-age.md) trata o
  procedimento do ambiente.
- [API server](api-server.md) é o consumidor principal.

## Fontes primárias

- [Kubernetes etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
- [etcd documentation](https://etcd.io/docs/)
