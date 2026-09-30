# libuv

libuv é uma biblioteca multiplataforma em C que oferece event loop, polling de rede,
timers, filesystem assíncrono, DNS, processos, sinais, IPC e thread pool. Ela foi criada
principalmente para o Node.js, mas também é usada por outros projetos.

libuv não é um broker, uma fila durável ou um scheduler de jobs. Suas filas e requests
existem dentro do processo e desaparecem quando ele termina. Para trabalho que precisa
sobreviver a restart, use uma fila persistente ou storage apropriado.

## Event loop

O event loop de libuv normalmente fica associado a uma thread. Ele usa o mecanismo de
notificação disponível no sistema, como epoll no Linux, kqueue em macOS e BSD, event ports
em SunOS e IOCP no Windows. Sockets de rede são observados pelo loop e callbacks são
executados quando há atividade.

Um processo pode criar vários loops, mas cada loop deve ser tratado com o escopo e a
thread apropriados. O loop e os handles não são thread-safe por padrão.

## Handles e requests

Handles representam objetos de longa duração, como TCP server, timer, signal watcher,
filesystem watcher ou pipe. Requests representam operações assíncronas, como uma leitura
de arquivo ou resolução de DNS. O ciclo de vida, callback, erro e liberação de memória
precisam ser respeitados pela aplicação nativa.

Essa distinção ajuda a entender Node.js: um servidor fica ativo como handle; uma operação
individual de leitura é um request que termina e chama uma continuação.

## Thread pool

Nem todo I/O possui uma API não bloqueante equivalente nos sistemas suportados. libuv usa
um pool para operações de filesystem, algumas funções de DNS e trabalho submetido por
`uv_queue_work`.

O pool é global para os loops do processo e tem capacidade limitada. Uma operação de
filesystem lenta pode atrasar outra operação que usa o mesmo pool. Ajustar o tamanho do
pool aumenta concorrência e também pode aumentar CPU, memória, pressão de disco e
concorrência no serviço externo.

I/O de rede não é simplesmente enviado para o thread pool. O loop usa polling do sistema
para observar sockets, enquanto callbacks continuam sendo executados pela thread do loop.

## Handles ativos e encerramento

O loop permanece vivo enquanto há handles referenciados, requests ativos ou handles em
fechamento. Fechar um socket ou timer deve liberar a referência quando o recurso não for
mais necessário. Um handle esquecido pode manter o processo vivo; um close prematuro pode
interromper uma resposta.

Encerramento gracioso precisa parar novos trabalhos, esperar ou cancelar requests,
fechar handles e só então parar o loop. Isso é diferente de matar o processo, que perde
requests e dados em memória.

## Relação com Node.js

Node.js embute V8 para executar JavaScript, usa bindings C++ para expor APIs e usa libuv
para o event loop e várias operações de I/O. A fila de microtasks e `process.nextTick()`
também são políticas do runtime Node, não primitivas de libuv isoladamente.

Quando um callback JavaScript demora, libuv pode continuar observando I/O, mas o callback
seguinte não poderá executar até a thread do loop ser liberada. A arquitetura não elimina
o custo de CPU; ela reduz threads bloqueadas durante espera de I/O.

## Relações

- [Event loop](event-loop.md) explica fases, timers, microtasks e starvation.
- [V8](v8.md) explica execução e memória JavaScript.
- [Filas](../../dados/mensageria/filas.md) diferencia filas em memória de mensageria
  durável.
- [Jobs e workers](../../dados/mensageria/jobs-e-workers.md) trata leases, retry e
  persistência do trabalho.

## Fontes

- [libuv, design overview](https://docs.libuv.org/en/v1.x/design.html)
- [libuv, basics](https://docs.libuv.org/en/v1.x/guide/basics.html)
- [libuv, event loop API](https://docs.libuv.org/en/v1.x/loop.html)
- [Node.js, não bloqueie o Event Loop ou o Worker Pool](https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop)
