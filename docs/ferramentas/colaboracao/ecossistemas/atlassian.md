# Atlassian

Atlassian é uma empresa e um ecossistema de produtos para desenvolvimento,
gestão de trabalho, colaboração, conhecimento e operação de serviços. Jira,
Confluence e Bitbucket são produtos relacionados, mas não são camadas
intercambiáveis de uma mesma aplicação.

## Fronteiras dos produtos

Jira acompanha trabalho, incidentes, projetos e workflows. Bitbucket hospeda
Git e revisão de código. Confluence organiza páginas, espaços, decisões e
conhecimento. Os produtos podem trocar links, eventos, identidade e contexto,
mas cada um tem seu próprio modelo de dados, permissões e histórico.

Essa separação é útil para escolher uma arquitetura de ferramentas. Uma equipe
pode usar Bitbucket sem Confluence, Confluence sem Bitbucket ou integrar ambos
ao Jira. Centralizar identidade não significa centralizar a responsabilidade
editorial, o backup ou a autorização dos dados.

## Administração

A administração de uma organização precisa tratar usuários, grupos, domínios,
autenticação, aplicações instaladas, tokens, OAuth, webhooks e auditoria. Uma
integração entre produtos deve ter um proprietário, escopo mínimo e um caminho
de revogação. Quando um usuário deixa a organização, a remoção precisa alcançar
todos os produtos e integrações, não apenas o diretório principal.

## Cloud e autogerenciamento

Os produtos possuem modalidades hospedadas e, conforme o produto e a edição,
opções autogerenciadas. A comparação precisa incluir ciclo de vida, limites,
exportação, residência de dados, suporte, backups e custo de operação. A
promessa de uma suíte integrada não remove a necessidade de restaurar cada tipo
de dado separadamente.

## Quando usar

O ecossistema Atlassian é adequado quando o valor está na integração entre
planejamento, código e conhecimento. Ele pode ser desnecessário para um projeto
pequeno que só precisa de Git e revisão. Também pode exigir governança forte em
organizações grandes, pois a proliferação de projetos, espaços, campos,
automações e apps torna permissões e retenção difíceis de manter.

## Relações

- [Bitbucket](../forjas/bitbucket.md) é a forge do ecossistema.
- [Confluence](confluence.md) é a camada de conhecimento.
- [Ferramentas de gestão de trabalho](../index.md) compara Jira com outras
  formas de organizar execução.

## Fontes

- [Atlassian](https://www.atlassian.com/)
- [Atlassian Cloud platform](https://www.atlassian.com/software)
- [Atlassian Administration](https://support.atlassian.com/organization-administration/)
