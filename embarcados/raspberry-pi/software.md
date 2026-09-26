# Software e ferramentas Raspberry Pi

O software Raspberry Pi depende da família de hardware. Computadores de placa única executam um sistema operacional e um bootloader; Pico executa firmware gravado em flash; Compute Modules combinam firmware, bootloader, armazenamento e uma carrier.

## Raspberry Pi OS

Raspberry Pi OS é o sistema operacional oficial para os computadores Raspberry Pi. Ele é baseado em Debian e possui edições Desktop, Full e Lite. Lite é adequado a servidores headless, gateways e sistemas que não precisam de ambiente gráfico.

A imagem deve corresponder à arquitetura, ao modelo e ao método de boot. Em equipamentos antigos, 32 bits pode oferecer compatibilidade; em modelos modernos, 64 bits permite usar melhor a CPU e a memória. Instalações de produção precisam de backup, atualização controlada e uma forma de recuperar a mídia.

## Raspberry Pi Imager

Raspberry Pi Imager grava imagens em microSD, USB e outros meios suportados. Ele também permite pré-configurar hostname, usuário, rede e SSH. Essa configuração inicial não substitui hardening posterior, rotação de credenciais, atualização e gestão de chaves.

## Bootloader e firmware

O bootloader do computador inicializa o hardware e localiza a mídia de boot. Em modelos recentes, parte da configuração reside em EEPROM. Atualizações de firmware podem alterar compatibilidade, boot de USB, rede, PCIe e comportamento térmico. Registre a versão e mantenha uma recuperação testada.

## Pico SDK e MicroPython

Pico usa o Pico SDK para C e C++ ou MicroPython para scripting. Esses ambientes não são distribuições Linux reduzidas. Eles produzem firmware que controla diretamente CPU, memória e periféricos do microcontrolador.

## Automação

Para imagens reproduzíveis, mantenha o arquivo de configuração, a versão do sistema, a arquitetura, o checksum e o processo de gravação. Para dispositivos no campo, acrescente atualização atômica, rollback, logs, health check e proteção contra interrupção de energia.

## Fontes primárias

- [Raspberry Pi OS](https://www.raspberrypi.com/documentation/computers/os.html)
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [Configuração de baixo nível](https://www.raspberrypi.com/documentation/computers/config_txt.html)
- [Pico SDK](https://www.raspberrypi.com/documentation/pico-sdk/)
