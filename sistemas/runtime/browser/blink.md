# Blink

Blink é a engine de navegador usada pelo Chromium. Ela implementa partes
centrais da plataforma web, como parsing de HTML, CSS, DOM, estilo, layout,
renderização e integração com APIs web. Blink não é o produto Chromium inteiro
e não é uma engine JavaScript isolada: o Chromium integra Blink com V8, o
módulo Content, a rede, o compositor, o sistema de processos e a interface do
navegador.

## Engine e navegador

O código de Blink vive no projeto Chromium e depende de abstrações fornecidas
por camadas superiores. A própria documentação do projeto descreve Blink como
uma engine de renderização que não funciona sozinha. O módulo Content fornece
parte da plataforma necessária para criar e executar um contexto de navegador.

Essa fronteira evita uma confusão comum. V8 executa JavaScript e WebAssembly;
Blink interpreta e atualiza documentos web; Chromium coordena processos,
navegação, permissões, rede e integração com o sistema operacional. Uma página
interativa normalmente atravessa todas essas camadas.

## Fluxo de uma página

Depois que o navegador recebe recursos, Blink transforma HTML e CSS em
estruturas internas, calcula estilo e layout e prepara fases de pintura e
composição. JavaScript pode modificar o DOM e invalidar parte desse trabalho.
Uma aplicação que altera muitos nós ou estilos em sequência pode provocar
recalculos, pintura e sincronizações dispendiosas.

O fluxo exato depende do tipo de mudança e da versão. O modelo útil para
diagnóstico é distinguir parsing, execução de script, estilo, layout, paint,
composição, decodificação de imagens e espera de rede. Não basta medir apenas o
tempo de carregamento do arquivo JavaScript.

## V8 e Web APIs

Blink utiliza V8 para executar JavaScript, mas as APIs visíveis ao script são
expostas pelo host e pelas camadas de plataforma. `document`, `fetch`,
`localStorage`, timers e APIs de mídia não são fornecidos por V8 sozinho.

Essa separação também explica por que um código pode funcionar em Node.js e
falhar no navegador. Node.js fornece outro host para V8, com filesystem,
processos e módulos próprios, enquanto Chromium combina V8 com Blink e as
restrições de uma página web.

## Segurança e processos

O isolamento de sites, sandbox de renderizadores, permissões e políticas de
navegação pertencem principalmente à arquitetura do Chromium e do sistema
operacional que o hospeda. Blink participa do modelo de execução de documentos,
mas não deve ser tratado como a fronteira completa de segurança do navegador.

O código web deve continuar sendo tratado como não confiável. Validação de
origem, políticas de conteúdo, sandbox, isolamento de processos, atualização do
navegador e controle de permissões precisam funcionar em conjunto. Embutir
Blink ou Chromium em outro produto exige revisar essas fronteiras, pois a
integração pode alterar a superfície de ataque.

## Padrões e compatibilidade

O desenvolvimento é guiado por especificações web, testes da plataforma e
revisões no projeto Chromium. A compatibilidade real depende da versão do
navegador, flags, políticas do produto, suporte da plataforma e comportamento
de outras engines.

Web Platform Tests ajudam a comparar implementações, mas passar um teste não
garante que uma aplicação complexa terá o mesmo comportamento em todos os
navegadores. Use detecção de capacidade e padrões web antes de depender de
detecção de marca ou engine.

## Embedding e operações

Quem precisa embutir uma experiência web pode usar Chromium, WebView ou uma
integração baseada nas APIs da plataforma, conforme o ambiente. Blink sozinho
não oferece um navegador pronto. O produto hospedeiro precisa fornecer
processos, ciclo de vida, navegação, armazenamento, rede, permissões,
telemetria e atualizações de segurança.

A atualização deve acompanhar o ciclo do Chromium e avaliar mudanças de
compatibilidade, consumo de memória, sandbox e dependências nativas. Manter
uma fork privada aumenta o custo de aplicar correções de segurança e de
acompanhar mudanças nas especificações.

## Diagnóstico

Ao analisar uma página lenta, separe o tempo de resposta da rede do tempo de
parsing, script, layout, paint e composição. Perfis do navegador, traces de
performance e ferramentas de cobertura ajudam a localizar trabalho desnecessário
e scripts que bloqueiam a thread principal.

Em problemas de compatibilidade, compare o comportamento com Web Platform
Tests, reduza o caso a uma página mínima e verifique se a diferença está no
JavaScript, no DOM, no CSS, na renderização ou em uma política do host.

## Relações

- [V8](../v8.md) executa JavaScript e WebAssembly dentro da integração do
  Chromium.
- [WebKit](webkit.md) e [Servo](servo.md) são outras engines de navegador.
- [SpiderMonkey](../javascript/spidermonkey.md) é uma engine JavaScript usada
  pelo Firefox, não uma implementação completa de navegador.
- [JavaScript](../../../linguagens/javascript.md) explica a diferença entre a
  linguagem e as APIs fornecidas pelo host.

## Fontes primárias

- [Blink, Chromium project](https://www.chromium.org/blink/)
- [Blink source tree](https://chromium.googlesource.com/chromium/src/+/main/third_party/blink/README.md)
- [Chromium documentation](https://chromium.googlesource.com/chromium/src/+/main/docs/)
- [Web Platform Tests](https://github.com/web-platform-tests/wpt)
