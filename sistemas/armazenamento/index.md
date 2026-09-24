# Armazenamento e filesystems

Armazenamento em Linux é composto por camadas diferentes. Um disco fornece um dispositivo de blocos, uma tabela de partições descreve regiões desse dispositivo, um gerenciador de volumes pode combinar ou recortar os blocos, um filesystem organiza arquivos e uma montagem expõe essa estrutura em um caminho.

Confundir essas camadas produz operações perigosas. LVM não é um filesystem, XFS não é um gerenciador de volumes, e um pool ZFS não é apenas uma partição. Btrfs e ZFS integram funções de filesystem e gerenciamento de armazenamento, mas continuam tendo modelos próprios para redundância, snapshots, recuperação e expansão.

## Páginas canônicas

- [LVM](lvm.md) explica volumes físicos, grupos de volumes, volumes lógicos, thin provisioning e snapshots.
- [Btrfs](btrfs.md) explica um filesystem copy-on-write com subvolumes, checksums, snapshots e send/receive.
- [XFS](xfs.md) explica um filesystem journaling orientado a escalabilidade e expansão online.
- [ZFS](zfs.md) explica a combinação entre pool, vdevs, datasets, checksums, snapshots e replicação.
- [`zpool`](zpool.md) explica a topologia e a operação dos pools ZFS.
- [`rpool`](rpool.md) explica o uso convencional de um pool ZFS para o sistema raiz e seus ambientes de boot.

## Como escolher a camada

Use uma tabela de partições e um filesystem diretamente quando a topologia for simples e a operação precisar de poucas camadas. Use LVM quando for importante redimensionar volumes lógicos, separar capacidade física de volumes consumidos e integrar o armazenamento com ferramentas tradicionais do Linux.

Considere Btrfs ou ZFS quando os requisitos incluírem checksums, snapshots integrados, replicação incremental, datasets ou administração do armazenamento como uma unidade coerente. A escolha não deve ser feita apenas pelo recurso de snapshot. É necessário avaliar memória, hardware, boot, observabilidade, ferramentas de recuperação, compatibilidade com a distribuição e experiência operacional da equipe.

## Relação com particionamento

[Ferramentas de particionamento no Linux](../../comparacoes/ferramentas/particionamento-linux.md) trata da tabela de partições e da diferença entre `cfdisk`, `fdisk`, `sfdisk`, `parted` e ferramentas gráficas. Depois da tabela, ainda é preciso decidir qual camada de volume e filesystem será colocada dentro da partição.

## Fontes primárias

- [Documentação do Btrfs](https://btrfs.readthedocs.io/)
- [Documentação XFS do kernel Linux](https://docs.kernel.org/filesystems/xfs.html)
- [OpenZFS documentation](https://openzfs.github.io/openzfs-docs/)
- [`lvm(8)` no manual do Linux](https://man7.org/linux/man-pages/man8/lvm.8.html)
