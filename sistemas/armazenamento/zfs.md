# ZFS

ZFS é um sistema de armazenamento que combina filesystem, gerenciamento de pools, checksums, snapshots, clones, quotas, compressão e replicação. Em vez de separar obrigatoriamente a tabela de partições, um gerenciador de volumes e um filesystem, ZFS organiza o armazenamento em pools e vdevs e expõe datasets e zvols.

O modelo mental é:

```text
discos ou partições -> vdevs -> zpool -> datasets ou zvols -> montagem ou consumidor de blocos
```

O pool administra a capacidade e a redundância. Datasets são filesystems ZFS com propriedades próprias. Zvols são dispositivos de blocos apresentados pelo ZFS para consumidores que precisam dessa interface.

## Integridade e cópia sob escrita

ZFS calcula checksums dos blocos e verifica esses checksums durante leituras e scrubs. Quando a topologia possui outra cópia íntegra, o sistema pode reparar o bloco corrompido. Sem redundância ou backup, checksum detecta o erro mas não inventa uma cópia correta.

Snapshots são visões copy-on-write de datasets. Clones são datasets graváveis derivados de snapshots. `zfs send` e `zfs receive` podem transportar snapshots completos ou incrementais para outro pool, mas o fluxo precisa preservar a cadeia de snapshots e ser validado por restaurações reais.

## Topologia

A redundância pertence ao vdev, não é aplicada livremente a cada disco depois que o pool foi criado. Um pool pode conter vdevs do tipo mirror, RAIDZ ou disco único, mas misturar topologias altera capacidade, desempenho e comportamento de falha.

Um pool com vdevs inadequados pode continuar online e ainda assim não oferecer o nível de proteção esperado. Avalie quantidade de discos, tolerância a falhas, tempo de reconstrução, capacidade útil, latência e possibilidade de substituição antes de criar o pool.

## Datasets e propriedades

Datasets permitem separar políticas de compressão, quota, reservation, recordsize, deduplicação, montagem e outras propriedades. Essa separação é uma das razões para não colocar todo o sistema em um único filesystem lógico.

Propriedades alteram comportamento e consumo de recursos. Deduplicação, por exemplo, exige avaliação de memória e do padrão de dados. Compressão costuma ter benefícios diferentes conforme o conteúdo. Não habilite propriedades globais sem medir o workload.

## Operação

Comandos de inspeção comuns incluem:

```sh
zpool status
zpool list
zfs list
zfs get all pool/dataset
```

Scrub verifica a integridade dos dados e pode reparar cópias quando a topologia permite. Substituição, importação, exportação e expansão exigem procedimentos próprios e não devem ser executadas apenas porque um comando aparece em um exemplo.

ZFS também tem requisitos de integração com kernel, distribuição e boot. Em Linux, use a documentação do OpenZFS e os pacotes compatíveis com a versão do sistema. Não transfira automaticamente um procedimento de Solaris para Linux ou o inverso.

## Quando usar

ZFS é adequado quando integridade ponta a ponta, pools, datasets, snapshots, replicação e políticas de armazenamento integradas compensam a complexidade adicional. Ele exige planejamento de memória, topologia, manutenção e recuperação.

Para um único filesystem tradicional com crescimento online, XFS pode ser mais simples. Para uma arquitetura Linux centrada em subvolumes e integração nativa do kernel, Btrfs pode se encaixar melhor. Para volumes lógicos convencionais sobre filesystems tradicionais, LVM é uma camada mais direta.

## Relações

- [`zpool`](zpool.md) detalha pools e vdevs.
- [`rpool`](rpool.md) explica o nome convencional de um pool usado pelo sistema raiz.
- [Btrfs](btrfs.md) é outra opção integrada de filesystem e gerenciamento de armazenamento.
- [LVM](lvm.md) separa gerenciamento de volumes e filesystem em camadas distintas.

## Fontes primárias

- [OpenZFS documentation](https://openzfs.github.io/openzfs-docs/)
- [OpenZFS concepts](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/)
- [OpenZFS administration](https://openzfs.github.io/openzfs-docs/Getting%20Started/)
