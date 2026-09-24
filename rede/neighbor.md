# NDP e vizinhança

A tabela de vizinhança associa endereços de rede a endereços de enlace no
próximo salto local. ARP cumpre esse papel para IPv4 e Neighbor Discovery,
sobre ICMPv6, cumpre o papel correspondente em IPv6.

## Estados

`ip neigh` mostra estados como REACHABLE, STALE, INCOMPLETE e FAILED.
REACHABLE indica confirmação recente; STALE pode ser reutilizado enquanto uma
nova confirmação ocorre; INCOMPLETE indica resolução pendente; FAILED indica
que a resolução não obteve resposta.

## Failure modes

Uma entrada correta não prova que o destino remoto está acessível. VLAN,
bridge, MTU, firewall, rota ou o próprio host podem falhar depois da
resolução. Uma entrada FAILED pode vir de ausência de vizinho, filtro de
ICMP/ARP, interface errada ou gateway incorreto.

Em IPv6, filtrar ICMPv6 sem distinguir Neighbor Discovery quebra a capacidade
de descobrir vizinhos e roteadores. A política precisa permitir as mensagens
necessárias ao funcionamento da rede.

## Relações

- [IPv4](fundamentos/ipv4.md) usa ARP no enlace local.
- [IPv6](fundamentos/ipv6.md) usa NDP.
- [Interface de rede](interface.md) fornece a interface consultada.

## Fontes primárias

- [ARP](https://www.rfc-editor.org/rfc/rfc826)
- [Neighbor Discovery](https://www.rfc-editor.org/rfc/rfc4861)
