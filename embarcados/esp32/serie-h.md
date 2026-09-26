# Série ESP32-H

A série ESP32-H reúne SoCs RISC-V orientados a conectividade de baixa potência e novos perfis de produto. ESP32-H2 é a variante mais conhecida da série e foi projetada para cenários com Bluetooth LE e IEEE 802.15.4, como Thread e Zigbee, sem funcionar como um ESP32 Wi-Fi genérico.

O catálogo de módulos também registra H4 e H21. Esses produtos pertencem a gerações e combinações de conectividade que podem ter suporte de hardware e software diferente do H2. O nome H não deve ser usado para inferir automaticamente rádio, frequência ou periféricos.

## ESP32-H2

H2 é adequado para dispositivos de baixa potência que precisam de BLE, Thread, Zigbee ou Matter sobre 802.15.4. A ausência de Wi-Fi em relação a várias outras variantes muda a arquitetura: um gateway, um border router ou outro dispositivo pode ser necessário para alcançar uma rede IP Wi-Fi.

## H4 e H21

H4 e H21 aparecem como produtos mais recentes no catálogo de módulos da Espressif. Ao usá-los, confirme datasheets, DevKits, versão do ESP-IDF, suporte no Arduino Core e disponibilidade de módulos. Não trate documentação de H2 como documentação suficiente para esses modelos.

## Cenários e limites

Escolha a série H quando o protocolo e o consumo forem mais importantes do que Wi-Fi integrado. Para um dispositivo que precisa de Wi-Fi e BLE no mesmo chip, uma variante C ou S pode ser mais adequada. Para produtos Matter, também compare requisitos de memória, rádio, certificação e suporte do SDK.

## Fontes primárias

- [ESP32-H2 no ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32h2/)
- [Módulos ESP32-H](https://www.espressif.com/en/products/modules/)
- [ESP-IDF e Matter](https://docs.espressif.com/projects/esp-matter/en/latest/)
