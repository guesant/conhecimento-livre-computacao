# Active deadline

activeDeadlineSeconds limita o tempo ativo permitido para um Job ou Pod conforme o contexto em que o campo é aplicado.

É uma proteção contra tarefas travadas ou que excedem uma janela operacional.

Timeout não torna a operação idempotente nem garante rollback do efeito parcial.