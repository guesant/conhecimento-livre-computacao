# TCP e UDP

TCP e UDP são protocolos de transporte. Ambos multiplexam aplicações por
portas, mas oferecem contratos diferentes para entrega e controle de fluxo.

## TCP

TCP estabelece uma conexão, confirma bytes, retransmite perdas, ordena o fluxo
e controla congestionamento. A aplicação recebe um stream, não mensagens
preservadas. O custo inclui handshake, estado por conexão e comportamento de
retransmissão.

## UDP

UDP entrega datagramas sem handshake, ordenação, retransmissão ou controle de
congestionamento fornecidos pelo protocolo. Ele é adequado quando a aplicação
implementa o comportamento necessário ou quando baixa latência e mensagens
independentes importam.

UDP não significa automaticamente rápido ou seguro. A aplicação precisa
definir limites, autenticação e resposta a perda. QUIC fornece transporte
confiável e criptografado sobre UDP com controle próprio.

## Diagnóstico

`ss -lntup` mostra listeners e conexões. Um timeout TCP pode vir de rota,
firewall ou ausência de listener. Em UDP, ausência de conexão estabelecida não
prova ausência de tráfego; capture datagramas e examine a resposta da
aplicação.

## Relações

- [Modelo TCP/IP](fundamentos/tcp-ip.md) posiciona o transporte na pilha.
- [IPv4](fundamentos/ipv4.md) e [IPv6](fundamentos/ipv6.md) carregam os
  segmentos ou datagramas.
- [Reverse proxy](proxy/reverse-proxy.md) pode terminar transporte e criar
  outro fluxo até o upstream.

## Fontes primárias

- [RFC 9293, TCP](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 768, UDP](https://www.rfc-editor.org/rfc/rfc768)
- [RFC 9000, QUIC](https://www.rfc-editor.org/rfc/rfc9000)
