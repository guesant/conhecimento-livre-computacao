# Docker Engine

Docker Engine é uma plataforma de containers centrada no daemon `dockerd`. O daemon expõe API, administra recursos e usa containerd na pilha de execução.

## Casos de uso

É adequado quando compatibilidade com o ecossistema Docker, sua API e ferramentas associadas são requisitos importantes.

## Segurança

Acesso de escrita ao socket do daemon concede poder administrativo amplo sobre containers e, em configurações comuns, sobre o host. Montar o socket em workloads exige tratar esse acesso como altamente privilegiado.

## Modos

Docker suporta execução rootful e um modo rootless com arquitetura e requisitos próprios.

## Continue por aqui

[Container engines](index.md) define a categoria. [Podman](podman.md) oferece outro modelo arquitetural.