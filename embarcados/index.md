# Sistemas embarcados

Sistemas embarcados combinam hardware especializado, firmware e uma aplicação que executa com recursos limitados. Diferentemente de um servidor geral, o dispositivo normalmente tem uma função delimitada, memória menor, requisitos de energia e uma relação estreita entre o software e os periféricos físicos.

Arduino e ESP32 ocupam partes relacionadas, mas não idênticas, desse espaço.
Arduino é um ecossistema de placas, plataformas, bibliotecas, ferramentas e uma
API de programação voltada a prototipação e ensino. ESP32 é uma família de SoCs
da Espressif, com módulos e placas de desenvolvimento que podem ser programados
por ESP-IDF, Arduino Core for ESP32 e outros ambientes.

## Categorias

- [Microcontroladores](microcontroladores/index.md) trata dispositivos voltados
  a firmware, periféricos, conectividade e restrições de energia.
- [Computadores de placa única](computadores-de-placa-unica/index.md) trata
  computadores que executam um sistema operacional mais geral.

## Como decompor um dispositivo

Uma placa de desenvolvimento não é o mesmo que um microcontrolador ou SoC. O SoC contém CPU, memória e periféricos. O módulo acrescenta memória externa, oscilador, RF e antena ou conector de antena. A placa acrescenta alimentação, USB, conversor serial, reguladores, botões e conectores. O firmware é o software gravado no dispositivo, enquanto o SDK fornece APIs, compiladores, bootloaders e ferramentas.

Essa distinção importa quando se escolhe uma placa. Dois produtos com o mesmo SoC podem ter flash, PSRAM, antena, regulador, pinagem e suporte de software diferentes. O nome comercial da placa não substitui a leitura do esquema elétrico e do datasheet.

## Arduino

[Arduino](arduino.md) é uma plataforma de desenvolvimento e uma comunidade, não uma arquitetura única de CPU. [Famílias de placas Arduino](arduino-familias.md) cobrem linhas como UNO, Nano, Mega, MKR, Portenta, Nicla e outras, usando microcontroladores e módulos de fornecedores diferentes.

[Arduino CLI](arduino-cli.md) fornece descoberta, instalação de plataformas e bibliotecas, compilação e upload sem depender da interface gráfica. [Arduino Core for ESP32](arduino-esp32.md) adapta o modelo de sketch e a API Arduino aos SoCs ESP32.

## ESP32

[ESP32](esp32/index.md) é uma família de SoCs, módulos e placas da Espressif. [Famílias de SoCs ESP32](esp32/familias.md) organiza as séries original, S, C, H, P e E. As páginas de cada série apresentam os modelos e as diferenças de projeto sem tratar uma placa específica como se fosse o chip.

[Software da família ESP32](esp32/software.md) explica ESP-IDF, Arduino Core for ESP32, ESP-AT, ESP-Hosted e ESP-Matter. [Módulos e placas ESP32](esp32/modulos-e-placas.md) separa SoC, módulo, DevKit e produto final.

## Preocupações comuns

Firmware embarcado precisa tratar atualização, recuperação, integridade da imagem, logs, watchdog, consumo de energia, armazenamento não volátil e proteção de credenciais. Um protótipo pode gravar por USB, mas um produto precisa definir como atualizar milhões de dispositivos sem perder o controle da versão ou bloquear o equipamento.

A conectividade também muda o modelo de risco. Wi-Fi, Bluetooth LE, Thread, Zigbee, USB e interfaces seriais têm limites e propriedades diferentes. O uso de um SDK não elimina a necessidade de configurar Secure Boot, flash encryption, credenciais por dispositivo, atualização segura e validação de entradas.

## Fontes primárias

- [Documentação Arduino](https://docs.arduino.cc/)
- [Hardware Arduino](https://docs.arduino.cc/hardware)
- [Documentação ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [SoCs ESP32](https://www.espressif.com/en/products/socs)
- [Módulos ESP32](https://www.espressif.com/en/products/modules/)
