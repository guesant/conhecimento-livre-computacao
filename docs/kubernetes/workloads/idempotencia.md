# Idempotência de tarefas

Uma operação idempotente pode ser repetida sem produzir efeitos adicionais incorretos além do estado desejado.

Jobs e sistemas distribuídos podem repetir trabalho por retry, timeout ou incerteza sobre conclusão. Idempotência reduz o risco dessas repetições.

Ela pode ser obtida com chaves de idempotência, operações de upsert, registros de execução ou desenho de domínio apropriado.
