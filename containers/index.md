# Containers

Containers não são uma tecnologia única. O ecossistema combina artefatos
distribuíveis, isolamento do sistema operacional, runtimes, engines, redes,
volumes e modelos de composição. Cada camada possui contrato, failure modes e
trade-offs próprios.

## Artefato

Uma [imagem de container](image.md) é o artefato que combina configuração e
camadas. O [manifesto](manifest.md), o [image index](image-index.md), o
[descriptor](oci/descriptor.md), a [tag](tag.md) e o [digest](digest.md)
possuem papéis diferentes na identidade e na seleção do conteúdo.

[OCI](oci/index.md) padroniza o formato de imagem, a distribuição e o runtime
em especificações independentes. [Dockerfile](build/dockerfile.md), BuildKit e
Buildah descrevem ou executam o build, mas não substituem a especificação do
artefato.

## Execução

Um [engine](engines/index.md) administra imagens, containers, redes e volumes.
Um [high-level runtime](runtimes/high-level-runtime.md) gerencia o ciclo de
vida do container e um [low-level runtime](runtimes/low-level-runtime.md)
executa o bundle segundo a OCI Runtime Specification. [CRI](runtimes/cri.md)
é a interface usada por um kubelet para conversar com runtimes de containers,
não um engine local.

## Distribuição e composição

Um [registry OCI](distribuicao/registry.md) distribui manifestos e blobs. Um
[repositório de artefatos](distribuicao/artifact-repository.md) pode juntar
essa função com outros formatos de pacote. [Skopeo](distribuicao/skopeo.md)
opera sobre imagens sem precisar executá-las.

[Compose Specification](compose/specification.md) descreve uma aplicação local
composta por serviços. [Docker Compose](compose/docker-compose.md) e [Podman
Compose](compose/podman-compose.md) são implementações diferentes do modelo.

## Escolha de cenário

Para um host único, compare processo nativo, Compose, Podman com Quadlet e
Kubernetes conforme o número de serviços, a necessidade de reconciliação, o
estado persistente e o custo operacional. [Single-node](../cenarios/execucao/single-node.md)
trata essa escolha como cenário, não como preferência universal.
