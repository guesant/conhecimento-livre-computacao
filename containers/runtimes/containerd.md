# containerd

containerd é um runtime de containers de alto nível. Ele administra imagens, snapshots e ciclo de vida e delega execução de baixo nível a runtimes OCI.

## Kubernetes

containerd pode atender ao kubelet por [CRI](cri.md). K3s o empacota como runtime padrão em sua distribuição.

## Fronteira

containerd não é a mesma camada de Docker Engine. Docker usa containerd internamente, enquanto Kubernetes pode usar containerd sem Docker Engine.

## Continue por aqui

[High-level runtime](high-level-runtime.md) explica a categoria e [runc](runc.md) a camada abaixo.