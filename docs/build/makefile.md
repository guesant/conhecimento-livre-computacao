# Makefile

Makefile é um arquivo declarativo que contém regras, pré-requisitos, variáveis
e receitas para um executor compatível com Make. O formato não é o mesmo que o
programa GNU Make: outras implementações podem interpretar parte da sintaxe e
divergir em extensões, funções e comportamento do shell.

## Estrutura

Uma regra associa um target a pré-requisitos e uma receita. O target normalmente
é um arquivo produzido pela receita. A existência e a data de modificação dos
pré-requisitos ajudam o executor a decidir se a saída precisa ser atualizada.

Targets de ação, como `test` e `lint`, devem ser declarados como `.PHONY` quando
não representam arquivos. Sem isso, um arquivo com o mesmo nome pode fazer o
executor considerar que a ação já foi realizada.

## Formato e limites

Makefiles misturam a linguagem de regras com a linguagem do shell que executa
cada receita. A indentação tradicional por tabulação, a expansão imediata ou
adiada de variáveis e os includes tornam a leitura sensível ao contexto. O grafo
fica frágil quando entradas descobertas dinamicamente não são declaradas.

O arquivo é apropriado quando as entradas e saídas podem ser representadas como
um grafo explícito. Ele não deve ser usado como um arquivo genérico de scripts
quando a tarefa não depende de validade incremental de artefatos.

## Relações

- [GNU Make](gnu-make.md) explica o executor, a expansão de variáveis e a
  decisão de quando executar uma receita.
- [CMake](cmake.md) pode gerar Makefiles para um projeto.
- [Ninja](ninja.md) é outro backend de execução, com um formato menor.
- [justfile](../just-executor-de-tarefas.md) organiza comandos sem modelar um
  grafo de artefatos por timestamps.
