# Comunicação

Comunicação é o conjunto de mecanismos pelos quais componentes trocam dados,
solicitam operações e coordenam estado. Os termos usados nesse domínio
representam camadas diferentes e não devem ser tratados como sinônimos.

IPC descreve comunicação entre processos, normalmente no mesmo sistema. RPC
descreve a abstração de chamar uma operação que é executada em outro processo.
APIs e protocolos definem contratos para consumidores. Comunicação assíncrona
separa a solicitação do processamento. Streams reativos coordenam valores ao
longo do tempo.

Uma arquitetura pode combinar todos eles. Um processo pode usar IPC local para
falar com um agente, gRPC para falar com outro serviço e JSON em uma API
GraphQL voltada ao navegador.

## Categorias

- [Comunicação entre processos](ipc/index.md) trata IPC e mecanismos locais.
- [APIs e protocolos](apis/index.md) trata RPC, gRPC, JSON e GraphQL.
- [Comunicação assíncrona](assinc/index.md) trata filas, eventos e trabalho desacoplado.
- [Streams reativos](streams/index.md) trata ReactiveX e Kotlin Flow.
- [Comunicação em tempo real](tempo-real/index.md) trata WebRTC e mídia interativa.

## Como separar as camadas

| Pergunta | Conceito que responde |
| --- | --- |
| Como dois processos no mesmo host trocam dados? | IPC |
| Como representar uma chamada a uma operação remota? | RPC |
| Qual framework e transporte implementam essa chamada? | gRPC, JSON-RPC ou outro |
| Como representar dados estruturados? | JSON, Protobuf, XML ou outro formato |
| Como o cliente descreve quais dados deseja? | GraphQL ou outro modelo de consulta |
| Como os bytes chegam ao destino? | Unix socket, TCP, HTTP/2, QUIC, memória compartilhada ou outro transporte |

Confundir essas camadas causa decisões ruins. JSON não é uma alternativa direta
a gRPC: JSON é formato, enquanto gRPC é framework de RPC. GraphQL não é apenas
um formato de resposta: ele define schema, linguagem, validação e execução.

## Páginas deste domínio

- [IPC](ipc.md) explica pipes, sockets Unix, memória compartilhada, filas,
  sinais, semáforos e barramentos.
- [RPC](rpc.md) explica chamadas remotas, contratos, serialização, erros,
  streaming e operação distribuída.
- [Comunicação assíncrona](comunicacao-assincrona.md) explica filas, pub/sub,
  eventos, streaming, entrega, retry, idempotência e backpressure.
- [RPC e comunicação assíncrona](rpc-e-comunicacao-assincrona.md) compara
  respostas imediatas, trabalho em background e eventos.
- [gRPC](grpc.md) explica a implementação baseada em HTTP/2 e Protocol Buffers.
- [JSON](json.md) explica o formato textual, interoperabilidade, segurança e
  limites.
- [GraphQL](graphql.md) explica schema, operações, resolvers, introspecção e
  custos operacionais.
- [ReactiveX e Rx](reactivex.md) explica Observable, Observer, operadores, schedulers,
  hot e cold streams, backpressure, erro e cancelamento.
- [Kotlin Flow](kotlin-flow.md) explica Flow, StateFlow, SharedFlow, coroutines,
  lifecycle, cancelamento e integração com streams.

## Critérios para escolher

Comece pela fronteira do sistema. Comunicação dentro do mesmo host possui
latência, isolamento e ciclo de vida diferentes de uma chamada entre clusters.
Depois defina se o consumidor conhece operações ou dados, se precisa de
streaming, se há clientes em navegador, como o contrato evolui e qual grau de
observabilidade é necessário.

Também avalie autenticação, autorização, timeouts, cancelamento, retries,
idempotência, limite de tamanho, backpressure, compatibilidade de versões,
cache, rate limiting e comportamento quando o destinatário está indisponível.

## Relações

[Cliente-servidor](../rede/modelos-comunicacao/cliente-servidor.md) descreve
os papéis lógicos de quem solicita e quem atende. [P2P](../rede/modelos-comunicacao/p2p.md)
descreve comunicação entre participantes que podem assumir ambos os papéis.
[Filas](../dados/mensageria/filas.md) e [event
streaming](../dados/mensageria/event-streaming.md) cobrem comunicação quando
ela não precisa ser uma chamada síncrona.
