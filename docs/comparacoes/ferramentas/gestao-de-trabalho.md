# Plataformas de gestão de trabalho

GitHub Projects, Linear, Jira, Azure DevOps, Redmine e OpenProject podem organizar trabalho, mas não representam a mesma decisão. A comparação precisa separar o modelo de trabalho da superfície de integração, do modo de hospedagem e do custo de governança.

## Resumo por modelo

| Plataforma | Unidade dominante | Integração principal | Hospedagem | Ponto forte |
| --- | --- | --- | --- | --- |
| GitHub Projects | Issue, pull request e draft issue | GitHub | SaaS | Planejamento próximo do código e da revisão |
| Linear | Issue, projeto, ciclo e iniciativa | Produto e engenharia | SaaS | Execução rápida com modelo opinionado |
| Jira | Item de trabalho, workflow e projeto | Ecossistema Atlassian | Cloud ou instalação conforme a edição | Workflows, esquemas e extensibilidade |
| Azure DevOps | Work item, area path e iteration path | Repos, Pipelines, testes e artefatos | Services ou Server | Integração ampla do ciclo de desenvolvimento |
| Redmine | Projeto, issue, versão e plugin | Repositórios e extensões | Self-hosted | Base enxuta e extensível |
| OpenProject | Work package, planejamento e board | Módulos de projeto e colaboração | Self-hosted, com edições distintas | Planejamento integrado e opção instalada |

## GitHub Projects ou Linear

GitHub Projects é mais natural quando issues, pull requests e permissões já estão no GitHub. A equipe ganha views e campos sem criar uma segunda fonte de verdade para o trabalho de engenharia. Linear oferece uma ontologia própria de equipes, workflows, ciclos, projetos e iniciativas, adequada quando o planejamento de produto precisa ser uma superfície independente do provedor de código.

A decisão depende de onde a equipe quer que a identidade do trabalho viva. GitHub reduz a distância entre item e mudança no repositório. Linear oferece mais estrutura de planejamento e uma experiência consistente entre equipes, mas aumenta a dependência de uma plataforma adicional.

## Jira ou Azure DevOps

Jira é mais flexível na construção de workflows, esquemas, tipos, campos, permissões e extensões. Azure DevOps é mais integrado quando Boards, Repos, Pipelines, Test Plans e Artifacts precisam participar de um mesmo conjunto operacional. Jira tende a exigir mais governança de configuração; Azure DevOps tende a exigir uma decisão mais forte sobre processos, paths, equipes e serviços do ecossistema.

Em ambientes Microsoft, Azure DevOps pode reduzir integrações entre planejamento e entrega. Em organizações com muitos fluxos distintos ou forte presença Atlassian, Jira pode acomodar melhor a variação. Nenhuma das duas opções deve ser avaliada apenas pela aparência do board.

## Redmine ou OpenProject

Redmine é menor e depende mais de plugins e convenções para ampliar seu modelo. OpenProject oferece mais módulos próprios para planejamento, boards, tempo, documentos e acompanhamento, com uma superfície operacional maior. Redmine pode ser melhor quando a equipe quer controlar uma base simples; OpenProject pode ser melhor quando os módulos integrados justificam o custo adicional.

As duas opções exigem operação de banco, anexos, autenticação, upgrades e backups. Self-hosting não significa ausência de custo, apenas desloca a responsabilidade para a organização.

## Critérios de escolha

Escolha primeiro o modelo que a equipe consegue sustentar:

- Use GitHub Projects quando o trabalho já está centrado em GitHub Issues e pull requests.
- Use Linear quando produto e engenharia precisam de ciclos, projetos e iniciativas em um workspace focado.
- Use Jira quando workflows, esquemas, permissões e integrações Atlassian são requisitos centrais.
- Use Azure DevOps quando planejamento, código, pipelines, testes e artefatos precisam de rastreabilidade integrada.
- Use Redmine quando uma base self-hosted enxuta e extensível é mais importante que módulos prontos.
- Use OpenProject quando planejamento e colaboração integrados justificam uma aplicação self-hosted mais ampla.

Depois valide exportação, permissões, auditoria, integrações, retenção, busca, notificações, API, limites, backup e recuperação. Um piloto deve incluir um fluxo completo, desde a criação do trabalho até revisão, entrega, encerramento e consulta histórica.

## Relações

- [Ferramentas de gestão de trabalho](../../ferramentas/gestao/index.md)
- [GitHub Projects](../../ferramentas/gestao/github-projects.md)
- [Linear](../../ferramentas/gestao/linear.md)
- [Jira](../../ferramentas/gestao/jira.md)
- [Azure DevOps](../../ferramentas/gestao/azure-devops.md)
- [Redmine](../../ferramentas/gestao/redmine.md)
- [OpenProject](../../ferramentas/gestao/openproject.md)

## Fontes primárias

- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [Linear conceptual model](https://linear.app/docs/conceptual-model)
- [Jira basics](https://www.atlassian.com/software/jira/guides/getting-started/basics)
- [Azure DevOps documentation](https://learn.microsoft.com/en-us/azure/devops/get-started/)
- [Redmine guide](https://www.redmine.org/guide)
- [OpenProject documentation](https://www.openproject.org/docs/)
