# Filesystems

Filesystem é o formato e o conjunto de estruturas que organizam dados em um volume. Disco, tabela de partição, volume e filesystem são camadas diferentes.

| Camada | Responsabilidade |
| --- | --- |
| Disco | Dispositivo físico ou virtual que armazena blocos. |
| Tabela de partição | Divide o disco em regiões, como GPT ou MBR. |
| Partição | Região descrita pela tabela de partição. |
| Volume | Espaço lógico apresentado a um filesystem, podendo vir de LVM, Storage Spaces, RAID ou outro agregador. |
| Filesystem | Estruturas, metadados, permissões e dados usados para organizar arquivos. |
| Diretório raiz | Ponto inicial da árvore de nomes daquele filesystem ou namespace. |

Uma partição pode conter diretamente um filesystem ou uma camada intermediária. Um volume lógico pode conter ext4, XFS, NTFS ou outro filesystem. Um mount pode apresentar uma árvore remota ou virtual sem corresponder a uma partição local.

## Linux

[Filesystems Linux](linux-filesystems.md) compara ext4, XFS, Btrfs, ZFS, tmpfs, procfs e sysfs. Linux normalmente expõe uma única árvore `/`, formada pela montagem do filesystem raiz e de outros filesystems em pontos como `/boot`, `/home`, `/var` e `/run`.

## Windows

[Filesystems Windows](windows-filesystems.md) compara NTFS, ReFS, FAT32, exFAT e UDF. [Organização de diretórios](diretorios.md) explica letras de unidade, volumes, caminhos UNC, junctions, symlinks e a relação com a árvore POSIX.

## Compatibilidade

Suporte de leitura e escrita depende do driver, do kernel, da versão do sistema, das permissões e das ferramentas. Um filesystem pode ser montável em mais de um sistema sem oferecer a mesma semântica de ACL, locks, links, case sensitivity, xattrs ou recuperação.

## Fonte primária

- [Microsoft local file systems](https://learn.microsoft.com/en-us/windows/win32/fileio/file-systems)
- [Linux filesystems documentation](https://www.kernel.org/doc/html/latest/filesystems/)
