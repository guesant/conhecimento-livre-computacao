# Ecossistema .NET

Aplicações .NET frequentemente precisam resolver dois problemas diferentes: executar
trabalho fora do ciclo de uma requisição e lidar com dependências que podem falhar ou
ficar lentas. Hangfire e Polly aparecem muitas vezes na mesma aplicação, mas não são
substitutos.

Hangfire fornece persistência, agendamento e processamento de jobs em background. Polly
fornece pipelines de resiliência para proteger uma operação contra falhas transitórias,
latência excessiva e sobrecarga. Um job Hangfire pode executar uma pipeline Polly, mas a
pipeline não substitui a fila, e a fila não substitui timeout ou circuit breaker.

## Como navegar

- [Hangfire](hangfire.md) trata jobs fire-and-forget, atrasados e recorrentes, storage,
  workers, retry e operação.
- [Polly](polly.md) trata pipelines de resiliência, timeout, retry, circuit breaker,
  rate limiting, fallback e hedging.

## Uma composição típica

Uma requisição HTTP pode validar a entrada e enfileirar um job. O servidor Hangfire
recupera o job do storage e chama o handler. Dentro do handler, Polly pode aplicar um
timeout e um retry limitado ao cliente HTTP usado para falar com um sistema externo.

Essa composição cria camadas diferentes de falha. O retry de Polly trata uma tentativa
contra o sistema externo. O retry do Hangfire trata a falha do job inteiro. Ambos devem
ser configurados juntos, porque um retry interno e três retries do job podem produzir
várias tentativas reais.

## Princípios

O job deve ser idempotente, carregar apenas os dados necessários, registrar um
identificador de operação e aceitar cancelamento quando o host estiver encerrando. A
pipeline deve reconhecer somente falhas transitórias, ter limite de tempo e evitar
repetir operações que já produziram efeito sem uma chave de idempotência.

Nenhuma das duas bibliotecas cria consistência distribuída ou garante exatamente uma
execução. A aplicação ainda precisa decidir o que pode ser repetido, como detectar uma
operação concluída e como recuperar um job que ficou incompleto.
