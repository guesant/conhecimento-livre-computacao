# Podman Quadlets: containers como unidades systemd

Rodar um container gerenciado pelo systemd, antes de Quadlets existirem, passava por `podman generate systemd`: criar o container manualmente uma vez, depois pedir ao Podman para inspecionar esse container já em execução e gerar um arquivo de unit `.service` a partir dele. O resultado funcionava, mas o arquivo gerado era um artefato derivado, não uma declaração: continha o comando `podman run` inteiro serializado dentro de um `ExecStart`, difícil de revisar num diff de código e fácil de deixar dessincronizado do container real se alguém recriasse o container manualmente depois. Quadlet resolve isso invertendo a direção: em vez de gerar a unit a partir de um container já existente, o operador escreve um arquivo declarativo descrevendo o container desejado, e é o systemd que gera a unit `.service` correspondente a partir dele, no momento em que recarrega sua configuração.

## O papel do gerador

Um Quadlet é um arquivo de configuração com uma das extensões `.container`, `.pod`, `.volume`, `.network` ou `.kube`, colocado num diretório específico que o Podman e o systemd já sabem procurar (`/etc/containers/systemd/` para configuração de todo o sistema, ou o diretório equivalente sob `~/.config/containers/systemd/` para uso rootless de um usuário). Um binário chamado `podman-system-generator` roda automaticamente sempre que o systemd recarrega sua configuração (`systemctl daemon-reload`, ou na própria inicialização do sistema), varre esses diretórios, e para cada arquivo `.container` encontrado gera uma unit `.service` completa na área de units geradas do systemd, nomeada a partir do arquivo de origem (`app.container` produz `app.service`). Esse `.service` gerado é o que efetivamente é iniciado, parado e monitorado, com o mesmo vocabulário de dependências, timers e targets que qualquer outra unit; a diferença é que ninguém escreve esse arquivo `.service` à mão, ele é regenerado deterministicamente a partir do Quadlet toda vez que a configuração é recarregada.

## Sintaxe: uma seção por conceito, mapeada para uma flag do Podman

Um arquivo `.container` usa a mesma sintaxe de seções `[Chave]` do resto do systemd, mas com uma seção própria, `[Container]`, cujas chaves mapeiam quase diretamente para as flags que um `podman run` equivalente usaria: `Image=` é a imagem, `PublishPort=` equivale a `-p`, `Volume=` equivale a `-v`, `Environment=` equivale a `-e`. Um exemplo mínimo:

```ini
[Container]
Image=docker.io/library/caddy:2.9.1-alpine
PublishPort=8080:80

[Service]
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

A seção `[Service]` e a seção `[Install]` são as mesmas seções de qualquer unit systemd comum, não algo específico do Quadlet: `Restart=on-failure` configura a política de reinício exatamente como faria numa unit `.service` escrita à mão, e `WantedBy=multi-user.target` declara que esse container deveria subir automaticamente no boot, o mesmo mecanismo de `enable` de qualquer serviço. Essa reutilização direta das seções nativas do systemd é o que faz um container Quadlet se comportar, para efeitos de dependência, log e ciclo de vida, como qualquer outro processo gerenciado pelo systemd: `journalctl -u app` mostra os logs do container, `systemctl status app` mostra seu estado, e `After=`/`Requires=` funcionam entre um Quadlet e qualquer outra unit do sistema sem tratamento especial.

## `.pod`, `.volume`, `.network` e `.kube`: o mesmo padrão para outros recursos

Um Quadlet não se limita a um container isolado. Um arquivo `.pod` declara um pod do Podman (um grupo de containers compartilhando namespace de rede, análogo a um Pod do Kubernetes em escala bem menor), permitindo que vários arquivos `.container` referenciem esse pod pelo nome, gerando uma unit própria para o pod que os demais containers dependem automaticamente através dela. Um arquivo `.volume` e um `.network` declaram, da mesma forma declarativa, um volume nomeado ou uma rede Podman, resolvendo a mesma armadilha de um volume ou rede criados manualmente uma vez e depois esquecidos, sem registro em lugar nenhum de como foram criados. Um arquivo `.kube` aceita diretamente um manifesto no formato Kubernetes (`Pod`, `Deployment` simplificado) e o traduz para os recursos Podman equivalentes via `podman kube play`, útil para reaproveitar um manifesto já escrito no formato Kubernetes num único host sem precisar de um cluster de verdade.

## Continue por aqui

[systemd: units, timers e dependências](systemd-units-timers-e-dependencias.md) cobre o modelo de unit, tipo de serviço e dependência que todo Quadlet gerado herda. [Docker vs. Podman: critérios de escolha](especificacoes-oci-e-pilha-de-runtimes.md#docker-vs-podman-criterios-de-escolha) cobre a arquitetura sem daemon do Podman que torna essa integração nativa com o systemd possível em primeiro lugar.
