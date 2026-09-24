# Ferramentas de particionamento no Linux

O `cfdisk` é uma interface curses simples para visualizar e editar tabelas de partição. Ele é uma boa opção quando uma pessoa precisa intervir manualmente em um disco, mas não é a melhor escolha para todos os cenários. A alternativa adequada depende da interface desejada, do tipo de tabela, da necessidade de automação e de a operação envolver somente a tabela de partições ou também o filesystem.

Toda ferramenta desta página pode alterar a estrutura de um disco. Antes de escrever qualquer mudança, confirme o dispositivo com `lsblk`, desmonte os volumes envolvidos e valide um backup restaurável. O nome `/dev/sdX` usado nos exemplos é um marcador, não um dispositivo que deva ser copiado sem conferência.

## Comparação rápida

| Ferramenta | Interface | Melhor uso | GPT | MBR |
| --- | --- | --- | --- | --- |
| `cfdisk` | TUI curses | Intervenção manual simples | Sim | Sim |
| `fdisk` | CLI interativa | Administração geral e operações avançadas | Sim | Sim |
| `cgdisk` | TUI curses | Experiência parecida com `cfdisk`, focada em GPT | Sim | Não como tabela nativa |
| `gdisk` | CLI interativa | Operações avançadas em GPT | Sim | Não como tabela nativa |
| `sfdisk` | CLI e scripts | Automação, instalação e IaC | Sim | Sim |
| `sgdisk` | CLI e scripts | Automação avançada em GPT | Sim | Não como foco |
| `parted` | CLI interativa e scripts | Tabelas variadas e discos grandes | Sim | Sim |
| GParted | GUI | Resize, move e operações visuais em partições e filesystems | Sim | Sim |
| KDE Partition Manager | GUI | Administração gráfica em ambientes KDE | Sim | Sim |

## O papel do cfdisk

O `cfdisk` faz parte do `util-linux`, assim como `fdisk` e `sfdisk`. Ele mantém as alterações em memória até a confirmação explícita da operação de escrita. Isso permite revisar o layout antes de modificar o disco, mas não remove o risco de escolher o dispositivo errado ou confirmar uma operação destrutiva.

O próprio manual apresenta o `cfdisk` como uma interface amigável para operações básicas e recomenda `fdisk` quando são necessários recursos avançados. Em uma sessão manual, o fluxo mais simples é:

```sh
lsblk --output NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS,MODEL
sudo cfdisk /dev/sdX
```

Use o `cfdisk` quando o operador precisa visualizar o layout e tomar decisões interativamente. Para alterar apenas a tabela, ele é suficiente. Para redimensionar o conteúdo de uma partição, ainda é necessário considerar o filesystem e a ferramenta correspondente. Editar a tabela não equivale a redimensionar dados.

## Famílias de ferramentas

### util-linux

```text
cfdisk
fdisk
sfdisk
```

O `fdisk` é a alternativa geral quando a interface do `cfdisk` não expõe a operação necessária. Ele continua sendo interativo, mas oferece comandos e informações mais adequados para administração avançada.

O `sfdisk` usa um formato adequado para scripts e pode importar ou exportar uma descrição da tabela. É a opção preferível para instalações repetíveis, automação de hosts e pipelines de infraestrutura. Como o script descreve a geometria e os tipos das partições, ele deve ser revisado como código antes da execução.

Exemplo conceitual para uma tabela GPT:

```sh
cat <<'EOF' | sudo sfdisk /dev/sdX
label: gpt
size=1G, type=uefi
size=4G, type=swap
type=linux
EOF
```

O exemplo não deve ser executado sem adaptar os tamanhos, os tipos e o dispositivo ao host real. Em produção, prefira uma entrada versionada e validada, sem depender de posições implícitas que possam mudar quando o disco já tiver dados.

### GPT fdisk

```text
gdisk
cgdisk
sgdisk
```

Essa família é orientada a GPT. O `gdisk` é a interface interativa mais poderosa, o `cgdisk` oferece uma experiência curses semelhante à do `cfdisk` e o `sgdisk` expõe as operações para scripts e automação.

Se o objetivo é usar uma TUI familiar em um disco GPT, a escolha mais próxima é:

```sh
sudo cgdisk /dev/nvme0n1
```

O `cgdisk` não é um substituto genérico para editar tabelas MBR. Quando há uma tabela MBR, é necessário usar uma ferramenta que a suporte diretamente ou planejar uma conversão com backup e validação. Não trate conversão de tabela como uma operação reversível por padrão.

### GNU Parted

O `parted` usa um modelo de comandos diferente do `fdisk` e cobre diversos formatos de disk label, incluindo GPT e MS-DOS. Ele é útil quando se precisa de uma ferramenta de linha de comando mais genérica ou de um fluxo que também seja executado em scripts.

```sh
sudo parted --list
sudo parted /dev/sdX print
```

