# IPv4

IPv4 usa endereços de 32 bits. Um prefixo CIDR separa bits de rede e de host,
permitindo subdividir redes sem depender do antigo modelo de classes.

## Endereçamento

Em `192.168.1.0/24`, os 24 primeiros bits identificam a rede e os oito
restantes identificam endereços dentro dela. O endereço de rede é obtido pelo
AND entre endereço e máscara; o broadcast usa os bits de host definidos como
um. A quantidade de hosts depende do prefixo e de reservas do contexto.

### Classes históricas

Antes do CIDR, o endereçamento era descrito por classes. A classe A usava
prefixo `/8` para redes cujo primeiro octeto ficava entre 1 e 126; a classe B
usava `/16` para os primeiros octetos entre 128 e 191; e a classe C usava `/24`
para valores entre 192 e 223. A classe D, entre 224 e 239, foi associada a
multicast. A faixa 240 a 255 ficou reservada para uso futuro, historicamente
chamada classe E. `0.0.0.0/8` e `127.0.0.0/8` possuem usos especiais e não devem
ser tratados como redes comuns.

Classes não são o modelo usado para planejar redes atuais. CIDR permite, por
exemplo, `/20`, `/27` ou `/30`, independentemente das antigas fronteiras A, B e
C. Os nomes ainda aparecem em documentação antiga, em equipamentos legados e
na descrição histórica de multicast, mas não devem determinar a máscara de um
novo projeto.

### Endereços especiais

Endereços privados RFC 1918 são `10.0.0.0/8`, `172.16.0.0/12` e
`192.168.0.0/16`. Eles podem ser usados em redes internas sem coordenação
global, mas precisam ser traduzidos ou encapsulados para alcançar a Internet.
As faixas de documentação `192.0.2.0/24`, `198.51.100.0/24` e `203.0.113.0/24`
devem ser usadas em exemplos, não em uma rede produtiva.

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
- [CIDR e subnetting](cidr-e-subnetting.md) mostra como calcular prefixos,
  máscaras e sub-redes.
- [Broadcast e multicast](broadcast-multicast.md) diferencia destinos locais,
  grupos e endereços unicast.
- [Interfaces e rotas](../../interfaces-rotas-e-l2-no-linux.md) mostra a operação
  no Linux.
- [Modelo TCP/IP](tcp-ip.md) posiciona IPv4 na pilha.

## Fontes primárias

- [RFC 791](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 4632](https://www.rfc-editor.org/rfc/rfc4632)
- [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)
