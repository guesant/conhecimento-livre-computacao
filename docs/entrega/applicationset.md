# Argo CD ApplicationSet

ApplicationSet gera várias Applications a partir de um template e de um
generator. Ele reduz cópia de manifestos quando ambientes, clusters ou
diretórios seguem uma estrutura previsível.

## Generators

Generators podem ler clusters registrados, diretórios Git, listas explícitas
ou combinações. O template deve ser validado como qualquer Application. Um
generator amplo pode criar Applications para destinos ou repositórios não
pretendidos.

## Failure modes

Mudança na estrutura do Git, cluster não registrado ou template inválido pode
gerar ausência, criação ou remoção inesperada. Observe o controller e valide o
conjunto resultante antes de habilitar prune.

## Relações

- [Application](application.md) é o objeto gerado.
- [AppProject](appproject.md) limita o destino.
- [Reconciliação](reconciliation.md) mantém o conjunto convergente.

## Fonte primária

- [ApplicationSet](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/)
