# Mapa de acessórios Raspberry Pi

O ecossistema Raspberry Pi inclui placas de expansão, módulos, HATs, carriers, câmeras, displays, fontes, aceleradores e acessórios de armazenamento. Eles não mudam automaticamente a família do computador. A compatibilidade depende do conector, do barramento, do driver, da alimentação e do software.

## HATs e HAT+

HATs são placas que usam o header GPIO e seguem convenções de identificação e mecânica. HAT+ é uma evolução das especificações de hardware para melhorar compatibilidade e identificação. Um HAT pode usar I2C, SPI, UART, GPIO, PWM ou combinações desses recursos.

O header não é uma garantia de compatibilidade universal. Dois modelos podem expor o mesmo pino com funções elétricas e limites diferentes. Confirme tensão, corrente, pull-ups, interrupções, overlays e conflitos com outros acessórios.

## Carriers e IO Boards

Carrier boards são essenciais para Compute Modules porque fornecem os conectores e a alimentação que o módulo não possui. A Compute Module IO Board serve como plataforma de desenvolvimento e referência. Em produção, a carrier precisa ser validada para sinais de alta velocidade, alimentação, EMI, térmica e fabricação.

## Câmeras, displays e aceleradores

Câmeras e displays podem usar CSI, DSI, HDMI, USB ou interfaces específicas. A compatibilidade depende do driver, do device tree, da versão do Raspberry Pi OS e do modelo. Aceleradores como AI HATs adicionam capacidade de inferência, mas também impõem requisitos de energia, resfriamento, bibliotecas e modelo de runtime.

## Alimentação e térmica

Falhas atribuídas ao software frequentemente são causadas por fonte insuficiente, cabo inadequado, queda de tensão, aquecimento ou armazenamento degradado. O acessório deve ser avaliado junto com o consumo máximo do computador e dos periféricos, não apenas pela corrente nominal da placa principal.

## Fontes primárias

- [Acessórios Raspberry Pi](https://www.raspberrypi.com/products/)
- [Hardware Raspberry Pi](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
- [Compute Module IO Board](https://www.raspberrypi.com/products/compute-module-io-board/)
- [Especificação HAT](https://github.com/raspberrypi/hats)
