# ESP32

ESP32 é o nome de uma família de sistemas em chip da Espressif e também o nome pelo qual muitas pessoas identificam módulos e placas baseados nesses chips. O catálogo inclui CPUs Xtensa e RISC-V, diferentes rádios, periféricos, memórias, recursos de segurança e perfis de consumo.

O nome sozinho não identifica o hardware suficiente para um projeto. ESP32 original, ESP32-S3, ESP32-C6 e ESP32-P4 têm capacidades e modelos de programação diferentes. Sempre associe o nome à variante do SoC, ao módulo ou à placa de desenvolvimento.

## Camadas do ecossistema

O SoC contém CPU, periféricos, controladores de memória e, em alguns modelos, rádio Wi-Fi, Bluetooth LE ou IEEE 802.15.4. O módulo integra o SoC com flash, PSRAM opcional, antena, cristal e componentes de RF. A placa DevKit fornece alimentação, USB, conversor serial, botões, headers e um circuito adequado para desenvolvimento.

O software pode ser composto por bootloader, tabela de partições, firmware da aplicação, componentes do ESP-IDF, Arduino Core for ESP32 e firmwares de conectividade como ESP-AT. Um produto final pode substituir a placa de desenvolvimento por um módulo ou por um circuito próprio.

## Famílias

[Famílias de SoCs ESP32](familias.md) organiza as linhas atualmente documentadas pela Espressif: ESP32 original, ESP32-S, ESP32-C, ESP32-H, ESP32-P e ESP32-E. As séries são categorias de produto, não garantias de compatibilidade entre todos os modelos.

- [ESP32 original](serie-original.md) cobre a primeira geração com Wi-Fi e Bluetooth.
- [Série ESP32-S](serie-s.md) cobre variantes como S2, S3 e S31.
- [Série ESP32-C](serie-c.md) cobre C2, C3, C5, C6 e C61.
- [Série ESP32-H](serie-h.md) cobre variantes voltadas a conectividade de baixa potência e novos produtos H.
- [Série ESP32-P](serie-p.md) trata o perfil de alto desempenho do P4.
- [Série ESP32-E](serie-e.md) registra a linha E e sua posição no catálogo atual.

## Escolha de uma variante

Comece pelo protocolo e pelos periféricos necessários, não pela frequência nominal. Wi-Fi, Bluetooth LE, Thread, Zigbee, USB, PSRAM, câmera, display, áudio, segurança e consumo eliminam algumas variantes antes que desempenho bruto seja comparado.

Depois valide memória, temperatura, encapsulamento, disponibilidade do módulo, suporte no ESP-IDF, suporte no Arduino Core, certificações e horizonte de fabricação. O datasheet do SoC e o datasheet do módulo são ambos necessários, porque o módulo pode impor limites de antena, flash, PSRAM e GPIO.

## Segurança

As variantes modernas oferecem recursos como Secure Boot, flash encryption, aceleradores criptográficos, eFuse e mecanismos de isolamento. A presença do recurso não significa que o produto esteja protegido. O projeto precisa provisionar chaves, definir o estado de produção, proteger o processo de atualização e impedir que credenciais de desenvolvimento sejam reutilizadas.

## Fontes primárias

- [ESP32 SoCs](https://www.espressif.com/en/products/socs)
- [ESP32 Modules](https://www.espressif.com/en/products/modules/)
- [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [Matriz de recursos de segurança ESP](https://docs.espressif.com/projects/esp-product-security/en/latest/security-features.html)
