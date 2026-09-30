# Arduino CLI

Arduino CLI é a ferramenta de linha de comando que automatiza o ciclo de desenvolvimento Arduino. Ela instala plataformas e bibliotecas, detecta placas, compila sketches, grava firmware e expõe uma interface adequada para scripts, CI e ferramentas gráficas.

O CLI é parte importante do ecossistema porque torna explícitas operações que, no IDE, aparecem como escolhas de menus. Um pipeline pode selecionar a placa, instalar uma versão de plataforma, compilar um sketch e produzir o artefato sem depender de uma sessão interativa.

## Modelo de plataforma

O CLI usa índices de plataformas e o Boards Manager para resolver cores e ferramentas. Uma plataforma define arquitetura, compilador, bootloader, parâmetros de build, placas disponíveis e método de upload. Bibliotecas possuem resolução própria e podem ser instaladas pelo Library Manager ou declaradas no projeto.

Essa separação permite instalar suporte para AVR, SAMD, ESP32 e outras arquiteturas, mas também cria risco de incompatibilidade. Registre as versões do core, das bibliotecas e do CLI. O build deve ser reproduzível dentro de um container ou ambiente controlado quando o firmware for parte de uma entrega automatizada.

## Operações comuns

Os comandos exatos podem variar entre versões, mas o fluxo conceitual é:

```bash
arduino-cli core update-index
arduino-cli core search esp32
arduino-cli board list
arduino-cli compile --fqbn arduino:avr:uno sketch
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno sketch
```

`--fqbn` identifica fabricante, arquitetura e placa. O identificador deve ser tratado como parte da configuração do build, não inferido silenciosamente pelo script.

## CI e segurança

Em CI, use versões fixadas do CLI, dos índices e das plataformas. Valide checksums dos artefatos quando a distribuição oferecer essa possibilidade e armazene logs de compilação e versão. Não grave tokens, chaves de dispositivo ou credenciais de rede no sketch ou no repositório.

O upload por USB concede controle do firmware ao host conectado. Em produtos, o método de gravação de desenvolvimento deve ser separado do mecanismo de atualização em campo. Bootloader, assinatura, proteção de leitura e provisionamento são decisões de produção, não apenas opções de compilação.

## Relação com Arduino IDE

O Arduino IDE oferece uma experiência gráfica sobre conceitos que também existem no CLI. Usar o IDE para exploração e o CLI para automação é uma combinação comum. A equipe deve evitar que configurações locais do IDE sejam a única fonte do processo de build.

## Fontes primárias

- [Documentação do Arduino CLI](https://docs.arduino.cc/arduino-cli/)
- [Especificação de plataformas](https://docs.arduino.cc/arduino-cli/platform-specification)
- [Documentação do Arduino IDE](https://docs.arduino.cc/software/ide-v2)
