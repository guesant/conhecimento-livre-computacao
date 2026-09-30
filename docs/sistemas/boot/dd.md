# dd

dd é um utilitário de cópia e conversão de dados, disponível no GNU coreutils e em sistemas Unix. Ele copia blocos de uma entrada para uma saída e, por isso, consegue gravar imagens raw em dispositivos, criar cópias de dispositivos e extrair partes de arquivos.

## O modelo

A operação é simples e perigosa:

- `if=` define a entrada;
- `of=` define a saída;
- `bs=` define o tamanho dos blocos;
- `status=progress` mostra progresso em implementações que suportam a opção;
- `conv=fsync` solicita sincronização antes do término.

O comando não sabe que um caminho é uma unidade USB, um disco de sistema ou um volume de dados. Ele segue o que foi informado.

## Gravar uma imagem

Desmonte as partições do dispositivo, confirme o disco inteiro e grave a imagem:

```bash
lsblk
sudo umount /dev/sdX1
sudo dd if=image.img of=/dev/sdX bs=4M status=progress conv=fsync
sync
```

No macOS, o dispositivo costuma aparecer como `/dev/diskN`. O nome exato e o procedimento de desmontagem variam. Não copie comandos Linux para macOS sem adaptar a identificação do disco.

Use o dispositivo inteiro, como `/dev/sdX`, quando a imagem contém tabela de partições. Usar uma partição, como `/dev/sdX1`, grava o conteúdo no lugar errado para esse caso.

## Verificação

Depois da gravação, compare checksum da imagem original e valide a leitura quando o procedimento exigir:

```bash
sha256sum image.img
sudo dd if=/dev/sdX bs=4M status=progress | sha256sum
```

A comparação pode exigir limitar a leitura ao tamanho exato da imagem se o dispositivo for maior. Em operações de recuperação, registre tamanho, checksum, dispositivo e horário.

## Clonagem e backup

Para copiar um dispositivo inteiro para uma imagem:

```bash
sudo dd if=/dev/sdX of=disk.img bs=4M status=progress conv=sync,noerror
sync
```

`noerror` permite continuar em algumas falhas de leitura, mas não recupera os dados ausentes. Para discos com setores defeituosos, ddrescue costuma ser mais adequado porque mantém um mapa de recuperação e permite retomar a operação.

## Riscos

Um erro em `if` ou `of` pode destruir dados imediatamente. Faça uma pausa antes de Enter, compare modelo e capacidade usando lsblk, desmonte o destino e mantenha um backup separado.

Não use dd como ferramenta de particionamento de alto nível, não interrompa uma gravação sem entender o estado resultante e não considere o comando concluído apenas porque o processo terminou sem erro de shell.

## Relações

- [balenaEtcher](balena-etcher.md) oferece uma interface de gravação com seleção guiada.
- [GParted Live](gparted-live.md) opera partições e filesystems.
- [MemTest86 e Memtest86+](memtest.md) são mídias de diagnóstico, não cópias raw.

## Fonte primária

- [GNU coreutils: dd invocation](https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html)
