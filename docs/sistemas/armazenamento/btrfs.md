# Btrfs

Btrfs é um filesystem copy-on-write para Linux. Ele combina organização de arquivos com recursos de gerenciamento de armazenamento, como subvolumes, snapshots, checksums, scrub, send/receive e perfis de múltiplos dispositivos.

O modelo não é equivalente a colocar ext4 ou XFS em um volume lógico. O filesystem administra estruturas internas que podem abranger vários dispositivos, e a capacidade, a redundância e os snapshots precisam ser compreendidos no nível do filesystem.

## Modelo mental

Um filesystem Btrfs pode conter subvolumes independentes dentro da mesma estrutura. Um subvolume tem uma árvore de arquivos própria e pode ser montado separadamente. Um snapshot é uma visão copy-on-write de um subvolume em um ponto do tempo. Os blocos compartilhados deixam de ser comuns quando uma das visões é alterada.

Checksums de dados e metadados ajudam a detectar corrupção silenciosa. Detectar um erro não significa que exista uma cópia íntegra disponível para repará-lo. A capacidade de recuperação depende do perfil de armazenamento, da redundância e da existência de backup externo.

## Subvolumes e snapshots

Subvolumes permitem separar raiz, dados, logs e estados que precisam de políticas diferentes. Um snapshot não deve ser tratado como backup independente: ele compartilha blocos com a origem e desaparece junto com o filesystem se o dispositivo for perdido.

Comandos de inspeção:

```sh
sudo btrfs filesystem show
sudo btrfs filesystem usage /mountpoint
sudo btrfs subvolume list /mountpoint
```

Os subcomandos exatos para criar, montar e remover snapshots devem ser incorporados ao procedimento da distribuição, com uma política explícita de retenção. Snapshots acumulados consomem espaço e podem tornar a limpeza mais difícil do que a criação.

## Integridade e manutenção

O scrub lê os dados e verifica os checksums. Em uma configuração com cópias suficientes, ele pode reparar blocos corrompidos a partir de outra cópia. Execute scrub como manutenção planejada e monitore o resultado, em vez de tratá-lo como uma operação ocasional depois de um incidente.

Balance reorganiza alocações internas e não deve ser executado como rotina indiscriminada. Ele pode consumir I/O e tempo sem resolver o problema que motivou a execução. Investigue primeiro a utilização com `btrfs filesystem usage`.

Não use `btrfs check --repair` como primeira tentativa. O modo de reparo pode agravar uma corrupção. Preserve uma imagem ou cópia do dispositivo e siga a documentação da versão instalada antes de qualquer reparo offline.

## Vários dispositivos e RAID

Btrfs possui perfis para dados e metadados, e esses perfis não precisam ser iguais. A redundância efetiva depende do perfil escolhido, do número de dispositivos e da distribuição atual dos chunks. Um filesystem com dois discos não é automaticamente tolerante a qualquer falha.

Antes de alterar um perfil, verifique a documentação da versão do kernel e do utilitário Btrfs. Perfis RAID com limitações conhecidas não devem ser avaliados somente pelo nome. Capacidade útil, comportamento durante falha, reconstrução, estado dos metadados e possibilidade de substituição precisam entrar na decisão.

## Send e receive

Btrfs send/receive transforma a diferença entre snapshots em um fluxo que pode ser aplicado em outro filesystem Btrfs. Isso é útil para replicação incremental, mas não elimina a necessidade de testar a restauração e validar a ordem das dependências entre snapshots.

## Quando usar

Btrfs é interessante quando subvolumes, snapshots, checksums e replicação incremental são requisitos de primeira classe. Ele exige disciplina para retenção, scrub, balance, capacidade e escolha de perfis. Para um filesystem tradicional com expansão online e poucas funções integradas, XFS pode ser mais simples. Para pools com topologia de vdevs e administração integrada, ZFS oferece outro modelo.

## Relações

- [LVM](lvm.md) fornece volumes lógicos abaixo de filesystems tradicionais, enquanto Btrfs integra funções diferentes em uma única camada.
- [XFS](xfs.md) prioriza um modelo de filesystem tradicional, com journaling e expansão online.
- [ZFS](zfs.md) também combina filesystem e gerenciamento de armazenamento, mas usa pools e vdevs.
- [Ferramentas de particionamento no Linux](../../comparacoes/ferramentas/particionamento-linux.md) trata a tabela de partições anterior ao filesystem.

## Fontes primárias

- [Documentação oficial do Btrfs](https://btrfs.readthedocs.io/)
- [Btrfs administration](https://btrfs.readthedocs.io/en/latest/Administration.html)
- [Btrfs send and receive](https://btrfs.readthedocs.io/en/latest/Send-receive.html)
