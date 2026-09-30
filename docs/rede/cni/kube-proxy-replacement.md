# Kube-proxy replacement

Kube-proxy replacement é um modo em que outra implementação assume funções de dataplane normalmente associadas ao kube-proxy para Services Kubernetes.

Cilium pode operar dessa forma usando eBPF.

## Por que importa

Não é apenas uma otimização local. A decisão muda quem implementa encaminhamento e load balancing de Services, portanto altera uma responsabilidade central da rede do cluster.

## Boa prática

Trate a mudança como arquitetura de dataplane: valide compatibilidade, modos suportados, observabilidade e rollback.

## Continue por aqui

[Cilium](cilium.md) é uma implementação capaz de operar nesse modo.
