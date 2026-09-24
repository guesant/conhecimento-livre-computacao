# Podman Quadlets: containers como unidades systemd

Rodar um container gerenciado pelo systemd, antes de Quadlets existirem, passava por `podman generate systemd`: criar o container manualmente uma vez, depois pedir ao Podman para inspecionar esse container já em execução e gerar um arquivo de unit a partir dele.

O resultado funcionava, mas o arquivo gerado era um artefato derivado, não uma declaração: continha o comando podman run inteiro serializado dentro do ExecStart, difícil de revisar num diff de código e fácil de deixar dessincronizado do container real se alguém recriasse o container manualmente depois.

Quadlet resolve isso invertendo a direção: em vez de gerar a unit a partir de um container já existente, o operador escreve um arquivo declarativo descrevendo o container desejado, e é o systemd que gera a unit correspondente a partir dele, no momento em que recarrega sua configuração.

## O papel do gerador

Um Quadlet é um arquivo de configuração com uma extensão específica por tipo de recurso, como `.container` (a tabela na próxima seção lista as demais), colocado num diretório específico que o Podman e o systemd já sabem procurar, listado na tabela abaixo.

| Escopo | Diretório |
| --- | --- |
| todo o sistema | `/etc/containers/systemd/` |
| rootless, por usuário | `~/.config/containers/systemd/` |

Um binário dedicado, `podman-system-generator`, roda automaticamente sempre que o systemd recarrega sua configuração, seja por um comando explícito ou na própria inicialização do sistema. Ele varre esses diretórios e, para cada arquivo `.container` encontrado, gera uma unit de serviço completa na área de units geradas do systemd, nomeada a partir do arquivo de origem.

Um `app.container` produz, por exemplo, um `app.service`.

Essa unit gerada é o que efetivamente é iniciado, parado e monitorado, com o mesmo vocabulário de dependências, timers e targets que qualquer outra unit; a diferença é que ninguém escreve esse arquivo à mão, ele é regenerado deterministicamente a partir do Quadlet toda vez que a configuração é recarregada.

## Sintaxe: uma seção por conceito, mapeada para uma flag do Podman

Um arquivo `.container` usa a mesma sintaxe de seções do resto do systemd, mas com uma seção própria chamada Container, cujas chaves mapeiam quase diretamente para as flags que um comando de execução equivalente usaria, como na tabela abaixo.

| Chave do Quadlet | Equivale à flag |
| --- | --- |
| `Image=` | a própria imagem |
| `PublishPort=` | `-p` |
| `Volume=` | `-v` |
| `Environment=` | `-e` |

Um exemplo mínimo:

```ini
[Container]
Image=docker.io/library/caddy:2.9.1-alpine
PublishPort=8080:80

[Service]
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

As seções Service e Install são as mesmas seções de qualquer unit systemd comum, não algo específico do Quadlet: `Restart=on-failure` configura a política de reinício exatamente como faria numa unit de serviço escrita à mão, e `WantedBy=multi-user.target` declara que esse container deveria subir automaticamente no boot, o mesmo mecanismo de enable de qualquer serviço.

Essa reutilização direta das seções nativas do systemd é o que faz um container Quadlet se comportar, para efeitos de dependência, log e ciclo de vida, como qualquer outro processo gerenciado pelo systemd.

`After=` e `Requires=` funcionam entre um Quadlet e qualquer outra unit do sistema sem tratamento especial, e os comandos usuais de inspeção continuam válidos, como na tabela abaixo.

| Comando | O que mostra |
| --- | --- |
| `journalctl -u app` | os logs do container |
| `systemctl status app` | o estado do serviço |

## `.pod`, `.volume`, `.network` e `.kube`: o mesmo padrão para outros recursos

Um Quadlet não se limita a um container isolado; a tabela abaixo resume os demais tipos de arquivo que ele aceita.

| Extensão | Declara |
| --- | --- |
| `.pod` | um pod do Podman, um grupo de containers compartilhando namespace de rede, análogo a um Pod do Kubernetes em escala bem menor |
| `.volume` | um volume nomeado |
| `.network` | uma rede Podman |
| `.kube` | recursos traduzidos de um manifesto Kubernetes, via `podman kube play` |

Um arquivo `.pod` permite que vários arquivos `.container` referenciem esse pod pelo nome, gerando uma unit própria para o pod da qual os demais containers dependem automaticamente.

Um volume ou uma rede declarados dessa forma resolvem a mesma armadilha de um recurso criado manualmente uma vez e depois esquecido, sem registro em lugar nenhum de como foi criado. Um manifesto Kubernetes aceito por um arquivo `.kube` é útil para reaproveitar algo já escrito nesse formato num único host, sem precisar de um cluster de verdade.

## Continue por aqui

[systemd: units, timers e dependências](systemd-units-timers-e-dependencias.md) cobre o modelo de unit, tipo de serviço e dependência que todo Quadlet gerado herda. [Podman](containers/engines/podman.md) cobre a arquitetura sem daemon que torna essa integração nativa com o systemd possível em primeiro lugar.
