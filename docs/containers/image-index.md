# Image index

Um image index é um manifesto que aponta para outros manifestos, normalmente um por combinação de sistema operacional e arquitetura. Ele permite publicar uma única referência lógica para uma imagem que possui variantes como `linux/amd64`, `linux/arm64` ou diferentes variantes de CPU.

## Seleção de plataforma

Cada entrada do índice contém um descriptor e metadata de plataforma. O cliente compara essa metadata com a plataforma que está executando e resolve o manifesto correspondente. A imagem não é uma camada universal que roda igualmente em qualquer lugar; a referência universal é um índice que seleciona um artefato específico.

Se nenhuma entrada compatível existir, o pull falha mesmo que o registry possua outras variantes. Se a seleção for ambígua, o comportamento depende do cliente e da metadata publicada, por isso os publishers devem declarar plataformas com precisão.

## Identidade

O digest do índice identifica a composição das referências e da metadata do próprio índice. O digest do manifesto selecionado identifica a variante concreta. Fixar o digest do índice preserva a seleção publicada, mas uma policy que precisa garantir uma plataforma específica pode fixar o digest do manifesto daquela plataforma.

## Build e publicação

Builders podem produzir uma imagem para uma plataforma ou várias variantes em uma operação. A publicação precisa enviar os manifestos individuais e depois o índice que os relaciona. Copiar apenas uma variante não equivale a copiar o índice completo.

## Falhas comuns

Uma imagem que funciona em amd64 pode falhar em arm64 por causa de um binário nativo, de uma dependência sem variante ou de uma instrução de build executada na arquitetura errada. Em pipelines multi-plataforma, a arquitetura do builder, a emulação e a disponibilidade de artefatos nativos precisam ser tratadas como parte do build, não como detalhe do pull.

## Relações

- [Manifesto](manifest.md) descreve cada variante concreta.
- [Descriptor OCI](oci/descriptor.md) referencia os manifestos dentro do índice.
- [Digest](digest.md) explica as identidades do índice e da variante.
- [OCI Image Specification](oci/image-spec.md) define o formato.

## Fonte primária

- [OCI Image Index Specification](https://github.com/opencontainers/image-spec/blob/main/image-index.md)
