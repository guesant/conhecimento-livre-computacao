# XFS

XFS é um filesystem journaling para Linux projetado para trabalhar com arquivos, diretórios e volumes grandes. Ele usa allocation groups para distribuir estruturas internas e oferece crescimento online do filesystem montado.

XFS é um filesystem, não um gerenciador de volumes. Ele pode ser criado em uma partição, em um LV ou em outra camada de blocos. O volume abaixo e o filesystem acima precisam ser aumentados de forma coordenada.

## Operação

Inspecione o filesystem e a montagem antes de alterar o volume:

```sh
findmnt /mountpoint
sudo xfs_info /mountpoint
df -hT /mountpoint
```

Para crescer um XFS montado, a ferramenta usual é `xfs_growfs`:

```sh
sudo xfs_growfs /mountpoint
```

O crescimento do dispositivo abaixo, como um LV, deve ocorrer antes ou em coordenação com o crescimento do filesystem. O comando não cria espaço por conta própria.

## Redução e reparo

O fluxo de redução deve ser tratado com cuidado porque XFS tradicionalmente não oferece redução online do filesystem. Quando é necessário terminar com um volume menor, o caminho usual envolve criar um filesystem novo, copiar os dados, validar a cópia e trocar a montagem. Não reduza o LV esperando que XFS acompanhe a operação.

`xfs_repair` é uma ferramenta de reparo offline. Desmonte o filesystem e preserve o diagnóstico antes de executar um reparo. Se a corrupção tiver causa física, reparar a estrutura sem tratar o disco pode apenas ocultar o sintoma por pouco tempo.

```sh
sudo umount /mountpoint
sudo xfs_repair -n /dev/vg_data/lv_app
```

`-n` faz uma verificação sem modificar o filesystem. A execução sem esse modo exige uma decisão explícita, backup e um procedimento de recuperação.

## Características e limites

Journaling ajuda a recuperar consistência estrutural depois de uma interrupção, mas não é backup nem impede perda de dados já confirmados. XFS não fornece, por si só, snapshots, replicação ou redundância entre dispositivos. Essas funções devem vir de uma camada como LVM, do armazenamento subjacente ou da estratégia de backup.

XFS possui ferramentas próprias para inspeção e manutenção, e algumas propriedades dependem da versão do kernel e do pacote `xfsprogs`. Registre a versão quando um procedimento depender de uma capacidade específica.

## Quando usar

XFS é uma boa escolha quando o requisito é um filesystem tradicional, escalável, com journaling e crescimento online, especialmente em volumes grandes. Ele combina bem com LVM, mas a dupla acrescenta duas camadas que precisam ser observadas separadamente.

Se subvolumes, snapshots copy-on-write e checksums forem requisitos centrais, avalie Btrfs. Se pools, vdevs, checksums de ponta a ponta e replicação ZFS forem necessários, avalie ZFS.

## Relações

- [LVM](lvm.md) pode fornecer o dispositivo de blocos abaixo do XFS.
- [Btrfs](btrfs.md) integra recursos que no XFS normalmente vêm de camadas externas.
- [ZFS](zfs.md) possui filesystem e gerenciador de armazenamento integrados.

## Fontes primárias

- [XFS no Linux kernel documentation](https://docs.kernel.org/filesystems/xfs.html)
- [xfsprogs no kernel.org](https://www.kernel.org/pub/linux/utils/fs/xfs/)
