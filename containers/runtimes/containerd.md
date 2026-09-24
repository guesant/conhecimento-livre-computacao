# containerd

containerd é um high-level container runtime que administra imagens, snapshots e ciclo de vida, delegando a execução de baixo nível a runtimes OCI.

Ele pode atender Kubernetes por [CRI](cri.md). Docker Engine usa containerd internamente, mas Kubernetes não precisa de Docker Engine para usar containerd.

## Fronteira

containerd não é um registry, um scheduler nem um engine completo de desenvolvimento. Ele gerencia operações de runtime, como resolução e armazenamento de imagens, criação de snapshots e execução de tarefas, enquanto plugins e runtimes complementares implementam partes específicas do fluxo.

No Kubernetes, o kubelet conversa com a interface CRI e o runtime configura o sandbox, o filesystem e o processo do container. A execução de baixo nível normalmente é delegada a um runtime compatível com a [OCI Runtime Specification](../oci/runtime-spec.md), como o runc.

## Relações

- [CRI](cri.md) define a interface Kubernetes para o runtime.
- [runc](runc.md) executa o bundle de baixo nível.
- [Imagem de container](../image.md), [camada](../layer.md) e snapshots explicam os artefatos que o runtime manipula.
- [Docker Engine](../engines/docker-engine.md) é uma camada superior que pode usar containerd.

## Fonte primária

- [containerd documentation](https://github.com/containerd/containerd/tree/main/docs)
