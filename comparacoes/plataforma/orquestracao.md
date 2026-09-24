# Compose, Swarm e Kubernetes

As três opções coordenam containers, mas operam em escopos e modelos diferentes.

## Compose

Compose descreve aplicações multi-container, normalmente dentro de um host. Seu valor é simplicidade, ecossistema Docker e um formato conhecido por muitos projetos upstream.

Escolha-o quando um host é suficiente e não há necessidade de uma API de cluster extensível.

## Swarm

Swarm adiciona scheduling multi-host, serviços, overlay networking e consenso entre managers mantendo um modelo próximo ao Docker.

É uma alternativa quando multi-host é requisito, a equipe quer uma superfície menor e não depende do ecossistema Kubernetes.

## Kubernetes

Kubernetes fornece uma API extensível, reconciliação por controllers, scheduler, primitives de rede/storage/policy e ecossistema amplo.

Seu custo operacional é maior e cresce com as extensões adotadas.

## Dimensões

| Dimensão | Compose | Swarm | Kubernetes |
| --- | --- | --- | --- |
| escopo natural | host | cluster | plataforma/cluster |
| scheduler multi-host | não | sim | sim |
| API extensível por CRDs | não | não | sim |
| operators | não | não | sim |
| curva conceitual | menor | intermediária | maior |
| ecossistema cloud-native | limitado | limitado | amplo |

## Cenários

Para um host com cinco serviços, Compose pode resolver tudo que importa. Para três hosts e requisitos simples, Swarm pode ser suficiente. Para uma plataforma que precisa de operators, policies, GitOps e integração padronizada, Kubernetes compra capacidades que as opções menores não fornecem.

Nenhuma linha da tabela prova uma escolha isoladamente.

## Continue por aqui

[Single-node](../../cenarios/execucao/single-node.md) aplica os critérios a um cenário. [Quando Kubernetes faz sentido](../../cenarios/execucao/quando-kubernetes.md) detalha o custo-benefício da plataforma.
