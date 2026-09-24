# Data source

Um data source consulta informação existente para que a configuração possa
referenciá-la sem administrar seu lifecycle. Ele pode ler uma rede, uma imagem,
um ID ou uma propriedade produzida por outro sistema.

## Limites

Ler um objeto não concede propriedade sobre ele. Um data source pode mudar entre
planos e introduzir não determinismo se o filtro for amplo ou a fonte não tiver
versionamento.

Use filtros estáveis e resultados únicos. Quando a configuração precisa
criar, atualizar ou destruir o objeto, resource é a abstração correta.

## Relações

- [Resource](resource.md) administra objetos.
- [Provider](provider.md) implementa a consulta.
- [Drift](drift.md) explica mudanças observadas fora do escopo.

## Fonte primária

- [OpenTofu data sources](https://opentofu.org/docs/language/data-sources/)
