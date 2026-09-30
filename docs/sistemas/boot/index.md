# Boot

Esta área reúne firmware, inicialização, instalação e recuperação. As categorias são separadas porque confiança de boot, seleção de uma fonte de instalação e reparo de um sistema já instalado possuem riscos e responsabilidades diferentes.

## Categorias

- [Firmware e confiança de boot](firmware/index.md)
- [Instalação e inicialização](instalacao/index.md)
- [Recuperação de sistemas](recuperacao/index.md)

## Firmware e confiança

[UEFI](uefi.md) define a interface moderna entre firmware e sistema operacional. [EFI](efi.md) explica a origem do modelo e a terminologia que ainda aparece em diretórios e ferramentas. [BIOS](bios.md) descreve o fluxo legado e os efeitos da compatibilidade oferecida por CSM.

[Secure Boot](secure-boot.md) valida imagens UEFI antes da execução. [Chaves e bancos do Secure Boot](secure-boot-keys.md) explica PK, KEK, db e dbx. [fwupd](fwupd.md) trata da atualização de firmware no Linux, inclusive dos fluxos que podem atualizar a lista dbx.

## Famílias de abordagem

[Métodos de boot](boot-methods.md) compara USB, disco interno, rede, mídia óptica e mídia virtual. A escolha do método é independente da ferramenta que prepara a mídia e deve ser analisada junto com o modo UEFI ou legado.

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
- A reconstrução de um cluster é um procedimento de infraestrutura, não uma mídia de boot.

## Fontes primárias

- [netboot.xyz documentation](https://netboot.xyz/docs/)
- [UEFI Forum, especificações](https://uefi.org/specifications)
- [UEFI Forum, Secure Boot e assinatura de drivers](https://uefi.org/specs/UEFI/2.10/32_Secure_Boot_and_Driver_Signing.html)
- [fwupd](https://fwupd.org/)
- [iPXE](https://ipxe.org/docs)
- [GParted Live](https://gparted.org/livecd.php)
- [Hiren's BootCD PE](https://www.hirensbootcd.org/)
- [MemTest86](https://www.memtest86.com/)
- [Memtest86+](https://memtest.org/)
