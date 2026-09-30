# GNU Make

GNU Make é um executor de regras que compara targets, pré-requisitos e
timestamps para decidir quais receitas precisam ser executadas. Ele pode ser
usado diretamente como sistema de build ou como parte de uma cadeia em que uma
ferramenta de configuração gera um Makefile.

## Modelo de regras

Uma regra associa um target a pré-requisitos e a uma receita. Se um pré-requisito
é mais recente que o target, ou se o target não existe, a receita pode ser
executada. O modelo funciona melhor quando as saídas são arquivos e todas as
entradas que influenciam a saída aparecem no grafo.

Targets que representam ações, como `test` ou `lint`, normalmente não produzem
um arquivo com o mesmo nome. Eles devem ser marcados como `.PHONY` para não serem
considerados satisfeitos apenas porque existe um arquivo chamado `test`.

## Variáveis e expansão

Variáveis podem ser expandidas de forma imediata ou adiada, dependendo da forma
de atribuição. Essa diferença altera quando referências são avaliadas e pode
causar resultados surpreendentes quando uma variável depende de outra. Receitas
também são executadas por um shell separado, portanto a sintaxe de shell não é
a mesma sintaxe usada para declarar regras e dependências.

O uso de curingas, includes, variáveis de ambiente e comandos que descobrem
entradas dinamicamente pode esconder dependências do grafo. Isso prejudica
reprodutibilidade e faz uma mudança ser recompilada apenas em uma máquina que
possui um estado local específico.

## Limites e escolha

Make continua adequado para builds incrementais com arquivos, dependências
explícitas e uma topologia que a equipe consegue compreender. Arquivos muito
grandes ficam difíceis de manter por causa de tabulação, expansão de variáveis,
portabilidade do shell e regras duplicadas.

Quando o objetivo é expor comandos nomeados de lint, testes e operação, um
task runner como [justfile](../just-executor-de-tarefas.md) comunica melhor a
intenção. Quando o projeto precisa de um grafo hermético, cache remoto ou
execução distribuída, avalie ferramentas como [Bazel](bazel.md). Make não deve
ser escolhido apenas por ser conhecido se suas entradas não puderem ser
declaradas de modo confiável.

## Relações

- [Makefile](makefile.md) descreve o formato do arquivo que contém as regras.
- [CMake](cmake.md) pode gerar Makefiles para um projeto.
- [Ninja](ninja.md) ocupa uma posição semelhante como backend de execução, com
  um formato menor e otimizado para ser gerado por outra ferramenta.
- [Sistemas de build](sistemas-de-build/index.md) compara as famílias de
  ferramentas que modelam entradas, saídas e dependências.

## Fonte primária

- [GNU Make manual](https://www.gnu.org/software/make/manual/)
