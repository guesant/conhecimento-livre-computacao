# Meson

Meson é um sistema de build que descreve projetos em arquivos `meson.build` e gera um backend de execução. Ele prioriza configuração rápida, sintaxe declarativa e detecção explícita de fontes, dependências e alvos.

## Modelo

O comando `meson setup build` configura um diretório separado da árvore de fontes. Depois, `meson compile -C build` delega a execução ao backend, normalmente Ninja. Essa separação evita misturar arquivos gerados com código-fonte e facilita manter configurações diferentes para debug, release e cross-compilation.

Meson não é o compilador. Ele resolve a descrição do projeto, verifica dependências e produz o grafo que será executado por uma ferramenta de backend.

## Quando usar

Meson é uma opção forte para projetos nativos que valorizam configuração curta, builds fora da árvore e integração com compiladores e bibliotecas de sistemas diferentes. A escolha ainda deve considerar o ecossistema já existente, a disponibilidade de módulos e a necessidade de consumir projetos que exportam CMake ou Makefiles.

## Relações

- [Ninja](ninja.md) é o backend mais comum.
- [CMake](cmake.md) resolve uma fronteira semelhante com outra linguagem e outro modelo de geração.
- [LLVM](llvm.md) é uma toolchain que pode ser compilada com Meson em projetos que ofereçam essa integração, embora o projeto LLVM use CMake como caminho principal.

## Fonte primária

- [Meson Build System](https://mesonbuild.com/)
