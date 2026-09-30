# Comunicação em tempo real

Comunicação em tempo real busca reduzir latência percebida e permitir interação contínua entre participantes. A necessidade pode envolver áudio, vídeo, presença, colaboração, jogos ou telemetria. Cada cenário possui limites diferentes de atraso, jitter, perda, largura de banda, NAT traversal e privacidade.

## WebRTC

[WebRTC](../webrtc.md) fornece APIs para mídia e dados entre navegadores e aplicações compatíveis. A conexão costuma exigir sinalização, descoberta de candidatos, STUN ou TURN, negociação de codecs e políticas de permissão. A mídia pode seguir diretamente entre participantes ou passar por um relay quando a conectividade direta não for possível.

## Relações

Tempo real não implica durabilidade. Uma chamada pode ser descartada quando um participante desconecta, enquanto uma conversa persistente exige armazenamento e sincronização. [RPC](../rpc.md), [eventos](../event-bus.md) e [streams reativos](../streams/index.md) podem participar da arquitetura, mas resolvem problemas diferentes.

## Critérios

Avalie latência, jitter, perda, NAT, custo de relay, escalabilidade, gravação, moderação, autenticação, autorização e observabilidade. Não confunda baixa latência com consistência forte: um sistema colaborativo pode precisar reconciliar operações mesmo quando cada atualização chega rapidamente.
