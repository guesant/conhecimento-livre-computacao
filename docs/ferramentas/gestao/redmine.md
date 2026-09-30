# Redmine

Redmine é uma aplicação web de gestão de projetos com projetos, issues, versões, roadmap, wiki, documentos, repositórios e plugins. A unidade central é o projeto, que organiza membros, permissões e os artefatos de trabalho associados.

## Quando usar

Redmine é adequado quando a equipe quer um sistema relativamente enxuto, extensível por plugins e orientado a issues e projetos. A flexibilidade do ecossistema permite adaptar workflows, mas também torna a governança de plugins e upgrades parte do custo operacional.

## Fronteira

Redmine não é um sistema de CI/CD, um registry ou um substituto para Git. Ele pode integrar esses serviços e registrar referências de trabalho, mas cada sistema continua responsável pelo seu próprio estado e pela sua segurança.

## Operação

Anexos, banco, plugins e versões do Ruby fazem parte do backup e da atualização. Antes de instalar um plugin, verifique compatibilidade com a versão do Redmine, manutenção upstream e comportamento em migrações de schema.

## Relações

- [OpenProject](openproject.md) é uma alternativa com outra base de funcionalidades e governança.
- [Comparação entre Redmine e OpenProject](../../comparacoes/ferramentas/redmine-openproject.md) organiza os critérios de escolha.

## Fonte primária

- [Redmine guide](https://www.redmine.org/guide)
