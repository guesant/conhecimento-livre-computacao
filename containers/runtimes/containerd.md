# containerd

containerd é um high-level container runtime que administra imagens, snapshots e ciclo de vida, delegando execução de baixo nível a runtimes OCI.

Pode atender Kubernetes por [CRI](cri.md). Docker Engine usa containerd internamente, mas Kubernetes não precisa de Docker Engine para usar containerd.