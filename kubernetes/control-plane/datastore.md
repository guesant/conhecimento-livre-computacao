# Datastore do K3s

O K3s precisa persistir o estado da API Kubernetes em um datastore consistente.
A escolha do backend define o modelo de quorum, a operação de backup e o
domínio de falha do control plane.

## Etcd embarcado

O etcd roda nos servidores K3s e usa consenso para replicar o estado. É a
opção integrada, sem outro serviço para operar, mas exige número ímpar de
servidores para tolerar falhas e exige snapshots próprios.

## Datastore externo

Um backend externo torna os servidores K3s mais simples e transfere quorum,
replicação e recuperação para o banco ou serviço escolhido. Isso pode ser
adequado quando já existe uma plataforma de dados operada separadamente, mas
cria uma dependência crítica: a perda do datastore externo afeta todos os
servidores K3s mesmo que eles estejam saudáveis.

## Kine

Kine traduz a interface esperada pelo K3s em operações SQL. Ele permite usar
PostgreSQL, MySQL ou SQLite como backend sem expor essa diferença ao API server,
mas acrescenta uma camada de tradução e não possui o mesmo modelo de desempenho
de um etcd operado diretamente.

## Critério de escolha

Etcd embarcado é a escolha simples para um cluster que pode operar sua própria
maioria. Backend externo faz sentido quando a organização já possui um serviço
de dados com backup, HA e observabilidade maduros. Kine atende ambientes em que
a integração com SQL é mais importante que o desempenho específico do etcd.

## Relações

- [Quorum](quorum.md) explica a maioria exigida pelo backend escolhido.
- [etcd](etcd.md) explica a implementação distribuída mais comum.
- [Topologias K3s multinó](../../topologias-rede-e-falhas-em-k3s-multino.md)
  relaciona datastore, servidores e agentes.
