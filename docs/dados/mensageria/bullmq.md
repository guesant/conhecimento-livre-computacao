# BullMQ

BullMQ é uma biblioteca de filas e jobs para Node.js baseada em Redis. Ela fornece filas, workers, jobs atrasados, retries, prioridades, jobs recorrentes, dependências e eventos de ciclo de vida. O Redis é parte da infraestrutura de armazenamento e coordenação, portanto a durabilidade e a disponibilidade do Redis fazem parte do contrato operacional.

## Componentes

`Queue` adiciona e administra jobs. `Worker` retira jobs e executa o processador. `QueueEvents` observa eventos de múltiplos workers, e `FlowProducer` organiza dependências entre jobs. A fila pode receber jobs antes de existir um worker; quando um worker se conecta, ele pode processar o backlog.

## Concorrência e escala

Um worker pode ter um fator de concorrência maior que um, principalmente para tarefas que esperam I/O. Vários workers em processos ou máquinas diferentes também aumentam paralelismo e disponibilidade. A concorrência precisa ser calculada considerando conexões Redis, banco, APIs externas e memória.

Para tarefas intensivas em CPU, aumentar a concorrência assíncrona do mesmo processo pode piorar a latência. Use processadores isolados ou mais processos conforme o modelo de execução e meça o throughput real.

## Retries e jobs recorrentes

Jobs podem ter tentativas, backoff, delay, prioridade e políticas de remoção. Um retry deve ser reservado para falhas transitórias. Jobs recorrentes precisam de uma identidade de agenda estável para que cada deploy não crie uma nova série duplicada.

O job deve possuir identificador e payload versionado. O worker precisa ser idempotente porque uma queda depois do efeito, mas antes da confirmação, pode levar a uma nova entrega.

## Eventos e observabilidade

Listeners locais observam eventos do processo atual. `QueueEvents` usa Redis Streams para observar eventos entre workers e pode alimentar dashboards, WebSockets, SSE ou outro serviço. Retenção e trimming do stream precisam ser configurados para evitar crescimento ilimitado.

Monitore idade do job, tempo de espera, duração, tentativas, falhas, jobs travados, backlog, taxa de conclusão e quantidade de jobs em dead letter. Um dashboard de jobs não substitui métricas do Redis nem da dependência chamada pelo worker.

## Quando usar

BullMQ é adequado para aplicações Node.js que já operam Redis e precisam de jobs persistentes, atrasados, recorrentes ou com dependências. Para integração entre organizações, retenção longa, replay amplo ou contratos independentes de Node.js, um broker ou event streaming pode ser mais adequado.

## Limitações

BullMQ não transforma Redis em um log de eventos ilimitado nem fornece uma transação automática entre banco de negócio e fila. Para publicar uma intenção junto com uma alteração SQL, use uma outbox e um worker. Proteja Redis, limite payload, defina retenção e não armazene segredos nos jobs.

## Fonte primária

- [BullMQ documentation](https://docs.bullmq.io/)
- [Concurrency](https://docs.bullmq.io/guide/workers/concurrency)
- [Events](https://docs.bullmq.io/guide/events/)
