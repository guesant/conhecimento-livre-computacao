# Azure DevOps

Azure DevOps é um conjunto integrado de serviços para planejar trabalho, hospedar código, executar pipelines, testar e armazenar artefatos. Azure Boards é a parte dedicada ao planejamento e acompanhamento; Azure Repos, Pipelines, Test Plans e Artifacts cobrem responsabilidades relacionadas, mas cada serviço possui permissões, dados e modos de operação próprios.

## Azure Boards

Boards usa work items como unidade de rastreabilidade. Dependendo do processo escolhido, a equipe pode trabalhar com itens básicos, histórias e tarefas, ou com uma hierarquia que inclui features e epics. Work items podem ser organizados em boards, backlogs, queries, dashboards e planos de entrega.

O processo Agile, Scrum, Basic ou CMMI define tipos e comportamento inicial. Essa escolha não é apenas estética: ela influencia campos, estados, backlog, boards e relatórios. Uma personalização precisa ser tratada como uma mudança de processo, com impacto em migração, treinamento e histórico.

## Áreas e iterações

Area Paths agrupam trabalho por equipe, produto ou área funcional. Iteration Paths agrupam trabalho por sprint, release ou outro período. Ambos formam árvores e podem ser usados em filtros, ownership, permissões e relatórios.

Áreas e iterações não devem ser criadas apenas para reproduzir a estrutura organizacional inteira. Árvores excessivas dificultam permissões, queries e relatórios históricos. Alterações destrutivas em paths podem afetar gráficos e tendências, portanto a governança do modelo deve preceder a expansão.

## Integração do conjunto

O valor do Azure DevOps está na possibilidade de relacionar work items a branches, commits, pull requests, builds, releases, testes e artefatos. Essa ligação cria rastreabilidade entre intenção, implementação, validação e entrega. Ela não elimina a necessidade de definir qual sistema é fonte de verdade para cada evento.

Azure DevOps Services é hospedado pela Microsoft. Azure DevOps Server é a opção instalada e administrada pela organização, com diferenças de versão e capacidade. Em ambos os casos, a decisão precisa considerar identidade, permissões, backup, atualização, extensões e integração com o restante do ambiente.

## Quando usar

Azure DevOps é forte quando a organização já opera no ecossistema Microsoft, precisa de Boards junto com Pipelines e Repos, ou quer uma plataforma com processos, hierarquia e rastreabilidade integrados. O modelo também atende equipes que precisam de uma opção instalada por política ou requisito de isolamento, desde que aceitem a operação do servidor.

## Limitações e riscos

A integração pode concentrar muitas responsabilidades em um conjunto grande de serviços. Isso melhora a rastreabilidade, mas aumenta o impacto de permissões, indisponibilidade, migração e governança. Paths, processos, work item types, extensões e pipelines precisam de donos claros.

A ferramenta não deve ser escolhida somente porque possui mais módulos. Para uma equipe que já tem GitHub, GitLab ou outra plataforma de código e precisa apenas de um quadro simples, a superfície integrada pode custar mais do que resolve.

## Relações

- [Gestão de trabalho](index.md) explica os critérios gerais de seleção.
- [GitHub Projects](github-projects.md) é mais leve quando o trabalho já vive em GitHub Issues e pull requests.
- [Jira](jira.md) é mais orientado a workflows e esquemas configuráveis entre equipes.
- [OpenProject](openproject.md) e [Redmine](redmine.md) são alternativas self-hosted com modelos diferentes.
- [Comparação entre plataformas](../../comparacoes/ferramentas/gestao-de-trabalho.md) compara escopo e operação.

## Fonte primária

- [Azure DevOps, Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/get-started/)
- [Azure Boards, Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/boards/)
- [Planejar e acompanhar trabalho no Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work)
- [Area Paths e Iteration Paths](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/about-areas-iterations)
