# Série ESP32-C

A série ESP32-C concentra variantes compactas e RISC-V com diferentes gerações de conectividade. Ela inclui ESP32-C2, C3, C5, C6 e C61. Os modelos não são intercambiáveis: rádio, CPU, periféricos, segurança e memória variam por chip.

## Modelos

| Modelo | Caracterização para escolha |
| --- | --- |
| ESP32-C2 | Variante compacta para conectividade e custo reduzido |
| ESP32-C3 | RISC-V com Wi-Fi e Bluetooth LE, ecossistema maduro |
| ESP32-C5 | Variante RISC-V com foco em Wi-Fi de nova geração |
| ESP32-C6 | Wi-Fi 6, Bluetooth LE e IEEE 802.15.4 para cenários como Thread e Zigbee |
| ESP32-C61 | Wi-Fi 6, Bluetooth LE e recursos recentes de segurança e isolamento |

A tabela é uma classificação inicial. Frequência, memória, periféricos, revisões e suporte de software devem ser consultados no datasheet e no guia ESP-IDF do modelo exato.

## RISC-V e compatibilidade

Grande parte da série C usa RISC-V, mas isso não significa que um binário ou uma biblioteca seja automaticamente portável entre C2, C3, C5, C6 e C61. O SoC continua definindo periféricos, registradores, memória, interrupções e capacidades de rádio.

Projetos Arduino devem testar a placa real e evitar acessar registradores específicos sem uma camada de abstração. Projetos ESP-IDF devem fixar o target e compilar componentes condicionais quando uma API não existir em todos os alvos.

## Conectividade

C3 e C2 atendem cenários de Wi-Fi e Bluetooth LE com perfis compactos. C6 acrescenta conectividade IEEE 802.15.4 além de Wi-Fi 6 e BLE, o que permite arquiteturas que combinam IP sobre Thread e conectividade Wi-Fi. C5 e C61 representam gerações mais recentes, com requisitos de suporte que devem ser confirmados na versão do SDK.

## Segurança

A série pode incluir secure boot, flash encryption, aceleradores criptográficos, eFuse, assinatura digital e mecanismos de isolamento. O conjunto exato varia por modelo. A configuração de produção precisa ser testada com o fluxo de atualização, porque habilitar recursos irreversíveis sem um plano de provisionamento pode impedir o desenvolvimento ou a recuperação.

## Fontes primárias

- [ESP32-C3 no ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/)
- [ESP32-C6 no ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/)
- [ESP32-C61 no ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c61/)
- [SoCs Espressif](https://www.espressif.com/en/products/socs)
