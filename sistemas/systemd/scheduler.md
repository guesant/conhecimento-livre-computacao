# Schedulers e timers

Um scheduler decide quando uma tarefa deve ser executada. O systemd oferece timers integrados ao lifecycle das units; cron, anacron e `at` continuam sendo alternativas úteis quando a aplicação já depende deles ou quando a simplicidade é mais importante que a integração com o manager.

## systemd timer

Um `.timer` ativa uma `.service`, normalmente com o mesmo nome. O disparo pode ser baseado em calendário ou em tempo monotônico relativo ao boot ou à última ativação.

| Recurso | Uso |
| --- | --- |
| `OnCalendar=` | Horários, dias da semana e expressões de calendário. |
| `OnBootSec=` | Tempo depois do boot. |
| `OnUnitActiveSec=` | Intervalo depois da última ativação da unit. |
| `Persistent=` | Recupera um disparo perdido quando o host volta. |
| `RandomizedDelaySec=` | Distribui a carga em uma janela de atraso. |

O timer não deve conter a lógica da tarefa. A lógica fica na service, onde pode receber timeout, sandbox, recursos, dependências e logs próprios.

## Cron e alternativas

Cron é adequado para uma tabela pequena de tarefas simples. Anacron considera que a máquina pode ficar desligada. `at` agenda uma execução única. Filas, workers e schedulers de aplicação são preferíveis quando a tarefa precisa de retry, estado, idempotência, concorrência ou observabilidade de negócio.

## Diagnóstico

Use `systemctl list-timers`, `systemctl status nome.timer` e `journalctl -u nome.service`. Verifique timezone, calendário calculado, dependências, permissões e se a service terminou com sucesso. `Persistent=` recupera apenas o evento do timer, não transforma uma tarefa não idempotente em segura para repetir.

## Fonte primária

- [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
- [systemd.time](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html)
