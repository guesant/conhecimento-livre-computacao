# RAID

RAID, Redundant Array of Independent Disks, combina dispositivos para formar uma
unidade lógica com uma política de distribuição, espelhamento ou paridade. O objetivo
pode ser desempenho, capacidade, continuidade durante falha ou uma combinação dessas
propriedades.

RAID não substitui backup. Um erro de aplicação, exclusão, ransomware, incêndio,
corrupção lógica ou falha do controlador pode atingir todos os discos do conjunto.

## Conceitos

Um stripe divide blocos entre dispositivos. Um mirror mantém cópias. Parity guarda
informação suficiente para reconstruir dados perdidos. Um array pode estar online,
degradado, reconstruindo, verificando ou falhando, e a mesma capacidade nominal pode
ter comportamentos muito diferentes conforme o nível escolhido.

| Conceito | Consequência |
| --- | --- |
| Capacidade bruta | Soma dos dispositivos antes da redundância e dos metadados. |
| Capacidade útil | Espaço disponível depois do perfil e das reservas. |
| Tolerância | Quantidade e posição de falhas que o perfil consegue suportar. |
| Rebuild | Leitura e gravação necessárias para reconstruir um membro. |
| URE ou erro de leitura irrecuperável | Falha de leitura que pode impedir uma reconstrução ou exigir cópia de backup. |
| Write hole | Risco de dados e paridade ficarem inconsistentes após falha durante uma escrita. |

## Níveis clássicos

| Nível | Distribuição | Tolerância | Capacidade útil aproximada | Característica |
| --- | --- | ---: | --- | --- |
| RAID 0 | striping sem cópia | 0 discos | soma dos discos | desempenho e capacidade, sem redundância. |
| RAID 1 | espelhamento | 1 disco em um espelho de dois | metade de um conjunto de dois | leitura simples e recuperação previsível. |
| RAID 2 | bits ou palavras com código Hamming | depende da implementação | histórica | praticamente não usado em sistemas atuais. |
| RAID 3 | striping por byte com paridade dedicada | 1 disco | capacidade menos um disco | adequado a padrões antigos e sequenciais. |
| RAID 4 | striping por bloco com paridade dedicada | 1 disco | capacidade menos um disco | paridade dedicada pode virar gargalo. |
| RAID 5 | striping por bloco com paridade distribuída | 1 disco | capacidade de todos menos um | capacidade eficiente, rebuild e escrita exigentes. |
| RAID 6 | striping por bloco com dupla paridade distribuída | 2 discos | capacidade de todos menos dois | mais proteção, mais escrita e reconstrução. |
| RAID 10 | espelhos combinados com striping | depende da posição das falhas | aproximadamente metade | baixa latência e rebuild geralmente mais simples. |

RAID 01 e RAID 10 não são a mesma topologia. RAID 10 espelha grupos e distribui
entre eles; RAID 01 primeiro distribui e depois espelha os conjuntos. Uma segunda falha
pode ter efeitos diferentes em cada arranjo.

RAID 50 e RAID 60 combinam grupos RAID 5 ou RAID 6 com striping entre grupos. Podem
oferecer capacidade e paralelismo maiores, mas acrescentam dependências, complexidade
de layout e risco de escolher uma largura de grupo inadequada.

JBOD não é um nível RAID. Pode significar discos apresentados individualmente ou
concatenados, sem a mesma redundância de um mirror ou de uma paridade. Alguns produtos
usam o termo de forma imprecisa, então confirme o layout real.

## Software, hardware e filesystem

RAID de hardware usa um controlador que apresenta volumes ao sistema operacional.
Ele pode oferecer cache protegido por bateria ou flash, mas introduz dependência do
controlador, de seu firmware e do procedimento de importação do array.

RAID de software usa o sistema operacional para administrar os dispositivos. Linux
md, ZFS e Btrfs possuem modelos diferentes de distribuição e redundância. LVM RAID
fica em outra camada e não deve ser confundido com um array criado pelo firmware.

ZFS usa vdevs mirror e RAIDZ dentro de um pool. Btrfs usa perfis de dados e metadados.
Esses modelos não devem ser reduzidos a nomes de RAID sem considerar checksums,
scrub, copy-on-write, substituição, expansão e recuperação do filesystem.

## Escolha do nível

Considere o padrão de leitura e escrita, o tamanho dos dispositivos, a capacidade
esperada, o número de falhas simultâneas, o tempo aceitável de reconstrução, a janela
de backup e a possibilidade de substituir discos. Um RAID 5 pequeno pode ser
adequado em um cenário de baixa escrita e dispositivos menores, mas uma grande
capacidade moderna pode tornar RAID 6, RAID 10 ou outro modelo mais coerente.

Não escolha pela porcentagem de capacidade apenas. Uma reconstrução lê muito estado
enquanto o sistema continua atendendo I/O. O risco operacional depende do tempo em
degradação, da taxa de erro, do estado dos outros discos e da existência de cópia
independente.

## Operação

Monitore estado, erros de leitura e escrita, temperatura, latência, setores pendentes,
resync, rebuild, capacidade e saúde do controlador. Faça scrubs ou verificações de
consistência conforme a implementação e registre sua duração.

Defina o procedimento para:

- identificar o dispositivo físico correto;
- retirar um disco sem remover o membro errado;
- substituir e particionar o novo disco;
- acompanhar rebuild e resync;
- lidar com duas falhas próximas;
- recuperar depois de perda do controlador;
- restaurar dados quando o array não puder ser montado.

Não remova ou force um membro para online apenas para eliminar um alerta. Primeiro
confirme o layout, o estado persistente, o dispositivo e a origem do erro. Uma
intervenção errada pode transformar um array degradado em um conjunto inconsistente.

## RAID e backup

RAID reduz o impacto de certas falhas de disco, mas mantém os dados no mesmo domínio
de falha. Backup deve usar outro armazenamento, outra credencial e, quando o risco
exigir, outro local. Testes de restauração precisam confirmar que o backup preserva
arquivos, permissões, metadados, banco e chaves necessárias.

Snapshots no mesmo pool ajudam em recuperação rápida, mas não protegem contra perda
do pool. Replicação para outro host melhora disponibilidade, mas pode reproduzir
exclusões e corrupção lógica. As camadas são complementares.

## Relações

- [Btrfs](btrfs.md) explica perfis, checksums e copy-on-write.
- [ZFS](zfs.md) explica pools, vdevs, mirror e RAIDZ.
- [zpool](zpool.md) detalha a composição de pools ZFS.
- [LVM](lvm.md) explica volumes lógicos e LVM RAID.
- [Backup](../../confiabilidade/backup/backup.md) explica recuperação independente.

## Fontes

- [Linux kernel, Multiple devices documentation](https://docs.kernel.org/admin-guide/md.html)
- [Linux kernel, md RAID personalities](https://docs.kernel.org/driver-api/md.html)
- [OpenZFS concepts](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/)
- [Btrfs documentation](https://btrfs.readthedocs.io/)
