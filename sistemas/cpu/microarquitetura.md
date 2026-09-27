# Microarquitetura

Microarquitetura é a implementação concreta de uma ISA. Ela inclui pipeline, unidades de execução, caches, predição de desvios, execução fora de ordem, renomeação de registradores, largura de emissão, interconexão e gerenciamento de energia. Dois processadores podem executar a mesma ISA e ter microarquiteturas muito diferentes.

Uma instrução de soma é uma operação da ISA. A quantidade de portas de execução que pode realizar somas, o número de instruções emitidas por ciclo e o modo como operandos são encaminhados pertencem à microarquitetura.

A microarquitetura influencia latência, throughput, consumo e comportamento térmico. Ela também define como o processador trata dependências, especulação, falhas de previsão, hierarquia de memória e paralelismo interno. Por isso, a frequência nominal ou o conjunto de instruções não basta para comparar duas implementações.

## Relação com a ISA

A ISA precisa permanecer compatível com o contrato visível ao software. A microarquitetura pode mudar sem exigir a recompilação dos programas, desde que preserve esse contrato. Extensões novas, porém, alteram a ISA e só podem ser usadas por software que detecte ou exija sua presença.

## Fontes

- [Intel 64 and IA-32 Architectures Optimization Reference Manual](https://www.intel.com/content/www/us/en/content-details/671488/intel-64-and-ia-32-architectures-optimization-reference-manual.html)
- [AMD Software Optimization Guide](https://www.amd.com/en/developer/resources/technical-articles/software-optimization-guide-for-amd-family-19h-processors.html)
- [Computer Systems: A Programmer's Perspective](https://csapp.cs.cmu.edu/3e/perspective.html)
