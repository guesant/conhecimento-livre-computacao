# Software da família ESP32

O software ESP32 é composto por camadas que vão do bootloader ao código da aplicação. A escolha do framework afeta as APIs, o sistema de build, o particionamento, a depuração, a atualização e a forma como os recursos de segurança são habilitados.

## ESP-IDF

ESP-IDF, Espressif IoT Development Framework, é o framework oficial da Espressif. Ele fornece componentes, drivers, APIs de rede, FreeRTOS, ferramentas de configuração, build, gravação e monitoramento. O projeto escolhe um target de SoC e o framework compila somente as capacidades disponíveis para aquele alvo.

O fluxo típico inclui configurar o projeto, compilar, gravar e monitorar o dispositivo. CMake e Ninja fazem parte do build, e ferramentas do ESP-IDF gerenciam o bootloader, a tabela de partições e a imagem da aplicação. A versão do ESP-IDF deve ser fixada quando a reprodução do firmware for importante.

## Arduino Core for ESP32

O Arduino Core for ESP32 oferece uma camada de compatibilidade com o modelo Arduino sobre componentes do ESP-IDF. Ele é apropriado para prototipação e para aplicações que se beneficiam da API Arduino e de seu ecossistema de bibliotecas. A compatibilidade com os SoCs mais novos pode ter níveis diferentes.

## ESP-AT

ESP-AT é um firmware que transforma um ESP32 em um coprocessador de conectividade controlado por comandos AT. Um host externo envia comandos por UART, SPI ou outras interfaces suportadas e delega Wi-Fi, BLE ou funções relacionadas ao ESP32. Essa abordagem reduz o trabalho no host, mas cria um protocolo, uma atualização e uma fronteira de diagnóstico adicionais.

## ESP-Hosted

ESP-Hosted permite usar um ESP32 como dispositivo de conectividade para um host Linux ou outro processador. A comunicação entre host e ESP32 transporta funções de rede e rádio, o que separa a aplicação principal do subsistema sem fio. O desenho precisa considerar latência, atualização de ambos os lados e recuperação quando o coprocessador reinicia.

## ESP-Matter

ESP-Matter é o SDK da Espressif para construir dispositivos Matter. Ele compõe conectividade, modelo de dados, comissionamento e integração com recursos dos SoCs suportados. Matter não é um rádio específico; ele depende de transportes e componentes compatíveis, como Wi-Fi, Thread e Bluetooth LE durante o comissionamento.

## Bootloader e partições

O bootloader decide como a aplicação é localizada e iniciada. A tabela de partições define regiões para aplicação, dados, NVS, OTA e outros componentes. Alterar partições sem considerar tamanho de firmware, rollback e atualização pode tornar um dispositivo incapaz de inicializar.

## Segurança e atualização

ESP-IDF oferece recursos para Secure Boot, flash encryption, armazenamento seguro, assinatura e OTA. O produto precisa definir quando as chaves são provisionadas, quem assina as imagens, como o rollback funciona e como um dispositivo comprometido é revogado. A configuração de desenvolvimento não deve ser copiada diretamente para produção.

## Fontes primárias

- [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/)
- [Arduino Core for ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/)
- [ESP-AT](https://docs.espressif.com/projects/esp-at/en/latest/)
- [ESP-Hosted](https://github.com/espressif/esp-hosted)
- [ESP-Matter](https://docs.espressif.com/projects/esp-matter/en/latest/)
