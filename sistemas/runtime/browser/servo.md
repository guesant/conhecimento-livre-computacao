# Servo

Servo é uma engine de navegador escrita em Rust, desenvolvida como um projeto
modular e embutível. O projeto explora uma arquitetura com segurança de memória,
paralelismo e componentes que podem ser usados para construir experiências web
em desktops, dispositivos móveis e sistemas embarcados. Servo não é uma
distribuição de navegador pronta equivalente ao Firefox, Safari ou Chromium.

## O que Servo fornece

Uma engine de navegador precisa lidar com documentos, estilos, layout, script,
renderização e integração com APIs web. Servo organiza essas responsabilidades
em componentes que podem ser executados por um host. A API de WebView e as
interfaces de embedding permitem que uma aplicação use a engine sem precisar
adotar a interface completa de um navegador.

A composição exata e a cobertura de padrões evoluem com o projeto. Antes de
adotar Servo, verifique a compatibilidade da versão desejada com HTML, CSS,
JavaScript, WebAssembly, mídia, acessibilidade, rede e APIs específicas do seu
produto.

## Rust e segurança de memória

O uso de Rust reduz classes de erros de memória em componentes escritos nessa
linguagem, como acessos fora dos limites e use-after-free que seriam possíveis
em uma implementação manual insegura. Isso não elimina bugs de lógica,
validação insuficiente, falhas de protocolo ou vulnerabilidades em código
unsafe, bibliotecas nativas e integrações do host.

A segurança completa continua dependendo do isolamento de processos, sandbox,
origem, permissões, atualização de dependências e exposição de APIs. Uma engine
memory-safe não torna automaticamente seguro um aplicativo que disponibiliza
uma função nativa perigosa para qualquer página.

## Paralelismo e arquitetura

Servo foi projetado para explorar paralelismo em partes do processamento de
documentos e estilos. O benefício depende da carga, da granularidade do
trabalho, da sincronização e do hardware. Paralelismo pode aumentar throughput,
mas também introduz custos de coordenação, memória e depuração.

O modelo operacional deve separar o trabalho da engine do ciclo de vida do
host. Rede, armazenamento, janelas, eventos, logs, permissões e atualizações
não devem ser presumidos apenas porque a engine consegue renderizar uma página.

## Embedding

Um aplicativo que embute Servo escolhe as superfícies web que expõe, conecta a
engine a uma janela ou superfície gráfica e define políticas para rede,
certificados, cookies, armazenamento e scripts. O host deve controlar ciclo de
vida, cancelamento, limites de recursos e telemetria.

A existência de uma API de WebView não significa que qualquer página web ou
aplicação complexa funcionará sem adaptação. Teste os fluxos reais, inclusive
fontes, mídia, acessibilidade, entrada do usuário, navegação, downloads e
autenticação.

## Compatibilidade e maturidade

Servo é útil para investigar arquiteturas de engine, integrar uma solução
embutida e avaliar componentes escritos em Rust. A escolha exige verificar a
profundidade de implementação dos padrões necessários e a disponibilidade de
integrações para o sistema alvo.

Quando compatibilidade ampla com o ecossistema web é o requisito principal,
Chromium ou WebKit podem oferecer uma superfície mais madura para uma
plataforma específica. Isso não torna Servo inferior em todos os cenários: o
trade-off depende do controle desejado, do tamanho do produto, da linguagem,
da segurança de memória, do modelo de embedding e da capacidade de manter a
integração.

## Desempenho e diagnóstico

Meça separadamente carregamento, parsing, script, estilo, layout, pintura,
composição, memória e chamadas entre o host e a engine. O paralelismo não deve
ser avaliado apenas pelo tempo total; observe também latência, consumo de CPU,
pressão de memória, sincronização e previsibilidade.

Ao reduzir um problema, mantenha uma página mínima e registre a versão do
Servo, o sistema operacional, o backend gráfico, os recursos habilitados e as
APIs do host. Essa informação é necessária para distinguir um defeito na
engine de uma diferença na integração.

## Governança e fontes

Servo é um projeto open source com governança associada à Linux Foundation
Europe. O código, as metas e as instruções de contribuição devem ser consultados
na fonte oficial antes de escolher uma versão para produção. A disponibilidade
de uma funcionalidade deve ser confirmada no código e na documentação da
versão utilizada, não apenas em uma descrição geral do projeto.

## Relações

- [Blink](blink.md) é a engine de navegador integrada ao Chromium.
- [WebKit](webkit.md) é a engine usada pelo Safari e por outras aplicações.
- [SpiderMonkey](../javascript/spidermonkey.md) é uma engine JavaScript, não
  uma engine completa de navegador.
- [Rust](../../../linguagens/rust.md) explica a linguagem usada na implementação
  de Servo.

## Fontes primárias

- [Servo](https://servo.org/)
- [Servo Book](https://book.servo.org/)
- [Servo source repository](https://github.com/servo/servo)
- [Servo project organization](https://github.com/servo)
