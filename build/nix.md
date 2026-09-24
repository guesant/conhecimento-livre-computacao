# Nix

Nix é um gerenciador funcional de pacotes e uma linguagem para descrever pacotes e ambientes reprodutíveis. Deriva caminhos de store a partir das entradas da construção, permitindo que versões diferentes convivam no mesmo host.

## Modelo

Uma derivação declara fontes, dependências, ferramentas e comandos de build. O resultado é colocado no Nix store e pode ser reutilizado quando as entradas são iguais. Flakes são uma convenção moderna para entradas versionadas, composição e comandos reproduzíveis.

## Quando usar

Nix é adequado quando a reprodução de toolchains, ambientes de desenvolvimento e builds entre máquinas é uma prioridade. A curva de aprendizagem da linguagem, do store e do garbage collector precisa ser aceita pelo time.

## Operação

O store deve ter política de retenção e garbage collection. Em CI, use caches de artefatos com autenticação e limites, mas preserve a capacidade de reconstruir o resultado a partir das entradas declaradas. Separe canais e revisões de inputs para evitar atualizações acidentais.

## Relações

- [Build e toolchains](index.md) reúne alternativas.
- [Hermit](hermit.md) é mais simples quando apenas algumas CLIs precisam ser fixadas.
- [Bazel](bazel.md) concentra-se na execução e no cache do grafo de build.

## Fontes primárias

- [Nix manual](https://nixos.org/manual/nix/stable/)
- [Nix flakes](https://nixos.wiki/wiki/Flakes)
