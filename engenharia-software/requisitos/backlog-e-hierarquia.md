# Backlog e hierarquia de trabalho

Backlog é uma coleção ordenada de oportunidades, problemas, riscos, requisitos e trabalho
técnico. Ele não é um depósito de todas as ideias já mencionadas. Um item precisa ter contexto,
responsável por decidir, estado de descoberta, prioridade suficiente para comparação e um
próximo passo claro.

## Níveis de trabalho

Não existe uma hierarquia universal. Os nomes mudam entre Scrum, XP, SAFe, Azure Boards, Jira,
GitHub Projects e outras ferramentas. Uma composição comum é útil para comunicação, mas deve
ser adotada como convenção explícita.

| Nível | Responsabilidade típica | Pergunta |
| --- | --- | --- |
| Theme ou objetivo | Direção ou problema estratégico | Que resultado amplo importa? |
| Initiative | Investimento que pode reunir frentes | Qual mudança estratégica será perseguida? |
| Epic | Corpo grande de valor ou hipótese ainda ampla | Que resultado exige decomposição? |
| Capability | Capacidade de produto ou plataforma | Que capacidade precisa existir? |
| Feature | Entrega compreensível como valor ou comportamento | Que parte utilizável será disponibilizada? |
| User story | Necessidade de uma pessoa ou papel | Que usuário precisa fazer o quê e por quê? |
| Task | Trabalho técnico ou operacional para entregar um item | Que ação precisa ser realizada? |
| Subtask | Parte pequena de uma task ou story | Qual divisão local ajuda a executar? |

Epic pode significar uma user story grande ou um tipo hierárquico específico da ferramenta.
Feature pode significar capacidade de produto, item de backlog ou a palavra-chave do Gherkin.
Use as definições do processo local e registre a equivalência antes de migrar dados entre
ferramentas.

## Feature em três contextos

`Feature` não tem um único significado.

1. Em BDD e Gherkin, `Feature` agrupa cenários sobre uma capacidade ou comportamento.
2. Em produtos, feature costuma ser uma capacidade percebida pelo usuário ou operador.
3. Em SAFe e em algumas ferramentas, Feature é um nível formal entre Epic e Story ou entre
   outros níveis de planejamento.

Esses significados podem se relacionar, mas não devem ser misturados automaticamente. Uma
feature de backlog pode possuir cenários Gherkin. Isso não significa que cada cenário seja uma
feature, nem que o campo `Feature` de uma ferramenta tenha exatamente o mesmo ciclo de vida do
keyword do Gherkin.

## User story

Uma user story é uma promessa de conversa sobre uma necessidade e seu valor, não um contrato
completo escrito sem interação. O formato "Como um papel, quero capacidade, para obter valor"
ajuda a lembrar usuário e resultado, mas não substitui exemplos, regras, dependências,
restrições e critérios de aceite.

Uma story saudável deve ser pequena o bastante para ser entendida, refinada, construída e
avaliada em uma cadência razoável. Divida por comportamento, regra, fluxo ou valor, não somente
por camadas técnicas como frontend, backend e banco. Uma divisão técnica pode ser uma task
quando existe um item de valor maior que a justifica.

## Definition of Ready e Definition of Done

Uma equipe pode usar uma Definition of Ready para indicar que um item tem contexto suficiente
para entrar em execução. Ela não deve virar burocracia que bloqueia aprendizado. A Definition of
Done descreve condições para considerar o resultado concluído, incluindo código, revisão, testes,
segurança, documentação, observabilidade, migração e suporte quando aplicável.

Critérios de aceite respondem se o comportamento está correto. Definition of Done responde se o
incremento está pronto segundo o acordo de qualidade da equipe. São complementares.

## Ferramentas e modelos

| Plataforma ou método | Como costuma representar trabalho |
| --- | --- |
| Azure Boards | Work items, processos configuráveis, áreas, iterações, backlogs, Features e Epics conforme o processo |
| Jira | Issues, workflows, Epic e itens padrão; níveis adicionais dependem da configuração e do plano |
| SAFe | Hierarquia e governança em escala, com Portfolio, Solution, Program e Team Backlogs e papéis próprios |
| Scrum | Product Backlog como lista ordenada; não exige tipos chamados Epic ou Feature |
| XP | Histórias e práticas de engenharia, com menor ênfase em uma taxonomia hierárquica fixa |
| GitHub Projects | Issues, pull requests, campos, views e automações, com hierarquia geralmente modelada por links e convenções |

Uma ferramenta não deve impor mais níveis que a decisão precisa. Se a equipe não consegue dizer
qual informação cada nível comunica, a hierarquia está adicionando custo sem aumentar clareza.

## Refinamento e fluxo

Refinamento é o trabalho contínuo de aprender o suficiente para ordenar e executar itens. Ele
inclui dividir, esclarecer, estimar quando útil, descobrir dependências, revisar risco e
descartar hipóteses. Não transforme todo backlog em especificação detalhada com meses de
antecedência.

Limite trabalho em progresso. Um backlog curto e ordenado é mais útil que milhares de itens
sem decisão. Separe ideias, oportunidades em descoberta, itens prontos, trabalho em andamento,
bloqueios e itens concluídos. Registre quando um item foi rejeitado ou arquivado para não
reapresentar a mesma hipótese sem aprendizado novo.

## Rastreabilidade sem acoplamento excessivo

Relacione iniciativa, item de valor, critérios, implementação, pull request, teste, release e
resultado quando essa ligação ajudar uma decisão. Não crie links apenas para preencher campos.
Uma relação deve permitir encontrar contexto, evidência, impacto ou responsável.

## Fontes e referências

- [Scrum Guide](https://scrumguides.org/download.html)
- [Agile Alliance, Epic](https://agilealliance.org/glossary/epic/)
- [Atlassian, epics e histórias](https://www.atlassian.com/agile/project-management/epics-stories-themes)
- [Cucumber, User Story](https://cucumber.io/docs/terms/user-story/)
- [Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/)
- [SAFe](https://scaledagileframework.com/)
