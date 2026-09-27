# Mapa de famílias Unix

Unix-like não é uma única implementação. A mesma família de interfaces pode
aparecer em um kernel Linux integrado por uma distribuição, em um sistema BSD
com base integrada ou em outro sistema que implemente parte do contrato comum.
Este mapa apresenta as relações sem repetir a explicação dos conceitos
canônicos.

## Contrato de portabilidade

[POSIX](sistemas/unix/posix.md) define interfaces e comportamentos mínimos para
shells, utilitários e APIs de sistema. Ele permite escrever uma base portátil,
mas não uniformiza empacotamento, inicialização, segurança, interface gráfica ou
virtualização.

## Famílias de sistemas

[BSD](sistemas/unix/bsd.md) descreve uma família em que kernel, userland,
ferramentas de administração e política de release são desenvolvidos como uma
base integrada. A página explica FreeBSD, OpenBSD, NetBSD e DragonFly BSD sem
confundir licença permissiva com garantia de segurança.

Uma distribuição Linux integra o kernel Linux com userland, bibliotecas,
empacotamento, sistema de inicialização e política de atualização que vêm de
projetos distintos. [Distribuições Linux](sistemas/distribuicoes-linux/index.md)
organiza suas famílias, releases, governança, segurança e empacotamento.

## Relações práticas

[Shells e scripts](shells-e-scripts.md) mostra como o contrato POSIX aparece na
portabilidade de scripts e quais extensões de Bash, Zsh e Fish exigem cuidado.
[GNU Coreutils](sistemas/linux/coreutils.md) e [documentação de comandos](sistemas/linux/documentacao.md)
explicam as diferenças entre implementações GNU, BusyBox e BSD.

O sistema de base, o gerenciador de pacotes e a distribuição devem ser
identificados separadamente ao diagnosticar um problema. Dizer apenas que uma
máquina é Linux ou Unix-like não informa qual comportamento de ferramenta,
serviço ou política será encontrado.

## Continue por aqui

- [POSIX](sistemas/unix/posix.md)
- [BSD](sistemas/unix/bsd.md)
- [Distribuições Linux](sistemas/distribuicoes-linux/index.md)
- [Shells e scripts](shells-e-scripts.md)
