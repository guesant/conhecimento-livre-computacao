# Resource

Um resource é uma declaração de um objeto que a ferramenta deve administrar.
Ele possui tipo, nome lógico, argumentos, dependências e atributos calculados.

## Lifecycle

A ferramenta cria, lê, atualiza e destrói o objeto por meio do provider. Uma
mudança em atributo pode ser atualizada no lugar ou exigir substituição. O
plano deve mostrar essa diferença antes do apply.

Dependências explícitas são necessárias quando a relação não é inferida por
referência. Evite dependências artificiais que serializam todo o grafo.

## Segurança

Recursos podem colocar valores sensíveis no state. Marcar um atributo como
sensitive reduz exposição na saída, mas não elimina a necessidade de proteger
o backend do state.

## Relações

- [Provider](provider.md) implementa operações contra a API.
- [Data source](data-source.md) consulta dados existentes.
- [State](state.md) registra a identidade do resource.

## Fonte primária

- [OpenTofu resources](https://opentofu.org/docs/language/resources/)
