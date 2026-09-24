# Interface de rede

Uma interface é a representação que o kernel usa para enviar e receber
tráfego. Ela pode corresponder a hardware, loopback, bridge, veth, túnel,
VLAN, WireGuard ou outra implementação virtual.

## Estado

`ip link` mostra nome, índice, tipo, MTU e estado administrativo. `UP`
indica que o operador habilitou a interface; `LOWER_UP` indica que a camada
inferior possui portadora ou ligação lógica. Uma interface pode estar UP sem
ter conectividade funcional.

`ip address` mostra endereços e escopos. Uma interface pode possuir vários
endereços, e o endereço escolhido para uma conexão depende de rota e regras de
seleção de origem.

## Diagnóstico

Confirme existência e estado, endereços, MTU, vizinhança, rota e firewall.
Quando existe encapsulamento, reserve MTU para cabeçalhos adicionais ou o
tráfego pode ser fragmentado ou descartado por Path MTU.

## Relações

- [Rota](route.md) decide o próximo salto.
- [NDP e vizinhança](neighbor.md) resolve o endereço local.
- [Interfaces, rotas e camada 2](../interfaces-rotas-e-l2-no-linux.md) reúne
  a aplicação dessas primitivas.

## Fonte primária

- [ip-link](https://man7.org/linux/man-pages/man8/ip-link.8.html)
