# Runtimes de execução

Runtime é o conjunto que transforma código carregado em execução observável. Ele pode
incluir uma máquina virtual, um garbage collector, bibliotecas de I/O, um scheduler,
bindings para o sistema operacional, um modelo de módulos e mecanismos de isolamento.

Runtime não é sinônimo de linguagem. JavaScript é uma linguagem; V8 é uma implementação de
engine; Node.js combina V8 com APIs de servidor e libuv; um navegador combina uma engine
JavaScript com DOM, Web APIs, renderização e políticas de segurança.

## Mapa

[Event loop](event-loop.md) explica execução cooperativa, callbacks, filas de tarefas,
microtasks, timers, fairness e bloqueio.

[V8](v8.md) explica a engine que interpreta, compila e coleta JavaScript e WebAssembly.

[SpiderMonkey](javascript/spidermonkey.md) explica a engine JavaScript e WebAssembly
mantida pela Mozilla e usada pelo Firefox.

[Blink](browser/blink.md), [WebKit](browser/webkit.md) e [Servo](browser/servo.md)
explicam engines de navegador, que integram documentos, estilos, layout, renderização
e APIs web com uma engine JavaScript e um host.

[libuv](libuv.md) explica o loop multiplataforma, polling de I/O, handles, requests e
thread pool usado por Node.js e outros projetos.

## Engine, navegador e host

Os termos costumam ser usados como se fossem sinônimos, mas representam camadas
distintas. Uma engine JavaScript executa ECMAScript e pode executar WebAssembly. Uma
engine de navegador também precisa lidar com documentos, DOM, CSS, layout e
renderização. Um host conecta essas engines a rede, armazenamento, timers, processos,
permissões, janelas e sistema operacional.

| Camada | Exemplos | Responsabilidade principal |
| --- | --- | --- |
| Engine JavaScript | V8, SpiderMonkey, JavaScriptCore, QuickJS | Executar JavaScript e, quando suportado, WebAssembly |
| Engine de navegador | Blink, WebKit, Servo | Processar documentos e renderizar a plataforma web |
| Host ou produto | Chromium, Firefox, Safari, Node.js, Bun, GJS | Fornecer APIs, ciclo de vida, segurança e integração com o sistema |

O limite não é absoluto em todos os projetos. Componentes podem ser distribuídos
entre camadas, e um host pode integrar várias bibliotecas. Ainda assim, a distinção é
útil para investigar compatibilidade, desempenho e segurança. Uma API ausente pode
ser uma decisão do host, não uma limitação da linguagem ou da engine.

## Modelo mental

Uma aplicação pode executar código JavaScript em uma thread principal, delegar I/O ao
kernel ou a workers e depois enfileirar um callback para continuar. Isso é concorrência
sem que cada callback rode em paralelo. Trabalho CPU-bound longo ainda bloqueia a thread
que executa JavaScript, a menos que seja dividido, movido para worker ou processado por
outro processo.

O runtime precisa responder onde a operação espera, quem possui o estado, quando o
callback pode executar, qual fila tem prioridade, como o erro é propagado e quando a
memória é liberada.

## Relações

- [Concorrência e sincronização](../../engenharia-software/concorrencia/index.md) trata
  race conditions, mutexes, semáforos e deadlocks.
- [Filas](../../dados/mensageria/filas.md) trata trabalho durável, ack e backpressure.
- [Comunicação assíncrona](../../comunicacao/comunicacao-assincrona.md) diferencia fila,
  pub/sub, streaming e callback.
