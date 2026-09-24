# Hypervisor

Um hypervisor apresenta recursos de hardware virtual para uma máquina virtual e
isola o kernel convidado do host e de outras máquinas. Ele pode executar
diretamente sobre o hardware ou sobre um sistema operacional hospedeiro.

## Tipos

Um hypervisor tipo 1 executa como camada de plataforma e controla o acesso ao
hardware sem depender de um sistema operacional geral para o caminho
principal. Um tipo 2 executa como aplicação sobre um host, delegando parte do
acesso ao sistema operacional hospedeiro.

A classificação ajuda a discutir o caminho de execução, mas não determina
sozinha segurança ou performance. KVM usa suporte de virtualização do Linux e
é operado em conjunto com QEMU; o conjunto pode ser usado como plataforma de
virtualização, embora os componentes tenham responsabilidades diferentes.

## Interfaces

A VM vê vCPU, memória, dispositivos de bloco e rede. Virtio reduz a necessidade
de emular hardware legado e permite que o convidado use dispositivos
paravirtualizados. IOMMU limita DMA quando dispositivos físicos são passados
diretamente para um convidado.

## Trade-offs

O kernel próprio aumenta isolamento e permite executar sistemas diferentes,
mas exige boot, memória, atualização e observabilidade do convidado. A
virtualização adiciona uma fronteira que containers não possuem, ao custo de
overhead e de uma superfície adicional no hypervisor e nos dispositivos
virtuais.

## Relações

- [VMs e hypervisors](../../vms-e-hipervisores.md) compara VM e container.
- [MicroVM](microvm.md) reduz o conjunto de dispositivos e o tempo de boot.
- [Processo Linux](../linux/process.md) explica o modelo compartilhado de
  containers.

## Fonte primária

- [Linux KVM](https://www.kernel.org/doc/html/latest/virt/kvm/index.html)
- [QEMU documentation](https://www.qemu.org/docs/master/)
