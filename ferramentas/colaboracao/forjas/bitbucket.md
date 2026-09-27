# Bitbucket

Bitbucket é a forge da Atlassian para repositórios Git. O Bitbucket Cloud
oferece repositórios, branches, pull requests, issues, wikis, webhooks e
Bitbucket Pipelines. O produto também se integra ao Jira, ao Confluence e à
administração de organizações da Atlassian.

## Modelo

O workspace organiza usuários, grupos e repositórios. Pull requests concentram
revisão, comentários, verificações e merge. Pipelines executam etapas definidas
no repositório e podem publicar artefatos ou acionar serviços externos.

A integração com Jira permite relacionar branches, commits e pull requests a
itens de trabalho. Essa conveniência depende de identidade, chaves de projeto,
permissões e convenções de nomenclatura coerentes. A integração não deve ser a
única fonte de verdade do release: o pipeline precisa produzir evidências
reprodutíveis e o repositório precisa continuar sendo recuperável sem a UI.

## Cloud e Data Center

Bitbucket Cloud é um serviço hospedado com cobrança e limites administrados pela
Atlassian. A opção Data Center atende cenários autogerenciados da organização,
com custo operacional próprio para disponibilidade, upgrades, banco, storage,
backup e integração com identidade. As capacidades, limites e ciclo de vida
devem ser conferidos na documentação da edição utilizada.

## Integrações e segurança

Aplicações instaladas podem usar scopes, OAuth, webhooks e APIs. Conceda apenas
as permissões necessárias e revise integrações antigas. Um app que lê todos os
repositórios ou escreve em branches protegidas é uma identidade de produção,
não apenas uma extensão visual.

Proteja branches, exija revisão e verificação de pipeline, trate variáveis
secretas como credenciais e limite runners. Para código de terceiros, prefira
execução isolada sem acesso a secrets de produção.

## Quando usar

Bitbucket faz sentido para organizações que já usam Jira, Confluence e
administração Atlassian, e querem reduzir o trabalho de integração entre código
e planejamento. Para uma plataforma DevSecOps mais abrangente, compare GitLab.
Para uma instalação pequena e autogerenciada, compare Gitea e Forgejo.

## Relações

- [Forjas de código](index.md) explica as capacidades comuns.
- [Atlassian](../ecossistemas/atlassian.md) descreve o ecossistema que integra
  Bitbucket, Jira e Confluence.
- [Confluence](../ecossistemas/confluence.md) trata a camada de conhecimento.

## Fontes

- [Get started with Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/)
- [Set up your repositories](https://support.atlassian.com/bitbucket-cloud/docs/set-up-your-repositories/)
- [Bitbucket Cloud apps](https://support.atlassian.com/bitbucket-cloud/docs/bitbucket-cloud-apps-overview/)
