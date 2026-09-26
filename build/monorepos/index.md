# Orquestração de monorepos

Um monorepo guarda vários projetos relacionados em um único repositório. A orquestração de monorepo decide quais projetos precisam ser construídos, testados ou publicados quando uma mudança ocorre e como tarefas independentes podem ser executadas em paralelo.

## Implementações

- [Nx](../nx.md) constrói um grafo de projetos e oferece cache, geração e coordenação de tarefas.
- [Turborepo](../turborepo.md) coordena tarefas de workspaces com foco em cache e execução incremental.
- [moon](../moon.md) combina configuração de projetos, toolchains e tarefas em um workspace.

Essas ferramentas não são equivalentes a CMake, Make ou Ninja. Elas podem chamar esses sistemas, mas o objeto principal é a relação entre projetos e tarefas do repositório. Também não substituem a política de dependências, o sistema de build de cada linguagem ou o pipeline de publicação.

## Riscos

Cache incorreto, detecção incompleta de dependências e scripts com efeitos colaterais produzem builds verdes que não representam o estado real do código. O cache deve ser invalidado por todas as entradas relevantes, incluindo configuração, versão da toolchain, variáveis que afetam o resultado e arquivos gerados.

## Escolha

Compare tamanho do workspace, linguagens, integração com o gerenciador de pacotes, suporte a cache remoto, observabilidade das tarefas, isolamento e facilidade de remover a ferramenta depois. Um monorepo pequeno pode precisar apenas de scripts e um build system convencional.
