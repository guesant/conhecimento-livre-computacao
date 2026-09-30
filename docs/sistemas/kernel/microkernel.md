# Microkernel

Microkernel é uma arquitetura de sistema operacional que mantém no modo
privilegiado somente mecanismos mínimos, como agendamento, comunicação entre
processos e parte da gestão de memória. Drivers, filesystems e serviços podem
rodar em user space e conversar por IPC.

## Mecanismo e política

O microkernel tenta separar mecanismos fundamentais de políticas e serviços.
Uma falha em um driver de user space pode ser isolada ou reiniciada sem
necessariamente derrubar o kernel. O custo é que mensagens, mudanças de
contexto e coordenação entre servidores ficam no caminho de operações que em um
monolithic kernel seriam chamadas internas.

O termo não define uma implementação única. Alguns sistemas colocam mais
serviços no kernel por desempenho ou compatibilidade; outros mantêm uma divisão
mais rígida. A classificação deve considerar o que é privilegiado no sistema
real, não apenas o nome do projeto.

## IPC e recuperação

IPC é a interface central. Portas, capabilities, mensagens e memória
compartilhada podem formar o contrato entre processos. O sistema precisa tratar
servidor ausente, mensagem malformada, timeout, reinício e estado parcialmente
persistido. Isolamento só ajuda se a política de comunicação limitar quem pode
acessar cada serviço.

## Comparação

Kernels monolíticos colocam mais drivers e subsistemas no espaço privilegiado,
reduzindo saltos IPC e usando uma integração madura de hardware. Microkernels
podem reduzir o TCB e permitir recuperação localizada, mas exigem desenho de
protocolos, drivers e observabilidade mais rigoroso. Sistemas híbridos misturam
as duas ideias.

## Relações

- [Syscalls](system-calls.md) apresenta a fronteira entre processos e kernel.
- [IPC](../../comunicacao/ipc.md) explica comunicação entre processos.
- [Capability](https://www.cl.cam.ac.uk/research/security/capsicum/) relaciona isolamento e autoridade.

## Fontes primárias

- [seL4 microkernel](https://sel4.systems/)
- [L4Re](https://l4re.org/)
- [MINIX 3](https://www.minix3.org/)
