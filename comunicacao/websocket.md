# WebSocket

WebSocket é um protocolo para comunicação bidirecional persistente entre um
cliente e um servidor. Ele é definido pelo [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455)
e costuma ser usado quando os dois lados precisam enviar mensagens depois que a
conexão foi estabelecida, sem criar uma nova requisição HTTP para cada evento.

## Abertura da conexão

Em aplicações web, o cliente inicia uma requisição HTTP com o mecanismo de
upgrade para WebSocket. Se o servidor aceitar, a negociação termina e os dois
lados passam a trocar frames do protocolo. `ws` representa uma conexão sem TLS;
`wss` usa TLS e é a forma adequada para aplicações expostas.

O handshake não transforma HTTP em uma sessão autenticada por si só. A
aplicação ainda precisa validar origem, credenciais, autorização e escopo da
conexão. Cookies, tokens, mTLS ou uma sessão já estabelecida podem participar
desse processo, conforme o desenho.

## Ciclo de vida

Uma conexão tem estados de abertura, funcionamento e encerramento. Durante o
funcionamento, mensagens de texto ou binárias são enviadas em ambas as
direções. Frames de ping e pong ajudam a detectar conexões quebradas e
manter a sessão ativa. O fechamento deve carregar um código e, quando
apropriado, uma razão que ajude o cliente a decidir se deve reconectar.

O protocolo entrega ordenação dentro de uma conexão TCP, mas não fornece
persistência de mensagens, confirmação de processamento, replay ou exatamente
uma entrega. Se o negócio exige essas propriedades, elas precisam ser
implementadas sobre o transporte, com identificadores de mensagem, cursor,
acknowledgement, deduplicação e recuperação de estado.

## Quando usar

WebSocket é adequado para colaboração em tempo real, presença, notificações,
painéis operacionais, jogos e interfaces que precisam receber alterações com
baixa latência. Ele também pode transportar eventos de uma sessão autenticada
que já foi autorizada para um recurso específico.

HTTP convencional ou SSE pode ser mais simples quando somente o servidor envia
eventos. Long polling pode ser suficiente em ambientes que não suportam
conexões persistentes. WebRTC é outra categoria, orientada a comunicação entre
pares de mídia ou dados, e normalmente precisa de sinalização separada.

## Escala e operação

Cada conexão consome memória, descritores, buffers e trabalho de heartbeat.
O servidor deve impor limites de tamanho, taxa, tempo ocioso e número de
conexões. O backpressure precisa ser explícito: um consumidor lento não pode
fazer o servidor acumular dados indefinidamente.

Quando há várias réplicas, uma conexão permanece ligada a uma instância. O
balanceador pode precisar de afinidade, ou as instâncias podem compartilhar
presença e mensagens por um broker. Pub/sub resolve distribuição de eventos,
mas não substitui autorização nem confirma que o cliente processou a
mensagem.

Proxies e gateways precisam encaminhar o upgrade, preservar os cabeçalhos
necessários e ter timeouts compatíveis com conexões longas. Idle timeout,
deploy, queda de uma réplica e alteração de credenciais devem fazer parte dos
testes. O cliente deve reconectar com backoff e revalidar a sessão, sem criar
um loop agressivo.

## Segurança

Valide a origem conforme o modelo de ameaça, mas não trate `Origin` como única
prova de autorização. Valide a identidade no servidor, associe cada conexão a
um tenant e recurso permitido e rejeite mensagens fora do schema. Proteja
contra abuso de tamanho, frequência, fanout e duração. Não coloque segredos
em URLs ou mensagens que podem ser registradas por proxies.

## Fontes

- [RFC 6455, The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455)
- [WebSocket na MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [WebRTC](webrtc.md)
- [Comunicação em tempo real](tempo-real/index.md)
