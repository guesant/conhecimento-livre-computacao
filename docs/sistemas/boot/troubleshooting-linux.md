# Troubleshooting de inicialização Linux

A inicialização de um Linux pode falhar em camadas diferentes. O firmware
precisa encontrar um dispositivo inicializável, o GRUB precisa carregar o
kernel e o initramfs, o kernel precisa montar o sistema raiz e o init precisa
iniciar os serviços e apresentar o login.

Identificar a camada antes de alterar o disco evita reinstalar o bootloader
para corrigir um problema de `fstab`, ou executar `fsck` em um filesystem ainda
montado. A sequência geral é:

| Sintoma | Camada provável |
| --- | --- |
| Disco não aparece no menu de boot | Firmware, cabos, controladora ou ordem de boot |
| GRUB não aparece ou mostra prompt `grub>` | Entrada EFI, arquivos do GRUB, módulo ou configuração |
| Kernel panic ou não encontra a raiz | Kernel, initramfs, LUKS, LVM ou driver de storage |
| Emergency mode | `fstab`, filesystem, unidade systemd ou dependência |
| Login aparece, mas a sessão falha | Serviços, display manager, usuário ou filesystem cheio |

## Diagnóstico sem Live USB

Antes de editar, registre o modo de boot e os dispositivos:

```bash
test -d /sys/firmware/efi && echo UEFI || echo BIOS
findmnt /
lsblk -f
blkid
cat /etc/fstab
```

Em uma sessão que ainda inicia, consulte o boot anterior e as falhas do
kernel:

```bash
journalctl -b -1 -p err
journalctl -b -1 -k
systemctl --failed
```

O argumento `-b -1` seleciona o boot anterior quando o journal persistente
existe. Sem journal persistente, esses registros podem não estar disponíveis
depois de uma reinicialização.

## Shell de emergência pelo GRUB

O GRUB permite editar temporariamente a entrada de boot. Essa alteração não é
gravada no menu. No menu do GRUB:

1. selecione a entrada Linux;
2. pressione `e` para editar;
3. encontre a linha que começa com `linux` ou `linuxefi`;
4. remova `quiet` e `splash` se precisar ver as mensagens;
5. no final da linha, acrescente `rw init=/bin/bash`;
6. pressione `Ctrl+X` ou `F10` para iniciar com os parâmetros editados.

`init=/bin/bash` pede ao kernel para iniciar um shell como processo inicial,
sem passar pelo fluxo normal do systemd. `rw` solicita que a raiz seja montada
com escrita, mas o resultado depende do initramfs, do driver e do filesystem.
Se a raiz continuar somente leitura, remonte-a explicitamente:

```bash
mount -o remount,rw /
findmnt /
```

Esse shell não é um boot normal. Não espere que `systemctl`, rede, udev,
montagem automática ou serviços estejam disponíveis. O objetivo é corrigir uma
configuração pequena, copiar um arquivo de diagnóstico ou desfazer uma
alteração que impede o init.

Exemplos de reparos possíveis incluem corrigir uma entrada inválida em
`/etc/fstab`, remover uma opção de kernel adicionada por engano ou redefinir a
senha local:

```bash
vi /etc/fstab
passwd root
sync
mount -o remount,ro /
reboot -f
```

Não use esse modo para executar `fsck` na raiz montada. Também não apague
diretórios de runtime, sockets ou arquivos de estado sem confirmar qual
processo os cria. Depois de um reparo, remova `init=/bin/bash` da entrada do
GRUB e faça um boot normal.

## `rd.break` e initramfs

Em distribuições que usam dracut, `rd.break` pode abrir um shell antes de o
initramfs entregar o controle ao sistema instalado. Nesse ponto, a raiz real
costuma estar em `/sysroot`, e não em `/`:

```bash
mount -o remount,rw /sysroot
chroot /sysroot /bin/bash
```

O caminho e o momento exato variam conforme a distribuição e o ponto de
interrupção. Para corrigir LUKS ou LVM, talvez seja necessário desbloquear o
volume e ativar o grupo antes de montar a raiz:

