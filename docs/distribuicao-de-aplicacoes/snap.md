# Snap

Snap é um formato de aplicação e um ecossistema operado pelo `snapd`. Um snap reúne aplicação, metadados e dependências em uma revisão distribuída por canais. O daemon administra instalação, conexões de interfaces, confinamento e atualizações transacionais.

## Empacotamento e publicação

O projeto declara o conteúdo em `snapcraft.yaml`. Snapcraft usa partes, bases, plugins e um build provider para produzir o artefato em ambiente isolado. A aplicação pode ser publicada na Snap Store, em uma store privada ou em uma infraestrutura compatível, com tracks, risk levels e revisions para controlar o caminho de promoção.

O build pode usar fontes upstream, dependências do projeto e partes remotas. O mantenedor precisa fixar fontes, validar checksums quando aplicável, revisar scripts e separar build de publicação. A store não transforma código não auditado em código confiável.

## Confinamento

O modo `strict` usa mecanismos como AppArmor, seccomp, namespaces e interfaces. Interfaces conectam a aplicação a recursos do sistema com permissões declaradas. `classic` remove grande parte do isolamento e deve ser tratado como uma exceção de confiança; `devmode` é apropriado para desenvolvimento e diagnóstico, não como baseline de produção.

## Canais e atualização

Um canal combina track, risk e branch. O usuário recebe revisões conforme o canal selecionado e o `snapd` controla refreshes. A organização deve definir canais de teste, promoção, retenção, rollback e validação antes de permitir atualizações automáticas em servidores ou dispositivos.

## Limitações

O daemon, o modelo de permissões, o armazenamento de revisões e a dependência da store formam um ecossistema próprio. Isso pode ser uma vantagem para uma frota heterogênea, mas pode conflitar com políticas que exigem somente repositórios nativos, builds totalmente internos ou controle local de todos os metadados.

## Fontes primárias

- [Snap documentation](https://snapcraft.io/docs/)
- [Snapcraft setup and build provider](https://snapcraft.io/docs/snapcraft-setup/)
- [Snap confinement](https://snapcraft.io/docs/snap-confinement/)
