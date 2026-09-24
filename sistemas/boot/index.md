# Instalação, boot e recuperação

Esta área reúne técnicas que executam antes do sistema operacional normal ou que inicializam um ambiente temporário para reparar armazenamento, testar hardware e reinstalar a máquina.

## Famílias de abordagem

[Instalação pela rede](network-install.md) explica a cadeia de boot, DHCP, TFTP, HTTP, PXE e iPXE. [netboot.xyz](netboot-xyz.md) é uma implementação prática que oferece um menu de instaladores e utilitários pela rede.

[Mídias live](gparted-live.md) e [Hiren's BootCD PE](hirens-bootcd-pe.md) carregam um ambiente temporário sem depender da instalação principal. [MemTest86 e Memtest86+](memtest.md) iniciam um teste especializado de memória, fora do sistema operacional.

[Ventoy](ventoy.md), [Rufus](rufus.md), [balenaEtcher](balena-etcher.md), [YUMI](yumi.md), [dd](dd.md), [Media Creation Tool](media-creation-tool.md) e [UNetbootin](unetbootin.md) são ferramentas para preparar mídias, mas não resolvem o mesmo problema. Algumas gravam uma imagem inteira, outras mantêm várias imagens e outras são específicas do instalador Windows.

## Escolha rápida

| Problema | Primeira ferramenta |
| --- | --- |
| Instalar sistemas repetidamente | PXE, iPXE ou netboot.xyz |
| Particionar ou mover volumes | GParted Live, com backup confirmado |
| Recuperar um Windows que não inicia | Hiren's BootCD PE e ferramentas específicas |
| Suspeita de memória defeituosa | MemTest86 ou Memtest86+ |
| Host remoto sem sistema operacional | BMC, console virtual ou boot de rede |

Nenhuma mídia live substitui backup. Uma ferramenta de recuperação que enxerga o disco tem permissão para alterar ou destruir seus dados.

## Relações

- [Gerenciamento de hardware](../hardware/index.md) trata BMC, IPMI e acesso remoto.
- [Backup e recuperação](../../confiabilidade/backup/index.md) define objetivos e validação.
- [Reconstrução de cluster](../../reconstrucao-de-cluster-single-node-e-recuperacao-de-segredos.md) é um procedimento de infraestrutura, não uma mídia de boot.

## Fontes primárias

- [netboot.xyz documentation](https://netboot.xyz/docs/)
- [GParted Live](https://gparted.org/livecd.php)
- [Hiren's BootCD PE](https://www.hirensbootcd.org/)
- [MemTest86](https://www.memtest86.com/)
- [Memtest86+](https://memtest.org/)
