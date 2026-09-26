# WebRTC

WebRTC é um conjunto de APIs e protocolos para comunicação em tempo real entre
aplicações, especialmente navegadores. Ele pode transportar áudio, vídeo e dados
entre peers, mas não define sozinho descoberta de usuários, autenticação, sinalização,
autorização, persistência ou modelo de negócio.

## Componentes da arquitetura

Uma aplicação WebRTC normalmente separa responsabilidades:

| Componente | Responsabilidade |
| --- | --- |
| Aplicação | Identidade, salas, permissões, estado e experiência do usuário |
| Sinalização | Trocar ofertas, respostas, candidatos e metadados de sessão |
| Peer connection | Negociar e manter a sessão de mídia ou dados |
| ICE | Procurar um caminho de rede viável entre os participantes |
| STUN | Ajudar a descobrir o endereço reflexivo do peer |
| TURN | Repassar o tráfego quando conexão direta não é possível |
| Codecs e RTP | Codificar, transportar e sincronizar mídia |
| DataChannel | Transportar dados entre os peers |

Sinalização fica deliberadamente fora do núcleo do WebRTC. Pode usar HTTPS, WebSocket,
SSE, uma fila ou outro mecanismo. Essa separação é flexível, mas transfere para a
aplicação o dever de autenticar mensagens e impedir que um usuário injete candidatos,
ingresse em uma sala indevida ou reutilize uma sessão expirada.

## Estabelecimento de uma sessão

O iniciador cria uma oferta contendo capacidades e candidatos. A outra parte responde
com suas capacidades. Os candidatos podem ser endereços locais, reflexivos obtidos por
STUN ou relay obtidos por TURN. O ICE testa pares de candidatos e escolhe um caminho
que funcione segundo as políticas de conectividade.

O caminho pode ser direto entre os peers ou passar por TURN. Conexão direta tende a
reduzir custo de relay, mas pode expor informações de rede aos participantes e falhar
em NATs restritivos. TURN aumenta a previsibilidade da conectividade, porém consome
banda e torna o serviço relay uma dependência operacional.

## Mídia e dados

Tracks representam fluxos de áudio ou vídeo e são negociados com os codecs aceitos.
Uma aplicação de chamada precisa tratar captura, permissões, mute, troca de câmera,
perda de pacotes, jitter, adaptação de bitrate, eco, sincronização e encerramento.

DataChannel fornece comunicação de dados entre peers. Sua configuração pode priorizar
ordenação e entrega confiável ou aceitar perda e menor latência, dependendo do caso de
uso. Um canal para controle de jogo, por exemplo, possui requisitos diferentes de um
canal que transfere um arquivo.

## Segurança e privacidade

WebRTC usa mecanismos criptográficos para proteger a sessão, mas a aplicação ainda
precisa autenticar os participantes e autorizar cada ação. HTTPS na página não substitui
controle de sala, expiração de tokens, validação de origem, política de conteúdo e
proteção contra abuso.

Os candidatos ICE podem revelar endereços locais ou reflexivos conforme o navegador,
a configuração e o caminho escolhido. O uso de TURN reduz exposição direta entre
peers, mas não elimina logs, metadados ou a necessidade de proteger o relay.

Não registre SDP, candidatos, tokens ou payloads de dados sem necessidade. Quando a
telemetria precisar correlacionar uma chamada, use identificadores de sessão não
secretos e retenção limitada.

## Operação

Uma implantação precisa dimensionar TURN por banda concorrente, e não apenas por
quantidade de usuários cadastrados. Monitore tentativas de conexão, tempo até conexão,
uso de relay, falhas ICE, perda, jitter, RTT, bitrate, encerramentos e capacidade do
broker de sinalização.

Teste redes corporativas, NATs restritivos, IPv4 e IPv6, mudanças de rede móvel,
permissões negadas, suspensão da aba, troca de dispositivo e reconexão. A aplicação
deve mostrar estados distintos para sinalização indisponível, ICE sem caminho, relay
sem capacidade e sessão encerrada pelo outro participante.

## O que WebRTC não resolve

WebRTC não é banco de dados, fila, sistema de presença, serviço de autenticação nem
protocolo de sincronização de documentos. Ele também não garante que uma conexão direta
será possível, que o codec será comum a todos os clientes ou que uma sessão continuará
viva durante uma mudança de rede.

Para colaboração, combine WebRTC com um modelo de estado, autorização e persistência.
Para publicação de vídeo, compare-o com CDN e streaming segmentado. Para dados entre
servidores, compare-o com RPC, QUIC ou filas, considerando observabilidade e operação.

## Relações

- [Comunicação](index.md) separa IPC, RPC, formatos e comunicação assíncrona.
- [Peer-to-peer](../rede/modelos-comunicacao/p2p.md) explica o modelo de participantes.
- [Snowflake](../rede/censura/snowflake.md) usa WebRTC como transporte anticensura.

## Fontes

- [W3C WebRTC 1.0](https://www.w3.org/TR/webrtc/)
- [RFC 8445, Interactive Connectivity Establishment](https://www.rfc-editor.org/rfc/rfc8445.html)
- [RFC 8489, Session Traversal Utilities for NAT](https://www.rfc-editor.org/rfc/rfc8489.html)
- [RFC 8656, Traversal Using Relays around NAT](https://www.rfc-editor.org/rfc/rfc8656.html)
- [RFC 8831, WebRTC Data Channels](https://www.rfc-editor.org/rfc/rfc8831.html)
