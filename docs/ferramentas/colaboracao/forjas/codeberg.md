# Codeberg

Codeberg é uma plataforma comunitária e sem fins lucrativos operada pela
Codeberg e.V. e baseada em Forgejo. Ela oferece hospedagem pública de projetos,
issues, pull requests, wiki, páginas estáticas e serviços relacionados ao
desenvolvimento de software livre.

## Codeberg não é Forgejo

Forgejo é o software livre autogerenciável que implementa uma forge. Codeberg
é um serviço operado pela comunidade que usa Forgejo e mantém serviços e
políticas próprias. É possível instalar Forgejo em outra infraestrutura sem
estar usando Codeberg; também é possível migrar um projeto de Codeberg para
outra instância Forgejo.

Essa distinção importa para portabilidade. O software da forge e a política do
provedor são camadas diferentes. Uma instância pode ter regras de retenção,
limites, autenticação, Pages, CI e suporte diferentes de outra, mesmo usando o
mesmo software base.

## Uso em projetos livres

Codeberg é voltado a projetos de software livre e a uma operação comunitária.
Além do repositório, a plataforma oferece issue tracking, pull requests, wiki
e Codeberg Pages. Pages pode publicar um site de usuário, organização ou
repositório por webhook ou por um workflow de CI.

A comunidade e a sustentabilidade financeira fazem parte do modelo. Antes de
usar o serviço como única cópia de um projeto importante, mantenha espelhos
Git, exporte dados relevantes e verifique como recuperar issues, anexos e
configurações específicas da plataforma.

## Segurança

Ative autenticação de dois fatores, use chaves SSH ou tokens com escopo mínimo e
revise quem possui acesso administrativo à organização. Workflows e webhooks
devem ser tratados como código executável, mesmo em um projeto público. Não
coloque secrets em um repositório público nem assuma que o nome público do
projeto seja uma barreira de segurança.

## Relações

- [Forjas de código](index.md) explica a categoria.
- [Gitea](gitea.md) é outra forge leve, enquanto Codeberg é um serviço
  comunitário baseado em Forgejo.
- [SourceForge](sourceforge.md) tem uma ênfase maior em distribuição e
  descoberta pública de software.

## Fontes

- [What is Codeberg?](https://docs.codeberg.org/getting-started/what-is-codeberg/)
- [Getting Started with Codeberg](https://docs.codeberg.org/getting-started/)
- [Codeberg Pages](https://docs.codeberg.org/codeberg-pages/)
