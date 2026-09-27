# Gitea

Gitea é uma forge de código leve e autogerenciada. Ela reúne hospedagem Git,
revisão, issues, organizações, registry de pacotes e uma solução de CI baseada
em Gitea Actions. O objetivo é entregar as capacidades essenciais de uma forge
sem exigir a escala operacional de uma plataforma de ciclo de vida completa.

## Modelo

O repositório é associado a um usuário ou organização, e equipes recebem
permissões sobre os repositórios. Pull requests, issues, branches protegidas,
webhooks e releases ficam próximos do histórico Git. O Package Registry pode
servir diferentes formatos de pacotes e imagens OCI, dependendo da configuração
e da versão instalada.

Gitea Actions usa runners separados. Um runner executa código definido por
workflows, portanto não deve ser compartilhado entre projetos com níveis de
confiança incompatíveis. Um runner com acesso a secrets ou ao socket do
container pode transformar uma alteração de workflow em acesso ao ambiente.

## Autogerenciamento

Uma instalação precisa de banco, armazenamento para repositórios e anexos,
configuração de SSH e HTTP, envio de e-mail, backup e atualização. O processo
é adequado para uma organização pequena, um laboratório ou uma rede que precisa
manter o código sob seu próprio domínio. A operação deixa de ser simples quando
há muitos runners, grandes volumes de artefatos, alta disponibilidade ou
integrações corporativas complexas.

O backup deve incluir o banco, os repositórios, anexos, configuração e secrets.
Um dump do banco sem os repositórios não recupera o conteúdo; um espelho Git sem
o banco não recupera issues, revisão, usuários ou permissões.

## Quando usar

Gitea faz sentido quando baixo consumo, controle da instalação e simplicidade
de migração pesam mais que um catálogo amplo de recursos corporativos. Para
projetos públicos de software livre, compare também uma instância comunitária
de Forgejo, como Codeberg, com uma instalação própria.

## Relações

- [Forjas de código](index.md) apresenta o modelo comum.
- [Codeberg](codeberg.md) é um serviço comunitário baseado em Forgejo, que é
  uma alternativa da mesma família de forjas leves.
- [GitLab](gitlab.md) cobre uma plataforma mais integrada de DevSecOps.

## Fontes

- [What is Gitea?, documentação do Gitea](https://docs.gitea.com/1.23/)
- [Gitea Actions](https://docs.gitea.com/usage/actions/overview/)
- [Package Registry](https://docs.gitea.com/usage/packages/overview/)
