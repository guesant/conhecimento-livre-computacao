# Sistemas e Linux

Esta área organiza os fundamentos que explicam como processos executam, recebem recursos, atravessam a fronteira com o kernel e são isolados.

## CPU e execução

[CPU](cpu/index.md) apresenta execução de instruções e o papel da ISA. [Níveis de privilégio](cpu/niveis-de-privilegio.md) explica por que código de usuário não pode executar qualquer operação diretamente.

## Kernel e processos

[System calls](kernel/system-calls.md) são a interface controlada entre processo e kernel. [Cgroups](linux/cgroups.md) controlam consumo de recursos; [capabilities](linux/capabilities.md) decompõem privilégios tradicionalmente associados a root; [seccomp](linux/seccomp.md) filtra chamadas de sistema.

## Isolamento

Namespaces, cgroups, capabilities, seccomp, LSMs e isolamento de filesystem são mecanismos relacionados, mas independentes. Combiná-los produz o isolamento típico de containers; nenhum deles, isoladamente, "é um container".

## Continue por aqui

Comece por [CPU](cpu/index.md) se a dúvida é execução, por [system calls](kernel/system-calls.md) para a fronteira com o kernel ou por [cgroups](linux/cgroups.md) para controle de recursos.