```bash
cryptsetup status cryptroot
vgchange -ay
lsblk -f
```

Não execute `cryptsetup open` ou `vgchange` repetidamente sem observar o estado
atual. Um volume já aberto ou um grupo já ativo precisa ser diagnosticado, não
recriado.

## Recuperação por Live USB

Use um Live USB quando o sistema não inicia, quando é necessário desmontar a
raiz para executar `fsck`, ou quando os arquivos do boot precisam ser
reinstalados. Inicie a mídia no mesmo modo do sistema instalado. Se o sistema
usa UEFI, verifique que `/sys/firmware/efi` existe no ambiente live.

Primeiro identifique partições, volumes e filesystems sem confiar no nome do
dispositivo:

```bash
sudo lsblk -o NAME,SIZE,FSTYPE,FSVER,LABEL,UUID,MOUNTPOINTS
sudo blkid
```

Desbloqueie LUKS e ative LVM somente quando esses componentes existirem:

```bash
sudo cryptsetup luksOpen /dev/nvme0n1p3 cryptroot
sudo vgchange -ay
sudo lvs
```

Monte a raiz, `/boot` separado, se existir, e a partição EFI. Os caminhos
abaixo são exemplos; substitua-os pelos dispositivos confirmados em `lsblk`:

```bash
sudo mount /dev/mapper/vg-root /mnt
sudo mount /dev/nvme0n1p2 /mnt/boot
sudo mount /dev/nvme0n1p1 /mnt/boot/efi
```

Não monte partições que não existam apenas porque aparecem neste exemplo. Em
seguida, disponibilize os pseudo-filesystems necessários ao `chroot`:

```bash
for directory in /dev /dev/pts /proc /sys /run; do
  sudo mount --rbind "$directory" "/mnt$directory"
  sudo mount --make-rslave "/mnt$directory"
done
sudo chroot /mnt /bin/bash
```

O `chroot` troca a raiz visível para os comandos, mas não cria isolamento nem
inicia o sistema como se fosse um boot normal. Se for necessário baixar pacotes,
garanta que a rede do Live USB funciona e que a resolução de nomes está
disponível dentro do ambiente. Não substitua cegamente `resolv.conf`, pois ele
pode ser um link gerenciado pelo systemd-resolved.

## Regenerar a configuração do GRUB

Se o bootloader está presente e o problema é apenas a configuração, regenerar
o menu pode ser suficiente. Em Debian e Ubuntu, o wrapper usual é:

```bash
update-grub
```

O comando equivalente mais explícito é:

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

Em outras distribuições, o caminho e o comando podem variar. Confirme onde o
pacote da distribuição instala o arquivo de configuração antes de escrever.
Regenerar `grub.cfg` não reinstala os executáveis EFI ou o código no setor de
boot.

## Reinstalar o GRUB no modo BIOS

Em um sistema instalado no modo BIOS, o destino do `grub-install` é o disco,
não uma partição:

```bash
grub-install --target=i386-pc --recheck /dev/nvme0n1
update-grub
```

Confirme o disco correto com `lsblk` antes de executar. Instalar no dispositivo
errado pode tornar outro sistema ou outro disco não inicializável.

## Reinstalar o GRUB no modo UEFI

Em UEFI, a partição EFI precisa estar montada em `/boot/efi` e o comando deve
usar o identificador esperado pela distribuição:

```bash
grub-install \
  --target=x86_64-efi \
  --efi-directory=/boot/efi \
  --bootloader-id=ubuntu \
  --recheck
update-grub
```

`ubuntu` é apenas um exemplo. Debian, Fedora, Arch e outras distribuições
podem usar outro nome e outra ferramenta de geração do menu. Se o comando não
conseguir acessar as variáveis EFI, confirme que o Live USB foi iniciado em
UEFI. `efibootmgr -v` mostra as entradas disponíveis quando o firmware permite
acesso.

