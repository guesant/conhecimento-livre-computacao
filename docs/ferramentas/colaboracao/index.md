# Ferramentas de colaboração

Ferramentas de colaboração para software combinam, em proporções diferentes,
repositórios Git, revisão de código, issues, automação, pacotes, documentação
e comunicação. A semelhança da interface não significa que todas sejam a mesma
categoria de produto.

Uma forge de código hospeda repositórios e organiza o fluxo de contribuição em
torno de branches, commits, pull requests ou merge requests. Uma plataforma de
gestão pode acompanhar trabalho sem hospedar o código. Um wiki ou workspace de
conhecimento resolve outro problema: preservar decisões, procedimentos e
informação contextual que não cabe no histórico de commits.

## Categorias

### Forjas

As [forjas de código](forjas/index.md) são o ponto de entrada para repositórios,
revisão, issues e automação associada ao ciclo de desenvolvimento. [Gitea](forjas/gitea.md)
é uma opção leve e autogerenciada. [GitLab](forjas/gitlab.md) integra o ciclo de
vida em uma plataforma mais ampla. [Codeberg](forjas/codeberg.md) oferece uma
instância comunitária baseada em Forgejo. [SourceForge](forjas/sourceforge.md)
combina hospedagem e distribuição de software com um diretório público. [Bitbucket](forjas/bitbucket.md)
é a forge da Atlassian, com integração especialmente estreita ao Jira e ao
ecossistema Atlassian.

### Ecossistema Atlassian

O [Atlassian](ecossistemas/atlassian.md) é um ecossistema de produtos, não uma
forge isolada. O [Confluence](ecossistemas/confluence.md) é seu workspace de
conhecimento e documentação. Jira, Bitbucket e Confluence podem compartilhar
identidade, links, permissões e automações, mas continuam tendo modelos de
dados diferentes.

## Critérios de escolha

Escolha primeiro a fronteira de responsabilidade. Para hospedar código e
revisões, compare Git, permissões, merge requests, CI, registry, runners,
integrações e possibilidade de migração. Para conhecimento, compare busca,
hierarquia, histórico, revisão editorial, permissões, exportação e retenção.

Em uma instalação autogerenciada, inclua no custo o banco de dados, anexos,
objetos grandes, busca, runners, atualização, backup, restauração, identidade,
saída de e-mail e resposta a incidentes. Em um serviço hospedado, avalie limites
de uso, residência de dados, dependência da conta, portabilidade e políticas de
retenção.

## Fontes

- [GitLab Docs](https://docs.gitlab.com/)
- [Gitea Documentation](https://docs.gitea.com/)
- [Codeberg Documentation](https://docs.codeberg.org/)
- [SourceForge](https://sourceforge.net/about)
- [Atlassian](https://www.atlassian.com/)
