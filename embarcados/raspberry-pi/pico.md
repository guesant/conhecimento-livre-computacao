# Raspberry Pi Pico

Raspberry Pi Pico é uma família de placas de microcontrolador. Ao contrário dos computadores Raspberry Pi, Pico não executa Raspberry Pi OS e não usa armazenamento removível como disco do sistema. O firmware é gravado na flash da placa, normalmente por USB, usando o bootloader UF2 ou uma ferramenta de programação.

## Gerações e variantes

| Geração | Variantes | Chip |
| --- | --- | --- |
| Pico 1 | Pico, Pico H, Pico W e Pico WH | RP2040 |
| Pico 2 | Pico 2 e Pico 2 W | RP2350 |

O sufixo H indica headers pré-soldados. O sufixo W indica conectividade sem fio, com Wi-Fi e Bluetooth nas variantes documentadas. A placa sem W não deve ser tratada como se pudesse oferecer conectividade wireless apenas por software.

## Pico 1 e RP2040

Pico 1 usa RP2040, um microcontrolador dual-core com PIO, USB, GPIO, ADC, PWM, UART, SPI e I2C. Ele é adequado a controle determinístico, automação, sensores, instrumentos e aplicações que não precisam de Linux.

## Pico 2 e RP2350

Pico 2 usa RP2350, uma geração mais recente com mais SRAM, maior desempenho e opções de CPU Arm Cortex-M33 ou Hazard3 RISC-V. Os recursos de segurança e o modelo de memória diferem do RP2040, portanto o firmware precisa ser validado para a geração escolhida.

## Desenvolvimento

Pico pode ser programado com C ou C++ pelo Pico SDK, com MicroPython ou com outras linguagens e toolchains que suportem o hardware. O modo de desenvolvimento, a biblioteca de periféricos, a depuração SWD e o processo de atualização devem ser escolhidos antes de definir o formato final da placa.

## Produtos derivados

O Pico é uma placa de desenvolvimento, não a única forma de usar RP2040 ou RP2350. Terceiros podem criar placas próprias com o mesmo microcontrolador, desde que respeitem alimentação, flash, cristal, USB, SWD e requisitos de layout. A compatibilidade de software não garante compatibilidade elétrica ou mecânica.

## Fontes primárias

- [Pico-series microcontroller boards](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- [Pico-series microcontrollers](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
- [RP2040 e RP2350](https://www.raspberrypi.com/documentation/microcontrollers/microcontroller-chips.html)
