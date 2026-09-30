# Manifesto de imagem

O manifesto OCI descreve uma imagem para uma plataforma específica. Ele aponta para um objeto de configuração e para as camadas que formam o filesystem, usando descriptors com media type, tamanho e digest. Um manifesto não é a lista de todas as arquiteturas disponíveis; essa função pertence ao [image index](image-index.md).

## Estrutura

Os campos centrais são:

- `schemaVersion`, que identifica a versão do schema do manifesto;
- `mediaType`, que identifica o formato do documento;
- `config`, um descriptor para a configuração da imagem;
- `layers`, a sequência ordenada de descriptors de filesystem.

O objeto de configuração contém parâmetros de execução e referências aos `DiffIDs` das camadas. O manifesto, por sua vez, relaciona os blobs necessários para obter aquele conteúdo. A configuração não substitui o manifesto e o manifesto não contém todo o conteúdo da camada.

## Pull

Um cliente começa resolvendo uma referência no registry, normalmente uma tag ou um digest. Depois de obter o manifesto, ele lê os descriptors e baixa os blobs ainda ausentes no armazenamento local. A verificação do digest acontece para cada conteúdo referenciado, não apenas para o documento inicial.

Se a referência for um image index, o cliente primeiro escolhe o manifesto compatível com a plataforma. Se a referência já for o digest de um manifesto específico, não existe essa etapa de seleção.

## Artefatos relacionados

Versões atuais do formato podem associar um manifesto a outro conteúdo por meio de `subject` e annotations. Essa relação permite distribuir metadata complementar sem alterar a imagem principal. Registry, cliente e ferramenta de policy precisam concordar sobre o suporte aos tipos e à API de referrers.

## O que o manifesto não garante

O manifesto não é uma prova de origem, não avalia vulnerabilidades e não define como o processo de build foi executado. Ele garante uma relação verificável entre a referência e os bytes descritos. Provenance e assinatura são camadas adicionais da cadeia de suprimentos.

## Relações

- [Descriptor OCI](oci/descriptor.md) define as referências usadas pelo manifesto.
- [Camada](layer.md) explica o conteúdo referenciado por `layers`.
- [Imagem de container](image.md) apresenta o modelo completo.
- [OCI Distribution Specification](oci/distribution-spec.md) define a API de distribuição.

## Fonte primária

- [OCI Image Manifest Specification](https://github.com/opencontainers/image-spec/blob/main/manifest.md)
