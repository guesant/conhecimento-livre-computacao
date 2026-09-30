# Processo Linux

Um processo é uma instância de um programa em execução, com espaço de
endereçamento, descritores de arquivo, credenciais, sinais e relações com
outros processos. Ele é criado por uma chamada como `clone` ou `fork` e
termina por saída voluntária, sinal ou falha não tratada.

Containers não criam um kernel separado. O processo do container continua sendo
um processo do host e pode ser observado no host, embora namespaces mudem a
visão que ele recebe de processos, rede e mounts.

## Ciclo de vida

O processo possui um PID no namespace em que foi criado, um processo pai e,
quando termina antes de o pai coletar seu status, pode permanecer como zombie.
O pai chama `wait` para obter o status e liberar a entrada restante na tabela
de processos.

Em um PID namespace, o primeiro processo recebe PID 1. Ele precisa tratar
sinais e adotar processos órfãos. Quando esse processo termina, o kernel
encerra os demais processos do namespace. Por isso o processo principal de um
container é também seu limite de vida.

## Recursos e isolamento

O processo usa recursos globais por meio do kernel. Namespaces controlam o que
ele consegue ver; cgroups controlam contabilização e limites; capabilities,
seccomp e LSMs reduzem operações privilegiadas. Nenhuma dessas camadas
substitui as outras.

A relação entre PID, namespace e cgroup é útil no diagnóstico: um processo
pode existir no host com um PID diferente do PID que enxerga dentro do
container, enquanto o cgroup mostra a hierarquia de recursos que o limita.

## Diagnóstico

Use `ps`, `/proc/<pid>`, `pstree`, `lsns` e `systemctl status` conforme
a camada investigada. Primeiro confirme se o processo existe, quem é seu
pai, qual estado apresenta e em qual namespace e cgroup está. Só depois
investigue rede, disco ou aplicação.

Um processo em estado `D` pode estar aguardando I/O não interrompível; matar
o processo não resolve a operação presa. Um zombie não consome CPU, mas indica
que o pai não está coletando filhos corretamente.

## Relações

- [Namespaces](namespaces.md) controlam a visão de recursos globais.
- [User namespaces](user-namespaces.md) traduzem identidade e privilégio.
- [Cgroups](cgroups.md) controlam e contabilizam recursos.
- [System calls](../kernel/system-calls.md) definem a interface com o kernel.

## Fontes primárias

- [proc(5)](https://man7.org/linux/man-pages/man5/proc.5.html)
- [pid_namespaces(7)](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html)
