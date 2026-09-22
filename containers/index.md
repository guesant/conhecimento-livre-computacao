# Containers

Containers combinam formatos de artefato, mecanismos do sistema operacional, runtimes, engines, redes, volumes e ferramentas de composição. Nenhuma dessas peças isoladamente define todo o ecossistema.

## Especificações

[OCI](oci/index.md) mantém especificações independentes para imagem, distribuição e runtime. [CRI](runtimes/cri.md) é a interface usada pelo kubelet para conversar com runtimes de containers.

## Execução

[Container engine](engines/index.md) é a camada orientada à administração de containers. [Docker Engine](engines/docker-engine.md) e [Podman](engines/podman.md) são implementações com arquiteturas diferentes.

[High-level runtime](runtimes/high-level-runtime.md) administra ciclo de vida e integração. [containerd](runtimes/containerd.md) e [CRI-O](runtimes/cri-o.md) são implementações. [Low-level runtime](runtimes/low-level-runtime.md) materializa o processo confinado; [runc](runtimes/runc.md) e [crun](runtimes/crun.md) são exemplos.

## Build e distribuição

[Dockerfile](build/dockerfile.md) descreve builds em uma sintaxe de facto. [BuildKit](build/buildkit.md) e [Buildah](build/buildah.md) constroem imagens. [Skopeo](distribuicao/skopeo.md) inspeciona e move artefatos. [Registry OCI](distribuicao/registry.md) armazena e distribui imagens.

## Composição

[Compose Specification](compose/specification.md) descreve aplicações multi-container. Implementações executam esse modelo sobre engines compatíveis.

## Continue por aqui

Para escolher entre execução simples e Kubernetes, use [cenários de single-node](../cenarios/execucao/single-node.md).