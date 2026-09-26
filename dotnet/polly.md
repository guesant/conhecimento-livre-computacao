# Polly

Polly é uma biblioteca .NET para compor pipelines de resiliência ao redor de operações
que podem falhar, demorar ou encontrar sobrecarga. A unidade moderna de composição é uma
resilience pipeline, formada por estratégias como retry, timeout, circuit breaker e
rate limiter.

Polly não torna uma dependência saudável. Ele define o que o chamador deve fazer diante
de certos resultados e exceções. Uma política mal configurada pode aumentar a carga,
esconder uma indisponibilidade ou atrasar a falha que o usuário deveria receber.

## Estratégias reativas e proativas

Estratégias reativas observam o resultado da operação. Retry pode repetir uma exceção ou
um resultado classificável. Circuit breaker conta falhas e interrompe chamadas quando a
dependência está em estado ruim.

Estratégias proativas tomam uma decisão antes de o callback concluir. Timeout cancela ou
interrompe a espera após um limite. Rate limiter rejeita ou atrasa trabalho quando a taxa
permitida foi atingida. A diferença é útil para escolher métricas e entender se a operação
chegou a ser iniciada.

## Retry

Retry é apropriado para falhas transitórias, como uma conexão interrompida ou uma
resposta temporária de sobrecarga. O código deve classificar exceções e resultados, usar
um número baixo de tentativas e aplicar atraso com backoff. Jitter evita que muitos
clientes repitam juntos depois da mesma falha.

Não repita indiscriminadamente `POST`, pagamentos, criação de recursos ou comandos que
produzem efeitos externos. Se a API suportar uma chave de idempotência, use-a. Caso
contrário, a aplicação precisa consultar o estado ou aceitar explicitamente o risco de
duplicação.

## Timeout

Toda dependência de rede deve ter um limite de tempo coerente com o orçamento da
operação. Um timeout interno não deve ser maior que o timeout externo do request, do job
ou do load balancer.

O timeout precisa ser propagado ao cliente e ao código de negócio por um
`CancellationToken`. Apenas parar de aguardar não garante que o trabalho interno foi
interrompido. Uma operação que continua executando pode consumir sockets, threads e
conexões depois que o chamador já desistiu.

## Circuit breaker

Circuit breaker impede chamadas quando uma dependência apresenta falhas suficientes. O
estado aberto falha rapidamente, o estado de teste permite algumas chamadas e o estado
fechado representa operação normal.

O breaker protege o chamador e a dependência, mas não substitui uma resposta de fallback
nem corrige a causa. O limite deve considerar volume, duração da janela e tipo de falha.
Um único timeout de uma operação longa não deve necessariamente abrir o circuito de todo
o serviço.

O estado do breaker pode ser local a uma instância. Com várias réplicas, cada instância
pode tomar decisões diferentes. Compartilhar o estado exige uma solução específica e
também introduz latência, falhas de armazenamento e coordenação.

## Fallback

Fallback define uma resposta alternativa quando a operação não pode ser concluída. Pode
servir dados stale, usar uma réplica, retornar uma resposta degradada ou registrar a
necessidade de processamento posterior.

Fallback não deve transformar um erro de autorização, validação ou integridade em sucesso.
Classifique as falhas e mantenha a diferença entre ausência legítima de dados e falha da
dependência.

## Rate limiter e hedging

Rate limiter limita o uso de uma dependência para respeitar sua capacidade. Ele pode
rejeitar rapidamente, esperar por um token ou controlar concorrência. O limite deve
considerar todas as réplicas e o contrato do provedor quando a aplicação escalar.

Hedging inicia tentativas alternativas quando uma chamada fica lenta. Pode reduzir cauda
de latência, mas aumenta carga e pode duplicar efeitos. Use-o apenas para operações
seguras ou com idempotência e quando houver evidência de variabilidade de latência.

## Ordem das estratégias

A ordem muda a semântica. Um timeout interno limita cada tentativa de retry; um timeout
externo pode limitar o conjunto inteiro. Um circuit breaker pode ficar fora do retry para
contar a falha da operação, ou dentro dele para observar cada tentativa. A escolha deve
ser documentada pelo orçamento de tempo e pelo significado das métricas.

Um pipeline não deve possuir várias camadas escondidas que aplicam retry sem coordenação.
Verifique também retries do cliente HTTP, do SDK, do broker, do Hangfire, do proxy e do
load balancer.

## Registro e telemetria

Registre a chave da operação, o destino, o número da tentativa, a exceção classificada,
o resultado, o atraso e o motivo de abertura do circuito. Não registre tokens, payloads
sensíveis ou dados pessoais apenas para diagnosticar uma falha.

Métricas úteis incluem tentativas por operação, taxa de retry, tempo até o sucesso,
timeouts, rejeições pelo breaker, tokens recusados pelo rate limiter e proporção de
fallbacks. Uma taxa alta de retry pode indicar que o sistema está mascarando uma falha,
não que a resiliência está funcionando bem.

## Polly dentro de um job Hangfire

Quando Polly está dentro de um job, ele protege a chamada externa de cada execução. Se a
pipeline esgotar suas tentativas e lançar uma exceção, Hangfire pode reprocessar o job.
Isso é útil apenas se o job for idempotente e o número combinado de tentativas for
conhecido.

Uma forma de calcular o limite é separar tentativas internas de reexecuções do job. Por
exemplo, duas tentativas Polly e três execuções Hangfire podem gerar até seis chamadas,
sem contar concorrência, timeout tardio ou redelivery. O número deve caber no orçamento
do provedor e no tempo máximo do fluxo.

## Anti-patterns

Evite retry infinito, retry em qualquer exceção, timeout maior que o timeout do chamador,
circuit breaker sem telemetria, fallback que mente para o usuário e hedging em operações
com efeito.

Também evite criar uma pipeline diferente em cada método sem uma convenção. A configuração
deve ser reutilizável por destino ou por classe de operação, com nomes, limites e métricas
que permitam comparação.

## Fontes

- [Polly, introdução](https://www.pollydocs.org/getting-started.html)
- [Polly, estratégias de resiliência](https://www.pollydocs.org/strategies/)
- [Polly, retry](https://www.pollydocs.org/strategies/retry)
- [Polly, circuit breaker](https://www.pollydocs.org/strategies/circuit-breaker)
- [Polly, timeout](https://www.pollydocs.org/strategies/timeout.html)
