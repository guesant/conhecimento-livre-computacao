# Access point

Um access point, AP, é o componente que fornece acesso de rádio a uma rede IEEE 802.11. Ele atende estações sem fio, anuncia um ou mais SSIDs, negocia associação e autenticação e encaminha quadros para um sistema de distribuição.

## Hardware

Um AP normalmente contém rádios, antenas, filtros, processadores, memória, interfaces Ethernet e firmware. A quantidade de rádios, bandas, cadeias MIMO, capacidade de processamento, alimentação PoE e portas de uplink limita a capacidade real da célula.

O AP pode usar Ethernet como backhaul ou rádio para alcançar outro nó. A velocidade anunciada do Wi-Fi não é a capacidade disponível para cada cliente. Ela depende de largura de canal, modulação, distância, interferência, airtime compartilhado, número de estações e capacidade do backhaul.

## Software

O firmware implementa a camada MAC e PHY suportada, associação, roaming, seleção de canal, potência, QoS, segurança e gerenciamento. Em uma implantação corporativa, um controlador ou sistema de gerenciamento pode distribuir configuração, atualizar firmware, coletar métricas e coordenar canais.

Um AP pode operar em bridge, em modo mesh, como repetidor, como ponto de acesso isolado ou como parte de uma arquitetura controlada. O modo escolhido altera o caminho dos quadros, a capacidade útil e o domínio de falha.

## AP não é roteador

Um AP pode entregar conectividade sem fio sem fornecer gateway, NAT ou DHCP. Se o AP estiver em bridge, o endereço IP do cliente pode vir de um servidor DHCP em outro equipamento. Produtos domésticos frequentemente combinam AP e roteador, o que cria a impressão de que as duas funções são inseparáveis.

## Segurança

A implantação deve usar autenticação e criptografia adequadas, separar redes por VLAN quando necessário, proteger a administração e controlar quais dispositivos podem ingressar. SSID oculto não substitui autenticação. Isolamento de clientes reduz comunicação lateral, mas não substitui firewall entre zonas.

## Fontes primárias

- [IEEE 802.11 Working Group](https://www.ieee802.org/11/)
- [IEEE 802.11, visão geral](https://www.ieee802.org/11/abt80211.html)
- [Wi-Fi Alliance](https://www.wi-fi.org/discover-wi-fi)
