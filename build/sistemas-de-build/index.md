# Sistemas de build

Um sistema de build transforma fontes, dependências e configurações em artefatos. Ele precisa conhecer entradas, saídas, dependências e condições de invalidação para decidir o que deve ser executado. Essa responsabilidade é diferente da instalação de ferramentas e também diferente da exposição de comandos cotidianos do projeto.

## Famílias

- [Bazel](../bazel.md) modela um grafo declarativo e busca builds reprodutíveis e incrementais em escala.
- [CMake](../cmake.md) descreve projetos e gera arquivos para backends de build.
- [Meson](../meson.md) oferece uma linguagem de configuração com foco em builds rápidos e previsíveis.
- [Makefile](../makefile.md) combina regras, dependências e comandos em um formato tradicional.
- [GNU Make](../gnu-make.md) executa regras e decide quando uma receita precisa rodar.
- [Ninja](../ninja.md) executa grafos de build com uma interface pequena e otimizada.

CMake e Meson são frequentemente geradores, enquanto Ninja e Make executam regras. Bazel ocupa uma posição mais integrada, porque mantém seu próprio modelo de grafo, regras e cache. A categoria não deve ser confundida com uma ferramenta de tarefas: um `justfile` pode chamar um build, mas não precisa conhecer a validade de cada artefato.

## Critérios de escolha

Avalie tamanho do grafo, linguagens, cache local ou remoto, builds herméticos, reprodutibilidade, integração com IDEs, suporte a cross-compilation, geração de código e facilidade de depurar uma ação. Uma ferramenta que acelera o build, mas oculta entradas do grafo ou depende de estado global, pode apenas trocar tempo de execução por falhas difíceis de reproduzir.

## Relações

[Toolchains](../toolchains/index.md) trata compiladores, SDKs e ambientes de dependência. [Orquestração de monorepos](../monorepos/index.md) trata coordenação entre projetos relacionados. [justfile](../../just-executor-de-tarefas.md) trata comandos de alto nível e não substitui o grafo de artefatos.
