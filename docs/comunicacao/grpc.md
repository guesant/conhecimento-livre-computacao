# gRPC

gRPC é um framework de Remote Procedure Call que permite a clientes e
servidores implementados em linguagens diferentes compartilhar um contrato,
gerar código e trocar mensagens. A implementação mais comum usa Protocol
Buffers para a definição da interface e HTTP/2 como transporte, mas o conceito
de gRPC é mais amplo que um formato isolado.

gRPC é particularmente usado em comunicação interna entre serviços, sistemas
poliglotas, telemetria, dispositivos e aplicações que precisam de streaming.
Ele não é automaticamente melhor que HTTP com JSON: a escolha depende do
consumidor, da interoperabilidade, do contrato, do debugging e dos requisitos
de latência.

## Contrato `.proto`

Um arquivo `.proto` descreve mensagens e serviços. O compilador `protoc` e os
plugins da linguagem geram tipos, stubs de cliente e interfaces de servidor.

```protobuf
service Catalog {
  rpc GetItem(GetItemRequest) returns (Item);
}

message GetItemRequest {
  string id = 1;
}

message Item {
  string id = 1;
  string title = 2;
}
```

O código gerado reduz a duplicação de contratos, mas não elimina a
necessidade de validar autorização, limites e regras de negócio no servidor.

## Tipos de RPC

gRPC define quatro formas de método:

| Forma | Declaração | Fluxo |
| --- | --- | --- |
| Unary | `rpc Method(Request) returns (Response)` | Uma mensagem em cada direção |
| Server streaming | `returns (stream Response)` | Uma requisição e várias respostas |
| Client streaming | `rpc Method(stream Request)` | Várias requisições e uma resposta |
| Bidirectional streaming | `stream` nos dois lados | Dois fluxos independentes |

Dentro de um stream, a ordem das mensagens é preservada. O streaming não
define sozinho persistência, retomada ou reprocessamento. Se a conexão cair,
o contrato precisa dizer se o cliente reinicia, retoma por cursor ou perde a
operação parcial.

## Ciclo de uma chamada

O cliente usa um stub local. O stub serializa a mensagem, cria ou reutiliza a
conexão HTTP/2 e envia a chamada para o servidor. O servidor decodifica a
mensagem, localiza o método, aplica interceptors e autorização, executa a
operação e devolve mensagem, status e trailers.

O HTTP/2 oferece multiplexação, controle de fluxo e streams bidirecionais. A
chamada ainda está sujeita a DNS, TLS, balanceamento, limites de cabeçalho,
timeouts e falhas da rede.

## Metadata, deadlines e status

Metadata é um canal de pares chave-valor associado à chamada. Pode transportar
credenciais, contexto de tracing, tenant e valores operacionais. Headers e
trailers têm limites e chaves reservadas, portanto não devem receber payloads
arbitrariamente grandes.

Deadline define até quando a chamada pode continuar. O cliente deve propagar
cancelamento e prazo para chamadas encadeadas, ou um serviço lento pode
consumir recursos mesmo depois de o cliente abandonar a requisição.

gRPC possui códigos de status próprios para categorias como não encontrado,
não autorizado, inválido, indisponível e deadline excedido. Uma aplicação deve
mapear esses estados de forma consistente e não converter todo erro em
sucesso HTTP ou em retry automático.

## Evolução do schema

Protocol Buffers usa números de campo para codificar mensagens. Não reutilize
um número removido para outro significado. Adicione campos novos sem alterar o
sentido dos antigos e mantenha compatibilidade entre versões durante a
migração.

Remover um método, mudar a semântica de um campo ou tornar obrigatório algo
que clientes antigos não enviam pode quebrar a compatibilidade mesmo quando o
compilador aceita o arquivo `.proto`.

Defina política para campos desconhecidos, versões do serviço, enum values,
mensagens grandes e compatibilidade de clientes gerados. O contrato deve ser
testado de maneira cruzada entre versões.

## Segurança

Use TLS para proteger o canal e autenticação para identificar o cliente. A
autorização precisa ocorrer por método, recurso e contexto, não apenas pela
existência de uma conexão válida.

Interceptors podem centralizar autenticação, tracing, logging e métricas, mas
não devem ocultar decisões de autorização importantes. Limite tamanho de
mensagens, número de streams, duração, concorrência e profundidade de dados.

Streaming exige limites ainda mais claros. Um cliente pode manter uma conexão
aberta por muito tempo ou enviar mensagens lentamente, consumindo buffers e
workers.

## Balanceamento e operação

gRPC mantém conexões HTTP/2 e, por isso, um balanceamento ingênuo por conexão
pode concentrar muitas chamadas em um único backend. O cliente, o proxy ou o
service mesh precisa entender a forma de balanceamento escolhida.

Health checking, retries, circuit breaking e load balancing precisam respeitar
idempotência e deadlines. Repetir um unary de leitura é diferente de repetir
uma mutação. Repetir um stream parcial pode criar efeitos duplicados.

Observe latência, status, tamanho de mensagem, resets de stream, conexões,
fila, deadlines e saturação do servidor. Logs devem evitar incluir dados
integrais de mensagens sensíveis.

## gRPC-Web e clientes de navegador

O navegador não expõe todas as capacidades de um cliente gRPC nativo. gRPC-Web
adapta o modelo para ambientes de navegador, normalmente com um proxy ou
servidor compatível. A disponibilidade de streaming, trailers, HTTP/2 e
autenticação depende da implementação.

Para uma API pública consumida diretamente por navegadores, HTTP com JSON pode
ser mais simples de depurar e integrar. gRPC pode continuar sendo usado entre
o backend e serviços internos.

## gRPC, REST e GraphQL

| Dimensão | gRPC | HTTP orientado a recursos | GraphQL |
| --- | --- | --- | --- |
| Contrato | IDL e métodos | Rotas, recursos e schema opcional | Schema e campos consultáveis |
| Payload comum | Protobuf binário | JSON textual | JSON, conforme a implementação |
| Streaming | Nativo em quatro formas | Requer mecanismo adicional | Queries, mutations e subscriptions |
| Cliente | Código gerado ou biblioteca | HTTP universal | Cliente GraphQL e cache específico |
| Melhor encaixe | Serviços internos e streaming | APIs públicas e interoperabilidade | Agregação e resposta escolhida pelo cliente |
| Custo principal | Operação e tooling próprios | Contratos e overfetch manual | Custo de consultas, resolvers e cache |

Não há uma hierarquia absoluta. O mesmo sistema pode oferecer REST para
consumidores externos, gRPC entre serviços e GraphQL para uma aplicação web.

## Quando evitar

Evite gRPC quando o consumidor precisa apenas de uma API HTTP simples, quando
proxies e ferramentas intermediárias não suportam bem o protocolo, quando o
contrato muda sem governança ou quando o debugging textual é requisito forte.

Também não use gRPC como fila durável, banco de dados ou mecanismo de workflow
sem adicionar os componentes que fornecem essas garantias.

## Fontes

- [gRPC introduction](https://grpc.io/docs/what-is-grpc/)
- [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
- [gRPC metadata](https://grpc.io/docs/guides/metadata/)
- [gRPC Protocol Buffers](https://grpc.io/docs/protoc-installation/)
- [Protocol Buffers language guide](https://protobuf.dev/programming-guides/proto3/)

## Continue por aqui

[RPC](rpc.md) explica a abstração geral. [JSON](json.md) apresenta o formato
textual usado por muitos contratos HTTP. [GraphQL](graphql.md) apresenta outro
modelo de API tipada.
