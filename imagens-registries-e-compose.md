# Mapa de compatibilidade: distribuição de containers

Esta página preserva a URL histórica do primeiro mapa do domínio. O conteúdo
foi separado porque imagem, camada, digest, registry e Compose possuem modelos
e fontes próprios. Ela agora funciona como um mapa de compatibilidade e não
como a página canônica de todos esses conceitos.

## Artefatos e identidade

- [Imagem de container](containers/image.md) apresenta o modelo completo.
- [Camada de filesystem](containers/layer.md) explica changesets e `DiffID`.
- [Manifesto](containers/manifest.md) descreve uma variante de plataforma.
- [Image index](containers/image-index.md) relaciona variantes de plataforma.
- [Tag](containers/tag.md) explica referências mutáveis.
- [Digest](containers/digest.md) explica identidade content-addressable.
- [Build context](containers/build-context.md) delimita as entradas do build.

## Distribuição e composição

- [Registry OCI](containers/distribuicao/registry.md) documenta o serviço de
  distribuição.
- [Repositório de artefatos](containers/distribuicao/artifact-repository.md)
  compara registry dedicado e gerenciador universal.
- [Compose Specification](containers/compose/specification.md) define o
  contrato de composição.
- [Docker Compose](containers/compose/docker-compose.md) descreve a
  implementação do Docker.
- [Podman Compose](containers/compose/podman-compose.md) explica o wrapper e
  o provedor externo.
- [Skopeo](containers/distribuicao/skopeo.md) trata cópia e inspeção de
  artefatos.

## Relação com este projeto

O [rollout de imagens](../arquitetura/rollout-de-imagens.md) documenta a
decisão específica deste repositório sobre tags, digests, Kargo e Argo CD. A
página pertence a Arquitetura porque explica a implementação local, enquanto
as páginas acima permanecem reutilizáveis fora deste cluster.
