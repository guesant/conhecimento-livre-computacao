# Bazel

Bazel é um sistema de build baseado em grafo, com regras explícitas, cache de artefatos e execução distribuída. Ele foi projetado para repositórios grandes em que reexecutar tudo a cada mudança seria caro.

## Modelo

Um workspace declara targets e dependências em arquivos `BUILD`. As regras descrevem entradas, ferramentas e saídas, e o Bazel calcula quais ações precisam ser executadas. A reprodutibilidade depende de toolchains, ambientes e regras herméticas, não apenas da presença de um compilador no host.

## Quando usar

Bazel é adequado quando há várias linguagens, dependências entre projetos e benefício mensurável de cache local ou remoto. Para um projeto pequeno, a modelagem das regras e a manutenção das toolchains podem custar mais do que o tempo economizado.

## Operação

Fixe versões de toolchains, separe cache de execução de artefatos publicáveis e trate credenciais de cache como segredos. Valide as regras em CI e defina limites de armazenamento para evitar que o cache remoto cresça sem controle.

## Relações

- [Build e toolchains](index.md) apresenta a categoria.
- [Nix](nix.md) pode fornecer ambientes reprodutíveis para toolchains.
- [Hermit](hermit.md) fixa ferramentas de desenvolvimento sem exigir uma instalação global.

## Fonte primária

- [Bazel documentation](https://bazel.build/docs)
