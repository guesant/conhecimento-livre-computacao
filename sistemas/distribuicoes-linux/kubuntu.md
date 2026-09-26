# Kubuntu

Kubuntu é uma flavor oficial do Ubuntu que usa KDE Plasma como ambiente de desktop principal e integra aplicações do ecossistema KDE. A base de distribuição, o instalador e o ciclo geral vêm do Ubuntu, enquanto a experiência visual e parte da seleção de software vêm do projeto Kubuntu/KDE.

## Lançamento e suporte

Kubuntu acompanha a cadência Ubuntu: releases intermediárias a cada seis meses e LTS a cada dois anos. O suporte de uma instalação deve ser analisado pela versão Ubuntu usada, pelo status da flavor e pelos pacotes KDE envolvidos.

O projeto Kubuntu é predominantemente comunitário. A Canonical oferece suporte comercial ao Ubuntu e a produtos associados, mas isso não significa que toda customização KDE receba automaticamente um SLA separado. Para ambientes corporativos, valide o escopo da subscrição e as certificações necessárias.

## Bugs e CVEs

Falhas podem estar no packaging da flavor, no KDE Plasma, no Ubuntu ou em uma aplicação específica. O reporte deve preservar essa distinção. Atualizações de segurança seguem os repositórios Ubuntu e os avisos dos projetos upstream, normalmente com backports para a release suportada.

## Segurança e defaults

Kubuntu herda o baseline Ubuntu, incluindo AppArmor quando a imagem o carrega. A troca do desktop para KDE Plasma não troca automaticamente o MAC, a política de sudo, o PAM, o SSH ou a `umask`.

Em uma instalação desktop, `openssh-server` normalmente precisa ser instalado quando o acesso remoto é desejado. O usuário criado pelo instalador pode receber `sudo`; root, senha, chaves e exposição do daemon devem ser revisados antes de usar a máquina como servidor.

## Empacotamento

Kubuntu usa `.deb`, `apt` e `dpkg`. Pacotes da base vêm dos archives Ubuntu; pacotes e integrações da flavor são construídos e publicados pelo fluxo Ubuntu/Kubuntu, com metadados APT e assinaturas. O KDE upstream continua sendo a origem de parte importante do código e das correções.

A forma correta de atribuir uma CVE ou um bug é separar o componente: Ubuntu, packaging Kubuntu, Qt, Plasma ou aplicação KDE. Isso evita esperar que uma equipe corrija um problema que pertence a outra camada.

## Fonte primária

- [Kubuntu](https://kubuntu.org/)
- [Obter Kubuntu](https://kubuntu.org/getkubuntu/)
- [Kubuntu FAQ](https://kubuntu.org/faq/)
