# GraphQL

GraphQL é uma linguagem de consulta e um motor de execução para APIs. O
serviço publica um schema tipado com tipos, campos, argumentos, operações e
diretivas. O cliente envia uma seleção de campos, e o servidor valida e
executa essa seleção contra o schema.

GraphQL não é apenas um endpoint JSON nem uma forma automática de consultar o
banco. Resolvers podem buscar APIs, bancos, caches ou outros serviços. Essa
flexibilidade exige limites de custo, autorização por campo e controle das
dependências.

## Schema

O schema descreve os tipos disponíveis e os pontos de entrada `Query`,
`Mutation` e, quando suportado, `Subscription`. Ele define nomes, tipos
obrigatórios, listas, argumentos, enums, interfaces, unions e descrições.

```graphql
type Query {
  finding(id: ID!): Finding
}

type Finding {
  id: ID!
  title: String!
  links: [Link!]!
}
```

O schema é um contrato de capacidade. A existência de um campo não significa
que todo usuário pode acessá-lo; autorização ainda precisa ser aplicada na
execução.

## Operações

### Query

Consulta dados sem intenção de alterar o estado. Isso não garante que cada
resolver seja livre de efeitos colaterais, portanto essa propriedade precisa
ser preservada pela implementação.

### Mutation

Representa uma operação que pode alterar estado. Mutations devem declarar
validação, autorização, idempotência, transação, erros e concorrência.

### Subscription

Entrega atualizações ao cliente por uma conexão de longa duração ou um
transporte associado. A especificação GraphQL define a operação, mas o
transporte, reconexão, autenticação e retenção dependem da implementação.

## Execução e resolvers

Cada campo pode ser resolvido por uma função ou por uma fonte de dados. O
executor percorre a seleção, resolve campos aninhados e monta o resultado na
forma solicitada pelo cliente.

Essa propriedade reduz overfetch, mas pode criar o problema N+1: uma lista
carrega muitos itens e cada resolver filho faz uma consulta separada. Use
batching, DataLoader, joins adequados, limites e seleção de campos no backend.

Um resolver não deve aceitar que o cliente escolha livremente uma tabela,
coluna ou expressão de banco. O schema deve expor capacidades intencionais e a
camada de dados deve parametrizar consultas.

## Seleção, variáveis e fragments

O cliente pode escolher subcampos, enviar argumentos e usar variáveis para
evitar concatenar valores no documento. Fragments reutilizam seleções e
diretivas condicionam partes de uma consulta.

```graphql
query GetFinding($id: ID!) {
  finding(id: $id) {
    id
    title
  }
}
```

Queries devem ser validadas contra o schema antes da execução. Persisted
queries ou allowlists podem reduzir superfície de abuso quando o conjunto de
operações conhecidas é relativamente estável.

## Respostas e erros

Uma resposta GraphQL normalmente contém `data`, `errors` ou ambos. Uma falha
em um campo pode produzir dados parciais e um erro com caminho até o campo
afetado. Clientes precisam distinguir ausência legítima, valor nulo e erro.

Esse modelo não deve ser convertido cegamente em HTTP 200 para qualquer falha
sem que observabilidade, cache e consumidores conheçam a convenção. Também
não é seguro ocultar todos os detalhes de erro nem expor stack traces.

## Autorização

Autenticar o cliente não autoriza todos os campos. A aplicação pode precisar de
regras por tipo, campo, argumento, registro, tenant e operação. Campos
administrativos e relações sensíveis devem ser protegidos explicitamente.

O schema publicado pode variar por identidade, ou a execução pode negar campos
em runtime. Evite uma introspecção pública que revele capacidades internas se
essa informação não for desejada.

## Limites de custo

Como o cliente escolhe campos e profundidade, uma query pequena em bytes pode
causar muito trabalho. O servidor deve considerar:

- profundidade máxima;
- número de campos e aliases;
- custo estimado por campo;
- tamanho de listas e paginação;
- complexidade de fragments;
- timeout e cancelamento;
- concorrência e rate limiting;
- tamanho de resposta;
- cache e operações persistidas.

Limitar apenas o número de caracteres da query não é suficiente. Um schema
com uma lista sem paginação pode permitir uma consulta cara mesmo com uma
string curta.

## Cache e invalidação

Cache de respostas depende do documento, das variáveis, da identidade, dos
headers e do estado consultado. Queries selecionadas pelo cliente não possuem
automaticamente a mesma chave de cache que uma rota REST estável.

Normalize documentos, use persisted queries quando adequado e separe dados
públicos de dados privados. Mutations precisam invalidar ou atualizar caches
de forma consistente. Subscriptions normalmente exigem uma estratégia
separada de conexão e fan-out.

## Transporte

GraphQL não fixa uma única forma de transporte. HTTP é comum para queries e
mutations. Subscriptions podem usar WebSocket, SSE ou outro transporte
compatível com a biblioteca escolhida.

Headers, cookies, CORS, CSRF, compressão, TLS, timeouts e proxies continuam
sendo responsabilidades da camada de transporte. GraphQL não substitui um API
gateway, embora possa ser publicado por um gateway.

## GraphQL, REST e gRPC

| Dimensão | GraphQL | REST | gRPC |
| --- | --- | --- | --- |
| Forma principal | Seleção de dados em um schema | Recursos e semântica HTTP | Métodos definidos em IDL |
| Controle da resposta | Cliente escolhe campos | Servidor define a representação | Método define mensagens |
| Contrato | Schema tipado e introspectivo | OpenAPI ou convenção | `.proto` e código gerado |
| Transporte comum | HTTP, WebSocket ou SSE | HTTP | HTTP/2 |
| Principal risco | Query cara e N+1 | Overfetch, endpoints numerosos | Acoplamento e tooling específico |
| Melhor encaixe | UIs com necessidades variadas | APIs públicas e cache HTTP | Comunicação interna e streaming |

Não é necessário escolher uma única abordagem para todo o sistema. Uma API
GraphQL pode agregar serviços gRPC e expor um modelo adequado para uma UI,
enquanto clientes de infraestrutura usam gRPC diretamente.

## Quando usar

GraphQL é útil quando vários clientes precisam de combinações diferentes de
dados, quando a agregação de relações é importante e quando a organização
consegue governar schema, custo, autorização e evolução.

Evite-o quando uma coleção pequena de recursos HTTP já expressa o domínio,
quando cache de resposta por URL é requisito central, quando os consumidores
são simples ou quando a equipe não consegue observar e limitar resolvers.

GraphQL não deve ser introduzido apenas para evitar criar duas rotas. O custo
de schema, tooling, autorização por campo, N+1, cache e operação precisa ser
aceito conscientemente.

## Fontes

- [GraphQL specification](https://spec.graphql.org/)
- [GraphQL September 2025 specification](https://spec.graphql.org/September2025/)
- [GraphQL Foundation](https://graphql.org/)
- [GraphQL security](https://graphql.org/learn/security/)

## Continue por aqui

[JSON](json.md) explica a representação textual comum das respostas. [RPC](rpc.md)
explica o modelo de chamadas remotas. [gRPC](grpc.md) cobre uma alternativa
orientada a métodos e streaming.
