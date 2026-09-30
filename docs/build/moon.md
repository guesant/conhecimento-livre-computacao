# moon

moon é uma ferramenta de orquestração de tarefas e projetos para monorepos. Ela combina configuração de projetos, tarefas, toolchains e cache para executar somente o trabalho necessário.

## Modelo

Cada projeto declara tarefas e dependências. O grafo permite executar tarefas em paralelo e reutilizar saídas quando as entradas relevantes não mudaram. O ganho depende de entradas bem definidas e de tarefas sem efeitos colaterais ocultos.

## Quando usar

moon é interessante para monorepos com várias aplicações e linguagens, quando uma convenção central reduz scripts repetidos. Um repositório simples pode obter resultado semelhante com `just`, `make` ou o gerenciador nativo da linguagem.

## Operação

Fixe a versão da ferramenta, mantenha as configurações revisáveis e diferencie cache de dependências de cache de artefatos. Não compartilhe credenciais de publicação com o processo que apenas calcula tarefas.

## Relações

- [Build e toolchains](index.md) reúne alternativas.
- [Nx](nx.md) e [Turborepo](turborepo.md) resolvem problemas semelhantes em monorepos JavaScript.
- [Bazel](bazel.md) oferece um modelo de build mais geral e rigoroso.

## Fonte primária

- [moon documentation](https://moonrepo.dev/docs)
