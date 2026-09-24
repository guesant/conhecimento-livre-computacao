# IPv6

IPv6 usa endereços de 128 bits, elimina broadcast e usa multicast e Neighbor
Discovery para funções que em IPv4 dependem de broadcast ou ARP.

## Endereçamento

SLAAC permite que hosts construam endereços a partir de Router Advertisements.
Uma interface pode ter endereços link-local, ULA e globais ao mesmo tempo.
Sub-redes normalmente usam prefixo /64, e um prefixo delegado maior permite
organizar múltiplas redes.

ULA fornece endereços estáveis para redes internas. Prefixos globais podem
mudar conforme a delegação do provedor, portanto o plano interno não deve
depender de um prefixo externo que pode ser rotacionado.

## Descoberta e firewall

NDP opera sobre ICMPv6 e resolve vizinhos, roteadores e parâmetros de rede.
Bloquear ICMPv6 inteiro quebra descoberta e Path MTU Discovery. IPv6 não usa
NAT como requisito estrutural, então firewall deve negar conexões de entrada
explicitamente conforme a política.

## Relações

- [IPv4](ipv4.md) usa ARP e broadcast no modelo tradicional.
- [Interfaces e rotas](../../interfaces-rotas-e-l2-no-linux.md) mostra o host.
- [NDP e vizinhança](../neighbor.md) detalha a descoberta local.

## Fontes primárias

- [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200)
- [RFC 4861](https://www.rfc-editor.org/rfc/rfc4861)
- [RFC 4862](https://www.rfc-editor.org/rfc/rfc4862)
