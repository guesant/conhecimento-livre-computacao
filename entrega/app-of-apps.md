# App of apps

App of apps usa uma Application raiz para entregar manifestos que declaram
outras Applications. A raiz se torna o ponto de entrada da topologia de
entrega.

## Composição

A raiz deve ter escopo pequeno, dependências claras e permissões compatíveis
com os recursos filhos. As Applications filhas precisam de AppProjects e
destinos que evitem que um arquivo adicionado por engano alcance todo o
cluster.

A remoção de um manifesto filho pode ativar prune. A política precisa definir
se a raiz pode remover a Application e os recursos que ela administra.

## Relações

- [Application](application.md) é a unidade filha.
- [AppProject](appproject.md) define a fronteira.
- [Sync, prune e self-heal](sync-prune-self-heal.md) controla convergência.

## Fonte primária

- [Argo CD app of apps](https://argo-cd.readthedocs.io/en/stable/user-guide/cluster-bootstrapping/)
