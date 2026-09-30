# Famílias de SoCs ESP32

A Espressif organiza o portfólio ESP32 em famílias com objetivos diferentes. Os nomes ajudam a localizar documentação, mas não substituem o datasheet. Um modelo dentro de uma série pode remover, acrescentar ou alterar periféricos, rádio, CPU, memória e recursos de segurança.

## Mapa do portfólio

| Família | Modelos representativos | Direção geral |
| --- | --- | --- |
| ESP32 | ESP32, ESP32-D0WD e variantes | Wi-Fi, Bluetooth e ecossistema original |
| ESP32-S | S2, S3 e S31 | Evolução de CPU, USB, BLE, segurança e eficiência |
| ESP32-C | C2, C3, C5, C6 e C61 | Variantes compactas, RISC-V e novas gerações de conectividade |
| ESP32-H | H2, H4 e H21 | Conectividade de baixa potência e produtos baseados em RISC-V |
| ESP32-P | P4 | Microcontrolador de alto desempenho e periféricos ricos |
| ESP32-E | E22 e produtos relacionados | Novas combinações de CPU, memória e conectividade |

Os modelos representativos refletem o catálogo consultado na revisão da documentação. Novos SoCs, módulos e variantes podem ser adicionados, descontinuados ou reorganizados pelo fabricante.

## Como ler o nome

O sufixo não é uma escala simples de desempenho. S, C, H e P indicam linhas com prioridades diferentes. O número identifica uma variante, mas a geração, o processo, o rádio e os periféricos precisam ser conferidos na documentação do chip.

Também existem nomes de módulos como WROOM, WROVER, MINI e PICO. Esses nomes não são novas famílias de SoC. Eles identificam integrações de hardware que combinam um chip com flash, PSRAM, antena e um formato mecânico.

## Compatibilidade de software

ESP-IDF tem alvos distintos para diferentes SoCs. O Arduino Core for ESP32 adiciona suporte por meio de plataformas e variantes de placa, mas o nível de suporte pode diferir entre modelos. Uma biblioteca que usa Wi-Fi e BLE não deve ser presumida compatível com uma variante que não tem ambos os rádios.

O suporte pode ter níveis diferentes: componente no ESP-IDF, suporte no Arduino Core, DevKit oficial, módulo comercial e certificação. Ao escolher um chip, verifique todos esses níveis para o produto real.

## Critérios de escolha

Compare a família por conectividade, CPU, memória, periféricos, consumo, segurança, temperatura, disponibilidade, encapsulamento, módulo e maturidade do SDK. Para dispositivos alimentados por bateria, os modos de sono e o comportamento do rádio são mais importantes do que a frequência máxima. Para visão, áudio ou interfaces rápidas, PSRAM, DMA e periféricos podem decidir a arquitetura.

## Fontes primárias

- [Portfólio de SoCs Espressif](https://www.espressif.com/en/products/socs)
- [Portfólio de módulos Espressif](https://www.espressif.com/en/products/modules/)
- [Guia de programação ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/)
