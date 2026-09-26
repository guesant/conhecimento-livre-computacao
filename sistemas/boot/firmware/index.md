# Firmware

Firmware executa antes do sistema operacional e estabelece as condições iniciais para encontrar, validar e iniciar um carregador. A categoria trata a raiz de confiança e os componentes que controlam a entrada no sistema, não as ferramentas de recuperação depois que o sistema já iniciou.

## Páginas

- [UEFI](../uefi.md) descreve a interface moderna entre firmware e sistema operacional.
- [EFI](../efi.md) explica a origem do modelo e sua terminologia.
- [BIOS](../bios.md) descreve o fluxo legado.
- [Secure Boot](../secure-boot.md) valida imagens antes da execução.
- [Chaves do Secure Boot](../secure-boot-keys.md) explica PK, KEK, db e dbx.
- [fwupd](../fwupd.md) trata atualização de firmware no Linux.

## Fronteira

Firmware e Secure Boot reduzem a chance de executar uma imagem não autorizada, mas não substituem hardening do sistema operacional, controle de credenciais, atualização de pacotes ou backup. O estado das chaves, da lista de revogação e do firmware precisa ser observado durante a manutenção.
