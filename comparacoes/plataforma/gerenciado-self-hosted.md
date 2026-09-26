# Kubernetes gerenciado e self-hosted

Kubernetes gerenciado e self-hosted expõem a mesma API, mas distribuem de
forma diferente as responsabilidades do control plane.

## Kubernetes gerenciado

Em Amazon EKS, Google GKE, Azure AKS e serviços equivalentes, o provedor opera
API server, etcd e controllers, além de patches e parte da alta disponibilidade.
O consumidor continua responsável pelos workloads, por políticas de acesso,
rede dentro do ambiente e, dependendo do serviço, pelos worker nodes.

Essa opção reduz o trabalho operacional e pode oferecer SLA, integração com os
serviços do provedor e alta disponibilidade entre zonas. O custo é a taxa do
control plane, dependência das APIs do provedor e menor controle sobre o
datastore e a topologia interna.

## Kubernetes self-hosted

Em K3s, RKE2 ou uma instalação própria, a equipe opera máquinas, control
plane, datastore, atualizações, certificados e recuperação. Isso permite
portabilidade, controle do custo e escolha detalhada de rede e storage, mas
transforma falhas do control plane, backups e upgrades em responsabilidades
diretas da equipe.

## Critério de escolha

Gerenciado tende a ser melhor quando o ambiente já está no provedor, existe
necessidade de SLA ou não há capacidade operacional para manter o control
plane. Self-hosted tende a ser melhor em on-premises, edge, laboratório ou
cenários que exigem portabilidade e controle do ciclo de vida.

## Relações

- [Distribuições Kubernetes](distribuicoes-kubernetes.md) compara opções de
  plataforma.
- [K3s](../../k3s.md) explica uma implementação self-hosted compacta.
- [HA multizona](../../kubernetes/arquitetura/ha-multizona.md) trata o
  problema de disponibilidade além de um cluster multinó simples.
