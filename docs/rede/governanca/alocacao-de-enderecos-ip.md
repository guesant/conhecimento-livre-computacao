# Mapa de alocação e reserva de endereços IP

Um endereço IP não é comprado da mesma forma que um domínio. Endereços
privados podem ser escolhidos dentro dos blocos reservados para redes internas.
Endereços públicos são recursos coordenados globalmente e normalmente chegam
ao usuário por um provedor de acesso, uma cloud, um datacenter ou uma
organização que recebeu um bloco de um registro regional.

## Reservar um IP privado

Em uma rede interna, escolha um plano sem sobreposição e documente a relação
entre sub-rede, gateway, DHCP, DNS e firewall. Uma reserva DHCP associa um
endereço a um identificador do cliente, normalmente um endereço MAC ou um
identificador de lease. Um endereço estático configurado no host não é uma
reserva DHCP e pode colidir se o intervalo não estiver separado.

Uma prática comum é reservar um intervalo para leases dinâmicos, outro para
endereços estáticos e outro para infraestrutura. A divisão é uma convenção
administrativa; o que evita conflito é a autoridade única sobre a alocação e a
validação contra o inventário.

## Obter um IPv4 público

Para um site ou uma API pequena, o caminho normal é contratar um IP estático do
provedor de Internet, da cloud ou do provedor de hospedagem. O contrato deve
esclarecer se o endereço é dedicado, se pode ser mantido durante migração, se
há filtro de portas, se existe PTR reverso, qual é o custo e o que acontece se
o serviço for cancelado.

Uma cloud pode chamar o recurso de endereço reservado, elástico ou flutuante.
Isso normalmente significa que o cliente pode associar o endereço a outro
recurso dentro da plataforma, não que ele se tornou proprietário do espaço
global. O endereço continua sujeito às regras do provedor e pode ser devolvido.

IPv4 público é escasso. Comprar endereços de terceiros em um mercado secundário
exige due diligence sobre titularidade, histórico de abuso, reputação, registro
regional, contrato de transferência, anúncios BGP e resolução reversa. Um bloco
que aparece disponível em um anúncio comercial pode estar filtrado ou ter
histórico que prejudica e-mail e reputação da aplicação.

## Obter um bloco e anunciar uma rede

Uma organização com necessidade própria e justificável pode buscar recursos de
numeração por meio do registro regional, de um Local Internet Registry ou de
um provedor que patrocine a conectividade. Na América Latina e no Caribe, o
LACNIC coordena IPv4, IPv6 e ASNs conforme políticas da comunidade. A IANA
mantém os registros globais e delega blocos aos RIRs; ela não funciona como uma
loja que vende um IPv4 isolado para qualquer usuário final.

Anunciar um bloco próprio na Internet exige mais do que possuir endereços. A
organização normalmente precisa de conectividade de trânsito ou peering, um ASN,
roteadores, BGP, filtros, documentação de contatos e controles de origem como
RPKI e ROA. Um provedor de hospedagem pode anunciar o bloco em nome do cliente,
mas a responsabilidade operacional e contratual precisa ser explícita.

IPv6 costuma ser obtido como um prefixo delegado pelo provedor ou pelo registro
regional. O planejamento deve considerar sub-redes por local e VLAN, anúncio,
renumeração, DNS, firewall e dependência de múltiplos upstreams. Receber um
`/64` para um único enlace não é o mesmo que receber um prefixo para toda uma
organização.

## Reverse DNS

O titular ou provedor que controla a delegação reversa configura registros PTR
para os endereços públicos. O cliente precisa solicitar essa configuração ou
receber acesso à zona reversa; possuir um domínio direto não concede controle
automático sobre o PTR. Reverse DNS é particularmente importante para servidores
de e-mail, diagnóstico e identificação operacional.

## O que pedir ao provedor

Antes de contratar, confirme:

- se o IP é dedicado, estático e roteável;
- se IPv4 e IPv6 são oferecidos e em qual prefixo;
- se o endereço pode ser movido entre recursos ou provedores;
- quem controla PTR, RDAP, BGP e RPKI;
- quais portas e protocolos são filtrados;
- qual é a política de abuso, mitigação e bloqueio;
- se há logs, suporte, SLA, backup e caminho de recuperação;
- se o bloco pode ser anunciado por outro upstream em uma migração.

## Fontes primárias

- [IANA number resources](https://www.iana.org/numbers)
- [IANA IPv4 address space](https://www.iana.org/assignments/ipv4-address-space)
- [IANA special-purpose address registries](https://www.iana.org/assignments/iana-ipv6-special-registry)
- [LACNIC](https://www.lacnic.net/pt/web/lacnic/acerca-lacnic)
- [RFC 1918, endereços privados](https://www.rfc-editor.org/rfc/rfc1918)
- [RFC 7020, sistema de registros de Internet](https://www.rfc-editor.org/rfc/rfc7020)
