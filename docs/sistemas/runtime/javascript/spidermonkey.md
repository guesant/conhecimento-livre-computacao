# SpiderMonkey

SpiderMonkey é a engine de JavaScript e WebAssembly mantida pela Mozilla. Ela é
usada pelo Firefox e também pode ser incorporada por outras aplicações por meio
das APIs de embedding. A engine implementa a linguagem e o modelo de execução,
mas não é um navegador completo e não fornece, sozinha, DOM, HTTP, filesystem,
permissões ou uma interface gráfica.

Essa separação é importante porque o mesmo código JavaScript pode executar em
SpiderMonkey com APIs diferentes quando o hospedeiro é o Firefox, o shell da
engine ou uma aplicação embutida. A engine fornece o núcleo da linguagem; o
host decide quais objetos nativos, módulos, callbacks e recursos externos serão
expostos.

## Papel no Firefox

No Firefox, SpiderMonkey é a camada responsável por executar JavaScript e
WebAssembly. Gecko, o conjunto de componentes de plataforma do Firefox,
integra a engine com DOM, Web APIs, rede, eventos, layout e segurança do
navegador. O produto Firefox ainda acrescenta interface, armazenamento,
políticas de navegação, isolamento de processos e integração com o sistema
operacional.

Portanto, SpiderMonkey não é sinônimo de Gecko ou Firefox. Uma falha ou
diferença observada em uma API web pode estar na engine, em uma camada de
plataforma, no processo do navegador ou na implementação específica de uma
Web API.

## Modelo de execução

O código é analisado, compilado para representações internas e executado por
uma combinação de interpretador e compiladores just-in-time. Funções quentes
podem ser otimizadas com base no comportamento observado. Quando as suposições
da otimização deixam de valer, a engine pode desotimizar o caminho e voltar a
uma execução mais conservadora.

O pipeline concreto muda entre versões. A propriedade estável é a existência de
parser, bytecode ou representação equivalente, interpretador, otimização em
runtime e gerenciamento de memória. Código que depende de nomes ou detalhes
internos da engine não deve ser tratado como portável entre versões.

Promises, `async` e `await` dependem do modelo de jobs e microtasks definido
para o host. O event loop do Firefox e o loop de uma aplicação embutida não são
necessariamente a mesma coisa. A engine executa callbacks quando o hospedeiro
os agenda, mas não decide sozinha como I/O, timers e eventos de janela serão
coordenados.

## Memória e isolamento

SpiderMonkey possui garbage collector e administra objetos JavaScript,
closures, estruturas internas e valores associados aos contextos de execução.
Referências mantidas em caches, listeners ou globais podem prolongar a vida de
objetos e aumentar o heap. A aplicação hospedeira continua responsável por
fechar sockets, arquivos e outros recursos externos.

Realms e compartimentos ajudam a separar globais, objetos e grupos de execução.
Eles não devem ser confundidos automaticamente com uma sandbox completa. Uma
aplicação que incorpora SpiderMonkey precisa controlar bindings nativos,
limitar operações custosas e estabelecer uma fronteira de segurança real para
código não confiável.

No navegador, a segurança também depende de origem, processos, políticas de
conteúdo, permissões e validações feitas fora da engine. Executar JavaScript em
um contexto separado não concede ao código acesso seguro ou isolado por si só.

## WebAssembly

SpiderMonkey implementa o formato e o modelo de execução de WebAssembly. O
programa WebAssembly só acessa recursos externos por meio de imports e APIs
oferecidas pelo host. Filesystem, rede, relógio, threads e armazenamento não
são permissões implícitas do formato.

Ao avaliar desempenho, meça compilação, warmup, garbage collection, chamadas
entre JavaScript e WebAssembly, cópias de memória e tempo de execução. Uma
rotina rápida em isolamento pode deixar de ser vantajosa quando o custo de
serialização e comunicação com o host domina a operação.

## Embedding

Um embedder cria runtimes ou contextos, carrega scripts, registra funções
nativas e traduz valores entre o programa e a engine. Essa integração precisa
definir tratamento de exceções, cancelamento, limites de CPU e memória,
finalização de recursos e observabilidade.

O shell de SpiderMonkey é útil para testar a linguagem e a engine, mas não
representa automaticamente as APIs do Firefox. Em uma aplicação própria, a
ausência de DOM ou `fetch` não é uma limitação da linguagem, e sim uma decisão
do host.

## Escolha e comparação

SpiderMonkey é uma escolha natural quando a integração com o ecossistema
Mozilla, o Firefox ou APIs de embedding da engine é relevante. V8 é comum em
Chrome, Node.js e muitos embedders. QuickJS favorece tamanho e inicialização
simples. JavaScriptCore é a engine associada ao WebKit e aos sistemas Apple.

Nenhuma dessas engines fornece, isoladamente, a mesma plataforma web. A
compatibilidade depende da combinação entre engine, APIs do host, DOM, rede,
renderização, política de segurança e versão do navegador.

## Desempenho e diagnóstico

Benchmarks devem separar parsing, compilação, warmup, execução otimizada,
garbage collection e interação com o host. Compare cargas reais, observe
alocações e retenção de memória e evite concluir que uma diferença em uma
microoperação representa o comportamento de uma aplicação inteira.

Ao investigar lentidão, diferencie tempo de JavaScript, espera por I/O, layout,
paint, composição, serialização e bloqueio do processo principal. No Firefox,
ferramentas de desenvolvimento e perfis da aplicação ajudam a separar a
engine das camadas de plataforma.

## Relações

- [JavaScript](../../../linguagens/javascript.md) descreve a linguagem e a
  fronteira entre ECMAScript e APIs do host.
- [V8](../v8.md) é outra engine de JavaScript e WebAssembly.
- [QuickJS](quickjs.md) é uma engine pequena e embutível.
- [Blink](../browser/blink.md), [WebKit](../browser/webkit.md) e
  [Servo](../browser/servo.md) são engines de navegador, não engines
  JavaScript equivalentes a SpiderMonkey.
- [Event loop](../event-loop.md) explica o modelo cooperativo usado pelo host.

## Fontes primárias

- [SpiderMonkey](https://spidermonkey.dev/)
- [Documentação de JavaScript do Firefox](https://firefox-source-docs.mozilla.org/js/)
- [Documentação do Firefox sobre a engine](https://firefox-source-docs.mozilla.org/js/index.html)
- [Especificação ECMAScript](https://tc39.es/ecma262/)
- [Especificação WebAssembly](https://webassembly.github.io/spec/core/)
