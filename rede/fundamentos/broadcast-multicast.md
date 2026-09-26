# Broadcast e multicast

Broadcast e multicast são formas de entregar um pacote a mais de um destino,
mas possuem semânticas e domínios diferentes. Unicast identifica um destino
individual. Broadcast alcança todos os hosts de um domínio definido. Multicast
alcança apenas os membros que ingressaram em um grupo.

## Broadcast IPv4

No IPv4, `255.255.255.255` é o limited broadcast e não deve atravessar
roteadores. Uma rede também possui um directed broadcast, obtido colocando os
bits de host em um, como `192.168.10.127` para `192.168.10.0/26`. Roteadores
normalmente bloqueiam ou não encaminham directed broadcast para reduzir abuso,
amplificação e ruído.

ARP, DHCP e algumas formas antigas de descoberta usam broadcast local. Uma
VLAN normalmente forma um domínio de broadcast, e roteá-la para outra VLAN
exige um equipamento ou serviço de camada 3. Broadcast excessivo pode consumir
capacidade de switches, access points e hosts, por isso separar domínios e
preferir mecanismos direcionados costuma melhorar a previsibilidade.

## Multicast IPv4

O espaço multicast IPv4 vai de `224.0.0.0` a `239.255.255.255`, ou `224.0.0.0/4`.
`224.0.0.0/24` é reservado para controle local e protocolos de descoberta, e
`239.0.0.0/8` é reservado para escopos administrativamente controlados. O host
entra em um grupo por mecanismos como IGMP; switches e roteadores podem usar
IGMP snooping e protocolos de roteamento multicast para evitar cópias em
portas que não têm membros.

Multicast não é simplesmente um broadcast com outro número. O grupo possui
membros, escopo e estado de encaminhamento. Firewall, switches, Wi-Fi e
provedor precisam suportar a semântica completa para que a aplicação funcione
fora de um segmento local.

## IPv6

IPv6 não possui broadcast. Descoberta de vizinhos, descoberta de roteadores e
outras funções usam multicast e ICMPv6. `ff00::/8` identifica endereços
multicast; os bits de escopo indicam se o grupo é local à interface, ao enlace,
à organização ou global. O grupo de todos os nós no enlace e os grupos de
solicited-node são exemplos importantes para a operação normal do protocolo.

Bloquear todo ICMPv6 para eliminar uma preocupação de segurança quebra NDP,
Path MTU Discovery e outras funções. A política deve permitir os tipos
necessários e bloquear tráfego incompatível com o desenho, em vez de apagar o
protocolo inteiro.

## Anycast

Anycast usa o mesmo endereço unicast em mais de um ponto e depende do
roteamento para encaminhar o cliente ao membro considerado mais próximo. Ele
não é broadcast nem multicast. DNS recursivo, CDNs e serviços distribuídos
usam anycast com frequência, mas a sessão e o estado precisam tolerar que o
caminho mude.

## Fontes primárias

- [RFC 1112, IPv4 multicast](https://www.rfc-editor.org/rfc/rfc1112)
- [RFC 2365, multicast administrativamente limitado](https://www.rfc-editor.org/rfc/rfc2365)
- [RFC 4291, arquitetura de endereçamento IPv6](https://www.rfc-editor.org/rfc/rfc4291)
- [IANA IPv4 multicast registry](https://www.iana.org/assignments/multicast-addresses)
- [IANA IPv6 multicast registry](https://www.iana.org/assignments/ipv6-multicast-addresses)