Com Secure Boot habilitado, preserve a cadeia assinada fornecida pela
distribuição. Uma reinstalação manual com binários não assinados pode resultar
em um GRUB que o firmware recusa. Antes de substituir arquivos, confirme como
a distribuição gerencia shim, GRUB assinado e chaves do firmware.

## Regenerar initramfs

Se o GRUB aparece, mas o kernel não encontra o volume raiz ou um driver
necessário, o problema pode estar no initramfs. Em Debian e Ubuntu, uma forma
comum de atualizar todas as imagens existentes é:

```bash
update-initramfs -u -k all
```

Em distribuições baseadas em dracut, o fluxo costuma ser:

```bash
dracut --regenerate-all --force
```

Não aplique o comando de uma família em outra distribuição sem confirmar o
gerenciador de initramfs instalado. Depois de regenerar, atualize a
configuração do GRUB se a distribuição exigir e reinicie somente após conferir
que `/boot` não está cheio.

## Sair do `chroot`

Depois dos reparos, saia do shell e desmonte os pseudo-filesystems antes de
reiniciar:

```bash
exit
sudo umount -R /mnt
sudo reboot
```

Remova o Live USB quando o firmware reiniciar. Se `umount -R` indicar que há
processos usando o filesystem, investigue antes de usar desmontagem forçada.

## Filesystem, fstab e init

Um GRUB funcional não corrige uma raiz corrompida. Para verificar um filesystem,
inicie por Live USB e confirme que ele está desmontado:

```bash
findmnt /dev/mapper/vg-root
sudo fsck -f /dev/mapper/vg-root
```

O comando e as opções dependem do tipo de filesystem. Não use `fsck` genérico
em Btrfs, XFS ou ZFS como se fossem ext4; use as ferramentas próprias e as
orientações do projeto. Antes de reparar, faça backup ou uma imagem quando os
dados forem importantes.

Uma entrada de `fstab` com UUID incorreto, filesystem removido ou opção
incompatível pode levar ao emergency mode. Corrija a entrada ou use uma opção
de montagem que reflita a intenção real. Evite simplesmente adicionar `nofail`
para esconder uma dependência que deveria impedir o boot.

## Segurança

Qualquer pessoa com acesso físico ao menu do GRUB pode tentar editar parâmetros
e obter um shell privilegiado se o sistema não estiver protegido. O parâmetro
`init=/bin/bash` deve ser tratado como um mecanismo de recuperação local, não
como uma autenticação.

Para reduzir o risco, avalie senha no GRUB, proteção física, Secure Boot,
criptografia completa de disco e controle do firmware. Secure Boot protege a
autenticidade de componentes assinados, mas não substitui a política de acesso
ao menu nem impede toda forma de recuperação por alguém que já desbloqueou o
dispositivo.

## Relações

- [Recuperação de sistemas](index.md) organiza mídias e ferramentas de recuperação.
- [UEFI](uefi.md) explica o modo de firmware usado pela reinstalação EFI.
- [BIOS](bios.md) explica o caminho legado de inicialização.
- [Secure Boot](secure-boot.md) explica a validação de componentes assinados.
- [LVM](../armazenamento/lvm.md) explica volumes lógicos usados em muitos sistemas.
- [GParted Live](gparted-live.md) trata particionamento e filesystems em um ambiente auxiliar.

## Fontes primárias

- [GNU GRUB Manual](https://www.gnu.org/software/grub/manual/grub/grub.html)
- [systemd, boot and system recovery](https://www.freedesktop.org/software/systemd/man/latest/bootup.html)
- [Debian Handbook, recovering a broken system](https://www.debian.org/doc/manuals/debian-handbook/sect.rescue-boot.en.html)
- [Ubuntu community, recovering Ubuntu after a failed boot](https://help.ubuntu.com/community/RecoveringUbuntuAfterInstallingWindows)
- [ArchWiki, GRUB](https://wiki.archlinux.org/title/GRUB)
