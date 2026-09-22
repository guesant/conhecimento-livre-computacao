# OCI Image Specification

OCI Image Specification define a representação de uma imagem: configuração, manifestos, índices e camadas de filesystem identificadas por conteúdo.

## Fronteira

A especificação descreve o artefato resultante. Ela não define Dockerfile, como o build é executado, como o artefato é transferido por HTTP ou como um processo é iniciado.

## Multi-plataforma

Um image index pode referenciar manifestos diferentes para plataformas distintas. Isso permite que uma referência represente variantes para arquiteturas como amd64 e arm64.

## Continue por aqui

[OCI Distribution Specification](distribution-spec.md) trata transporte e registry. [OCI Runtime Specification](runtime-spec.md) trata execução.