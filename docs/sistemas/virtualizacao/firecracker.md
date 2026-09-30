# Firecracker

Firecracker é um VMM voltado a microVMs. Ele usa KVM e oferece uma superfície
reduzida de dispositivos, API e configuração para executar workloads isolados
com baixo overhead operacional.

## Modelo de execução

O processo VMM cria uma máquina virtual com kernel e root filesystem definidos
pelo operador. O convidado recebe dispositivos virtio de rede e bloco e se
comunica com o host por uma API controlada. O desenho reduz componentes que
não são necessários para o workload.

A aplicação continua responsável por seu próprio lifecycle dentro do guest.
Firecracker não é um orquestrador, registry, scheduler ou substituto de
Kubernetes.

## Escolha

Firecracker faz sentido quando o isolamento de kernel é requisito e o número
de instâncias ou a duração das cargas torna importante reduzir o custo de uma
VM tradicional. Ele exige integração própria para imagens, rede, armazenamento,
logs, atualização de kernels e coleta de métricas.

## Failure modes

Falhas podem ocorrer no boot do kernel convidado, no root filesystem, na
configuração de virtio, no socket da API ou na rede configurada no host. Um
health check da aplicação não prova que o VMM e o guest estão disponíveis; os
dois níveis precisam de diagnósticos separados.

## Relações

- [MicroVM](microvm.md) apresenta o modelo.
- [Hypervisor](hypervisor.md) posiciona KVM e o VMM.
- [gVisor](gvisor.md) compara uma sandbox de syscalls.

## Fonte primária

- [Firecracker](https://github.com/firecracker-microvm/firecracker)
