# Nx

Nx é uma plataforma de monorepo com grafo de projetos, tarefas, cache e plugins para ecossistemas como JavaScript, TypeScript e outras linguagens. A ferramenta torna explícitas as dependências entre aplicações, bibliotecas e tarefas.

## Modelo

O grafo permite executar apenas projetos afetados por uma mudança. O cache pode ser local ou distribuído, e o resultado depende da definição correta das entradas, das variáveis relevantes e das saídas da tarefa.

## Quando usar

Nx se encaixa em repositórios com múltiplos projetos relacionados, convenções compartilhadas e necessidade de acelerar CI. Deve ser evitado como camada adicional quando o workspace já é pequeno e os scripts nativos são suficientes.

## Segurança e cache

Cache distribuído precisa de autenticação, escopo por repositório e política de retenção. Nunca inclua segredos nas entradas ou nas saídas cacheáveis, e valide se uma tarefa declarada como cacheável realmente é determinística.

## Relações

- [Build e toolchains](index.md) apresenta o espaço de decisão.
- [moon](moon.md) é uma alternativa independente de um ecossistema específico.
- [Turborepo](turborepo.md) concentra-se no pipeline de tarefas para JavaScript e TypeScript.

## Fonte primária

- [Nx documentation](https://nx.dev/docs)
