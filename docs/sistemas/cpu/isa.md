# Arquitetura de conjunto de instruções

Uma arquitetura de conjunto de instruções, ou ISA, é o contrato que o processador expõe ao software. Ela define instruções, registradores visíveis, modos de endereçamento, tipos de dados, exceções, níveis de privilégio e regras de acesso à memória. Assembly, compiladores, sistemas operacionais e hipervisores dependem desse contrato.

## ISA não é sinônimo de fabricante

Intel e AMD fabricam processadores x86-64. A compatibilidade de instruções permite executar um grande conjunto de binários nos dois fabricantes, mas extensões, níveis de suporte, recursos de virtualização, características de energia e desempenho podem divergir. O nome comercial do processador não é a ISA.

Arm define arquiteturas e licenças de núcleos e instruções. AArch64 é o estado de execução de 64 bits associado ao conjunto A64 de Armv8-A e às extensões posteriores. RISC-V é uma ISA aberta e modular, cuja especificação separa uma base de extensões.

## O que a ISA descreve

Uma ISA normalmente define:

- registradores gerais, de ponto flutuante, vetoriais e de controle;
- largura e formato das instruções;
- operações aritméticas, lógicas, de comparação e transferência;
- modos de endereçamento e alinhamento;
- modelo de memória e regras de ordenação;
- instruções de salto, chamada, retorno, interrupção e exceção;
- níveis de privilégio e instruções reservadas ao sistema;
- extensões opcionais e identificadores de capacidade.

## RISC e CISC

RISC e CISC são rótulos históricos para tendências de desenho, não uma classificação suficiente de um processador moderno. x86-64 preserva uma ISA historicamente CISC, enquanto processadores modernos traduzem muitas instruções para operações internas menores. AArch64 e RISC-V seguem uma estética mais regular, mas podem ter pipelines profundos, execução fora de ordem, caches sofisticados e unidades vetoriais.

## ABI e compatibilidade

A ISA não é o único contrato necessário para executar um programa. A ABI define convenções de chamada, passagem de argumentos, uso de registradores, layout de dados, alinhamento e formato de objetos. O sistema operacional acrescenta chamadas de sistema, formato de executável, bibliotecas e regras de processo.

Dois sistemas podem usar a mesma ISA e ainda exigir binários diferentes. Um programa x86-64 para Linux não é automaticamente um programa x86-64 para Windows.

## Fontes

- [Armv8-A Instruction Set Architecture](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Learn%20the%20Architecture/Armv8-A%20Instruction%20Set%20Architecture.pdf)
- [RISC-V International, especificações](https://riscv.org/technical/specifications/)
- [Intel Architecture, The Basics](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/ia-introduction-basics-paper.pdf)
- [Intel 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- [AMD64 Architecture Programmer's Manual](https://www.amd.com/en/support/tech-docs/amd64-architecture-programmers-manual-volumes-1-5)
