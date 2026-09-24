# Makefile e GNU Make

GNU Make é um executor de regras que compara timestamps e dependências para decidir quais targets precisam ser refeitos. O `Makefile` é o arquivo que declara essas regras, variáveis e comandos.

## Modelo

Uma regra associa um target a pré-requisitos e a uma receita. Se um pré-requisito é mais recente ou o target não existe, a receita pode ser executada. Esse modelo funciona bem quando as saídas são arquivos e as dependências estão declaradas com precisão.

Receitas que representam comandos, como `test` ou `lint`, normalmente não produzem um arquivo com o mesmo nome. Elas precisam ser marcadas como `.PHONY` para não serem confundidas com targets satisfeitos por um arquivo existente.

## Limitações

O uso de tabulação na receita, a expansão de variáveis e a diferença entre shell e sintaxe do Make tornam arquivos grandes difíceis de manter. Quando o objetivo é apenas expor comandos nomeados, [just](../just-executor-de-tarefas.md) comunica melhor a intenção. Quando o objetivo é construir artefatos incrementais, Make continua sendo um modelo válido.

## Relações

- [CMake](cmake.md) pode gerar Makefiles.
- [Ninja](ninja.md) ocupa a mesma posição de backend, com um formato otimizado para ser gerado por outra ferramenta.

## Fonte primária

- [GNU Make manual](https://www.gnu.org/software/make/manual/)
