# CPU e arquitetura de processadores

Uma CPU executa instruções definidas por uma arquitetura de conjunto de instruções, ou ISA. A ISA especifica operações, registradores, formatos de instrução e comportamento observável pelo software; uma microarquitetura concreta decide como implementar isso internamente. Esta área separa o contrato da ISA, o ciclo lógico da instrução, o desenho interno e a relação da CPU com memória, GPU, SoC e entrada e saída.

## Mapa da área

- [Conjunto de instruções e microarquitetura](isa-e-microarquitetura.md) separa o contrato da ISA da implementação em silício.
- [Ciclo de instrução](ciclo-de-instrucao.md) explica fetch, decode, execute, pipeline, ULA e unidade de controle.
- [CPU, RAM, GPU e SoC](cpu-ram-gpu-e-soc.md) diferencia os componentes e apresenta memória unificada.
- [Famílias e gerações de processadores](familias-de-processadores.md) organiza Intel, AMD, Arm e Apple Silicon sem confundir produto com arquitetura.
- [Barramento do sistema](barramento-do-sistema.md) descreve CPU, memória, entrada e saída, DMA, IOMMU e o modelo de von Neumann.

## Exemplo

Uma instrução de soma pode ser parte da ISA enquanto pipeline, execução fora de ordem, caches e unidades funcionais pertencem à microarquitetura. Duas CPUs podem implementar a mesma ISA com desempenho e organização interna diferentes.

## Boa prática

Separe sempre arquitetura visível ao software de detalhes de implementação. Essa distinção evita explicar compatibilidade binária usando propriedades acidentais de um processador específico.

## Má prática

Tratar "CPU", "x86" e "microarquitetura" como sinônimos mistura níveis diferentes. Também é inadequado deduzir desempenho apenas pela ISA.

## Continue por aqui

[Níveis de privilégio](niveis-de-privilegio.md) explica como a CPU participa da proteção do kernel. [System calls](../kernel/system-calls.md) mostra a transição controlada entre aplicação e kernel.
