# Descriptor OCI

Um descriptor é a referência tipada a um conteúdo armazenado por digest. Ele informa pelo menos o media type, o digest e o tamanho em bytes do conteúdo referenciado. Manifestos, índices, configurações, camadas e artefatos relacionados usam o mesmo mecanismo de referência.

## Por que existe

O descriptor separa um documento que descreve um artefato do blob que contém o artefato. Um cliente pode verificar o tamanho esperado e calcular o digest do conteúdo recebido antes de aceitá-lo. A identidade deixa de depender do nome de um arquivo ou da localização física no registry.

O media type informa como o conteúdo deve ser interpretado. Um cliente não deve tentar interpretar um blob desconhecido apenas porque consegue baixá-lo. Isso permite que a distribuição carregue tipos novos sem transformar cada registry em um parser de todos os artefatos.

## Onde aparece

Um manifesto usa descriptors para apontar para a configuração e para as camadas. Um image index usa descriptors para apontar para manifestos de plataformas diferentes. Artefatos relacionados podem usar `subject` para indicar o manifesto ao qual estão associados, como acontece com determinados tipos de assinatura, SBOM e atestação.

O descriptor não é uma tag. A tag é um nome mutável resolvido no repositório. O descriptor é uma referência content-addressable que identifica bytes específicos.

## Limites

Verificar um digest demonstra integridade do conteúdo recebido em relação à referência usada. Não demonstra que o conteúdo foi produzido por uma entidade esperada, que o build foi reprodutível ou que a imagem é segura. Essas propriedades exigem assinatura, provenance, policy e análise de vulnerabilidades complementares.

## Relações

- [Digest](../digest.md) explica a identidade content-addressable.
- [Manifesto](../manifest.md) usa descriptors para formar uma imagem.
- [Image index](../image-index.md) usa descriptors para selecionar uma plataforma.
- [OCI Distribution Specification](distribution-spec.md) define como esses conteúdos são transportados.

## Fonte primária

- [OCI Descriptor](https://github.com/opencontainers/image-spec/blob/main/descriptor.md)
