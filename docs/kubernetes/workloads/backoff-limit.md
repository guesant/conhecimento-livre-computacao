# Backoff limit

backoffLimit limita falhas/tentativas consideradas por um Job antes de marcá-lo como falho segundo a semântica do controller.

Ele evita retries indefinidos de tarefas que não conseguirão concluir sem intervenção.

Veja [Job](job.md) e [active deadline](active-deadline.md).
