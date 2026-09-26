# Volumes

Volumes e redundância organizam capacidade de bloco, combinam dispositivos e preservam dados contra determinados tipos de falha. A categoria não é um filesystem: ela define como blocos são reunidos, espelhados, particionados ou apresentados ao sistema operacional.

## Páginas

- [LVM](../lvm.md) fornece volumes físicos, grupos e volumes lógicos.
- [RAID](../raid.md) explica striping, espelhamento, paridade e rebuild.
- [zpool](../zpool.md) descreve a topologia de pools ZFS.
- [rpool](../rpool.md) descreve o uso de um pool ZFS para o sistema raiz.

Redundância melhora disponibilidade ou tolerância a falhas, mas não substitui backup. Um erro lógico, ransomware ou exclusão propagada pode atingir todas as cópias online. A escolha precisa considerar rebuild, monitoramento, capacidade livre, janela de reparo e recuperação testada.
