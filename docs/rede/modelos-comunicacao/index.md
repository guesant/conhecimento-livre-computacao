# Modelos de comunicação

Um modelo de comunicação descreve como participantes trocam dados e dividem
responsabilidades. Cliente-servidor e peer-to-peer, ou P2P, são modelos
lógicos. Eles podem usar os mesmos protocolos de transporte e coexistir na
mesma aplicação. Não são sinônimos de topologia física, de tipo de cabo ou de
uma tecnologia específica de nuvem.

## Modelos principais

- [Cliente-servidor](cliente-servidor.md) atribui a um serviço a
  responsabilidade de receber pedidos, manter estado ou oferecer recursos.
- [Peer-to-peer](p2p.md) permite que participantes equivalentes consumam e
  ofereçam recursos, sem exigir um servidor central para toda a comunicação.

Uma aplicação pode combinar os dois. Um sistema P2P pode usar um servidor para
descoberta e autenticação, enquanto os dados passam entre os peers. Um sistema
cliente-servidor pode permitir conexões diretas entre clientes para mídia,
com o servidor mantendo sinalização e autorização.

## Como escolher um modelo

Avalie descoberta, autenticação, autorização, estado, disponibilidade,
observabilidade, NAT traversal, armazenamento, consistência, privacidade e
controle de abuso. Centralizar facilita governança e auditoria, mas cria
dependência e um alvo concentrado. Distribuir aumenta resiliência ou escala em
alguns cenários, mas torna identidade, revogação, atualização e diagnóstico
mais difíceis.

## Relações

O modelo de comunicação deve ser relacionado ao [TCP/IP](../fundamentos/tcp-ip.md),
ao [roteamento](../roteamento/index.md), ao [DNS](../dns/resolver.md) e às
[redes móveis](../redes-moveis/index.md), mas não substitui esses conceitos.
