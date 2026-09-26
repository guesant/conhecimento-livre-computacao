# Contexto e propagação no OpenTelemetry

Contexto é o estado associado a uma unidade de execução. Ele permite que uma operação
seja relacionada enquanto atravessa funções, threads, processos, filas e serviços. O
contexto não é o payload de negócio e não deve ser usado para transportar autorização
sem validação própria.

## Trace context

Trace context identifica a relação entre spans de uma mesma operação distribuída. Uma
requisição HTTP pode carregar o contexto em headers; uma chamada RPC pode usar metadata;
uma mensagem pode transportar os campos dentro de seu envelope.

O código de instrumentação extrai o contexto ao receber uma operação e injeta o contexto
ao chamar a próxima fronteira. Se um proxy, gateway, biblioteca ou consumidor remover o
header, o trace será quebrado em vários trechos independentes.

O W3C Trace Context é uma convenção comum para headers de trace. A aplicação ainda deve
validar formato, limites e confiança da fronteira. Não aceite valores recebidos de um
cliente externo como prova de identidade ou autorização.

## Baggage

Baggage transporta pares nome-valor que acompanham a operação. Pode ser útil para um
identificador de tenant, uma região ou uma dimensão de roteamento que não pertence ao
trace em si.

Baggage é propagado entre serviços e pode aumentar o tamanho de headers, a exposição de
dados e o custo de cada chamada. Não coloque tokens, credenciais, dados pessoais ou
informações que permitam alterar decisões de segurança sem uma validação local.

## Carriers e propagators

Carrier é o meio usado para transportar os valores, como headers, metadata ou campos de
uma mensagem. Propagator sabe serializar e extrair um tipo de contexto daquele carrier.

Um protocolo pode suportar mais de um propagator, mas a escolha precisa ser consistente
entre produtores e consumidores. Ao atravessar uma fila, defina se o contexto representa
o produtor, o consumidor, uma operação individual ou uma cadeia de processamento.

## Filas, jobs e processamento assíncrono

Uma mensagem pode iniciar um novo span ligado ao span que publicou a mensagem. O tipo de
relação depende do modelo de consumo: o consumidor pode ser filho, um link ou uma nova
operação relacionada. Não presuma que o contexto síncrono continuará correto depois de
um retry ou redelivery.

Se a mesma mensagem for processada duas vezes, o trace pode conter duas tentativas. Use
identificador de mensagem, job e tentativa em atributos de baixa ambiguidade ou em logs,
sem transformá-los em labels de alta cardinalidade de métricas.

## Falhas de correlação

Falhas comuns incluem headers removidos por proxies, propagator diferente em cada
linguagem, contexto perdido ao criar uma thread, contexto reutilizado fora do escopo,
jobs sem metadata e mensagens que excedem limites de tamanho.

Diagnostique comparando trace ID na entrada, saída, mensagem e consumidor. Um trace
ausente não prova que a operação não foi executada; pode indicar apenas que a fronteira
não propagou ou que o sampling descartou parte dos dados.

## Segurança

Propagação é transporte de contexto, não autenticação. Proteja os canais com TLS quando
necessário, filtre atributos sensíveis e defina quais fronteiras podem aceitar contexto
externo. Um usuário não deve conseguir escolher um valor de baggage que altere tenant,
permissão, cobrança ou roteamento privilegiado.

## Fontes

- [OpenTelemetry, contexto](https://opentelemetry.io/docs/concepts/context-propagation/)
- [OpenTelemetry, especificação de contexto](https://opentelemetry.io/docs/specs/otel/context/)
- [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- [W3C Baggage](https://www.w3.org/TR/baggage/)
