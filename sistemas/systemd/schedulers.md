# Schedulers

Um scheduler decide quando uma tarefa deve ser executada. O critério pode ser um calendário, um intervalo, um evento, uma fila ou uma janela de capacidade.

Cron usa uma tabela compacta de horários. Anacron considera períodos em que o host ficou desligado. `at` agenda uma execução única. Schedulers de aplicação acrescentam estado de negócio, retries, idempotência, concorrência e observabilidade que não pertencem a uma tabela cron simples.

A escolha deve considerar persistência do agendamento, comportamento após reinício, timezone, concorrência, recuperação de falhas e necessidade de coordenar múltiplos hosts. Um scheduler decide o disparo, mas não substitui a lógica idempotente da tarefa.
