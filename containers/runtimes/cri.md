# Container Runtime Interface

Container Runtime Interface, CRI, é a API usada pelo kubelet para solicitar operações de runtime sem acoplar Kubernetes a uma implementação específica.

## Efeito arquitetural

O kubelet conversa com implementações CRI como containerd ou CRI-O. Essa fronteira explica por que Docker Engine não é requisito para executar Pods.

## Continue por aqui

[containerd](containerd.md) e [CRI-O](cri-o.md) implementam essa responsabilidade.