# Lua

Lua é uma linguagem de script dinâmica, leve e embutível. A implementação
oficial é escrita em C e pode ser usada como biblioteca dentro de outro
programa. O host cria um estado de execução, carrega código, registra funções
nativas e decide quais recursos o script pode acessar.

Essa característica faz Lua aparecer em jogos, ferramentas de configuração,
automação, servidores embutidos e aplicações que precisam de extensibilidade.
O interpretador standalone é apenas um host fornecido pela distribuição; a
linguagem não exige que exista um processo principal próprio.

## Modelo da linguagem

Lua é dinamicamente tipada. Valores carregam seu tipo e podem ser armazenados,
passados e retornados como valores de primeira classe. Os tipos básicos incluem
`nil`, booleanos, números, strings, funções, userdata, threads e tabelas.

Tabelas são a principal estrutura de dados da linguagem. Uma tabela pode
representar um array, um mapa, um registro, um conjunto, uma árvore ou um
objeto. Essa flexibilidade simplifica configurações e APIs, mas exige
convenções claras quando o programa cresce.

Metatables e metamethods permitem definir operações para tabelas e userdata.
Eles podem fornecer uma forma de orientação a objetos, sobrecarga de operações,
proxies e comportamento de índices. Como esse mecanismo é dinâmico, uma equipe
deve limitar convenções implícitas e testar os caminhos que dependem dele.

## Execução e memória

O código Lua é compilado para bytecode e executado por uma máquina virtual
baseada em registradores. A linguagem possui gerenciamento automático de
memória, com modos incremental e generational no Lua 5.4. O garbage collector
reduz a necessidade de liberar objetos manualmente, mas não fecha
automaticamente todos os recursos externos do host.

Arquivos, conexões, handles e objetos C precisam de uma política explícita de
finalização. Tabelas globais, closures e caches também podem manter dados vivos
por mais tempo que o esperado. Em aplicações com restrições de latência, meça
alocações, ciclos de coleta e tamanho das estruturas, em vez de alterar os
parâmetros do GC por tentativa.

## Coroutines

Coroutines são unidades cooperativas de execução. Uma coroutine pode ceder
explicitamente e ser retomada depois, mas não é automaticamente uma thread do
sistema operacional. Elas são úteis para iteradores, pipelines, servidores e
protocolos que alternam entre operações sem bloquear o fluxo principal.

Coroutines não criam paralelismo por si só. Para usar vários núcleos, o host
precisa fornecer processos, threads ou outra forma de execução paralela e
definir como estados e erros serão compartilhados.

## Embedding e segurança

O host pode registrar funções C e userdata para expor recursos especializados.
Essa ponte é também a fronteira de segurança. Validar argumentos, limitar
tempo de execução, restringir memória e evitar funções nativas perigosas é
responsabilidade da aplicação que incorpora Lua.

Executar texto vindo de terceiros no mesmo processo não é uma sandbox de
segurança. Para conteúdo não confiável, combine uma API mínima com isolamento
de processo, permissões reduzidas, limites de recursos e uma política de
atualização das bibliotecas C.

## Escolha

Lua é adequada quando tamanho, simplicidade de embedding, inicialização rápida
e controle da API exposta são importantes. O custo está na tipagem dinâmica,
na necessidade de estabelecer convenções de projeto e no ecossistema menor que
o de runtimes generalistas de servidor.

Use o Lua oficial quando a compatibilidade com a linguagem e a biblioteca C
forem prioritárias. Variantes como LuaJIT podem oferecer desempenho diferente,
mas introduzem um ciclo de compatibilidade próprio. A escolha deve considerar
versão da linguagem, suporte a arquitetura, garbage collection e bindings
usados pelo host.

## Relações

- [JavaScript](javascript.md) também é usado como linguagem embutida, mas possui
  outro modelo de objetos, bibliotecas e ecossistema.
- [QuickJS](../sistemas/runtime/javascript/quickjs.md) é outra engine pequena
  para incorporar uma linguagem de script.
- [Rust](rust.md), [Go](go.md) e [D](d.md) são alternativas compiladas para
  componentes nativos, com outros modelos de memória e integração.

## Fontes primárias

- [Lua 5.4 Reference Manual](https://www.lua.org/manual/5.4/manual.html)
- [Lua official site](https://www.lua.org/)
- [Programming in Lua](https://www.lua.org/pil/)
