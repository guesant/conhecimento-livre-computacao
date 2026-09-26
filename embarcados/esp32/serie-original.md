# ESP32 original

O ESP32 original é a primeira geração amplamente conhecida da família. Ele combina CPU Xtensa, Wi-Fi e Bluetooth em um SoC voltado a conectividade, automação e IoT. O ecossistema de módulos WROOM e WROVER tornou essa geração comum em placas de desenvolvimento e produtos comerciais.

## Características de projeto

O chip oferece dois núcleos em várias revisões, periféricos de uso geral, Wi-Fi de 2,4 GHz e Bluetooth. Módulos da família podem acrescentar flash e PSRAM, além de antena integrada ou conector de antena. A quantidade de GPIO e o uso seguro de cada pino dependem do módulo e da placa.

O ESP32 original não deve ser usado como referência para todas as variantes posteriores. Nomes de APIs, periféricos, restrições de boot e recursos de segurança podem mudar entre o original e as séries S, C, H e P.

## Uso adequado

É uma opção madura quando o projeto precisa de Wi-Fi e Bluetooth, bibliotecas amplas e disponibilidade de módulos conhecidos. Ele é adequado para protótipos, automação residencial, gateways pequenos e produtos cuja cadeia de fornecimento ainda oferece o módulo escolhido.

Para um novo produto, compare a disponibilidade de longo prazo e os requisitos de segurança com variantes mais recentes. Uma placa popular não é automaticamente a melhor base para um desenho novo.

## Desenvolvimento

O ESP-IDF fornece suporte oficial e controle detalhado. O Arduino Core for ESP32 reduz o custo inicial e permite reaproveitar sketches e bibliotecas Arduino. A escolha deve ser registrada junto com a versão do SDK, o board ID, as partições e o método de atualização.

## Fontes primárias

- [ESP32 da Espressif](https://www.espressif.com/en/products/socs/esp32)
- [Guia ESP-IDF do ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [Módulos ESP32](https://www.espressif.com/en/products/modules/)
