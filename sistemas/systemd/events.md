# Eventos e ativação

O systemd pode reagir a eventos em vez de manter todos os processos ativos desde o boot. Uma unit pode ser ativada por conexão em socket, mudança de arquivo, dispositivo, timer, target ou mensagem D-Bus. Essa abordagem reduz consumo ocioso e expressa dependências no mesmo grafo de lifecycle.

## Fontes de ativação

| Mecanismo | Unit | Exemplo |
| --- | --- | --- |
| Socket | `.socket` | Iniciar um daemon quando chega a primeira conexão. |
| Arquivo ou diretório | `.path` | Reagir a criação ou alteração de um arquivo. |
| Dispositivo | `.device` | Relacionar lifecycle a um dispositivo exposto pelo udev. |
| Calendário ou tempo | `.timer` | Iniciar tarefa periódica ou atrasada. |
| Estado lógico | `.target` | Coordenar um grupo de units. |
| D-Bus | propriedade da service | Ativar um serviço quando um nome ou objeto é solicitado. |

A ativação não elimina a necessidade de readiness. Um socket pode aceitar uma conexão antes de a aplicação terminar de carregar configuração, e uma dependência D-Bus pode falhar se a service estiver mal configurada.

## Eventos e dependências

Um evento inicia ou altera uma unit; `After=` e `Before=` definem ordenação; `Requires=`, `Wants=` e `BindsTo=` definem requisitos. Misturar esses conceitos produz sistemas que iniciam na ordem aparentemente correta, mas continuam sem a dependência realmente necessária.

## udev e dispositivos

udev observa eventos do kernel e materializa dispositivos em `/dev` e propriedades. O systemd pode representar esses dispositivos como units `.device` e associar services ou mounts. A política de segurança deve impedir que a presença de um dispositivo seja usada como caminho inesperado para executar código privilegiado.

## Fonte primária

- [systemd architecture](https://systemd.io/ARCHITECTURE/)
- [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html)
- [systemd.path](https://www.freedesktop.org/software/systemd/man/latest/systemd.path.html)
- [systemd.socket](https://www.freedesktop.org/software/systemd/man/latest/systemd.socket.html)
