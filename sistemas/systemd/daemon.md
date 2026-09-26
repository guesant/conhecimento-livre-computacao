# Daemons e serviços

Um daemon é um processo que presta um serviço sem depender de uma janela ou de uma sessão interativa. O termo descreve um modo de execução e uma responsabilidade, não um tipo específico de arquivo. No systemd, um daemon costuma ser representado por uma unit `.service`, mas uma service também pode executar uma tarefa curta e terminar.

## Daemon, processo, service e unit

| Termo | Significado |
| --- | --- |
| Processo | Instância executável que o kernel agenda e supervisiona. |
| Daemon | Processo de serviço que normalmente espera trabalho ou eventos. |
| Service | Unit do systemd que descreve como iniciar e parar um processo ou tarefa. |
| Unit | Objeto genérico de lifecycle, que também pode ser socket, timer, mount ou target. |

O systemd pode iniciar um daemon sob demanda, reiniciá-lo após falhas, limitar seus recursos por cgroup, registrar sua saída no journal e aplicar credenciais ou sandboxing. Isso não transforma o processo em uma unit: a unit é a descrição que o manager usa para controlá-lo.

## Managers

O system manager normalmente é o PID 1 e administra serviços do sistema. Um user manager administra services e timers de um usuário, podendo continuar ativo por meio de linger. Os dois usam o mesmo modelo de units, mas têm permissões, diretórios e escopos diferentes.

## Lifecycle

Uma unit pode estar carregada, habilitada, ativa, inativa ou falha. Habilitar uma unit altera o vínculo usado no boot; não significa que ela esteja ativa agora. Iniciar uma unit altera o estado runtime; não necessariamente configura o próximo boot.

Use `systemctl status`, `systemctl show` e `journalctl -u` para diagnosticar o lifecycle. Em produção, combine restart automático com limites e alertas, porque reiniciar um daemon com configuração inválida pode apenas ocultar a causa e produzir um loop.

## Fontes primárias

- [systemd architecture](https://systemd.io/ARCHITECTURE/)
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [systemd portability](https://systemd.io/PORTABILITY_AND_STABILITY/)
