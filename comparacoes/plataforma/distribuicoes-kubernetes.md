# K3s, MicroK8s e Kubernetes gerenciado

A API Kubernetes pode ser consumida por distribuições e modelos operacionais diferentes. A primeira decisão é quanto da plataforma a equipe quer operar diretamente.

## K3s

K3s empacota componentes e defaults para reduzir footprint e instalação. É comum em edge, laboratório, pequenos clusters e ambientes self-managed.

## MicroK8s

MicroK8s empacota Kubernetes com foco em instalação compacta e addons habilitáveis, especialmente integrado ao ecossistema Ubuntu/Canonical.

## Gerenciado

EKS, GKE, AKS e ofertas semelhantes transferem parte relevante da operação do control plane ao provedor. Isso reduz algumas responsabilidades, mas não remove operação de workloads, policies, rede, custos, upgrades de componentes do usuário e desenho de disponibilidade.

## Critérios

Hardware restrito e operação local favorecem distribuições leves. Integração profunda com cloud e redução da responsabilidade pelo control plane favorecem gerenciado. Necessidade de controlar todos os componentes favorece self-managed, ao custo de possuir os failure modes.

## Má comparação

Comparar apenas consumo de RAM ignora upgrade, datastore, suporte, integração, lifecycle e conhecimento da equipe.

## Continue por aqui

[K3s](../../k3s.md) aprofunda uma implementação. [Kubernetes gerenciado e HA](../../kubernetes-gerenciado-e-ha-avancada.md) trata topologias mais amplas.