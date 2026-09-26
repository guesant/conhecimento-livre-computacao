# VLAN

VLAN, definida pelo IEEE 802.1Q, marca quadros Ethernet com uma tag para que
um único switch físico carregue múltiplos domínios de broadcast isolados. Uma
porta access pertence a uma VLAN e entrega quadros sem tag ao equipamento
final. Uma porta trunk carrega várias VLANs e preserva a identificação para o
próximo switch.

## Limites e roteamento

A identificação de VLAN usa 12 bits e permite 4094 segmentos utilizáveis.
Esse limite é suficiente para muitas redes locais, mas pode ser pequeno em
ambientes multi-tenant. Uma VLAN não atravessa um roteador por si só: os dois
lados precisam de adjacência de camada 2 ou de uma tecnologia de túnel.

O isolamento de broadcast não substitui uma política de firewall. Quando duas
VLANs precisam se comunicar, o tráfego passa por roteamento de camada 3 e
deve ser filtrado como qualquer outra comunicação entre redes.

## Relação com o Linux

No Linux, interfaces VLAN aparecem como interfaces virtuais associadas a uma
interface física ou bridge. A configuração pode ser feita pelo gerenciador de
rede adotado pelo host, mas o modelo subjacente continua sendo uma tag
802.1Q.

## Continue por aqui

[VXLAN](vxlan.md) estende uma rede de camada 2 sobre uma rede de camada 3.
[Interfaces, rotas e camada 2](../../interfaces-rotas-e-l2-no-linux.md)
mostra como essas interfaces participam do caminho de um pacote.
