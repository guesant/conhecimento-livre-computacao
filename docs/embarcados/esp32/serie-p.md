# Série ESP32-P

ESP32-P4 é uma linha de alto desempenho dentro do portfólio ESP32. Ela se distancia do uso típico de ESP32 como microcontrolador Wi-Fi e deve ser avaliada como uma plataforma de processamento com periféricos ricos, memória externa e interfaces para aplicações de edge, visão, áudio e interfaces humanas.

O P4 pode ser combinado com outro dispositivo de conectividade quando o produto precisa de Wi-Fi ou Bluetooth. Essa composição separa processamento e rádio, mas acrescenta custo de placa, software e comunicação entre os chips.

## Seleção

Escolha P4 quando o workload justificar mais CPU, memória, DMA ou interfaces. Para um sensor simples, um C2, C3, C6 ou H2 pode oferecer menor consumo, custo e complexidade. Para uma aplicação com câmera, display ou processamento local, compare PSRAM, largura de banda e suporte de componentes.

## Software

O ESP-IDF é a referência de desenvolvimento. O suporte Arduino pode não oferecer a mesma cobertura ou abstração disponível em variantes mais maduras. Antes de portar uma biblioteca, verifique o suporte do target e a disponibilidade da API necessária.

## Fontes primárias

- [ESP32-P4 no ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32p4/)
- [SoCs Espressif](https://www.espressif.com/en/products/socs)
- [Documentação de hardware Espressif](https://www.espressif.com/en/products/hardware)
