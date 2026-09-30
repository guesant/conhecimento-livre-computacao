# Compute Modules Raspberry Pi

Compute Module é um System-on-Module baseado em uma geração de Raspberry Pi. Ele contém o núcleo de processamento e interfaces necessárias, mas omite conectores comuns de uma placa de computador. Uma carrier board fornece alimentação, armazenamento externo, USB, Ethernet, vídeo, GPIO e os conectores específicos do produto.

## Modelos

| Modelo | Base aproximada | Forma de integração |
| --- | --- | --- |
| CM1 | Raspberry Pi 1 | DDR2 SODIMM |
| CM3 | Raspberry Pi 3 | DDR2 SODIMM |
| CM3+ | Raspberry Pi 3 B+ | DDR2 SODIMM |
| CM4 | Raspberry Pi 4 | Dois conectores de alta densidade |
| CM4S | Raspberry Pi 4 em formato CM3 | DDR2 SODIMM |
| CM5 | Raspberry Pi 5 | Dois conectores de alta densidade |
| CM Zero | Família Zero | Módulo compacto para produtos menores |

Os modelos diferem em RAM, eMMC, wireless, I/O, disponibilidade e requisitos de carrier. Variantes Lite ou L normalmente não possuem armazenamento eMMC integrado. A carrier precisa atender o modelo escolhido; uma placa desenhada para CM4 não deve ser presumida compatível com CM5.

## Carrier e produção

A carrier é parte do produto, não apenas um adaptador. Ela define alimentação, integridade de sinal, conectores, armazenamento, dissipação, montagem e acesso a interfaces. A Raspberry Pi Compute Module IO Board funciona como referência de protótipo e ajuda a validar o módulo antes de uma carrier própria.

## Boot e atualização

O Compute Module pode inicializar de eMMC, SD, USB ou outros meios conforme o modelo e a configuração. O bootloader EEPROM e o fluxo de gravação precisam ser documentados para recuperação de fábrica e atualização de campo.

## Quando escolher

Escolha Compute Module quando o produto precisa de integração mecânica, eMMC, carrier própria, maior controle de I/O ou fabricação em volume. Uma placa flagship é mais simples para protótipos e pequenos servidores, mas deixa conectores, formato e alimentação menos controlados.

## Fontes primárias

- [Compute Module hardware](https://www.raspberrypi.com/documentation/computers/compute-module.html)
- [Compute Module 5](https://www.raspberrypi.com/products/compute-module-5/)
- [Compute Module 4](https://www.raspberrypi.com/products/compute-module-4/)
- [Compute Module IO Board](https://www.raspberrypi.com/products/compute-module-io-board/)
