# CMake

CMake é um sistema de configuração e geração de build. Ele lê arquivos `CMakeLists.txt`, detecta toolchains e dependências e gera arquivos para um backend como Ninja, Make ou um ambiente de IDE.

## Modelo

CMake separa configuração de execução. `cmake -S . -B build` configura uma árvore de build e `cmake --build build` chama o backend selecionado. O diretório de build deve permanecer separado da fonte para evitar misturar cache, arquivos gerados e outputs com o código versionado.

O arquivo CMake não é necessariamente o build final. Ele descreve targets, propriedades, dependências e instalações; o generator transforma essa descrição em um grafo específico do ambiente.

## Quando usar

CMake é adequado quando o projeto precisa suportar toolchains, plataformas, IDEs ou backends diferentes. O custo é uma linguagem e um modelo de escopo próprios, que podem produzir configurações difíceis de manter quando a lógica de seleção de plataforma é acumulada sem modularização.

## Relações

- [Ninja](ninja.md) executa o grafo gerado.
- [Makefile](makefile.md) pode ser o backend Unix escolhido pelo CMake, mas não é a mesma camada.
- [LLVM](llvm.md) usa CMake como caminho principal de configuração do projeto.

## Fonte primária

- [CMake documentation](https://cmake.org/cmake/help/latest/)
