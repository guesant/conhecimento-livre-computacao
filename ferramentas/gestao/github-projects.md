# GitHub Projects

GitHub Projects é a camada de planejamento e acompanhamento integrada ao GitHub. Um projeto reúne issues, pull requests e rascunhos em uma superfície que pode ser apresentada como tabela, quadro ou roadmap. O projeto pode estar associado a uma conta pessoal, organização ou repositório, enquanto os itens continuam relacionados aos objetos de trabalho do GitHub.

## Modelo mental

O item principal pode ser uma issue ou pull request já existente, ou um draft issue que ainda não foi convertido em uma issue. O projeto acrescenta campos, visualizações, filtros, agrupamentos e automações sem criar uma cópia independente do estado do item. Alterar campos compatíveis pela visão do projeto também atualiza o objeto de origem.

Esse vínculo é importante para evitar duas fontes de verdade. O código, a revisão e a discussão continuam no repositório e no pull request. O projeto oferece uma perspectiva de planejamento, triagem, priorização e acompanhamento.

## Visualizações e campos

Uma mesma coleção pode ter visualizações diferentes para perguntas diferentes. A tabela favorece triagem e edição densa, o quadro favorece fluxo por estado e o roadmap favorece datas e planejamento temporal. Filtros, ordenação, agrupamento e campos personalizados permitem representar prioridade, esforço, prazo, iteração ou outro metadado que não exista no modelo padrão de issues.

Campos precisam ser poucos e semanticamente estáveis. Um campo de prioridade deve ter uma definição que a equipe consiga aplicar de forma consistente; criar um campo para cada exceção apenas transfere a desordem para a configuração do projeto. Também é preciso acompanhar o limite de campos e o efeito de campos obrigatórios sobre automações e importações.

## Automação

Projects oferece automações internas para preencher campos, arquivar itens e adicionar itens que atendam a critérios. GitHub Actions e a API GraphQL permitem integrar a gestão com validações e eventos do repositório. Automação não deve substituir o workflow de revisão: ela deve reduzir trabalho mecânico e deixar o histórico de mudança compreensível.

## Quando usar

GitHub Projects é uma escolha natural quando o código, as issues e os pull requests já estão no GitHub e a equipe quer uma camada de planejamento com pouca separação operacional. Ele funciona bem para backlog, triagem, roadmap de repositório e acompanhamento de iniciativas menores sem introduzir outra plataforma de identidade e integração.

## Limitações e riscos

O modelo é fortemente acoplado ao GitHub. Isso reduz a duplicação quando a equipe já está no ecossistema, mas aumenta a dependência da plataforma e não transforma Projects em uma ferramenta self-hosted independente. Organizações com portfólios complexos, processos regulatórios, múltiplas fontes de código ou planejamento financeiro podem precisar de outra camada.

A flexibilidade também exige governança. Defina quem pode criar projetos, campos, views e automações; estabeleça convenções para estados e labels; e teste a exportação dos dados necessários. Uma visão filtrada não é um backup nem substitui o histórico de issues e pull requests.

## Relações

- [Gestão de trabalho](index.md) explica as dimensões comuns às plataformas.
- [Jira](jira.md) oferece workflows, esquemas e hierarquias mais configuráveis.
- [Linear](linear.md) organiza issues, projetos, ciclos e iniciativas em um workspace próprio.
- [Azure DevOps](azure-devops.md) integra Boards com repositórios, pipelines, testes e artefatos.
- [Comparação entre plataformas](../../comparacoes/ferramentas/gestao-de-trabalho.md) coloca as alternativas na mesma matriz.

## Fonte primária

- [About Projects, GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [Customizing views in your project, GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project)
- [Understanding fields, GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields)
