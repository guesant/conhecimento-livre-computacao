# systemd timer

Um timer agenda a ativação de uma service. Ele combina calendário ou intervalos
relativos com o lifecycle, logs e dependências do systemd.

## Agendamento

`OnCalendar=` representa datas e horários. `OnBootSec=` agenda relativo ao
boot e `OnUnitActiveSec=` relativo à última ativação da unit. A service
disparada pode ser indicada em `Unit=`; sem essa diretiva, o systemd procura
a service com o mesmo nome base.

`RandomizedDelaySec=` distribui execuções semelhantes e evita que vários hosts
façam trabalho pesado no mesmo instante. `Persistent=yes` permite executar
uma ocorrência perdida quando o host retorna, o que precisa ser avaliado para
tarefas em que atraso e repetição são seguros.

## Operação

Use `systemctl list-timers` para observar próxima e última execução,
`systemctl start nome.timer` para ativar e `journalctl -u nome.service`
para examinar o trabalho. O log pertence à service disparada, não ao timer.

A service deve ser idempotente. Um timer persistente pode disparar depois de
um longo período desligado, e uma tarefa que não tolera repetição ou atraso
precisa registrar seu próprio estado.

## Relações

- [systemd unit](unit.md) explica como timers participam do lifecycle.
- [systemd service](service.md) executa o trabalho agendado.
- [Dependências systemd](dependencies.md) define condições e ordem.

## Fonte primária

- [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
