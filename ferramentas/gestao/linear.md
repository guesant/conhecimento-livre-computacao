# Linear

Linear é uma plataforma SaaS de gestão de produto e engenharia centrada em issues. Um workspace contém equipes; cada issue pertence a uma equipe, percorre o workflow da equipe e pode ser associada a projeto, ciclo, milestone, iniciativa, labels e relações como bloqueio ou duplicidade.

## Modelo mental

O issue é a unidade de execução. Projetos agrupam trabalho relacionado a uma entrega, milestones organizam etapas dentro de um projeto e iniciativas ficam acima dos projetos para representar objetivos mais amplos. Ciclos são períodos recorrentes de planejamento por equipe, com duração e calendário configuráveis, e não devem ser confundidos automaticamente com releases.

Essa hierarquia separa execução de estratégia. Uma issue pode ser concluída sem pertencer a uma iniciativa, enquanto uma iniciativa pode acompanhar vários projetos. Views oferecem outras perspectivas sobre os mesmos dados, sem criar uma nova cópia do trabalho.

## Workflows e ciclos

Os workflows são definidos por equipe e agrupam estados de execução. A equipe deve preferir poucos estados com significado operacional claro a uma sequência que tenta representar todos os detalhes do processo. Ciclos ajudam a criar cadência e limitar o foco de curto prazo, mas o rollover automático de itens inacabados precisa ser acompanhado para que o backlog não se torne um depósito de trabalho adiado.

Projetos e iniciativas podem receber atualizações estruturadas de saúde e progresso. Esses sinais são úteis para comunicação entre equipes, mas não substituem evidências como issues concluídas, riscos conhecidos, dependências e mudanças de escopo.

## Documentos e integrações

Documentos podem ser anexados a projetos, issues, equipes ou ciclos. Isso permite manter contexto longo próximo do trabalho sem colocar toda a decisão em comentários curtos. Integrações com repositórios e ferramentas externas relacionam commits, pull requests e incidentes às issues, mas a fonte de verdade de cada evento continua sendo o sistema que o produz.

## Quando usar

Linear faz sentido para equipes de produto e engenharia que querem uma experiência SaaS focada em velocidade de execução, workflows por equipe, ciclos recorrentes, projetos e iniciativas. Ele tende a funcionar melhor quando a organização aceita um modelo de dados relativamente opinionado e não precisa hospedar o núcleo da plataforma por conta própria.

## Limitações e riscos

O workspace, a identidade, o armazenamento e a disponibilidade dependem do serviço hospedado e do plano contratado. Antes de migrar, verifique permissões, retenção, exportação, API, webhooks, limites e como documentos e relações são preservados. A flexibilidade das views não elimina a necessidade de uma convenção para estados, prioridade, ownership e definição de pronto.

Linear também não é um substituto automático para Git, CI/CD, observabilidade ou uma base de conhecimento. As integrações devem ligar os sistemas sem duplicar manualmente o mesmo estado em vários lugares.

## Relações

- [Gestão de trabalho](index.md) explica o espaço comum às plataformas.
- [GitHub Projects](github-projects.md) é mais integrado ao modelo de issues e pull requests do GitHub.
- [Jira](jira.md) oferece uma superfície mais ampla de configuração de workflows e esquemas.
- [Azure DevOps](azure-devops.md) combina gestão de trabalho com serviços integrados de desenvolvimento.
- [Comparação entre plataformas](../../comparacoes/ferramentas/gestao-de-trabalho.md) organiza os critérios de escolha.

## Fonte primária

- [Conceptual model, Linear Docs](https://linear.app/docs/conceptual-model)
- [Cycles, Linear Docs](https://linear.app/docs/use-cycles)
- [Initiatives, Linear Docs](https://linear.app/docs/initiatives)
- [Documents, Linear Docs](https://linear.app/docs/documents)
