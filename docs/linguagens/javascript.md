# JavaScript

JavaScript é uma linguagem dinâmica, baseada em protótipos, com funções de
primeira classe, coleta de lixo e suporte a estilos imperativo, funcional e
orientado a objetos. A especificação da linguagem é ECMAScript. O navegador,
Node.js, Bun, GJS e outros hosts fornecem APIs diferentes ao redor do mesmo
núcleo da linguagem.

## Linguagem e host

ECMAScript define valores, objetos, funções, classes, módulos, promises,
iteradores, generators, typed arrays e regras de coerção. Ele não define DOM,
`fetch`, filesystem, sockets, `process`, `setTimeout` ou uma política de
permissões. Essas APIs pertencem ao host.

Essa separação explica por que um módulo pode funcionar no navegador e falhar
no Node, ou funcionar no Node e não existir no GJS. Uma biblioteca deve
declarar seu ambiente, seus globals e seus requisitos de módulos em vez de
assumir que todo JavaScript é browser JavaScript.

## Modelo de valores

A linguagem possui tipos primitivos e objetos. Objetos podem receber
propriedades em runtime e herdam comportamento por uma cadeia de protótipos.
`class` oferece uma sintaxe de composição, mas não transforma o modelo em
classes tradicionais como as de Java. Closures capturam o ambiente léxico e
podem manter dados vivos por mais tempo que o esperado quando são guardadas em
listeners, caches ou filas.

Conversões implícitas e igualdade frouxa podem esconder defeitos. Em código de
aplicação, prefira igualdade estrita, valide entradas externas e trate
explicitamente `null`, `undefined`, `NaN` e valores ausentes. TypeScript pode
adicionar análise estática, mas o JavaScript executado continua sujeito às
regras do runtime.

## Assincronicidade

Promises e `async`/`await` representam operações que podem terminar depois.
O event loop pertence ao host e coordena callbacks, timers, microtasks e
operações de I/O. Um loop assíncrono não torna uma função CPU-bound paralela:
um cálculo longo ainda bloqueia a thread que executa JavaScript.

Para trabalho pesado, use workers, processos, WebAssembly ou uma fila externa,
conforme a necessidade. Propague cancelamento, limite concorrência e defina o
que acontece quando uma promise rejeita. Uma exceção não observada pode causar
perda de estado, resposta incompleta ou encerramento do processo.

## Módulos e ferramentas

ECMAScript Modules usam `import` e `export`. CommonJS continua presente em
parte do ecossistema Node. Bundlers, transpilers e package managers podem
alterar o formato final, resolver dependências e introduzir código que não
estava visível no arquivo fonte. Fixe versões, valide lockfiles, limite scripts
de instalação e trate dependências como parte da supply chain.

Lint, typecheck, testes e análise de bundle devem fazer parte do ciclo de
desenvolvimento. Não confunda uma transformação de sintaxe com uma garantia de
compatibilidade do runtime ou das Web APIs.

## Segurança e desempenho

Não execute strings externas com `eval` ou mecanismos equivalentes sem uma
fronteira de segurança explícita. Escape dados quando forem inseridos em HTML,
URLs, comandos ou consultas. No servidor, não exponha secrets em bundles,
logs ou mensagens de erro.

Meça alocações, garbage collection, tempo bloqueando o event loop, tamanho de
payload e cache. Uma engine pode otimizar caminhos quentes, mas otimizações
dependem das entradas e podem ser desfeitas quando as suposições mudam.

## Relações

- [V8](../sistemas/runtime/v8.md) é uma engine que executa JavaScript e
  WebAssembly.
- [SpiderMonkey](../sistemas/runtime/javascript/spidermonkey.md) é a engine
  JavaScript e WebAssembly mantida pela Mozilla.
- [Blink](../sistemas/runtime/browser/blink.md),
  [WebKit](../sistemas/runtime/browser/webkit.md) e
  [Servo](../sistemas/runtime/browser/servo.md) são engines de navegador que
  integram uma engine JavaScript a DOM, CSS, renderização e Web APIs.
- [Node.js](../sistemas/runtime/javascript/node.md) fornece um host de servidor
  baseado em V8 e libuv.
- [Bun](../sistemas/runtime/javascript/bun.md) é outro runtime e toolkit.
- [Event loop](../sistemas/runtime/event-loop.md) explica a execução
  cooperativa do host.

## Fontes primárias

- [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [ECMAScript Language Specification](https://tc39.es/ecma262/)
- [ECMAScript Internationalization API](https://tc39.es/ecma402/)
