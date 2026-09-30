# OpenProject

OpenProject é uma aplicação web de gestão de projetos que reúne work packages, planejamento, boards, tempo, documentos, wiki e recursos relacionados a colaboração e acompanhamento. Seus módulos atendem desde fluxos ágeis até planejamento mais estruturado.

## Quando usar

OpenProject faz sentido quando a equipe precisa de uma superfície mais ampla de planejamento e acompanhamento, com módulos integrados e uma edição self-hosted. A escolha deve considerar a distinção entre recursos disponíveis na edição comunitária e recursos dependentes de edição comercial.

## Fronteira

Ele não substitui o repositório de código, o sistema de entrega ou o armazenamento de artefatos. Integrações podem conectar issues, commits e pipelines, mas o estado operacional de cada integração precisa continuar observável no sistema que o produz.

## Operação

Instalação, upgrades, armazenamento de anexos, banco, autenticação e edição licenciada precisam ser tratados como uma aplicação com estado. Backups devem incluir o banco e os arquivos que não podem ser reconstruídos a partir do código.

## Relações

- [Redmine](redmine.md) atende uma fronteira semelhante com outra abordagem de extensibilidade.
- [Comparação entre Redmine e OpenProject](../../comparacoes/ferramentas/redmine-openproject.md) apresenta critérios comuns.

## Fonte primária

- [OpenProject documentation](https://www.openproject.org/docs/)
