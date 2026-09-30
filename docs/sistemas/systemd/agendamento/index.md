# Mapa de agendamento de tarefas

O agendamento de tarefas combina um mecanismo de disparo com a execução de uma service, processo ou job. Esta página compara os caminhos mais comuns e encaminha para as páginas específicas.

- [Schedulers](../schedulers.md) trata da decisão de quando uma tarefa pode executar.
- [systemd timer](../timer.md) trata do mecanismo integrado ao lifecycle do systemd.

Cron é adequado para tabelas pequenas de tarefas simples. Anacron considera que a máquina pode ficar desligada. `at` agenda uma execução única. Filas, workers e schedulers de aplicação são preferíveis quando a tarefa precisa de retry, estado, idempotência, concorrência ou observabilidade de negócio.

## Diagnóstico comum

Verifique timezone, calendário calculado, dependências, permissões e se a service terminou com sucesso. `Persistent=` recupera apenas o evento do timer, não transforma uma tarefa não idempotente em segura para repetir.

## Fontes primárias

- [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
- [systemd.time](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html)
