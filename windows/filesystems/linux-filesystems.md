# Filesystems Linux

## ext4

ext4 é um filesystem de propósito geral muito usado em instalações Linux. Ele oferece journaling, permissões Unix, ACLs, extended attributes, quotas e expansão online em cenários suportados. É uma escolha conservadora quando compatibilidade e ferramentas de recuperação são prioridades.

## XFS

XFS é um filesystem journaling orientado a escalabilidade, arquivos grandes e paralelismo. Ele é comum em servidores e ambientes empresariais. Seu modelo de expansão é forte, mas reduzir um filesystem XFS não é a operação simples que muitos administradores esperam de um volume.

## Btrfs

Btrfs combina filesystem copy-on-write, subvolumes, checksums, snapshots e send/receive. Isso permite políticas de rollback e replicação integradas, mas exige disciplina com snapshots, capacidade, scrub e perfis de múltiplos dispositivos.

## ZFS

ZFS combina filesystem e pool de armazenamento, com datasets, vdevs, checksums, snapshots, clones e replicação. Ele não é apenas outro filesystem para uma partição: o administrador precisa entender a topologia do pool e os limites do sistema operacional e da distribuição.

## Filesystems virtuais

`tmpfs` representa memória e swap como uma árvore temporária. `procfs`, `sysfs` e `cgroupfs` expõem interfaces de kernel, dispositivos, processos e controles. Eles não devem ser tratados como armazenamento persistente.

## Organização de montagem

Linux usa uma árvore única. `/` é o filesystem raiz; outros filesystems aparecem como subdiretórios montados. `/run` é estado runtime, `/proc` e `/sys` são interfaces do kernel, `/dev` expõe dispositivos e `/etc`, `/var`, `/home` e `/usr` têm responsabilidades operacionais distintas. A divisão exata depende da distribuição e do layout escolhido.

## Fontes primárias

- [Linux kernel filesystem documentation](https://www.kernel.org/doc/html/latest/filesystems/)
- [ext4 kernel documentation](https://www.kernel.org/doc/html/latest/filesystems/ext4/index.html)
- [XFS documentation](https://docs.kernel.org/filesystems/xfs.html)
