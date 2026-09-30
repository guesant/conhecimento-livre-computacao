# Correlation ID

Correlation ID é um identificador atribuído a uma requisição ou a uma operação de
negócio para localizar seus registros em vários componentes. Ele costuma aparecer em
logs estruturados, headers HTTP, metadata de mensagens e informações de jobs.

O identificador não precisa representar uma única execução técnica. Uma operação de
negócio pode produzir mais de um request, trace, retry ou job ao longo do tempo. Nessa
situação, o Correlation ID mantém a relação mais ampla, enquanto trace ID e span ID
descrevem uma execução específica.

## Diferenças entre identificadores

| Identificador | Escopo | Uso principal |
| --- | --- | --- |
| Correlation ID | Fluxo de negócio ou requisição definida pela aplicação | Encontrar registros relacionados |
| Trace ID | Uma operação distribuída observada pelo tracing | Reconstituir o caminho entre serviços |
| Span ID | Uma etapa dentro de um trace | Localizar uma operação específica |
| Request ID | Uma requisição em um componente | Diagnosticar uma entrada local |
| Job ID | Uma unidade persistida de trabalho | Acompanhar fila, retry e execução |
| Event ID | Uma ocorrência ou mensagem | Deduplicar e auditar processamento |

Um request pode criar um trace e vários spans. Um retry pode criar outro trace ou outra
tentativa associada ao mesmo fluxo de negócio. Não use um campo como substituto universal
sem definir seu escopo.

## Geração

O gateway ou a primeira aplicação confiável pode gerar o Correlation ID. Se o cliente
enviar um valor, a aplicação deve validar comprimento, caracteres, formato e contexto
antes de aceitar o valor. Outra opção é sempre gerar um valor interno e preservar o valor
externo como um campo separado, quando isso for necessário para suporte.

Use um identificador opaco, não sequencial e sem informações de usuário, tenant ou
credencial. UUID ou um formato equivalente pode funcionar, mas a escolha deve considerar
logs, limites de transporte, privacidade e necessidade de busca.

Não use email, CPF, token, endereço IP ou uma chave de banco como Correlation ID. Esses
valores expõem informação e podem ser usados para injeção ou enumeração.

## Propagação HTTP

Em HTTP, uma aplicação pode receber ou criar um header dedicado, como
`X-Correlation-ID`, e devolvê-lo na resposta para facilitar o atendimento e a
investigação. O nome não é uma convenção universal do mesmo nível de `traceparent`, então
produtores e consumidores precisam documentar a política.

A aplicação deve normalizar o valor, impedir quebras de linha ou caracteres de controle
nos logs e aplicar um limite de tamanho. Serviços internos não devem confiar no header
para autenticação ou autorização.

Quando OpenTelemetry estiver ativo, o header de correlation pode coexistir com o Trace
Context. O trace context cria a relação técnica entre spans; o Correlation ID ajuda a
buscar o fluxo definido pela aplicação.

## Filas, eventos e jobs

Ao publicar uma mensagem, carregue o Correlation ID em metadata ou no envelope, sem
misturá-lo automaticamente ao payload de domínio. O consumidor deve preservar o valor ao
criar logs e novos jobs.

O consumidor também deve criar ou propagar o contexto de tracing apropriado. Uma mensagem
redeliverada pode ter a mesma correlação, um novo span e uma nova tentativa. Registre
separadamente message ID, job ID, attempt e trace ID.

Para uma operação longa, mantenha o Correlation ID estável, mas não mantenha um contexto
de span aberto por horas. Crie traces menores para cada etapa e relacione-os pela
correlação de negócio ou por links de trace.

## Logs estruturados

Inclua Correlation ID em logs de entrada, saída, chamadas externas, persistência, eventos
de fila e falhas. O campo deve ter o mesmo nome e formato em todas as aplicações que
participam do fluxo.

Um log útil pode conter:

- `correlation_id`;
- `trace_id` e `span_id`, quando houver contexto OpenTelemetry;
- `request_id`, `job_id`, `event_id` ou `message_id`, quando aplicável;
- serviço, ambiente, versão e severity;
- operação e resultado, sem payload sensível.

Não transforme Correlation ID em label de uma métrica Prometheus. Cada requisição criaria
uma série nova e a cardinalidade destruiria o modelo de métricas. Use logs, traces ou
eventos para buscar ocorrências individuais.

## Respostas e suporte

Devolver o Correlation ID ao cliente pode facilitar suporte e comunicação com usuários.
O valor retornado não deve permitir descobrir dados internos ou substituir um identificador
de autorização. Em uma API pública, documente se o consumidor pode enviar o header e se o
valor será preservado ou regenerado.

Um operador deve conseguir pesquisar o valor nos logs e navegar para traces, eventos,
jobs e incidentes relacionados. Essa capacidade depende de retenção compatível e de
permissões de leitura, não apenas de criar o header.

## Privacidade e segurança

Correlation ID pode aparecer em URLs, logs de proxy, tickets, screenshots e respostas de
erro. Trate-o como dado operacional potencialmente exposto. Não use o identificador como
segredo, não o aceite para escolher uma conta e não permita que seu conteúdo seja
interpretado como comando pelo sistema de logs.

Se a correlação atravessar uma fronteira de confiança, considere gerar um novo ID externo
e registrar a relação somente em um sistema protegido. O objetivo é investigar a operação
sem criar um canal de vazamento entre tenants ou ambientes.

## Falhas comuns

As falhas mais frequentes são gerar um ID em cada serviço sem propagar o original, usar
trace ID como se fosse uma correlação de negócio, perder o valor ao criar um job, registrar
o valor apenas no erro ou aceitar qualquer header do cliente sem sanitização.

Outro problema é manter o mesmo Correlation ID para operações de usuários diferentes em
um fluxo compartilhado. A correlação deve representar uma operação, e não uma categoria
genérica que faça eventos independentes parecerem relacionados.

## Relações

- [OpenTelemetry](opentelemetry/index.md) padroniza contexto, traces, métricas e logs.
- [Contexto e propagação](opentelemetry/context.md) trata Trace Context, baggage e carriers.
- [Distributed tracing](tracing.md) explica trace ID e span ID.
- [Logs](logs.md) trata registros estruturados e retenção.
- [Sentry](sentry.md) mostra como usar correlação na investigação de erros.

## Fontes

- [OpenTelemetry, correlação em logs](https://opentelemetry.io/docs/specs/otel/logs/)
- [OpenTelemetry, modelo de logs](https://opentelemetry.io/docs/specs/otel/logs/data-model/)
- [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- [W3C Baggage](https://www.w3.org/TR/baggage/)
