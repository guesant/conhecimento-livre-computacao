# Armazenamento local e distribuído

Armazenamento local vincula os dados ao disco de um nó. Ele costuma ter baixa
latência, mas exige que o scheduler respeite o nó e que backup externo cubra a
perda do host.

Armazenamento distribuído replica blocos entre nós ou oferece um serviço
externo acessível por rede. Ele pode permitir reagendamento e tolerar a perda
de um componente, mas introduz latência, dependências de rede, capacidade
reservada e uma camada operacional adicional.

## Nó único

Num cluster de nó único, réplica distribuída não cria um segundo failure
domain. Ela pode proteger contra perda de disco se houver outro dispositivo,
mas a perda do host continua afetando workload e armazenamento.

## Banco de dados

Replicação de storage protege uma camada diferente da replicação do banco.
Uma escrita destrutiva ou corrupção lógica pode ser replicada para todas as
réplicas. Backup e teste de restauração continuam necessários.

## Relações

- [Longhorn](longhorn.md) é uma implementação distribuída para Kubernetes.
- [PersistentVolume](persistent-volume.md) abstrai o backend.
- [Backup](../../confiabilidade/backup/backup.md) cria ponto de recuperação.

## Fonte primária

- [Kubernetes storage](https://kubernetes.io/docs/concepts/storage/)
