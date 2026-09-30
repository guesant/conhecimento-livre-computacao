# Mapa de daemons e services

Daemon, processo, service e unit são abstrações relacionadas, mas não equivalentes. Esta página orienta a navegação entre elas.

- [Daemons](../daemons.md) trata de processos que prestam serviços sem depender de uma sessão interativa.
- [systemd service](../service.md) trata da unit que descreve como iniciar e parar um processo ou tarefa.
- [systemd unit](../unit.md) trata do objeto genérico de lifecycle, que também pode ser socket, timer, mount ou target.

O systemd pode iniciar um daemon sob demanda, reiniciá-lo após falhas, limitar seus recursos por cgroup, registrar sua saída no journal e aplicar credenciais ou sandboxing. A unit é a descrição que o manager usa para controlar o processo.

## Fontes primárias

- [systemd architecture](https://systemd.io/ARCHITECTURE/)
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
