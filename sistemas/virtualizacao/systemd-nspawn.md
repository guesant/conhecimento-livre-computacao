# systemd-nspawn

`systemd-nspawn` executa um processo ou um sistema Linux em um container de
sistema integrado ao ecossistema systemd. Ele usa namespaces, cgroups,
filesystem e isolamento de recursos, mas não é uma implementação completa de
OCI nem substitui automaticamente um orchestrator de containers.

## Modelo

O container pode possuir uma árvore de root filesystem, PID 1 próprio, rede,
hostname e limites. `machinectl` e `systemd-machined` ajudam a listar e operar
machines. A unidade pode ser transitória ou declarada como serviço, dependendo
do fluxo operacional.

O nível de isolamento precisa ser explicitado. Compartilhar diretórios, rede,
devices ou capacidades pode reduzir a separação. Um container de sistema é
adequado para ambientes de user space, testes e serviços locais; não deve ser
considerado uma VM quando o requisito é isolar um kernel ou firmware.

## Segurança

Use filesystem somente leitura quando possível, limite capabilities, restrinja
devices e avalie `PrivateUsers`, `SystemCallFilter`, cgroups e rede. Um root
dentro do container não deve ser confundido com root do host, mas configurações
como acesso ao socket Docker, bind mounts amplos ou capabilities excessivas
podem romper a fronteira.

## Operação

Atualizações do root filesystem, logs, lifecycle e rede precisam de uma política
própria. O processo principal deve lidar com sinais, readiness e shutdown. Não
use um container nspawn como forma de esconder uma dependência que deveria ser
modelada em uma unidade systemd, uma VM ou um serviço de orchestrator.

## Relações

- [Containers de sistema](system-containers.md) compara esse modelo com outras opções.
- [systemd](../systemd/unit.md) trata units, targets e serviços.
- [Namespaces Linux](../linux/namespaces.md) explica o isolamento de processos.

## Fontes primárias

- [systemd-nspawn](https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html)
- [machinectl](https://www.freedesktop.org/software/systemd/man/latest/machinectl.html)
- [systemd container interface](https://systemd.io/CONTAINER_INTERFACE/)
