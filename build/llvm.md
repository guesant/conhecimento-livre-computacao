# LLVM

LLVM é uma infraestrutura modular para compiladores, linkers, analisadores e ferramentas de desenvolvimento. O projeto inclui componentes como LLVM, Clang, lld e runtimes, mas não deve ser resumido a um compilador único.

## Camadas

LLVM fornece representações intermediárias, bibliotecas e passes que podem ser usados por linguagens e toolchains diferentes. Clang é um frontend para C, C++ e outras linguagens compatíveis; lld é um linker; sanitizers e ferramentas de análise ocupam outras partes do ecossistema.

## Build

O projeto LLVM usa CMake para configurar o build e normalmente Ninja para executar o grafo. Uma configuração típica separa a fonte do diretório de build, seleciona os projetos necessários e escolhe o tipo de build. O mesmo princípio vale para projetos que consomem LLVM de forma standalone.

## Quando usar

LLVM faz sentido quando um projeto precisa de frontend, backend, representação intermediária, otimização, análise estática, instrumentação ou ferramentas de linking com uma base compartilhada. Usar LLVM não implica usar Clang como compilador nem adotar todos os projetos do monorepo.

## Relações

- [CMake](cmake.md) configura o projeto LLVM.
- [Ninja](ninja.md) executa o build comumente usado pelo projeto.
- [OSS-Fuzz](../seguranca/appsec/fuzzing/oss-fuzz.md) usa compiladores e sanitizers em campanhas de fuzzing para projetos elegíveis.

## Fonte primária

- [LLVM documentation](https://llvm.org/docs/)
