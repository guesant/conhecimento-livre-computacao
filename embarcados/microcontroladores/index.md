# Microcontroladores

Microcontroladores integram CPU, memória e periféricos em um dispositivo
voltado à execução de firmware. O software costuma operar próximo ao hardware,
com recursos limitados, requisitos de tempo de resposta e modos de baixo
consumo.

## Ecossistemas

- [Arduino](../arduino.md) oferece placas, APIs, bibliotecas e ferramentas para
  prototipação e desenvolvimento.
- [Famílias de placas Arduino](../arduino-familias.md) organiza as linhas de
  hardware do ecossistema.
- [ESP32](../esp32/index.md) documenta a família de SoCs, módulos e placas da
  Espressif.
- [Arduino Core for ESP32](../arduino-esp32.md) explica a adaptação do modelo
  Arduino aos SoCs ESP32.

## Limites

Uma placa de desenvolvimento não é o mesmo que o microcontrolador nela
instalado. O SoC pode ter variantes de memória, rádio, periféricos e segurança,
enquanto a placa acrescenta alimentação, conversor USB, reguladores e
conectores. A escolha precisa considerar o chip, o módulo e o produto final
separadamente.
