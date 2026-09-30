# MicroVM

Uma microVM usa virtualização de hardware com um conjunto reduzido de
dispositivos e uma finalidade estreita. Ela mantém um kernel convidado próprio
e a fronteira de uma VM, mas busca tempo de inicialização e consumo próximos
dos de um container.

## Modelo

A microVM normalmente reduz dispositivos emulados, escopo da configuração e
superfície de gerenciamento. A aplicação continua sendo executada em um
kernel convidado, portanto não compartilha diretamente o kernel do host como
um container comum.

Esse modelo é útil quando a carga não deve confiar no kernel do host, mas o
overhead de uma VM tradicional é alto para workloads curtos ou densos.

## Limitações

O kernel convidado ainda precisa ser inicializado e atualizado. Dispositivos
reduzidos podem impedir aplicações que esperam hardware virtual completo. A
observabilidade deve atravessar host, hypervisor, guest kernel e aplicação, e
o custo de boot pode dominar workloads muito curtos.

## Relações

- [Hypervisor](hypervisor.md) explica a fronteira de hardware.
- [Firecracker](firecracker.md) é uma implementação de microVM.
- [gVisor](gvisor.md) escolhe uma fronteira de syscall diferente.
- [Containers de sistema](system-containers.md) compartilham o kernel do host.

## Fonte primária

- [Firecracker design](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md)
