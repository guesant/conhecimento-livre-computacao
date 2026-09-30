# D-Bus

D-Bus é um sistema de comunicação entre processos, IPC, orientado a mensagens e usado em sistemas Linux para integrar serviços do sistema e aplicações de desktop. Ele é um projeto do ecossistema freedesktop.org e fornece nomes, objetos, interfaces, métodos, sinais e erros para que componentes se comuniquem sem conhecer diretamente o processo que implementa o serviço.

## Modelo

Uma mensagem D-Bus atravessa um bus. O bus daemon aplica políticas, encaminha a mensagem e mantém nomes bem conhecidos. Um serviço expõe um object path com interfaces; cada interface declara métodos, propriedades e sinais.

| Elemento | Papel |
| --- | --- |
| Bus | Canal lógico de comunicação. |
| Name | Identidade bem conhecida ou nome temporário de um processo. |
| Object path | Endereço de um objeto dentro do serviço. |
| Interface | Contrato de métodos, propriedades e sinais. |
| Method | Operação solicitada por um cliente. |
| Signal | Evento publicado sem exigir uma resposta direta. |
| Error | Resultado que informa falha na chamada. |

## Buses e segurança

O system bus atende serviços do sistema. O session bus atende a sessão do usuário. Políticas do bus controlam quem pode adquirir nomes e enviar ou receber determinadas mensagens. A existência de uma API D-Bus não deve ser confundida com autorização da operação: a política do serviço precisa validar identidade, privilégio e argumentos.

## Relação com systemd

systemd usa D-Bus para administração e pode ativar services sob demanda quando um nome, objeto ou interface é solicitado. Serviços de desktop usam D-Bus para configuração, notificações, gerenciamento de energia, rede, portais e integração entre aplicações. D-Bus não é uma API exclusiva do systemd e não substitui todos os mecanismos de IPC.

## Diagnóstico

Inspecione nomes, objetos e interfaces com ferramentas como `busctl`, `gdbus` ou `dbus-monitor`, respeitando o escopo system e session. Ao investigar uma falha, identifique o bus correto, o nome do serviço, o object path, a interface e o método antes de alterar permissões.

## Fonte primária

- [D-Bus specification](https://dbus.freedesktop.org/doc/dbus-specification.html)
- [D-Bus tutorial](https://dbus.freedesktop.org/doc/dbus-tutorial.html)
- [D-Bus FAQ](https://dbus.freedesktop.org/doc/dbus-faq.html)
- [busctl](https://www.freedesktop.org/software/systemd/man/latest/busctl.html)
