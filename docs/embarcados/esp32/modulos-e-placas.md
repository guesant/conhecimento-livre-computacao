# Mapa de módulos e placas ESP32

Um módulo ESP32 é uma integração de hardware pronta para ser soldada a uma placa maior. Uma placa de desenvolvimento, como uma DevKit, adiciona alimentação, USB, conversor serial, botões e headers ao módulo ou ao SoC. Um produto final pode usar o módulo, o chip sem módulo ou uma placa própria.

## SoC, módulo e DevKit

| Camada | Responsabilidade | Documento necessário |
| --- | --- | --- |
| SoC | CPU, rádio, memória interna e periféricos | Datasheet e Technical Reference Manual |
| Módulo | SoC, flash, PSRAM, cristal e RF | Datasheet, desenho mecânico e certificação |
| DevKit | Alimentação, USB, conversor e acesso aos pinos | Esquema elétrico e guia da placa |
| Produto | Gabinete, energia, sensores e integração | Projeto completo e requisitos regulatórios |

Um módulo WROOM, WROVER, MINI ou PICO não implica que todos os pinos do SoC estejam disponíveis. Antena, flash, PSRAM e GPIO podem ocupar sinais que seriam acessíveis em um chip sem módulo.

## Flash e PSRAM

Flash externa armazena bootloader, tabela de partições, firmware e dados persistentes. PSRAM aumenta a memória disponível para buffers, gráficos, câmera e outros workloads, mas possui características de latência e inicialização diferentes da RAM interna. A aplicação deve ser projetada conforme o mapa de memória do chip e do módulo.

## Antena e RF

A antena pode ser uma trilha na placa, uma antena no módulo ou um conector para antena externa. O layout, o keep-out, o aterramento, o gabinete e a certificação afetam o alcance e a conformidade. Copiar o nome do módulo sem copiar as restrições de layout pode produzir um produto funcional na bancada e instável em campo.

## USB e gravação

Algumas placas incluem conversor USB para UART; outras expõem USB nativo ou USB Serial/JTAG do SoC. O método de gravação, o driver, os pinos de boot e a possibilidade de recuperação variam. O fluxo de produção deve ter um mecanismo de programação e um mecanismo separado de atualização em campo.

## Seleção

Escolha primeiro a variante do SoC e depois o módulo que atende memória, antena, temperatura, formato e certificação. Escolha a DevKit para validar software e periféricos, mas não assuma que o circuito da DevKit é adequado para o produto final.

## Fontes primárias

- [Módulos Espressif](https://www.espressif.com/en/products/modules/)
- [DevKits Espressif](https://www.espressif.com/en/products/devkits)
- [Documentação técnica de módulos](https://www.espressif.com/en/support/download/documents/modules)
- [ESP Hardware Design Guidelines](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/)
