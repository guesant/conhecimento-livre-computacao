# VLAN

VLAN, definida pelo IEEE 802.1Q, marca quadros Ethernet com uma tag para que
um único switch físico carregue múltiplos domínios de broadcast isolados. Uma
porta access pertence a uma VLAN e entrega quadros sem tag ao equipamento
final. Uma porta trunk carrega várias VLANs e preserva a identificação para o
próximo switch.

## Tagging e tipos de porta

Em uma porta trunk, o quadro normalmente recebe uma tag 802.1Q com o
identificador da VLAN. Em uma porta access, o switch associa o quadro recebido
à VLAN configurada e remove a tag antes de entregá-lo ao host. O PVID define a
VLAN atribuída a quadros que chegam sem tag. Alguns equipamentos chamam de
VLAN nativa a VLAN transmitida sem tag em um trunk.

Uma VLAN nativa compartilhada sem planejamento pode causar vazamento de tráfego
ou facilitar erros de configuração. Em trunks entre equipamentos, explicite a
lista de VLANs permitidas, confirme o comportamento de quadros sem tag e use a
mesma convenção nas duas pontas. Não use a VLAN nativa como substituto de uma
política de segurança.

## Limites e roteamento

A identificação de VLAN usa 12 bits e permite 4094 segmentos utilizáveis.
Esse limite é suficiente para muitas redes locais, mas pode ser pequeno em
ambientes multi-tenant. Uma VLAN não atravessa um roteador por si só: os dois
lados precisam de adjacência de camada 2 ou de uma tecnologia de túnel.

O isolamento de broadcast não substitui uma política de firewall. Quando duas
VLANs precisam se comunicar, o tráfego passa por roteamento de camada 3 e
deve ser filtrado como qualquer outra comunicação entre redes.

## Desenhos comuns

É comum separar usuários, servidores, gerenciamento, voz, convidados, câmeras
e dispositivos IoT em VLANs diferentes. O switch de acesso usa portas access
ou trunks para pontos de acesso e telefones IP; o switch de distribuição,
roteador ou firewall faz o roteamento entre VLANs. O DHCP pode usar escopos
separados e um relay para cada interface de camada 3.

VLAN não é uma fronteira física completa nem uma forma de criptografia. Ela
reduz o domínio de broadcast e ajuda a organizar políticas, mas ataques ao
plano de gerenciamento, erros de trunk, configuração de native VLAN e acesso
ao equipamento podem atravessar a separação. Use ACLs, firewall, autenticação
de porta e controle da administração conforme o risco.

## Relação com outras tecnologias

802.1Q é uma tecnologia de VLAN em Ethernet local. QinQ adiciona outra camada
de tags para transportar VLANs de clientes dentro de uma rede de provedor.
VXLAN transporta segmentos sobre uma rede IP e pode ser usado quando o espaço
de VLAN ou o domínio de camada 2 não atende ao desenho. Essas tecnologias não
eliminam a necessidade de roteamento, MTU, observabilidade e políticas.

## Relação com o Linux

No Linux, interfaces VLAN aparecem como interfaces virtuais associadas a uma
interface física ou bridge. A configuração pode ser feita pelo gerenciador de
rede adotado pelo host, mas o modelo subjacente continua sendo uma tag
802.1Q.

## Continue por aqui

[VXLAN](vxlan.md) estende uma rede de camada 2 sobre uma rede de camada 3.
[Interfaces, rotas e camada 2](../../interfaces-rotas-e-l2-no-linux.md)
mostra como essas interfaces participam do caminho de um pacote.

## Fonte primária

- [IEEE 802.1 Working Group](https://www.ieee802.org/1/)
