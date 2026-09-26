# Comunicação entre processos

Comunicação entre processos, IPC, é o conjunto de mecanismos usados por processos para trocar dados, sinais ou coordenação. O escopo normalmente é um host ou kernel, embora alguns mecanismos também possam ser usados como base para uma comunicação entre máquinas.

## Mecanismos

[IPC](../ipc.md) reúne pipes, sockets Unix, memória compartilhada, filas, sinais, semáforos e barramentos. Cada mecanismo oferece propriedades diferentes de cópia, ordenação, bloqueio, descoberta, permissões e recuperação quando um processo termina.

Um socket Unix pode ser uma boa fronteira para um daemon local. Memória compartilhada reduz cópias, mas exige sincronização e tratamento cuidadoso de lifecycle. Pipes funcionam bem para fluxos simples entre processos relacionados. Filas e barramentos tornam a coordenação mais explícita, mas introduzem retenção e políticas de entrega.

## Segurança e operação

Permissões de filesystem, namespaces, identidade do processo e limites de tamanho fazem parte do contrato do IPC. Um socket local não é automaticamente seguro se qualquer usuário puder escrevê-lo. O diagnóstico deve separar processo ausente, permissão negada, backlog cheio, protocolo incompatível e consumidor travado.

## Relações

IPC é diferente de [RPC](../rpc.md), que descreve uma chamada de operação normalmente remota. Um RPC local pode usar IPC como transporte. [Comunicação assíncrona](../assinc/index.md) trata filas, eventos e trabalho desacoplado, inclusive quando o transporte deixa de ser local.
