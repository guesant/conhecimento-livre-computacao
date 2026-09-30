# Event loop

Event loop é um mecanismo que observa eventos prontos e executa as funções associadas a
eles. Em vez de manter uma thread bloqueada para cada espera de rede, o processo registra
interesse em sockets, timers ou outras fontes e retorna ao scheduler quando existe trabalho
pronto.

O modelo típico executa um callback até ele terminar. A execução cooperativa facilita
compartilhar estado dentro da thread, mas cria uma obrigação: nenhum callback pode bloquear
por tempo indefinido. Um loop parado não atende timers, sockets, callbacks ou novas
requisições.

## Fila de tarefas e microtasks

Uma implementação costuma ter filas ou fases para eventos de I/O, timers, fechamento de
recursos e tarefas agendadas. Promises e APIs equivalentes também usam uma fila de
microtasks, que normalmente é drenada em pontos específicos antes que o loop avance.

Microtasks são úteis para continuar uma operação assíncrona com baixa latência, mas uma
cadeia que agenda microtasks indefinidamente pode impedir que I/O e timers progridam. O
mesmo vale para callbacks que sempre recolocam trabalho na fila sem backpressure.

## Node.js

No Node.js, o event loop permite I/O não bloqueante mesmo com uma thread JavaScript
principal por padrão. A documentação oficial descreve fases como timers, pending callbacks,
poll, check e close callbacks. `process.nextTick()` possui uma fila própria e não é uma
fase comum do loop; `setImmediate()` agenda trabalho para a fase check.

Timers representam um limite mínimo para execução, não uma garantia de horário. Um callback
agendado para 100 ms pode atrasar se a thread estiver executando outro callback ou se o
sistema estiver ocupado.

## V8 não é o event loop

V8 executa JavaScript, administra objetos e garbage collection. O host fornece o modelo de
eventos. No Node.js, libuv fornece o loop e a integração com I/O; no navegador, o host do
browser integra engine, DOM, Web APIs, renderização e filas próprias.

Essa separação explica por que o mesmo JavaScript pode ter comportamentos temporais
distintos em Node, Chrome, Firefox, Deno ou outro host.

## Thread pool e I/O

Nem toda operação assíncrona significa que uma thread de aplicação está executando o
trabalho. Sockets normalmente usam polling do kernel. Operações de filesystem, DNS ou
trabalho nativo que não possui API não bloqueante podem usar um pool.

O pool também é um recurso limitado. Saturá-lo com filesystem, criptografia ou funções
nativas atrasa operações aparentemente independentes. Monitore tempo no loop, fila do pool,
latência de callback, CPU e memória.

## Bloqueio e starvation

Código CPU-bound, parsing de payload enorme, expressão regular patológica, serialização
grande e loop síncrono bloqueiam o event loop. Divida o trabalho, use streaming, worker
threads, child process ou uma fila de jobs conforme o requisito.

Uma função `async` não torna automaticamente seu corpo não bloqueante. Ela pode executar
longos trechos síncronos antes do primeiro `await`, e uma biblioteca pode oferecer uma API
com nome assíncrono que ainda consome o thread pool ou a thread principal.

## Cancelamento e deadlines

Uma operação enfileirada deve ter cancelamento, timeout e limite de memória quando esses
conceitos fizerem parte do contrato. Cancelar a espera do cliente não cancela
automaticamente o trabalho no kernel, no worker ou no servidor remoto.

Use AbortSignal, deadlines e propagação de contexto quando o ecossistema suportar. A
operação precisa deixar claro se foi cancelada antes do efeito, durante o efeito ou depois
de o efeito ter sido confirmado.

## Relações

- [V8](v8.md) trata a engine JavaScript.
- [libuv](libuv.md) trata o loop e a abstração de I/O do Node.js.
- [Comunicação assíncrona](../../comunicacao/comunicacao-assincrona.md) trata filas e
  persistência fora do processo.
- [Worker threads no Node.js](https://nodejs.org/api/worker_threads.html) separa trabalho
  CPU-bound da thread JavaScript principal.

## Fontes

- [Node.js Event Loop](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [Node.js, não bloqueie o Event Loop ou o Worker Pool](https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop)
