# Compose Specification

Compose Specification define um modelo declarativo para aplicações compostas
por serviços, redes, volumes, configs e secrets. A especificação descreve a
forma do projeto e as relações entre seus componentes, enquanto cada
implementação decide quais capacidades suporta e como as traduz para o engine
subjacente.

## Modelo

Um serviço pode usar uma imagem pronta ou um build context. Ele declara
ambiente, portas, mounts, dependências e políticas que a implementação pode
aplicar ao criar e iniciar o container. Redes nomeadas conectam serviços dentro
do projeto e volumes nomeados permitem separar o ciclo de vida do dado do
ciclo de vida do container.

Configs e secrets expressam material que não deve ser confundido com uma
imagem. A semântica de montagem, permissões, interpolação e armazenamento
depende do engine, do sistema operacional e do modo rootless ou rootful usado
pela implementação.

## Arquivos e combinação

Uma execução pode combinar arquivos base e sobreposições. O arquivo posterior
normalmente substitui valores escalares e combina determinados campos de lista,
mas a regra exata depende da especificação e da implementação. A composição
deve ser validada pelo mesmo provedor usado na execução, especialmente quando
usa extensões com prefixo `x-` ou campos específicos de um engine.

## O que não é

Compose não é um scheduler de cluster, não define reconciliação contínua e não
garante disponibilidade de um volume quando o host falha. Também não define a
linguagem de build da imagem, que pertence ao Dockerfile ou a outro formato
interpretado pelo builder.

É especialmente útil para uma aplicação multi-container executada como unidade
num ambiente simples. Veja [single-node](../../cenarios/execucao/single-node.md),
[Docker Compose](docker-compose.md) e [Podman Compose](podman-compose.md).

## Fonte primária

- [Compose Specification](https://github.com/compose-spec/compose-spec)
