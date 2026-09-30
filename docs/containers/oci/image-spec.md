# OCI Image Specification

A OCI Image Specification define o formato de um artefato de imagem e a
relação entre seus documentos e blobs. Ela descreve a configuração, os
descriptors, os manifestos, os image indexes e as camadas de filesystem que um
runtime pode consumir.

## Fronteiras

A especificação define o artefato, não a linguagem de build, o transporte HTTP
ou a execução do processo. [Dockerfile](../build/dockerfile.md) e Containerfile
são formatos de instrução interpretados por builders. A distribuição é tratada
pela [OCI Distribution Specification](distribution-spec.md), e a execução do
bundle é tratada pela [OCI Runtime Specification](runtime-spec.md).

## Documentos do formato

- [Descriptor](descriptor.md) referencia conteúdo por media type, tamanho e
  digest.
- [Manifesto](../manifest.md) descreve uma imagem para uma plataforma.
- [Image index](../image-index.md) relaciona manifestos de plataformas
  diferentes.
- [Camada](../layer.md) descreve changesets do root filesystem.
- [Imagem de container](../image.md) relaciona essas unidades num modelo único.

## Identidade e portabilidade

O formato é content-addressable. Manifestos e blobs são identificados por
digests, e uma alteração no conteúdo produz uma nova identidade. Um image index
pode referenciar variantes de `linux/amd64` e `linux/arm64`, permitindo que uma
mesma referência lógica selecione o manifesto compatível com o cliente.

A portabilidade não significa que qualquer imagem roda em qualquer host. A
variante precisa existir para a plataforma e o runtime precisa suportar o
formato e as propriedades de execução publicadas.

## Fonte primária

- [OCI Image Format Specification](https://github.com/opencontainers/image-spec)
