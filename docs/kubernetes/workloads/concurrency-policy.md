# CronJob concurrency policy

concurrencyPolicy define o que um CronJob faz quando chega um novo horário enquanto execução anterior ainda está ativa.

Allow permite concorrência. Forbid evita iniciar a nova execução. Replace substitui a anterior.

A escolha depende de o trabalho aceitar sobreposição e interrupção, não de preferência estética.
