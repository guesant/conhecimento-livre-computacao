# Jira

Jira é uma plataforma de gestão de trabalho da Atlassian baseada em itens de trabalho, workflows, boards, backlogs, projetos e esquemas de configuração. O mesmo produto pode atender equipes de software e áreas não técnicas, mas o resultado depende de como tipos, estados, transições, campos e permissões são modelados.

## Modelo mental

O item de trabalho representa uma unidade rastreável, como bug, tarefa, história, feature ou epic. Um projeto ou espaço reúne trabalho, board, backlog e configurações. Boards são visualizações do trabalho, enquanto workflows definem seu ciclo de vida por meio de estados, transições, condições, validadores e ações posteriores.

A distinção entre item, board e workflow evita uma configuração comum e equivocada: tratar cada board como se fosse o processo inteiro. Um board mostra um recorte do trabalho; o workflow e os esquemas associados determinam quais transições são permitidas e o que acontece quando elas ocorrem.

## Planejamento e hierarquia

Equipes podem usar backlogs, sprints, Kanban, versões, componentes, dependências e uma hierarquia de itens. O nível de hierarquia deve corresponder a uma decisão real de planejamento. Criar epics, subtarefas e campos para todos os casos aumenta o custo de manutenção e torna relatórios menos confiáveis.

Workflows compartilhados e esquemas permitem padronizar processos entre projetos, enquanto projetos administrados de forma independente dão mais autonomia local. Essa escolha tem impacto direto em governança: uma alteração em um esquema compartilhado pode afetar muitas equipes ao mesmo tempo.

## Configuração e extensões

Jira é extensível por configurações, automações, integrações e Marketplace. Essa superfície permite adaptar o produto a processos complexos, mas cria uma obrigação de inventariar apps, permissões, webhooks, regras, campos e dependências de upgrade. Configuração que não tem dono ou documentação tende a se tornar comportamento invisível do processo.

## Quando usar

Jira é adequado quando a organização precisa de workflows configuráveis, hierarquia de trabalho, rastreabilidade, relatórios e integração com um ecossistema corporativo amplo. Ele é especialmente útil quando diferentes equipes precisam compartilhar uma plataforma, mas não necessariamente o mesmo processo.

## Limitações e riscos

A flexibilidade pode gerar excesso de tipos, estados, campos e automações. Antes de criar uma nova configuração, verifique se uma view, label, componente ou convenção existente resolve o problema. O custo real inclui administração, treinamento, governança, migração e controle de apps, além do preço da edição utilizada.

Jira não substitui automaticamente repositório, pipeline, registry, observabilidade ou documentação. A integração deve preservar links, autoria, histórico e permissões sem transformar o item de trabalho em cópia incompleta do evento original.

## Relações

- [Gestão de trabalho](index.md) define as dimensões comuns para avaliar a ferramenta.
- [Redmine](redmine.md) oferece uma base mais enxuta e extensível por plugins.
- [OpenProject](openproject.md) oferece planejamento integrado em uma opção self-hosted.
- [Linear](linear.md) é uma alternativa SaaS mais opinionada e centrada em produto e engenharia.
- [Comparação entre plataformas](../../comparacoes/ferramentas/gestao-de-trabalho.md) compara modelos e custos operacionais.

## Fonte primária

- [Como usar o Jira, Atlassian](https://www.atlassian.com/software/jira/guides/getting-started/basics)
- [Gerenciar workflows e esquemas, Atlassian Support](https://support.atlassian.com/jira-cloud-administration/docs/create-and-manage-issue-workflows-and-issue-workflow-schemes/)
