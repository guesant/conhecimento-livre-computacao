# High-level container runtime

Um high-level runtime administra ciclo de vida de containers, imagens, snapshots e integração com consumidores como Kubernetes.

Ele delega a materialização final do processo a um [low-level runtime](low-level-runtime.md).

## Implementações

[containerd](containerd.md) e [CRI-O](cri-o.md) ocupam essa camada com escopos diferentes.