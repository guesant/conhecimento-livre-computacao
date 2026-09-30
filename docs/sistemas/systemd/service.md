# systemd service

Uma service representa um processo ou uma tarefa que o systemd pode iniciar,
parar, reiniciar e supervisionar. Seu `Type=` define quando a unit é
considerada iniciada, o que influencia dependentes e readiness operacional.

## Tipos de inicialização

`simple` considera a unit iniciada quando o processo é criado. `exec`
aguarda a execução do binário. `forking` é destinado a daemons que fazem
fork e exigem um PIDFile ou outra forma de identificação. `oneshot` executa
uma tarefa e termina, podendo usar `RemainAfterExit=yes`. `notify` espera
um sinal explícito do processo por `sd_notify`.

Escolha o tipo que representa o lifecycle real. Um serviço que ainda está
carregando configuração não deve declarar readiness só porque o processo foi
criado.

## Supervisão

`Restart=`, `RestartSec=`, limites de tentativas e timeouts definem como o
systemd reage a falhas. Um restart automático pode recuperar uma falha
transitória, mas também pode esconder uma configuração inválida e gerar um
loop. Combine logs, limites e alertas para diferenciar recuperação de
instabilidade persistente.

`ExecStartPre=`, `ExecStart=` e `ExecStartPost=` possuem papéis distintos.
Mantenha a preparação idempotente e não use scripts grandes como substituto
de uma unidade de aplicação bem definida.

## Diagnóstico

Use `systemctl status nome.service`, `journalctl -u nome.service` e
`systemctl show nome.service`. Diferencie `inactive`, `failed` e
`activating`. Se dependentes iniciam cedo demais, verifique a combinação de
`Type=`, `After=` e readiness reportado.

## Relações

- [systemd unit](unit.md) explica os tipos e a precedência.
- [Dependências systemd](dependencies.md) diferencia ordem de requisito.
- [systemd timer](timer.md) pode ativar uma service de curta duração.

## Fonte primária

- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
