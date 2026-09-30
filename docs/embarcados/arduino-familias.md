# Famílias de placas Arduino

As famílias Arduino organizam placas por formato, capacidade, conectividade e cenário de uso. O nome da família não garante que todas as placas compartilhem a mesma CPU, pinagem ou core. Antes de portar um projeto, consulte a página do modelo exato, o esquema elétrico e a definição da plataforma instalada.

## Famílias principais

| Família | Característica comum | Uso recorrente |
| --- | --- | --- |
| UNO | Formato clássico e ecossistema amplo | Ensino, prototipação e shields |
| Nano | Formato compacto e compatível com protoboard | Protótipos pequenos e integração em placas |
| Mega | Mais GPIO, memória e interfaces | Automação e projetos com muitos periféricos |
| MKR | Formato compacto com conectividade ou sensores | IoT e dispositivos de baixo consumo |
| Classic | Placas históricas com formatos e cores distintos | Educação, prototipação e compatibilidade legada |
| Portenta | Desempenho e conectividade para aplicações profissionais | Edge, automação e produtos avançados |
| Nicla | Módulos pequenos com sensores | Sensoriamento e TinyML |
| GIGA | Processamento e interfaces mais amplos | Interfaces, visão e protótipos complexos |
| Opta | Automação industrial e entradas e saídas | Controle e integração industrial |
| Modulino | Módulos plugáveis para sensores e atuadores | Expansão rápida por I2C e conectores |

## O que pertence a cada família

### UNO

A família UNO inclui o UNO R3 e revisões anteriores, UNO R4 Minima, UNO R4 WiFi, variantes WiFi e produtos recentes como UNO Q. O formato de shield é uma relação importante, mas não garante que o processador, a tensão, o core ou o sistema operacional sejam iguais. O UNO Q, por exemplo, é uma classe de computador diferente de um microcontrolador UNO tradicional.

### Nano

A família Nano inclui o Nano clássico, Nano Every, Nano 33 IoT, Nano 33 BLE, Nano 33 BLE Sense, Nano RP2040 Connect, Nano ESP32 e variantes recentes. O formato pequeno é a característica comum; CPU, rádio, sensores e suporte a MicroPython variam por placa. Carriers e conectores Nano são acessórios da família, não novos microcontroladores.

### Mega e Classic

Mega reúne placas com mais GPIO e interfaces, como Mega 2560, Due e GIGA R1 WiFi. Classic reúne placas como Leonardo, Micro e Zero que não devem ser confundidas com a linha Mega apenas por terem formato de placa semelhante. A compatibilidade de shield e biblioteca deve ser verificada por modelo.

### MKR, Portenta e Nicla

MKR prioriza formato compacto e conectividade, com placas, shields e carriers. Portenta é uma linha de módulos e placas de maior desempenho, com conectores de alta densidade e integração com outras famílias. Nicla concentra sensores e processamento em placas pequenas que normalmente trabalham com Portenta, MKR ou carriers.

### GIGA, Opta e Modulino

GIGA atende aplicações com mais processamento e interfaces. Opta é voltada a automação e controle industrial. Modulino não é uma família de placas de CPU; são módulos de sensores, atuadores e interface que expandem placas Arduino por conectores padronizados.

Kits, shields, carriers e acessórios formam categorias próprias. Eles podem ser projetados para uma família, mas não devem ser documentados como se fossem variantes do microcontrolador.

As linhas evoluem e podem ganhar novos modelos. A tabela é uma classificação de navegação, não um catálogo permanente. O [catálogo oficial de hardware](https://docs.arduino.cc/hardware) é a fonte para disponibilidade, especificações e compatibilidade atual.

## MCU, módulo e placa

Uma família de placas pode combinar microcontroladores muito diferentes. UNO R4, por exemplo, não deve ser tratado como uma simples revisão do UNO clássico, porque a plataforma de hardware, o core e alguns periféricos mudam. O mesmo vale para placas Nano e Portenta de gerações distintas.

A placa fornece uma pinagem e uma experiência de desenvolvimento. O microcontrolador define CPU, memória, timers, ADC, interfaces e limites elétricos. O core Arduino traduz parte dessas capacidades para uma API comum, mas não pode criar periféricos que o chip não possui.

## Shields, módulos e bibliotecas

Shields seguem convenções mecânicas e elétricas de uma placa, mas a compatibilidade é determinada pelos pinos, tensões e bibliotecas utilizadas. Um shield projetado para 5 V pode não ser seguro em uma placa de 3,3 V. Uma biblioteca que usa pinos fixos também pode funcionar em uma família e falhar em outra.

Em um projeto reutilizável, trate a placa como uma variante explícita. Separe a lógica de negócio da camada de GPIO, declare o mapeamento de pinos e valide a tensão, a corrente e o método de alimentação.

## Critérios de seleção

Escolha a família pelo problema, não pelo nome mais conhecido. Considere processamento, RAM, flash, interfaces, conectividade, consumo, formato, disponibilidade, certificação, depuração e política de atualização. Para protótipos educacionais, a compatibilidade de exemplos e shields pode pesar mais. Para produção, ciclo de vida, fabricação e segurança costumam dominar a decisão.

## Fontes primárias

- [Hardware Arduino](https://docs.arduino.cc/hardware)
- [Visão geral oficial do hardware Arduino](https://www.arduino.cc/en/Main/Hardware)
- [Arduino Learn](https://docs.arduino.cc/learn)
- [Arduino, suporte de hardware](https://support.arduino.cc/)
