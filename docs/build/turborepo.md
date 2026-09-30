# Turborepo

Turborepo é um sistema de build incremental para monorepos JavaScript e TypeScript. Ele usa um grafo de tarefas e cache para evitar reconstruir projetos cujas entradas não mudaram.

## Modelo

As tarefas são declaradas no `turbo.json`, com dependências entre tarefas, entradas e saídas. A ferramenta pode executar tarefas em paralelo e usar cache local ou remoto. A qualidade do resultado depende da precisão dessas declarações.

## Quando usar

Turborepo é uma escolha direta para workspaces que já usam npm, pnpm ou yarn e precisam coordenar aplicações e pacotes. Não é um substituto geral para um sistema de build nativo de C++, Java ou do kernel.

## Limitações

Uma tarefa com saída incompleta, dependência ambiental omitida ou efeito externo não declarado pode produzir um cache incorreto. Revise a lista de outputs e não armazene tokens, arquivos de configuração secretos ou resultados dependentes de credenciais.

## Relações

- [Build e toolchains](index.md) apresenta alternativas.
- [Nx](nx.md) oferece um grafo mais abrangente de projetos e plugins.
- [Bazel](bazel.md) aplica um modelo de regras e hermeticidade mais amplo.

## Fonte primária

- [Turborepo documentation](https://turborepo.com/docs)
