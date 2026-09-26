# Arch Linux

Arch Linux é uma distribuição rolling, minimalista e orientada a usuários que querem montar o sistema de acordo com suas necessidades. A instalação oficial entrega uma base; desktop, serviços e políticas adicionais são escolhas do operador.

## Flavors e ecossistema

Arch não possui flavors oficiais como Ubuntu. GNOME, KDE Plasma, Xfce, sway, Hyprland e outros ambientes são pacotes ou composições instalados sobre a mesma base. Imagens e distribuições derivadas podem oferecer instaladores ou defaults diferentes, mas não são releases oficiais do Arch.

O Arch User Repository, AUR, é uma coleção comunitária de receitas de build. Um pacote no AUR não recebe automaticamente a mesma validação, assinatura ou responsabilidade dos repositórios oficiais.

## Lançamento e suporte

Não há releases periódicas. Atualizações contínuas substituem a migração entre versões. O suporte é comunitário, com destaque para ArchWiki, fóruns, listas e canais do projeto. Consultoria externa é possível, mas não há uma assinatura central de suporte empresarial fornecida pelo Arch Project.

## Bugs e CVEs

O projeto publica notícias, atualiza os repositórios e mantém um Security Tracker. A política rolling entrega correções rapidamente, mas pode exigir intervenção manual quando uma mudança incompatível precisa de ação do administrador. Leia as notícias antes de atualizações relevantes e não faça atualizações parciais.

## Segurança e defaults

Arch instala uma base mínima e não habilita AppArmor ou SELinux como política MAC universal. O usuário escolhe o mecanismo, os perfis, o firewall, o daemon SSH e o modelo de autorização. Uma instalação sem `openssh-server` ou `sudo` é normal; uma instalação que os adiciona precisa definir explicitamente chaves, grupos, login de root e autenticação.

`umask` vem das configurações de shell, PAM ou service manager e não deve ser presumida pelo sistema base. A responsabilidade de construir uma baseline segura é maior porque o Arch não escolhe um desktop ou uma coleção completa de serviços pelo operador.

## Empacotamento

Arch usa `pacman` e pacotes `pkg.tar.zst`. Mantenedores mantêm receitas `PKGBUILD`; `makepkg` ou as ferramentas de build oficiais produzem os pacotes, e os repositórios oficiais publicam artefatos assinados. `pacman` exige assinaturas para os repositórios oficiais conforme `SigLevel`.

O AUR distribui receitas, não uma garantia de binários oficiais. Antes de executar um `PKGBUILD`, revise fontes, patches, comandos de build e scripts de instalação. Um pacote criado localmente deve ser assinado e distribuído por um repositório sob controle do operador se for usado em mais de uma máquina.

## Fontes primárias

- [Arch Linux](https://archlinux.org/about/)
- [Arch Linux Wiki](https://wiki.archlinux.org/title/Arch_Linux)
- [Arch Linux news](https://archlinux.org/news/)
- [Arch security tracker](https://security.archlinux.org/)
