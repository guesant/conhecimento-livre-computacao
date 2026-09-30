# IOMMU

Input-Output Memory Management Unit, IOMMU, traduz endereços usados por
dispositivos de I/O e restringe quais regiões de memória eles podem acessar.
Ela fornece uma camada análoga à paginação da CPU para DMA e é essencial para
isolar dispositivos quando há passthrough para máquinas virtuais ou workloads.

## DMA e domínios

Um dispositivo pode acessar memória por DMA sem executar instruções da CPU.
Sem tradução e proteção, um dispositivo comprometido ou mal configurado pode
ler ou sobrescrever memória fora do buffer autorizado. A IOMMU associa o
dispositivo a um domínio com tabelas de tradução e permissões.

Em virtualização, o hypervisor pode entregar uma função PCI a uma VM e mapear
os endereços DMA da VM para a memória que ela possui. O dispositivo não deve
conseguir alcançar a memória do host ou de outra VM. Interrupt remapping ajuda
a controlar interrupções direcionadas ao sistema.

## Grupos e passthrough

IOMMU groups representam unidades que a plataforma não consegue isolar
independentemente com segurança. Um grupo contendo várias funções pode limitar
passthrough para uma única VM. ACS, topology PCIe, firmware e suporte do
dispositivo influenciam esse agrupamento.

Passthrough reduz a abstração do hypervisor. Live migration, snapshot,
overcommit e recuperação podem ficar limitados porque o estado do dispositivo
está ligado à VM. SR-IOV oferece funções virtuais em algumas placas, mas cria
outro modelo de isolamento e dependência do driver.

## Segurança e desempenho

IOMMU não torna um driver correto nem um dispositivo confiável. Um dispositivo
passado diretamente à VM continua tendo acesso conforme as permissões do grupo.
Firmware, reset, DMA remapping, interrupt remapping e isolamento de grupos
precisam ser verificados. Tradução pode ter custo, mas grandes páginas, caching
de IOTLB e configuração correta reduzem overhead.

## Relações

- [Hypervisor](hypervisor.md) explica a fronteira de virtualização.
- [DMA](../cpu/barramento-do-sistema.md) apresenta acesso de dispositivos à memória.
- [PCI passthrough](https://www.kernel.org/doc/html/latest/driver-api/vfio.html) usa VFIO e IOMMU.

## Fontes primárias

- [VFIO no kernel Linux](https://www.kernel.org/doc/html/latest/driver-api/vfio.html)
- [Intel VT-d specification](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-virtualization-technology-for-directed-io-architecture-spec.html)
- [Linux IOMMU documentation](https://www.kernel.org/doc/html/latest/driver-api/iommu.html)
