# Filesystems

Um filesystem organiza blocos em arquivos, diretórios, metadados, permissões e estruturas de recuperação. Alguns também oferecem checksums, snapshots, subvolumes, compressão e replicação. Essas capacidades não eliminam a necessidade de compreender o volume ou o dispositivo abaixo delas.

## Páginas

- [Btrfs](../btrfs.md) usa copy-on-write, subvolumes, checksums e send/receive.
- [XFS](../xfs.md) prioriza escalabilidade e operações journaling.
- [ZFS](../zfs.md) combina filesystem e administração de pools com checksums, datasets e snapshots.

## Critérios

Compare compatibilidade com a distribuição e o boot, consumo de memória, expansão, quotas, snapshots, ferramentas de reparo, observabilidade, desempenho e experiência da equipe. Snapshot não é backup até que exista uma cópia independente e um teste de restauração.