O `parted` não substitui automaticamente as ferramentas específicas de cada filesystem. Uma operação de particionamento pode exigir uma etapa posterior para criar, verificar ou redimensionar o filesystem com os utilitários apropriados.

### Interfaces gráficas

O GParted e o KDE Partition Manager são adequados quando a operação exige inspeção visual, redimensionamento ou movimentação de partições e filesystems compatíveis. Eles ficam em uma categoria diferente de `cfdisk`: não são apenas editores de tabelas, pois coordenam operações adicionais quando a implementação do filesystem permite.

O [GParted Live](../../sistemas/boot/gparted-live.md) inicializa um ambiente separado para editar um volume que não pode ser desmontado pelo sistema instalado. Isso é útil para partições de sistema, mas não transforma a operação em segura. O backup continua sendo obrigatório.

## Escolha por intenção

| Necessidade | Ferramenta inicial | Motivo |
| --- | --- | --- |
| Inspecionar e editar manualmente um layout simples | `cfdisk` | TUI compacta e fácil de revisar |
| Usar uma interface semelhante, somente em GPT | `cgdisk` | TUI da família GPT fdisk |
| Fazer uma operação interativa avançada | `fdisk` ou `gdisk` | Mais controle sobre a tabela correspondente |
| Repetir o mesmo layout em vários hosts | `sfdisk` ou `sgdisk` | Entrada declarativa para scripts |
| Trabalhar com vários formatos de disk label | `parted` | Modelo mais genérico |
| Mover ou redimensionar visualmente partições e filesystems | GParted | Integra operações de tabela e filesystem quando suportadas |
| Administrar graficamente em KDE | KDE Partition Manager | Integração com o ambiente KDE |

Para intervenção humana, a sequência prática costuma ser `cfdisk` ou `cgdisk` para simplicidade e `fdisk` ou `gdisk` quando a tabela exige mais controle. Para automação, prefira `sfdisk` ou `sgdisk`, porque um procedimento reproduzível deve declarar o layout em vez de depender de teclas e posições escolhidas por uma sessão interativa.

## Tabela de partição não é filesystem

As ferramentas desta página operam principalmente sobre a tabela de partições. Depois delas, ainda podem ser necessárias operações em camadas diferentes:

1. criar ou validar a partição;
2. criar ou ajustar o filesystem;
3. ativar LUKS, LVM ou RAID, quando aplicável;
4. montar o volume;
5. atualizar `fstab`, initramfs ou bootloader, quando a alteração afetar o boot;
6. validar os dados e a inicialização.

Mover o início ou o fim de uma partição pode exigir mover os dados internos. A tabela pode parecer correta e, ainda assim, o filesystem ou o bootloader estar inconsistente. Separe o diagnóstico da tabela, do filesystem, das camadas de armazenamento e do boot.

## Segurança operacional

Antes de qualquer escrita:

- confirme o modelo, o tamanho e o caminho do disco com `lsblk` e `udevadm info`;
- confirme que nenhum volume importante está montado ou sendo usado;
- valide o backup e, quando possível, um teste de restauração;
- registre o layout atual com `sfdisk --dump` ou `sgdisk --print`;
- prefira executar uma alteração por vez em discos críticos;
- aguarde o kernel reler a tabela e valide os dispositivos resultantes;
- não interrompa uma operação de resize ou move;
- mantenha um meio de recuperação, como [GParted Live](../../sistemas/boot/gparted-live.md), quando a máquina não puder ser reparada pelo sistema instalado.

Uma tabela de partições é metadado essencial, mas não é uma cópia dos dados. Fazer dump da tabela ajuda na reconstrução do layout, porém não substitui um backup do conteúdo.

## Relações

- [GParted Live](../../sistemas/boot/gparted-live.md) explica o uso de um ambiente inicializável para editar volumes fora do sistema instalado.
- [Ferramentas de instalação e boot](../../sistemas/boot/index.md) reúne mídias e métodos para iniciar ambientes de manutenção.
- [Comandos de processos, disco e arquivos](../../../referencia/comandos-de-processos-disco-e-arquivos.md) reúne comandos de inspeção e diagnóstico usados antes e depois do particionamento.

## Fontes primárias

- [`cfdisk(8)` no manual do Linux](https://man7.org/linux/man-pages/man8/cfdisk.8.html)
- [`fdisk(8)` no manual do Linux](https://man7.org/linux/man-pages/man8/fdisk.8.html)
- [`sfdisk(8)` no manual do Linux](https://man7.org/linux/man-pages/man8/sfdisk.8.html)
- [`parted(8)` no manual do Linux](https://man7.org/linux/man-pages/man8/parted.8.html)
- [`cgdisk(8)` no manual do Ubuntu](https://manpages.ubuntu.com/manpages/noble/man8/cgdisk.8.html)
- [GParted](https://gparted.org/)
