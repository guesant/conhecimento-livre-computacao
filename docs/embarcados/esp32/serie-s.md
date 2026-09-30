# Série ESP32-S

A série ESP32-S reúne variantes derivadas do ESP32 com mudanças relevantes de CPU, USB, memória, segurança e conectividade. Os modelos mais conhecidos são ESP32-S2 e ESP32-S3; o catálogo atual também registra a linha ESP32-S31.

## ESP32-S2

ESP32-S2 é uma variante de núcleo único orientada a Wi-Fi, segurança e periféricos como USB. Ela não deve ser tratada como uma versão de dois núcleos do ESP32 original. O suporte Bluetooth e a pinagem diferem, portanto bibliotecas que dependem de Bluetooth precisam de validação específica.

## ESP32-S3

ESP32-S3 amplia a série com CPU Xtensa de dois núcleos, BLE, USB e instruções vetoriais úteis para alguns workloads de processamento de sinais e machine learning embarcado. O módulo, a PSRAM e a placa escolhida influenciam diretamente o uso de câmera, display e modelos de inferência.

## ESP32-S31

ESP32-S31 representa uma geração mais recente da linha, com CPU RISC-V e variantes de memória e conectividade em evolução. Como o suporte pode depender de versões recentes do ESP-IDF e do Arduino Core, confirme a versão mínima do SDK e o nível de suporte antes de fixar o chip em produção.

## Escolha dentro da série

Escolha S2 quando USB, Wi-Fi e um perfil de núcleo único forem suficientes. Escolha S3 quando BLE, processamento local, PSRAM e recursos de interação forem importantes. Considere S31 quando o projeto aceitar uma plataforma mais recente e precisar acompanhar a disponibilidade e o suporte atual do fabricante.

Essas regras são orientações de triagem. A decisão final depende do datasheet, do módulo, do consumo, da disponibilidade e das bibliotecas usadas pela aplicação.

## Fontes primárias

- [ESP32-S2 no ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/)
- [ESP32-S3 no ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/)
- [Portfólio de módulos ESP32-S](https://www.espressif.com/en/products/modules/)
- [Arduino ESP32, suporte a novos SoCs](https://docs.espressif.com/projects/arduino-esp32/en/latest/guides/adding_new_soc.html)
