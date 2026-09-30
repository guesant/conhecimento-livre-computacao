# APIs

Uma API define como um consumidor descobre operações, envia entradas, recebe resultados e interpreta erros. Um protocolo de aplicação define a forma das mensagens e das interações. Essas responsabilidades são diferentes do transporte e também diferentes do formato isolado de uma mensagem.

## Páginas

- [RPC](../rpc.md) trata a abstração de chamar uma operação em outro processo.
- [gRPC](../grpc.md) trata uma implementação de RPC baseada em Protocol Buffers e HTTP/2.
- [JSON](../json.md) trata um formato textual de representação de dados.
- [GraphQL](../graphql.md) trata schema, operações, resolvers e seleção de dados.

JSON não é concorrente direto de gRPC, porque um é formato e o outro é framework de RPC. GraphQL também não é apenas um formato de resposta. Uma API pode usar GraphQL sobre HTTP, JSON como serialização e RPC interno entre seus serviços.

## Critérios

Defina o contrato, evolução, compatibilidade, autenticação, autorização, limites, timeouts, cancelamento, idempotência e observabilidade antes de comparar bibliotecas. A escolha do protocolo deve refletir consumidores reais, necessidade de streaming, suporte de navegadores, proxies, geração de clientes e tolerância a falhas.

## Relações

[Comunicação entre processos](../ipc/index.md) cobre o caso local. [Comunicação assíncrona](../assinc/index.md) trata operações que não precisam devolver um resultado na mesma conexão. [WebRTC](../tempo-real/index.md) cobre comunicação interativa em tempo real entre participantes.
