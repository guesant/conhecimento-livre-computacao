# CPU

A CPU executa instruções definidas por uma arquitetura de conjunto de instruções, ou ISA. A ISA especifica operações, registradores, formatos de instrução e comportamento observável pelo software; uma microarquitetura concreta decide como implementar isso internamente.

## Casos de uso

Entender CPU e ISA é útil para interpretar assembly, ABI, virtualização, diferenças entre arquiteturas como x86-64 e AArch64 e por que um binário compilado para uma ISA não executa nativamente em outra.

## Exemplo

Uma instrução de soma pode ser parte da ISA enquanto pipeline, execução fora de ordem, caches e unidades funcionais pertencem à microarquitetura. Duas CPUs podem implementar a mesma ISA com desempenho e organização interna diferentes.

## Boa prática

Separe sempre arquitetura visível ao software de detalhes de implementação. Essa distinção evita explicar compatibilidade binária usando propriedades acidentais de um processador específico.

## Má prática

Tratar "CPU", "x86" e "microarquitetura" como sinônimos mistura níveis diferentes. Também é inadequado deduzir desempenho apenas pela ISA.

## Continue por aqui

[Níveis de privilégio](niveis-de-privilegio.md) explica como a CPU participa da proteção do kernel. [System calls](../kernel/system-calls.md) mostra a transição controlada entre aplicação e kernel.