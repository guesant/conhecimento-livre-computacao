# Argo CD Application

Application é o objeto que conecta uma fonte de configuração a um destino. Ele
declara repositório, revisão, caminho ou chart, cluster, Namespace e política
de sincronização.

## Responsabilidade

A Application representa uma unidade de entrega observável. Seu status expõe
revisão observada, recursos gerenciados, condições de sync e saúde. Ela não é
um Deployment nem o workload executado: é a intenção de que um conjunto
renderizado seja aplicado a um destino.

## Segurança

AppProject limita repositórios, destinos e tipos de recursos permitidos. Uma
Application sem fronteira de projeto pode ampliar o raio de dano de um
manifesto comprometido.

## Relações

- [AppProject](appproject.md) define fronteiras de permissão.
- [ApplicationSet](applicationset.md) gera Applications.
- [App of apps](app-of-apps.md) usa uma Application raiz.

## Fonte primária

- [Argo CD Application specification](https://argo-cd.readthedocs.io/en/stable/user-guide/application-specification/)
