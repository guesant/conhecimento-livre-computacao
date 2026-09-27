# WebKit

WebKit é uma engine de navegador open source usada pelo Safari e por outras
aplicações. O projeto reúne componentes para interpretar e renderizar páginas,
executar JavaScript, integrar rede, armazenar dados e expor uma API ao produto
que hospeda a engine. WebKit não é sinônimo de Safari, e Safari não é apenas a
engine: ele também inclui interface, serviços do sistema, políticas,
armazenamento e integração específica das plataformas Apple.

## Componentes

WebCore contém grande parte da plataforma de documentos, incluindo DOM, CSS,
layout, pintura e integração com recursos web. JavaScriptCore é a engine que
executa JavaScript e WebAssembly. O produto hospedeiro conecta esses componentes
a processos, rede, armazenamento, janelas, permissões e APIs do sistema.

Essa divisão é útil para investigar defeitos. Uma incompatibilidade pode estar
na interpretação do padrão, na engine JavaScript, em um port de WebKit, no
produto que hospeda a engine ou em uma política específica da plataforma.

## Ciclo de uma página

WebCore analisa documentos, calcula estilo, constrói o layout e prepara as
etapas de pintura e composição. Alterações feitas por JavaScript podem
invalidar parte desse trabalho. O custo percebido pelo usuário resulta da
combinação de rede, parsing, execução de scripts, estilo, layout, pintura,
composição, imagens e fontes.

Uma aplicação deve medir esses estágios separadamente. A redução do tamanho de
um bundle não garante, sozinha, que layout e composição serão rápidos. Da mesma
forma, uma resposta HTTP rápida não impede que scripts bloqueiem a thread
principal ou que uma árvore DOM excessiva aumente o custo de renderização.

## JavaScriptCore e APIs do host

JavaScriptCore implementa a linguagem e o modelo de execução. Ele não fornece
DOM, `fetch`, filesystem, sockets ou permissões automaticamente. WebCore e o
host registram objetos, eventos e APIs que tornam o ambiente um navegador.

Esse modelo também existe fora da Apple. Uma engine JavaScript pode ser
embutida em um aplicativo, enquanto a plataforma de documentos e as APIs
disponíveis dependem do host. Código que assume a presença de uma Web API deve
declarar essa dependência e testar a capacidade antes de usá-la.

## Ports e plataformas

WebKit possui ports, que adaptam os componentes comuns a sistemas operacionais,
toolkits, bibliotecas gráficas, redes e modelos de processo diferentes. O mesmo
conceito web pode ter diferenças de disponibilidade, permissões, codecs,
políticas de armazenamento e integração entre ports.

Uma página deve ser escrita contra padrões e capacidades disponíveis, não contra
uma suposição de que todas as plataformas WebKit são idênticas. Em particular,
restrições de APIs e de distribuição em sistemas móveis podem vir do produto ou
do sistema operacional, e não do núcleo compartilhado do projeto.

## Segurança

WebKit participa do processamento de conteúdo não confiável, mas a segurança
completa depende do host. Sandboxing, isolamento de processos, origem,
permissões, armazenamento, políticas de conteúdo, atualizações e integração com
o sistema operacional formam uma defesa em camadas.

Ao embutir WebKit, não exponha funções nativas sem validação, não confie em
conteúdo remoto por padrão e defina claramente quais esquemas, origens,
protocolos e recursos são permitidos. A API do host é parte da superfície de
ataque tanto quanto a engine.

## Padrões e compatibilidade

WebKit acompanha padrões da plataforma web e participa de testes e discussões
do ecossistema. A compatibilidade observada em Safari, WebKitGTK, WPE WebKit e
outras integrações pode divergir por causa de versão, port, flags, APIs do
sistema e decisões do produto.

Quando houver uma diferença, reduza o caso e compare parsing, JavaScript, DOM,
CSS, mídia e permissões. Prefira recursos padronizados e progressive
enhancement. Polyfills devem ser usados quando a capacidade realmente não
existe, não apenas para esconder uma detecção incorreta do ambiente.

## Embedding e manutenção

Aplicações que usam WebKit precisam acompanhar a versão do port e as correções
de segurança do projeto e do sistema operacional. Atualizações podem alterar
renderização, APIs, políticas de armazenamento, certificados e comportamento
de mídia, por isso testes de regressão devem cobrir as páginas e fluxos que o
produto realmente oferece.

No diagnóstico, use ferramentas de desenvolvimento e traces para separar
tempo de rede, script, estilo, layout, paint e composição. Observe também
consumo de memória, retenção de objetos, tamanho da árvore DOM e custo de
decodificação de imagens e fontes.

## Relações

- [V8](../v8.md) e [SpiderMonkey](../javascript/spidermonkey.md) são engines
  JavaScript diferentes de JavaScriptCore.
- [Blink](blink.md) e [Servo](servo.md) são outras engines de navegador.
- [JavaScript](../../../linguagens/javascript.md) explica a fronteira entre
  ECMAScript e APIs do host.

## Fontes primárias

- [WebKit project](https://webkit.org/project/)
- [WebKit](https://webkit.org/)
- [WebKit source repository](https://github.com/WebKit/WebKit)
- [JavaScriptCore no projeto WebKit](https://github.com/WebKit/WebKit/tree/main/Source/JavaScriptCore)
- [Web Platform Tests](https://github.com/web-platform-tests/wpt)
