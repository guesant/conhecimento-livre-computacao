# Resiliência

Resiliência é a capacidade de um sistema manter comportamento aceitável durante falhas,
degradar de forma controlada e recuperar suas funções depois que a causa é removida. Ela
é uma propriedade do sistema inteiro, não apenas de uma biblioteca de retry ou da
existência de réplicas.

Disponibilidade, confiabilidade e resiliência são relacionadas, mas não idênticas.
Disponibilidade descreve se o serviço está acessível. Confiabilidade inclui a capacidade
de produzir resultados corretos ao longo do tempo. Resiliência inclui resposta a falhas,
contenção do impacto e recuperação.

## Começar pelo failure mode

Antes de adicionar um mecanismo, descreva o que pode falhar:

- latência ou timeout de uma dependência;
- erro transitório de rede;
- resposta inválida ou incompatível;
- saturação de CPU, memória, conexões ou fila;
- perda de uma instância, nó, zona ou volume;
- erro de dados, configuração ou migração;
- falha de um operador ou de um deploy;
- indisponibilidade completa de uma dependência.

Cada falha precisa de uma resposta proporcional. Retry pode ajudar em uma desconexão
transitória e piorar uma dependência que já está sobrecarregada. Um fallback pode manter
uma leitura, mas ser perigoso em uma operação de escrita. Um backup ajuda na recuperação,
mas não mantém a requisição atual disponível.

## Orçamento de tempo

Uma operação deve possuir um deadline ou timeout que atravesse suas chamadas internas. O
timeout da dependência precisa caber no orçamento do request, job ou workflow. Caso
contrário, cada camada pode esperar seu próprio limite e o tempo total crescer muito além
do que o consumidor tolera.

Cancelamento deve chegar ao cliente HTTP, banco, fila e código de negócio. Apenas deixar
de aguardar uma task não garante que o trabalho parou. O trabalho abandonado pode continuar
consumindo threads, conexões, memória e capacidade da dependência.

## Retry

Retry é adequado para uma falha transitória quando a operação tem probabilidade razoável
de funcionar depois. Use número finito de tentativas, backoff exponencial e jitter quando
vários clientes podem repetir ao mesmo tempo.

Não faça retry em erros permanentes, validação, autorização ou uma operação de escrita
sem idempotência. Considere um orçamento agregado de retries por dependência, porque três
tentativas por request ainda podem produzir milhares de chamadas quando muitas requisições
falham simultaneamente.

## Circuit breaker

Circuit breaker interrompe chamadas para uma dependência que está falhando. No estado
fechado, as chamadas passam e as falhas são observadas. No estado aberto, elas falham
rapidamente. No estado semiaberto, poucas chamadas de teste verificam se a dependência
recuperou.

O breaker evita esperar por uma dependência indisponível e ajuda a impedir uma cascata de
falhas. Ele não substitui timeout, tratamento de erro ou uma política de recuperação. O
estado pode ser local a uma instância, então várias réplicas podem tomar decisões
independentes.

## Bulkhead e limites

Bulkhead separa recursos para impedir que uma operação consuma tudo. Pools de conexão,
filas, workers, memória ou limites de concorrência podem formar compartimentos diferentes.
O objetivo é limitar o blast radius: uma integração lenta não deve impedir operações
críticas que usam outro recurso.

Rate limiting protege a capacidade de um componente e throttling reduz o ritmo de entrada.
Backpressure comunica que o consumidor não consegue acompanhar. Os três mecanismos são
relacionados, mas produzem decisões diferentes: rejeitar, atrasar ou desacelerar.

## Degradação controlada

Uma aplicação pode continuar funcionando com dados stale, uma réplica, uma resposta
parcial ou uma funcionalidade secundária desabilitada. A degradação precisa ser explícita:
o usuário não deve interpretar um valor antigo como confirmação atual, nem uma resposta
parcial como sucesso completo.

Escritas normalmente exigem uma política mais conservadora que leituras. Não confirme
uma alteração apenas porque o sistema não conseguiu verificar se ela foi persistida.

## Recuperação

Resiliência inclui o retorno ao comportamento normal. Defina como detectar recuperação,
como reabrir tráfego, como reconciliar trabalho pendente e como evitar que o retorno
repentino sobrecarregue a dependência.

Filas, dead-letter queues, compensações, outbox, backups e restauração podem participar
da recuperação. Cada mecanismo possui uma finalidade diferente. Replicação melhora
continuidade, mas não substitui backup contra erro lógico; retry preserva uma operação,
mas não recupera dados apagados.

## Observabilidade e teste

Monitore taxa de erro, latência, timeouts, estado dos breakers, retries, profundidade e
idade de filas, saturação de pools, uso de fallback e tempo de recuperação. Um sistema
que se recupera mas não registra a causa continua difícil de operar.

Teste hipóteses com carga, stress, soak e chaos engineering. O teste deve verificar tanto
a falha primária quanto os efeitos secundários, como retry storm, exaustão de conexões e
perda de contexto de tracing.

## Resiliência não é complexidade ilimitada

Cada wrapper adiciona estados, métricas, configuração e possibilidades de interação.
Duplicar retries no SDK, proxy, service mesh e aplicação pode aumentar a latência e a
carga. Comece por timeout, cancelamento, limites e observabilidade; adicione retry,
breaker ou fallback quando o failure mode justificar.

## Relações

- [Fail-safe, fault tolerance e error handling](fail-safe-fault-tolerance-e-error-handling.md) explica estados seguros, redundância,
  tratamento de erro, failover e limites da tolerância a falhas.
- [Idempotência](idempotencia.md) permite repetir certas operações com segurança.
- [OpenTelemetry](../observabilidade/opentelemetry/index.md) ajuda a observar falhas e
  recuperação.
- [Polly](../dotnet/polly.md) implementa pipelines de resiliência em .NET.
- [Filas](../dados/mensageria/filas.md) absorvem trabalho e permitem processamento posterior.
- [Chaos engineering](testes/chaos-engineering.md) testa hipóteses de falha controlada.

## Fontes

- [Microsoft, Circuit Breaker pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
- [Microsoft, transient fault handling](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults)
- [Microsoft, reliability design patterns](https://learn.microsoft.com/en-ie/azure/well-architected/reliability/design-patterns)
