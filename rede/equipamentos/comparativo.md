# Comparação entre access point, modem, switch e roteador

Esses nomes descrevem responsabilidades diferentes, embora um produto residencial possa reunir todas elas no mesmo gabinete.

## Access point

O access point, AP, fornece uma rede sem fio baseada em IEEE 802.11. Ele associa estações, anuncia um ou mais SSIDs, aplica autenticação e criptografia do enlace sem fio e normalmente faz bridge dos quadros para uma rede cabeada ou para outro nó de distribuição.

Um AP não precisa ser o gateway IP da rede. Ele pode operar em uma LAN que possui um roteador separado. Em uma rede mesh, vários APs podem cooperar com enlaces de backhaul e controladores, mas continuam sendo pontos de acesso sem fio, não necessariamente roteadores independentes.

## Modem

Modem é a contração de modulador e demodulador. Ele adapta dados para o meio de acesso do provedor, como cobre telefônico, cabo coaxial ou rádio. Em fibra, o equipamento equivalente pode ser uma ONT ou ONU, embora produtos residenciais frequentemente chamem todo o conjunto de "modem".

O modem pode entregar um enlace de camada 2 ou uma interface IP ao equipamento seguinte. Ele não precisa oferecer NAT, Wi-Fi ou firewall. Quando esses recursos existem, pertencem a outras funções do mesmo equipamento.

## Switch

Um switch Ethernet encaminha quadros com base em endereços MAC e em sua tabela de encaminhamento. Ele conecta hosts, servidores, APs, roteadores e outros switches dentro de uma LAN ou de um domínio de bridge.

Switches gerenciáveis podem implementar VLAN, trunk, STP, LACP, QoS, 802.1X, espelhamento, telemetria e roteamento de camada 3. Isso não elimina a distinção conceitual: quando ele roteia entre VLANs, está executando também uma função de roteador.

## Roteador

Um roteador encaminha pacotes IP entre interfaces e redes. Ele escolhe o próximo salto a partir de prefixos, métricas e políticas. Pode usar rotas estáticas, OSPF, IS-IS, BGP ou outros mecanismos, além de implementar ACLs, NAT, VPN, DHCP, firewall e QoS.

O roteador normalmente separa domínios de broadcast. Um host pode enviar tráfego para seu gateway padrão quando o destino está fora da sub-rede local. Dentro da mesma rede, a entrega pode ser feita pelo switch e por mecanismos de vizinhança, como ARP ou NDP.

## O produto residencial multifunção

Um "roteador Wi-Fi" doméstico pode conter:

1. modem, ONT ou interface de uplink;
2. roteador IPv4 e IPv6;
3. NAT e firewall stateful;
4. switch Ethernet;
5. access point 802.11;
6. cliente DHCP, servidor DHCP e encaminhador DNS;
7. painel Web, aplicativo, atualização e telemetria.

O diagnóstico deve identificar qual função falhou. Sinal de rádio ruim não é resolvido por uma rota estática. Falha de sincronização do modem não é resolvida alterando o SSID. Um host que alcança o gateway, mas não resolve nomes, pode estar com problema no DNS, não no switch.

## Fonte primária

- [RFC 1812, requisitos para roteadores IPv4](https://datatracker.ietf.org/doc/html/rfc1812)
- [IEEE 802.11, redes locais sem fio](https://www.ieee802.org/11/abt80211.html)
- [IEEE 802.1Q, bridges e VLANs](https://standards.ieee.org/ieee/802.1Q/10323/)
