# Build

Um build de software combina pelo menos três responsabilidades: descrever entradas e dependências, decidir quais saídas precisam ser atualizadas e executar compiladores, linkers ou geradores. Essas responsabilidades podem viver em uma ferramenta única ou em camadas diferentes. Esta página organiza o domínio e encaminha cada responsabilidade para sua categoria.

## Categorias

- [Sistemas de build](sistemas-de-build/index.md) tratam entradas, saídas, dependências e execução incremental.
- [Toolchains](toolchains/index.md) tratam compiladores, SDKs, linkers e ambientes de desenvolvimento.
- [Orquestração de monorepos](monorepos/index.md) trata a coordenação entre projetos e tarefas relacionadas.

[CMake](cmake.md) e [Meson](meson.md) descrevem o projeto e geram arquivos para um backend. [Ninja](ninja.md) executa um grafo de build de forma rápida e previsível. [Makefile](makefile.md) descreve o formato das regras e [GNU Make](gnu-make.md) executa esse modelo. [justfile](../just-executor-de-tarefas.md) é um arquivo de receitas para comandos, não um sistema de build baseado em timestamps.

[LLVM](llvm.md) é uma infraestrutura de compiladores e ferramentas, não um build system. Ele pode ser compilado usando CMake e Ninja e pode servir de toolchain para projetos que escolhem Clang, LLVM libc ou outras partes do ecossistema.

## Como escolher

Comece pela pergunta de execução. Se é necessário recalcular somente saídas desatualizadas, dependências e artefatos, escolha um build system. Se a necessidade é oferecer comandos previsíveis para lint, testes, geração ou operação, escolha um task runner. Se a preocupação é compilar ou analisar uma linguagem, escolha uma toolchain.

Uma composição comum usa CMake ou Meson para gerar Ninja, o Ninja para executar o grafo e um `justfile` para expor comandos de alto nível. Cada camada precisa continuar explicando seu próprio contrato, em vez de esconder toda a lógica em scripts sem dependências declaradas.
