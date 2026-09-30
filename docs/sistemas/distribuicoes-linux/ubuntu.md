# Ubuntu

Ubuntu é uma distribuição baseada em Debian mantida pela Canonical e por uma comunidade ampla. O projeto publica uma edição principal e um conjunto de flavors que compartilham a base Ubuntu, mas escolhem ambientes, aplicações e objetivos diferentes.

## Flavors e edições

| Flavor ou edição | Foco |
| --- | --- |
| Ubuntu Desktop | GNOME e uma experiência geral de estação de trabalho. |
| Ubuntu Server | Serviços de servidor, automação e operação sem desktop. |
| Kubuntu | KDE Plasma e aplicações do ecossistema KDE. |
| Xubuntu | Xfce, com menor consumo e uma experiência tradicional. |
| Lubuntu | LXQt, voltado a hardware mais modesto. |
| Ubuntu MATE | MATE, com uma interface clássica e configurável. |
| Ubuntu Budgie | Budgie, com foco em simplicidade e integração visual. |
| Ubuntu Studio | Produção de áudio, vídeo, gráficos e criação de conteúdo. |
| Ubuntu Cinnamon | Cinnamon como desktop principal. |
| Edubuntu | Educação e ambientes de aprendizagem. |
| Ubuntu Unity | Unity como desktop principal. |
| Ubuntu Kylin | Experiência orientada ao público chinês. |
| Ubuntu Core | Sistema transacional e imutável para dispositivos e edge. |
| Ubuntu Cloud e imagens de servidor | Imagens para nuvens, máquinas virtuais e automação. |

As flavors de desktop não são apenas temas. Elas definem seleção de pacotes, defaults, instalador e integração com o ambiente. Consulte a página oficial de flavors antes de assumir que toda flavor recebe exatamente o mesmo conjunto de suporte.

## Lançamento e suporte

Há releases intermediárias a cada seis meses. As releases LTS aparecem a cada dois anos, em abril de anos pares. Uma release intermediária recebe suporte por um período curto; a LTS é a escolha usual para servidores porque mantém a base por vários anos. O Ubuntu Pro estende a cobertura de segurança para mais pacotes e oferece suporte comercial opcional, conforme o produto e a assinatura contratada.

## Bugs e CVEs

A Canonical publica Ubuntu Security Notices e mantém correções por release e pacote. A equipe pode fazer backport de correções para preservar a estabilidade da LTS. Bugs gerais são reportados pelos canais Ubuntu e Launchpad; o canal correto depende de o problema estar na distribuição, na flavor ou no projeto upstream.

## Segurança e defaults

Ubuntu instala e carrega AppArmor por padrão. Perfis podem ser fornecidos pelos próprios pacotes e verificados com `aa-status`. SELinux existe no ecossistema Ubuntu, mas AppArmor é a política MAC esperada no baseline padrão.

O servidor SSH depende da imagem e do instalador. Desktop normalmente não instala o daemon SSH sem solicitação, enquanto imagens de servidor e cloud podem instalá-lo ou configurá-lo via cloud-init. O primeiro usuário administrativo costuma receber acesso a `sudo`; `umask`, login de root e autenticação por senha devem ser verificados na imagem efetiva, não presumidos pelo nome Ubuntu.

## Empacotamento

O sistema base usa pacotes `.deb`, `dpkg` e `apt`. A Canonical publica source packages, compila binários em builders do Launchpad e distribui os artefatos por arquivos APT com metadados e assinaturas. PPAs recebem source packages e fazem o build para as séries e arquiteturas suportadas pelo PPA.

Snaps formam um segundo ecossistema de distribuição, com confinamento e atualização próprios. Um snap não deve ser tratado como apenas outra forma de instalar o mesmo `.deb`: o formato, o canal, a revisão e o modelo de permissões são diferentes.

## Suporte

O suporte comunitário inclui documentação, fóruns, Ask Ubuntu, Launchpad e canais de desenvolvimento. O suporte comercial é oferecido pela Canonical por meio de Ubuntu Pro, contratos e serviços relacionados. Uma flavor pode ter uma comunidade própria sem oferecer um SLA independente.

## Fontes primárias

- [Ubuntu releases](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)
- [Ubuntu release cycle](https://ubuntu.com/about/release-cycle)
- [Ubuntu flavors](https://ubuntu.com/desktop/flavours)
- [Ubuntu security updates](https://documentation.ubuntu.com/security/security-updates/)
- [Ubuntu Launchpad packaging](https://ubuntu.com/docs/launchpad/user/reference/packaging/)
