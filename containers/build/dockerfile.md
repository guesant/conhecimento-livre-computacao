# Dockerfile

Dockerfile é uma linguagem de instruções para construir imagens em camadas. Containerfile é um nome neutro usado por ferramentas compatíveis para o mesmo formato de instruções.

## Fronteira

Dockerfile não faz parte da OCI Image Specification. OCI define o formato do artefato; Dockerfile descreve um processo de build interpretado por builders.

## Build context

O build context define quais arquivos podem ser referenciados por instruções como COPY. Arquivos sensíveis no contexto precisam ser excluídos e nunca devem ser persistidos em layers.

## Continue por aqui

[BuildKit](buildkit.md) e [Buildah](buildah.md) são builders que podem consumir esse formato.
