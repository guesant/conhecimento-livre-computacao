# VDSO

Virtual Dynamic Shared Object, VDSO, é uma área fornecida pelo kernel e mapeada
no processo para que certas operações possam ser executadas sem uma entrada
completa em modo kernel. A biblioteca C descobre as funções VDSO e pode usá-las
para obter tempo ou realizar operações específicas com menor custo.

## Por que existe

Uma syscall envolve troca de privilégio, validação e retorno. Para dados que o
kernel consegue publicar de forma segura em uma página compartilhada, como
algumas fontes de relógio, a VDSO evita parte desse custo. O processo não recebe
acesso arbitrário ao kernel: a página é preparada e protegida pelo sistema.

O uso é transparente para a maioria das aplicações. `clock_gettime` pode ser
resolvido pela libc para uma função VDSO ou cair em syscall quando a fonte de
tempo ou a arquitetura não permite o caminho rápido.

## Portabilidade e diagnóstico

VDSO varia por arquitetura e versão do kernel. Seu endereço não deve ser
hardcoded e o código não deve depender de símbolos internos. `strace` pode não
mostrar uma syscall para toda chamada que a libc resolveu via VDSO, então a
ausência de uma linha não prova que a função não foi executada.

O clocksource, virtualização, ajuste de relógio e suspensão podem mudar a
latência e a semântica observada. VDSO acelera a leitura, mas não transforma
`CLOCK_REALTIME` em monotônico nem corrige uma escolha errada de relógio.

## Relações

- [Syscalls](system-calls.md) explica a entrada no kernel.
- [Libc](../unix/libc.md) pode selecionar a implementação VDSO.
- [Relógio monotônico](../tempo/fusos-horarios.md) diferencia tempo de parede e duração.

## Fontes primárias

- [The Linux VDSO](https://www.kernel.org/doc/html/latest/arch/x86/elf_hwcaps.html)
- [vdso(7)](https://man7.org/linux/man-pages/man7/vdso.7.html)
- [timekeeping no kernel Linux](https://www.kernel.org/doc/html/latest/core-api/timekeeping.html)
