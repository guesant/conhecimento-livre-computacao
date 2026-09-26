# Concorrência e sincronização

Concorrência existe quando várias atividades podem avançar durante a mesma janela de
tempo, mesmo que o hardware execute apenas uma parte delas por vez. O problema não é
somente paralelismo. Processos, threads, callbacks, workers e requisições podem intercalar
suas etapas de formas diferentes e observar estados intermediários.

Uma solução de concorrência precisa declarar a invariável, o estado compartilhado, o
protocolo de ownership e o comportamento quando uma atividade falha. Locks, mutexes,
semáforos, filas, leases e heartbeats são mecanismos diferentes. Nenhum deles torna uma
operação automaticamente correta.

## Mapa do domínio

[Condição de corrida](race-condition.md) explica quando o resultado depende da ordem não
controlada entre atividades concorrentes.

[Mutex](mutex.md) protege uma seção crítica permitindo um proprietário por vez.

[Semáforos](semaforos.md) representam capacidade ou sinalização e podem coordenar mais de
um participante.

[Deadlock](deadlock.md) explica espera circular, prevenção, detecção e recuperação.

[Heartbeat](../../confiabilidade/heartbeat.md) usa sinais periódicos para indicar atividade,
renovar leases ou detectar participantes que deixaram de responder.

[TTL](../../dados/ttl.md) limita a validade temporal de uma entrada, lease, mensagem ou
cache. Ele é relacionado a heartbeat, mas não substitui um protocolo de renovação.

## Como escolher

Use mutex quando existe um recurso compartilhado que só pode ser manipulado por uma
atividade por vez. Use semáforo quando o recurso possui uma capacidade maior que um ou
quando um sinal precisa liberar uma atividade bloqueada. Use uma fila quando o objetivo é
transferir trabalho e absorver uma diferença temporal entre produtor e consumidor.

Use uma transação, constraint ou operação atômica quando a invariável pertence ao banco ou
ao armazenamento. Um mutex local não protege réplicas de um serviço, processos em hosts
diferentes ou operações que continuam depois que o lock expirou.

## Relações

- [Transações e ACID](../../dados/transacoes-acid.md) trata atomicidade, isolamento e
  durabilidade no banco.
- [Locks e transações no PostgreSQL](../../dados/postgresql-locks-e-transacoes.md) trata
  MVCC, locks e conflitos dentro do PostgreSQL.
- [Filas de mensagens](../../dados/mensageria/filas.md) trata ack, retry, backpressure e
  dead letter.
- [Fila de prioridade](../../dados/mensageria/fila-de-prioridade.md) trata ordenação por
  urgência e custo operacional.
