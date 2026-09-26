# Computadores de placa única Raspberry Pi

Os computadores de placa única Raspberry Pi são pequenos computadores completos, normalmente usados com Raspberry Pi OS ou outra distribuição Linux. Eles têm CPU, memória, interfaces de armazenamento, vídeo, USB e rede em uma placa que pode ser usada como desktop, servidor headless, gateway ou plataforma educacional.

## Famílias e gerações

| Família | Modelos representativos | Característica |
| --- | --- | --- |
| Raspberry Pi flagship | Pi 1, Pi 2, Pi 3, Pi 4 e Pi 5 | Computador geral com conectores, rede e expansão |
| Raspberry Pi Zero | Zero, Zero W e Zero 2 W | Formato compacto e menor consumo |
| Raspberry Pi 400 e 500 | 400, 500 e 500+ | Computador integrado ao teclado |
| Compute Module | CM1, CM3, CM3+, CM4, CM4S, CM5 e CM Zero | System-on-Module para carrier própria |

Os computadores de teclado e Compute Modules possuem páginas separadas porque a forma física e o uso são diferentes. A tabela serve para navegação, não para substituir as especificações de cada modelo.

## Gerações flagship

O Raspberry Pi 1 estabeleceu a plataforma. Pi 2 e Pi 3 ampliaram CPU e conectividade. Pi 4 trouxe uma classe de desempenho e interfaces adequada a mais servidores e desktops. Pi 5 acrescentou desempenho significativamente maior e uma arquitetura de I/O que inclui o controlador RP1.

A compatibilidade de software não é perfeita entre gerações. Imagens, kernels, firmware, alimentação, armazenamento e periféricos devem ser avaliados para o modelo real. Um sistema que inicializa em Pi 3 pode precisar de outra configuração de kernel ou alimentação em Pi 5.

## Raspberry Pi Zero

Zero prioriza tamanho e consumo. Zero W adiciona conectividade sem fio, e Zero 2 W aumenta a capacidade de processamento mantendo o formato compacto. Os modelos possuem menos portas e recursos de expansão do que as placas flagship, por isso são adequados a gateways leves, sensores, automação e projetos compactos.

O formato pequeno não elimina as necessidades de alimentação, armazenamento e dissipação. Em um produto, avalie acesso ao conector USB, qualidade do cartão microSD, recuperação e possibilidade de atualizar o sistema remotamente.

## Boot e armazenamento

Computadores Raspberry Pi precisam de uma mídia de boot com uma imagem de sistema operacional. microSD é a opção comum; modelos mais recentes podem suportar USB Mass Storage, boot de rede e NVMe conforme o hardware e a configuração. Consulte também [métodos de boot](../../sistemas/boot/boot-methods.md) para a comparação geral.

## Critérios de escolha

Escolha a linha flagship quando precisar de mais conectores, RAM, desempenho ou expansão. Escolha Zero quando tamanho e consumo forem prioritários. Escolha Compute Module quando a placa final precisar de carrier própria, eMMC, montagem industrial ou controle mecânico do produto.

## Fontes primárias

- [Hardware de computadores Raspberry Pi](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
- [Como começar com Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [Produtos Raspberry Pi](https://www.raspberrypi.com/products/)
