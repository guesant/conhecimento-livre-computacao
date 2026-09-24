# Ninja

Ninja é um sistema de build pequeno e rápido, orientado à execução de um grafo já descrito. Seus arquivos `build.ninja` normalmente são gerados por CMake, Meson ou outra ferramenta de configuração, em vez de escritos manualmente.

## Modelo

O gerador decide quais comandos, dependências e outputs existem. Ninja calcula o que precisa ser refeito e executa tarefas independentes em paralelo. O formato reduz trabalho de interpretação e mantém o executor focado na atualização correta dos artefatos.

## Quando usar

Ninja é adequado como backend de projetos grandes ou de builds frequentes, especialmente quando a configuração já é gerenciada por CMake ou Meson. Ele não tenta substituir a camada que descreve opções de plataforma, descoberta de dependências ou targets de alto nível.

## Limitações

Escrever `build.ninja` manualmente pode ser apropriado para casos pequenos, mas transfere ao autor a responsabilidade por gerar todas as dependências corretas. Ninja também não é um task runner para comandos administrativos sem outputs; para isso, [just](../just-executor-de-tarefas.md) tem uma semântica mais direta.

## Relações

- [CMake](cmake.md) e [Meson](meson.md) são geradores comuns.
- [LLVM](llvm.md) normalmente é configurado com CMake e executado com Ninja.

## Fonte primária

- [Ninja manual](https://ninja-build.org/manual.html)
