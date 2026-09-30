# systemd unit

Uma unit é um objeto de configuração e lifecycle que o systemd pode carregar,
ativar, parar, monitorar ou relacionar a outras units. O sufixo do arquivo
define o tipo e o conjunto de propriedades aplicável.

## Tipos importantes

| Tipo | Responsabilidade |
| --- | --- |
| service | processo ou tarefa executável |
| timer | agenda a ativação de uma service |
| socket | escuta socket e pode ativar uma service |
| mount | gerencia um ponto de montagem |
| target | agrupa units e representa um estado lógico |

A unit pode estar instalada, habilitada, ativa, falha ou apenas carregada. Esses
estados não são equivalentes: uma service habilitada será iniciada por uma
target futura, mas pode estar parada agora.

## Arquivo e precedência

A configuração pode vir da unit distribuída pelo pacote, de um drop-in e de
uma unit local. `systemctl cat nome.service` mostra a composição efetiva.
Drop-ins são preferíveis a copiar um arquivo inteiro, porque preservam as
atualizações do pacote e expressam apenas a alteração necessária.

Use `systemctl daemon-reload` depois de alterar arquivos de unit. Isso
recarrega a configuração, mas não inicia nem reinicia automaticamente o
serviço.

## Relações

- [systemd service](service.md) descreve processos long-running e tarefas.
- [systemd timer](timer.md) substitui agendamentos simples quando lifecycle e
  logs do systemd importam.
- [systemd target](target.md) agrupa estados e pontos de sincronização.
- [Dependências systemd](dependencies.md) separa ordem de requisito e
  propagação.

## Fonte primária

- [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html)
