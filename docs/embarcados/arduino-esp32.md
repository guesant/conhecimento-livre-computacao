# Arduino Core for ESP32

Arduino Core for ESP32 é a implementação do modelo Arduino para SoCs da Espressif. Ela permite usar sketches, bibliotecas e APIs Arduino enquanto aproveita parte dos recursos de uma plataforma ESP32, como Wi-Fi, Bluetooth LE, GPIO, ADC, SPI, I2C, UART, USB e modos de baixo consumo quando o chip oferece esses recursos.

O core não transforma todos os ESP32 em placas equivalentes. A disponibilidade de um periférico, a pinagem, a memória, o rádio e o método de upload dependem do SoC e da placa. Uma API compilável ainda pode produzir comportamento incorreto se o projeto assumir um GPIO ou recurso que não existe no alvo.

## Relação com ESP-IDF

O Arduino Core for ESP32 é construído sobre componentes do ESP-IDF e pode coexistir com APIs do framework. Essa composição é útil para projetos que começam com uma API simples e precisam acessar recursos específicos da plataforma. Ela também aumenta o acoplamento com a versão do core, do ESP-IDF empacotado e das bibliotecas.

Use Arduino quando o modelo de sketch, o ecossistema de bibliotecas e a velocidade de prototipação forem prioritários. Use ESP-IDF diretamente quando o projeto exigir controle explícito de tarefas, partições, bootloader, segurança, componentes, depuração ou ciclo de vida de firmware.

## Seleção de alvo

No Arduino CLI ou IDE, o alvo deve identificar a placa e o core correto. Em um projeto compartilhável, documente o board ID, a versão da plataforma e os requisitos de memória. Um ESP32 original, um ESP32-S3 e um ESP32-C6 não devem ser substituídos apenas porque o nome comercial contém ESP32.

## Segurança e produção

Desenvolvimento por USB é conveniente, mas a implantação exige considerar Secure Boot, flash encryption, armazenamento de credenciais, atualização OTA, rollback e proteção do dispositivo. As opções de segurança devem ser habilitadas e testadas no fluxo completo, porque podem alterar o processo de gravação e recuperação.

Não trate uma biblioteca Arduino como neutra em relação à segurança. Bibliotecas de rede, atualização e armazenamento podem manipular chaves, certificados e dados persistentes. Fixe versões, revise dependências e valide o firmware produzido antes de conectar o dispositivo a uma rede de produção.

## Fontes primárias

- [Arduino ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/)
- [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [Guia para adicionar um novo SoC ao Arduino ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/guides/adding_new_soc.html)
