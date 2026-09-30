# Node.js

Node.js é um runtime de JavaScript baseado em V8, com APIs de sistema e rede
e uma camada de I/O assíncrono baseada em libuv. Ele não é a linguagem
JavaScript, o navegador nem um framework web. O processo Node fornece o host
que define `process`, filesystem, sockets, timers, streams e módulos.

## Event loop e I/O

Operações de rede e filesystem podem ser iniciadas sem bloquear a thread que
executa callbacks. O event loop processa fases e filas do host, enquanto parte
do trabalho pode usar o thread pool do libuv ou worker threads. Async não torna
um cálculo longo paralelo: parsing enorme, compressão síncrona e loops CPU-bound
podem bloquear todas as requisições daquela instância.

Use APIs assíncronas, limites de concorrência, streams e backpressure. Para
CPU-bound, considere worker threads, child processes ou uma fila de jobs. O
processo deve possuir timeouts, cancelamento e limites de memória, conexões e
tarefas pendentes.

## Módulos e dependências

Node suporta ECMAScript Modules e CommonJS, com regras de resolução e
interoperabilidade próprias. `package.json`, lockfile, scripts de instalação e
exports formam parte do contrato de build. Dependências devem ser pinadas,
auditadas e executadas com permissões mínimas.

## Servidor e operação

O runtime não substitui um proxy, load balancer, TLS termination, autenticação
ou observabilidade. Configure graceful shutdown para parar de aceitar tráfego,
aguardar requisições e encerrar workers sem abandonar efeitos externos.

Monitore event loop lag, heap, garbage collection, RSS, thread pool, conexões,
fila de requests, latência de dependências e rejeições. Uma métrica de CPU baixa
não prova que a aplicação está saudável se o event loop estiver bloqueado ou
aguardando um banco lento.

## Fontes primárias

- [Node.js documentation](https://nodejs.org/docs/latest/api/)
- [Node.js event loop](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [Node.js worker threads](https://nodejs.org/api/worker_threads.html)
