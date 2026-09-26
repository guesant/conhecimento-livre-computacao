# Arquitetura

A Internet é uma rede de redes. Hosts e servidores se conectam a redes de acesso; switches e bridges organizam segmentos locais; roteadores conectam sub-redes e sistemas autônomos; redes de transporte e backbones carregam grandes volumes; serviços como DNS, TLS, HTTP, CDN e aplicações dão significado ao tráfego.

Não existe um único "equipamento da Internet". A experiência de abrir uma página depende de uma cadeia que pode incluir a NIC do dispositivo, um access point, um switch, um modem ou ONT, um roteador residencial, a rede de acesso do provedor, roteadores metropolitanos, pontos de troca, trânsito IP, roteadores de backbone, balanceadores, servidores e software da aplicação.

## Camadas da cadeia

1. o meio físico transporta sinais elétricos, ópticos ou de rádio;
2. o enlace entrega quadros em uma rede local ou de acesso;
3. o IP endereça e encaminha pacotes entre redes;
4. o transporte entrega fluxos, datagramas ou conexões aos endpoints;
5. a aplicação usa DNS, TLS, HTTP e outros protocolos para oferecer serviços;
6. a operação controla identidade, configuração, observabilidade, segurança e capacidade.

As fronteiras não são caixas rígidas. Um dispositivo residencial combina camadas; um switch de camada 3 roteia; um firewall pode inspecionar aplicações; uma CDN termina TLS e HTTP antes de encaminhar ao origin.

## Backbone

Um backbone é uma parte de alta capacidade e alta disponibilidade que interliga redes de acesso, regiões, data centers, cidades ou sistemas autônomos. O termo descreve uma função na topologia, não um protocolo ou uma marca. Um backbone pode ser operado por uma operadora, uma empresa de conteúdo, uma universidade, um consórcio de pesquisa ou uma organização pública.

Backbones usam enlaces ópticos, sistemas DWDM, roteadores de alta capacidade, múltiplos caminhos, BGP, engenharia de tráfego, sincronização, telemetria e centros de operação. A redundância precisa existir no equipamento, no enlace, na energia, no caminho físico e na operação.

## Acesso, agregação e núcleo

Uma rede de provedor costuma separar:

- acesso, onde assinantes, empresas, torres, residências ou dispositivos entram na rede;
- agregação, onde vários enlaces de acesso são concentrados e transportados;
- núcleo ou backbone, onde grandes volumes percorrem poucos saltos de alta capacidade;
- borda, onde a rede troca tráfego com clientes, pares, IXPs, provedores de trânsito e serviços.

Os nomes variam entre organizações. A função é mais importante que o rótulo: identificar quem origina o tráfego, quem agrega enlaces, quem toma decisões de roteamento e onde as políticas de segurança são aplicadas.

## Fontes primárias

- [RFC 1122, Internet como rede de redes](https://datatracker.ietf.org/doc/html/rfc1122)
- [RFC 1812, requisitos de roteadores](https://datatracker.ietf.org/doc/html/rfc1812)
- [RFC 4271, BGP-4](https://datatracker.ietf.org/doc/html/rfc4271)
- [IX.br](../conectividade/ixp.md)
