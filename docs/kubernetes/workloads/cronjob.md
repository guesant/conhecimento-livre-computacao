# CronJob

CronJob cria Jobs segundo um agendamento.

## Controles

[Concurrency policy](concurrency-policy.md) define sobreposição. [Starting deadline](starting-deadline.md) limita atraso aceitável.

## Casos de uso

Rotinas periódicas como reconciliações, limpeza e relatórios. A tarefa deve tolerar características de sistemas distribuídos e, quando necessário, ser [idempotente](idempotencia.md).

## Má prática

Assumir sem desenho adicional que um schedule implica exatamente uma execução efetiva do efeito de negócio.
