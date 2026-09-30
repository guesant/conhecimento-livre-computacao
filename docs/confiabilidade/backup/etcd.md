# Backup do etcd

O etcd guarda o estado da API Kubernetes: objetos, configurações, Secrets e
metadados dos recursos. Um snapshot do datastore protege esse estado declarado,
mas não contém volumes persistentes, arquivos fora do cluster ou imagens de
container. Restaurar o snapshot recria os objetos, não os dados que eles
referenciam.

Um snapshot mantido apenas no mesmo host não é uma proteção contra a perda do
host. A cópia precisa sair do domínio de falha original. Em K3s, o snapshot e o
token do servidor são materiais diferentes: o primeiro recupera o datastore; o
segundo permite que novos servidores sejam reintegrados ao cluster restaurado.

## Restauração

Restaurar um snapshot substitui o estado atual pelo estado congelado no ponto
do snapshot. É uma operação destrutiva e deve ser testada fora do ambiente
ativo. Em um cluster com vários managers, um único nó se torna a fonte
restaurada e os demais precisam ser reintegrados como membros novos. Em um
cluster de nó único, a operação é mais simples, mas continua destrutiva.

## Relações

- [Backup](backup.md) apresenta o vocabulário geral.
- [Snapshot](snapshot.md) diferencia cópia pontual, réplica e backup.
- [Datastore do K3s](../../kubernetes/control-plane/datastore.md) explica o
  papel do etcd na topologia usada pelo projeto.

## Fonte primária

- [K3s server snapshots](https://docs.k3s.io/cli/etcd-snapshot)
- [etcd disaster recovery](https://etcd.io/docs/latest/op-guide/recovery/)
