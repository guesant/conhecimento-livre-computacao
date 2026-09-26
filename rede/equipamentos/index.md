# Equipamentos de rede

Equipamentos de rede não têm todos a mesma função. Um access point fornece acesso sem fio a uma rede local; um modem adapta a rede do assinante ao meio de acesso do provedor; um switch encaminha quadros dentro de uma rede; e um roteador encaminha pacotes entre redes diferentes.

Um equipamento comercial pode combinar várias dessas funções. Um dispositivo vendido como “roteador Wi-Fi residencial” normalmente contém modem ou ONT, roteador IP, firewall, switch Ethernet, access point, DHCP, DNS encaminhador, NAT e uma interface de gerenciamento. A embalagem não deve ser usada como classificação técnica.

## Comparação rápida

| Componente | Unidade principal | Onde atua | Responsabilidade |
| --- | --- | --- | --- |
| [Access point](access-point.md) | Quadros 802.11 | Acesso sem fio e bridge local | Conectar estações Wi-Fi à rede de distribuição |
| [Modem](modem.md) | Sinais e símbolos do meio de acesso | Enlace entre o cliente e o provedor | Modulação, demodulação e sincronização do enlace |
| [Switch](switch.md) | Quadros e endereços MAC | LAN ou data center | Comutação dentro de um domínio de camada 2 |
| [Roteador](roteador.md) | Pacotes IP e prefixos | Entre sub-redes, ASs ou redes de serviço | Encaminhamento, roteamento e políticas de camada 3 |
| Firewall | Fluxos, sessões e políticas | Entre zonas de confiança | Permitir, bloquear, inspecionar ou traduzir tráfego |
| Load balancer | Conexões e requisições | Frente de serviços | Distribuir tráfego entre backends |

## Hardware de rede

Além dos equipamentos principais, uma rede utiliza placas de rede, transceptores, módulos ópticos, cabos de cobre ou fibra, antenas, fontes, sistemas de energia, racks, sensores e mecanismos de sincronização. O desempenho final depende da combinação entre capacidade de portas, buffers, CPU, memória, ASICs, rádio, óptica, temperatura, energia e software.

Uma NIC pode operar como interface de um host, de um servidor ou de um equipamento intermediário. Um transceptor converte sinais entre a interface elétrica ou óptica e o meio físico, mas não toma decisões de roteamento. Um cabo ou enlace pode suportar determinada velocidade sem que o equipamento conectado consiga processar o tráfego nessa taxa.

## Software e firmware

O equipamento também é um sistema computacional. Seu firmware ou sistema operacional implementa drivers, tabelas MAC, tabelas de rotas, protocolos de controle, autenticação, filtros, telemetria, logs e uma interface de administração. Alguns equipamentos usam um sistema operacional de rede completo; outros usam firmware embarcado com funções restritas.

As funções costumam ser divididas entre:

- plano de dados, que encaminha quadros ou pacotes em alta velocidade;
- plano de controle, que aprende vizinhos, calcula rotas, negocia sessões e constrói tabelas;
- plano de gerenciamento, que recebe configuração, expõe métricas, registra eventos e aplica políticas;
- plano de segurança, que autentica operadores, filtra tráfego, valida atualizações e protege segredos.

Em uma rede IP aparecem ainda software de host e serviços distribuídos, como Ethernet, Wi-Fi, ARP, NDP, DHCP, DNS, IPv4, IPv6, TCP, UDP, QUIC, TLS, HTTP, BGP, OSPF, VPN, NAT, RADIUS, SNMP, syslog e APIs de automação. Nem todo equipamento implementa todos eles.

## Equipamento multifunção

Integrar funções reduz quantidade de caixas e simplifica uma instalação pequena, mas concentra domínio de falha. Se o único equipamento combina modem, roteador, switch, access point e firewall, uma atualização ou falha elétrica pode interromper todas as camadas simultaneamente.

Separar funções facilita capacidade, substituição e diagnóstico. Em contrapartida, aumenta quantidade de enlaces, credenciais, configurações, pontos de monitoramento e interfaces entre equipes ou fornecedores.

## Fontes primárias

- [RFC 1122, requisitos para hosts e gateways](https://datatracker.ietf.org/doc/html/rfc1122)
- [RFC 1812, requisitos para roteadores IPv4](https://datatracker.ietf.org/doc/html/rfc1812)
- [IEEE 802 LAN/MAN Standards Committee](https://www.ieee802.org/)
