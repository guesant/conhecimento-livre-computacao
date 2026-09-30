# Mapa de xterm e X11 remoto

`xterm` é um emulador de terminal para o X Window System. Ele não é um protocolo de acesso remoto, um servidor VNC ou um substituto de SSH. O programa pode executar no host remoto e desenhar sua janela em um servidor X local por meio de X11 forwarding.

## X11 forwarding

Com `ssh -X` ou `ssh -Y`, o SSH cria um caminho para que clientes X11 remotos enviem requests ao display local. O processo `xterm` e seus filhos executam no host remoto, mas os eventos e a renderização atravessam o canal X11.

Esse modelo exige um servidor X local, funciona melhor em redes de baixa latência e pode expor uma superfície ampla de interação. X11 forwarding não deve ser habilitado apenas para obter um terminal: para shell, use SSH sem forwarding; para uma aplicação gráfica pesada, prefira uma solução de desktop remoto adequada.

## Segurança

`-X` aplica restrições ao cliente X11; `-Y` confia mais no cliente e deve ser reservado a ambientes controlados. Não confunda forwarding com isolamento. Um cliente X11 pode observar ou interagir com outras partes da sessão conforme o servidor e as extensões disponíveis.

## Relações

- [SSH](../../ssh.md) fornece autenticação e transporte.
- [VNC](vnc.md) transporta um framebuffer, não requests X11.
- [RDP](rdp.md) usa um protocolo de desktop remoto diferente.

## Fonte primária

- [xterm](https://invisible-island.net/xterm/)
- [OpenSSH X11 forwarding](https://man.openbsd.org/ssh#X)
