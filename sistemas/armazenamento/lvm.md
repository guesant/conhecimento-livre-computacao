# LVM

LVM, Logical Volume Manager, é uma camada de gerenciamento de volumes para Linux. Ele abstrai a relação direta entre uma partição e um filesystem, permitindo agrupar dispositivos físicos e criar volumes lógicos com tamanhos independentes da geometria original do disco.

LVM não é um filesystem. Um volume lógico normalmente recebe XFS, ext4 ou outro filesystem depois de ser criado. A sequência conceitual é:

```text
physical volume -> volume group -> logical volume -> filesystem -> mount
```

## Componentes

Um physical volume, ou PV, é um dispositivo ou partição inicializado para ser usado pelo LVM. Um volume group, ou VG, reúne um ou mais PVs em um espaço de alocação. Um logical volume, ou LV, consome extents do VG e aparece para o sistema como um dispositivo de blocos.

O VG pode ter espaço livre mesmo quando todos os LVs existentes estão cheios. Essa separação permite criar um novo LV ou expandir um existente, desde que haja capacidade e que o filesystem suporte a operação.

## Fluxo básico

Inspecione antes de alterar:

```sh
lsblk --output NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
sudo pvs
sudo vgs
sudo lvs --all --options lv_name,vg_name,lv_size,lv_attr,devices
```

Um fluxo inicial em um dispositivo dedicado pode ser descrito assim:

```sh
sudo pvcreate /dev/sdX1
sudo vgcreate vg_data /dev/sdX1
sudo lvcreate --name lv_app --size 100G vg_data
sudo mkfs.xfs /dev/vg_data/lv_app
```

`pvcreate`, `vgcreate` e `lvcreate` alteram metadados de armazenamento. O dispositivo, o tamanho e o estado do backup precisam ser confirmados antes da execução. O caminho `/dev/vg_data/lv_app` é uma referência ao LV, não uma indicação de que esse dispositivo exista neste host.

## Expansão e redução

Um LV pode ser expandido com `lvextend`, mas aumentar o dispositivo não aumenta automaticamente todos os filesystems. Em muitos casos, é necessário executar também a ferramenta de crescimento do filesystem, como `xfs_growfs` para XFS ou `resize2fs` para ext4.

Reduzir é mais arriscado. A ordem depende do filesystem: normalmente o filesystem precisa ser reduzido antes do LV. Um filesystem que não suporta redução não deve ser colocado em uma sequência que presuma essa capacidade.

```sh
sudo lvextend --size +20G /dev/vg_data/lv_app
sudo xfs_growfs /mountpoint
```

Não use `lvreduce` para corrigir um volume cheio sem um plano específico. Reduzir o bloco antes de reduzir o filesystem pode destruir dados imediatamente.

## Thin provisioning e snapshots

Um thin pool permite apresentar volumes virtuais maiores do que a capacidade física atualmente alocada. Isso aumenta a flexibilidade, mas cria uma obrigação operacional: monitorar a capacidade real do pool e seus metadados. Quando o pool fica sem espaço, vários volumes podem ser afetados.

Snapshots LVM usam cópia sob escrita para preservar o estado anterior de blocos alterados. Eles são úteis para uma janela curta de backup ou teste, mas não são uma política completa de backup. O desempenho pode cair e o snapshot pode ficar inválido quando seu espaço reservado se esgota.

## Diagnóstico e recuperação

Use `pvs`, `vgs`, `lvs`, `dmsetup ls` e `lsblk` para comparar as camadas. Verifique também o filesystem e a montagem, porque um LV ativo não significa que os arquivos estejam acessíveis.

Quando um PV desaparece, não recrie a assinatura com `pvcreate` por tentativa. Preserve os metadados, registre o estado de cada dispositivo e siga o procedimento de recuperação da distribuição e do LVM. Em um VG com redundância de dados fornecida por outra camada, diferencie a recuperação do PV da recuperação do filesystem.

## Quando usar

LVM é adequado quando volumes precisam crescer independentemente de suas partições originais, quando vários dispositivos devem formar grupos administráveis ou quando a infraestrutura já usa ferramentas tradicionais de Linux. Ele acrescenta uma camada que deve ser documentada e diagnosticada, então pode ser desnecessário em um host simples com um único filesystem.

Não escolha LVM apenas para obter snapshots se o requisito real for checksum, replicação integrada ou gerenciamento de datasets. Btrfs e ZFS tratam esses problemas com modelos diferentes.

## Relações

- [Btrfs](btrfs.md) integra filesystem e recursos de volume em um modelo copy-on-write.
- [XFS](xfs.md) é um filesystem frequentemente usado dentro de um LV.
- [ZFS](zfs.md) não usa LVM como camada necessária para seus pools.
- [Ferramentas de particionamento no Linux](../../comparacoes/ferramentas/particionamento-linux.md) trata a camada anterior ao LVM.

## Fontes primárias

- [`lvm(8)` no manual do Linux](https://man7.org/linux/man-pages/man8/lvm.8.html)
- [Red Hat, Configuring and managing logical volumes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/)
