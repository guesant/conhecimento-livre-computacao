# Microcontroladores Raspberry Pi

Raspberry Pi produz microcontroladores próprios para controle em tempo real e projetos embarcados. RP2040 e RP2350 são chips, enquanto Pico e Pico 2 são placas que os integram com flash, alimentação, USB e acesso aos pinos.

## RP2040

RP2040 é o microcontrolador original da Raspberry Pi. Ele possui dois núcleos Arm Cortex-M0+, SRAM em bancos, USB, DMA e PIO. PIO permite implementar interfaces e protocolos com temporização previsível sem consumir continuamente a CPU.

## RP2350

RP2350 é a geração de maior desempenho. Ele oferece núcleos Arm Cortex-M33 ou Hazard3 RISC-V, mais SRAM e recursos adicionais de segurança. O projeto escolhe a arquitetura e a toolchain conforme o firmware e a necessidade de compatibilidade.

## Chip e placa

Usar o chip diretamente exige desenhar alimentação, clock, flash, USB, debug SWD, reset e layout. Usar Pico acelera desenvolvimento, mas acrescenta o formato e os componentes da placa. Uma carrier própria pode reutilizar o módulo Pico ou integrar o chip diretamente para reduzir custo e volume.

## SDKs

O Pico SDK fornece bibliotecas C e C++, exemplos, ferramentas de build e suporte aos periféricos. MicroPython oferece uma camada de scripting para prototipação. A escolha depende de desempenho, latência, tamanho do firmware, depuração e manutenção do produto.

## Segurança e ciclo de vida

Um microcontrolador não herda automaticamente a segurança de um sistema operacional. Firmware precisa de política de atualização, proteção de chaves, controle de acesso ao debug, integridade da imagem e recuperação. O fluxo de produção deve ser testado com a flash apagada e com falha de energia durante a atualização.

## Fontes primárias

- [Chips de microcontrolador Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/microcontroller-chips.html)
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [RP2350 Datasheet](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf)
- [Pico SDK](https://www.raspberrypi.com/documentation/pico-sdk/)
