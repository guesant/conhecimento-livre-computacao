# Arduino

Arduino é um ecossistema para desenvolver dispositivos eletrônicos programáveis. Ele reúne placas, plataformas de hardware, bootloaders, bibliotecas, ferramentas de compilação e upload, documentação e uma API de alto nível conhecida pelo modelo de sketch.

Arduino não define uma CPU única. O mesmo modelo de desenvolvimento pode ser usado com AVR, ARM Cortex-M, RISC-V, Renesas e módulos de conectividade. A compatibilidade real depende do core instalado, da plataforma selecionada e das capacidades da placa.

## Modelo de programação

Um sketch normalmente fornece `setup()` e `loop()`. `setup()` executa durante a inicialização, e `loop()` é chamado repetidamente pelo core. Esse modelo esconde parte da inicialização de clocks, GPIO e runtime, o que reduz a barreira de entrada, mas não elimina as restrições de tempo real, memória ou concorrência do microcontrolador.

A API comum inclui GPIO, ADC, PWM, temporização, UART, SPI, I2C e abstrações de impressão. Recursos mais específicos, como Wi-Fi, BLE, USB, CAN, PDM ou I2S, dependem do core e da placa. Um sketch portável precisa declarar suas dependências e evitar assumir uma pinagem ou periférico que não existe em todas as famílias.

## O que compõe uma plataforma Arduino

Uma plataforma instalada pelo Boards Manager possui arquivos de configuração, ferramentas, definição das placas, core, variantes de pinos, bibliotecas e parâmetros de compilação e upload. O arquivo `boards.txt` descreve placas e o `platform.txt` define partes do processo de build.

O core implementa o runtime e as funções Arduino para uma arquitetura. A variante adapta pinagem e detalhes da placa. Bibliotecas fornecem funcionalidades adicionais, mas podem depender de uma arquitetura ou de periféricos específicos. A seleção de uma placa muda compilador, flags, bootloader e método de upload.

## Placas e produtos

Uma placa Arduino oficial inclui mais do que o microcontrolador. Ela pode conter conversor USB, regulador, sensores, rádio, memória externa e conectores. Placas de terceiros podem usar o mesmo core e a mesma API, mas a qualidade do circuito, o bootloader e o suporte variam.

Não confunda uma placa Arduino com um módulo de produção. A placa é adequada para desenvolvimento e prototipação. Um produto final normalmente usa um módulo certificado ou um circuito próprio, com decisões adicionais sobre EMC, alimentação, atualização, fabricação, testes e segurança.

## Ferramentas

[Arduino CLI](arduino-cli.md) é a interface de automação para instalar plataformas, compilar, detectar placas e fazer upload. O Arduino IDE usa os mesmos conceitos com uma interface gráfica. O Arduino Cloud acrescenta serviços remotos, mas não substitui o controle local de versões e artefatos.

O processo de build deve registrar a versão do core, das bibliotecas, do compilador e das ferramentas. Um sketch que compila hoje pode mudar de comportamento quando uma plataforma ou biblioteca é atualizada sem pinagem.

## Limitações e critérios de escolha

Arduino é uma boa escolha para prototipação, ensino, automação simples e dispositivos em que uma API comum acelera o desenvolvimento. ESP-IDF, Zephyr, Mbed e SDKs do fabricante podem ser mais adequados quando o projeto exige controle fino de memória, RTOS, segurança, conectividade avançada, suporte de longo prazo ou uma cadeia de build totalmente explícita.

A escolha deve considerar o ciclo de vida do produto, a disponibilidade do core, o suporte da arquitetura, as bibliotecas necessárias, a depuração e a atualização em campo. A simplicidade da API não deve esconder o custo operacional do firmware depois que o dispositivo deixa a bancada.

## Fontes primárias

- [Documentação Arduino](https://docs.arduino.cc/)
- [Referência da linguagem Arduino](https://docs.arduino.cc/language-reference/)
- [Especificação de plataformas Arduino](https://docs.arduino.cc/arduino-cli/platform-specification)
- [Arduino CLI](https://docs.arduino.cc/arduino-cli/)
