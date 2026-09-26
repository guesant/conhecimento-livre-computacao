# Fabricantes

Fabricantes de rede não representam a mesma camada do sistema. Um switch ou ponto de acesso é um equipamento; um sistema operacional de rede fornece encaminhamento, filtragem e gerenciamento; um controlador centraliza configuração; e um appliance combina hardware, software e suporte. Comparar apenas a velocidade de portas ou a quantidade de recursos costuma esconder diferenças de operação, licenciamento, automação e ciclo de vida.

Esta área trata Cisco, TP-Link, pfSense, Netgate, MikroTik e Ubiquiti como famílias distintas. O objetivo não é criar uma lista de produtos para compra, mas explicar onde cada portfólio se encaixa, quais aplicações atende e quais restrições precisam ser verificadas antes de uma decisão.

## Como ler os portfólios

Há quatro perguntas que devem ser respondidas antes de comparar marcas:

1. qual plano precisa ser atendido: borda, campus, data center, Wi-Fi, WISP, segurança ou laboratório;
2. onde ficará o plano de controle: no equipamento, em um controlador local ou em um serviço de nuvem;
3. quais protocolos e integrações são necessários: VLAN, roteamento dinâmico, VPN, AAA, automação, telemetria e logs;
4. qual suporte e ciclo de atualização são aceitáveis para o ambiente.

Um appliance de firewall não substitui automaticamente um switch de campus, assim como um controlador Wi-Fi não substitui um sistema de roteamento de borda. Algumas plataformas reúnem funções, mas a convergência aumenta a importância de capacidade, domínio de falha e recuperação.

## Famílias documentadas

- [Cisco](cisco.md) cobre redes corporativas, data center, segurança, wireless e gerenciamento em escala.
- [TP-Link e Omada](tp-link-omada.md) cobre equipamentos residenciais, SMB e a plataforma de gerenciamento Omada.
- [pfSense](../roteamento/pfsense.md) cobre a plataforma de firewall e roteamento baseada em FreeBSD.
- [Netgate](netgate.md) cobre appliances, pfSense Plus, TNSR e suporte comercial.
- [MikroTik](mikrotik.md) cobre RouterOS, RouterBOARD, switches, wireless e conectividade LTE ou 5G.
- [Ubiquiti](ubiquiti.md) cobre UniFi, UISP e os equipamentos voltados a redes integradas e WISP.
- [Comparativo](comparativo.md) organiza os critérios de escolha sem transformar uma marca em recomendação universal.

## Interoperabilidade

Mesmo quando os equipamentos são administrados por controladores diferentes, uma rede pode ser composta por mais de um fabricante. VLANs, Ethernet, PoE, IPv4, IPv6, DHCP, DNS, BGP, OSPF, WireGuard, IPsec, RADIUS, TACACS+, SNMP, syslog e APIs são pontos de interoperabilidade, mas a implementação e o licenciamento variam.

Antes de misturar plataformas, valide o comportamento de spanning tree, LACP, MTU, LLDP, roaming Wi-Fi, QoS, listas de controle, exportação de configuração e observabilidade. A interoperabilidade do plano de dados não garante que o plano de controle ou a operação diária sejam equivalentes.

## Fontes primárias

- [Cisco products](https://www.cisco.com/site/us/en/products/index.html)
- [TP-Link Omada](https://www.tp-link.com/us/business-networking/omada/)
- [pfSense documentation](https://docs.netgate.com/pfsense/en/latest/)
- [Netgate appliances](https://www.netgate.com/appliances)
- [MikroTik products](https://mikrotik.com/products)
- [Ubiquiti](https://www.ui.com/)
