# Peer-to-peer

Peer-to-peer, ou P2P, é um modelo em que os participantes podem consumir e
oferecer recursos. Um peer pode atuar como cliente em uma operação e como
servidor em outra. A ausência de uma autoridade central para todo o tráfego
não significa ausência de servidores auxiliares, diretórios, autoridades de
certificação ou mecanismos de coordenação.

## Formas de organização

| Forma | Característica | Exemplo de preocupação |
| --- | --- | --- |
| P2P direto | peers descobrem e conectam uns aos outros | NAT, firewall e identidade |
| P2P com diretório | um serviço ajuda a localizar peers | disponibilidade e privacidade do diretório |
| P2P estruturado | uma tabela distribuída organiza a busca | manutenção do overlay e churn |
| P2P não estruturado | busca e distribuição dependem de vizinhos ou regras locais | descoberta, spam e eficiência |
| Híbrido | servidor central coordena, peers transferem ou processam dados | fronteira de confiança entre coordenação e dados |

## Aplicações

Distribuição de arquivos, redes de conteúdo, colaboração, comunicação em
tempo real, blockchain, computação distribuída e protocolos de descoberta
podem usar P2P. WebRTC, por exemplo, permite mídia ou dados entre navegadores,
mas normalmente usa servidores de sinalização e STUN ou TURN para superar
limitações de conectividade.

## Trade-offs

P2P pode reduzir concentração de banda e melhorar disponibilidade, mas torna
mais complexos controle de identidade, revogação, moderação, atualização,
observabilidade, consistência e resposta a peers maliciosos. O protocolo
precisa lidar com peers que entram e saem, anunciam dados incorretos ou
tentam consumir sem contribuir.

Antes de escolher P2P, defina a autoridade de identidade, a forma de
descoberta, a autenticação dos dados, o mecanismo de NAT traversal, o limite de
recursos, a política de abuso e o comportamento quando poucos peers estão
disponíveis.

[WebRTC](../../comunicacao/webrtc.md) é uma implementação importante de comunicação
entre peers no navegador. [Snowflake](../censura/snowflake.md) usa WebRTC para criar
um transporte temporário entre um cliente Tor e um proxy voluntário.

## Fontes primárias

- [WebRTC specifications](https://www.w3.org/TR/webrtc/)
- [RFC 8484, DNS over HTTPS](https://www.rfc-editor.org/rfc/rfc8484)
- [RFC 4787, NAT behavioral requirements](https://www.rfc-editor.org/rfc/rfc4787)
