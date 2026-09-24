# IPv4

IPv4 usa endereços de 32 bits. Um prefixo CIDR separa bits de rede e de host,
permitindo subdividir redes sem depender do antigo modelo de classes.

## Endereçamento

Em `192.168.1.0/24`, os 24 primeiros bits identificam a rede e os oito
restantes identificam endereços dentro dela. O endereço de rede é obtido pelo
AND entre endereço e máscara; o broadcast usa os bits de host definidos como
um. A quantidade de hosts depende do prefixo e de reservas do contexto.

Os blocos privados RFC 1918 não são roteados na internet pública. NAT pode
permitir que hosts privados iniciem conexões, mas não substitui endereçamento,
roteamento ou firewall como modelo de segurança.

## Roteamento

O host escolhe uma rota por longest prefix match e usa a rota default quando
nenhuma rota mais específica corresponde. A atribuição de endereço não cria
automaticamente conectividade: gateway, rota de retorno, vizinhança e filtros
também precisam estar corretos.

## Relações

- [IPv6](ipv6.md) usa espaço de endereçamento e descoberta diferentes.
- [Interfaces e rotas](../../interfaces-rotas-e-l2-no-linux.md) mostra a operação
  no Linux.
- [Modelo TCP/IP](tcp-ip.md) posiciona IPv4 na pilha.

## Fontes primárias

- [RFC 791](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 4632](https://www.rfc-editor.org/rfc/rfc4632)
- [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)
