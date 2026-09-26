# Raspberry Pi

Raspberry Pi é um ecossistema que reúne computadores de placa única, computadores em formato de teclado, Compute Modules, placas de microcontrolador Pico, chips RP2040 e RP2350, sistemas operacionais, acessórios e ferramentas de desenvolvimento.

A marca não identifica uma única classe de dispositivo. Um Raspberry Pi 5 executa Linux e possui armazenamento de boot; um Compute Module é um System-on-Module para uma carrier board; um Pico é uma placa de microcontrolador que grava firmware em flash e não executa Raspberry Pi OS.

## Famílias

- [Computadores de placa única](computadores.md) cobre as linhas flagship e Raspberry Pi Zero.
- [Computadores de teclado](computadores-de-teclado.md) cobre Raspberry Pi 400, 500 e 500+.
- [Compute Modules](compute-modules.md) cobre módulos para produtos embarcados e industriais.
- [Pico](pico.md) cobre Pico 1 e Pico 2, com variantes wireless e headers.
- [Microcontroladores](microcontroladores.md) explica RP2040 e RP2350 como chips.
- [Software e ferramentas](software.md) separa Raspberry Pi OS, Imager, bootloader e SDKs.
- [Acessórios e expansão](acessorios-e-expansao.md) explica HATs, carriers, câmeras, displays e aceleradores.

## Como escolher a família

Escolha primeiro o modelo de execução. Se a aplicação precisa de Linux, processos, containers, rede completa e armazenamento, comece pelos computadores de placa única ou Compute Modules. Se precisa de controle determinístico de GPIO, baixo consumo e firmware pequeno, considere Pico e RP2040 ou RP2350.

Depois compare CPU, RAM, conectividade, armazenamento, alimentação, temperatura, disponibilidade, suporte de software e forma de montagem. Uma placa de desenvolvimento pode acelerar o protótipo, mas um produto embarcado pode exigir Compute Module, carrier própria, eMMC, boot seguro e controle de fabricação.

## Relação com Raspberry Pi OS

Raspberry Pi OS é o sistema operacional oficial dos computadores Raspberry Pi. Ele não é o firmware de um Pico e não transforma um microcontrolador em um computador Linux. O boot media, a arquitetura de CPU, o firmware e os drivers devem ser escolhidos conforme a família.

## Fontes primárias

- [Documentação Raspberry Pi](https://www.raspberrypi.com/documentation/)
- [Produtos Raspberry Pi](https://www.raspberrypi.com/products/)
- [Hardware de computadores Raspberry Pi](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
- [Microcontroladores Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/microcontroller-chips.html)
