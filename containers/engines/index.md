# Container engines

Um container engine oferece uma interface administrativa para construir ou consumir imagens, criar containers, redes e volumes e acompanhar seu ciclo de vida.

## Implementações

[Docker Engine](docker-engine.md) usa um daemon central e containerd. [Podman](podman.md) possui arquitetura daemonless para a operação local e integra o ecossistema containers/image, containers/storage e runtimes OCI.

## Escolha

A decisão envolve compatibilidade de ecossistema, modelo de privilégio, daemon, APIs necessárias, integração systemd e ferramentas existentes. Para cenários, veja [single-node](../../cenarios/execucao/single-node.md).
