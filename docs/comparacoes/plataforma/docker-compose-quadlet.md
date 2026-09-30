# Comparação entre Docker Compose e Podman Quadlet

Docker Compose e Podman Quadlet podem descrever containers que executam no
mesmo host, mas não são duas sintaxes para o mesmo modelo operacional. Compose
descreve uma aplicação composta e seus recursos. Quadlet descreve recursos do
Podman que serão transformados em units do systemd.

Essa diferença determina o que pode ser traduzido diretamente, o que precisa
ser redesenhado e qual ferramenta deve permanecer como fonte de verdade.

## O que cada modelo representa

Compose é um modelo de aplicação. Um arquivo pode declarar serviços, redes,
volumes, configs, secrets, dependências, perfis e políticas relacionadas ao
projeto. O comando `docker compose` interpreta essa descrição e coordena o
ciclo de vida dos containers no escopo do projeto.

Quadlet é um modelo de integração entre Podman e systemd. Arquivos como
`.container`, `.pod`, `.volume`, `.network`, `.image`, `.build` e `.kube`
descrevem recursos que o gerador do Podman transforma em units do systemd.
Depois disso, o systemd assume o ciclo de vida, as dependências, os logs e as
políticas de reinício.

Compose costuma responder à pergunta "quais serviços compõem esta aplicação?".
Quadlet costuma responder à pergunta "como este recurso do Podman deve ser
operado neste host pelo systemd?".

Nenhum dos dois fornece, por si só, scheduling entre vários nós,
reconciliação de cluster, rollout progressivo, autoscaling distribuído ou
failover de volumes. Quando essas propriedades são requisitos, é necessário
avaliar um orquestrador ou uma plataforma que as implemente.

## Tabela de correspondência

| Docker Compose | Podman Quadlet | Observação |
| --- | --- | --- |
| `services.<nome>` | `<nome>.container` | Um serviço normalmente vira uma unit de container. |
| Serviço com vários containers no mesmo namespace | `.pod` e arquivos `.container` associados | Use um pod quando o compartilhamento de namespaces fizer parte do desenho. |
| `image` | `Image=` em `[Container]` | A referência da imagem deve continuar sendo determinística. |
| `build` | `.build` ou uma etapa externa de build | Não há tradução geral para todos os campos e extensões de `build`. |
| `command` | `Exec=` | A forma exata depende de como o processo deve ser iniciado no container. |
| `entrypoint` | `Entrypoint=` | O comportamento precisa ser validado com a imagem usada. |
| `environment` | `Environment=` | Pode ser repetido para várias variáveis. |
| `env_file` | `EnvironmentFile=` | O arquivo precisa existir no escopo e nas permissões do serviço. |
| `ports` | `PublishPort=` | A rede host e o escopo rootless alteram as portas possíveis. |
| `volumes` | `Volume=` | Pode referenciar volume nomeado, bind mount ou um `.volume`. |
| `networks` | `Network=` e `.network` | A rede precisa ser criada ou referenciada explicitamente no host. |
| `depends_on` | `Requires=`, `Wants=` e `After=` em `[Unit]` | `After=` ordena inicialização, mas não prova prontidão da aplicação. |
| `restart` | `Restart=` e `RestartSec=` em `[Service]` | A política passa a ser do systemd, não do projeto Compose. |
| `healthcheck` | Opções de health check do Podman | O suporte e a semântica dependem da versão do Podman. |
| `logging` | journald e opções de log do Podman | A consulta principal passa a ser feita com `journalctl`. |
| `profiles` | units, targets, templates ou seleção de enable | Não existe uma tradução única para perfis Compose. |
| `secrets` e `configs` | arquivos protegidos, mounts, credenciais do systemd ou um secret manager | Não presuma equivalência de armazenamento e ciclo de vida. |
| `scale` | units instanciadas ou um orquestrador | Quadlet não fornece scaling distribuído. |
| `docker compose up` | `systemctl start` ou `systemctl enable --now` | O comando opera uma unit em vez de um projeto Compose. |
| `docker compose down` | `systemctl stop` e remoção explícita de recursos | Parar uma unit não significa apagar volumes e redes. |
| `docker compose logs -f` | `journalctl -u <unidade> -f` | O journal é a interface operacional do serviço. |
| `docker compose ps` | `systemctl status` e `podman ps` | É necessário distinguir estado da unit e estado do container. |

Essa tabela é uma correspondência operacional, não uma promessa de
compatibilidade. A unidade de configuração muda de um projeto Compose para uma
unit systemd gerada a partir de um recurso Quadlet.

## Exemplo de migração

Uma composição simples pode ser escrita assim:

```yaml
services:
  web:
    image: ghcr.io/example/web:1.2.3
    environment:
      APP_ENV: production
    env_file:
      - web.env
    ports:
      - "8080:8080"
    volumes:
      - web-data:/var/lib/web
    restart: unless-stopped

volumes:
  web-data:
```

Uma versão inicial para um host Podman poderia ser:

```ini
[Unit]
Description=Web application
Wants=network-online.target
After=network-online.target

[Container]
Image=ghcr.io/example/web:1.2.3
Environment=APP_ENV=production
EnvironmentFile=%h/.config/web/web.env
PublishPort=8080:8080
Volume=web-data:/var/lib/web

[Service]
Restart=always
RestartSec=5s

[Install]
WantedBy=default.target
```

O arquivo deve ser salvo como `web.container` em um diretório Quadlet do
usuário, como `~/.config/containers/systemd/`, ou no diretório rootful
correspondente. Depois da alteração, o operador recarrega as units e inicia o
serviço:

```sh
systemctl --user daemon-reload
systemctl --user enable --now web.service
systemctl --user status web.service
journalctl --user -u web.service -f
```

Em uma instalação rootful, use o escopo de sistema e os comandos `systemctl`
apropriados. Para containers rootless persistirem sem uma sessão interativa,
o usuário precisa ter um serviço de usuário com linger habilitado. A política
de portas, os caminhos de configuração e as permissões de volume também
precisam ser revisados nesse escopo.

O campo `restart: unless-stopped` não tem uma conversão textual perfeita para
`Restart=always`. A tradução acima expressa a intenção de reiniciar o
serviço, mas a política final deve considerar o comportamento desejado durante
paradas administrativas, falhas do processo e reinicialização do host.

## O que não deve ser traduzido mecanicamente

### Build de imagem

O Compose pode combinar o build com a inicialização da aplicação. Em Quadlet,
é mais previsível manter o build como uma etapa de CI ou como um recurso `.build`
separado, publicar uma imagem identificável e fazer o `.container` consumir
essa imagem por `Image=`. Isso separa a produção do artefato do ciclo de vida
do serviço.

### Dependências e prontidão

`depends_on` estabelece uma relação entre serviços Compose, mas a ordenação e a
prontidão não são a mesma coisa. Em Quadlet, `After=` apenas controla a ordem
de ativação da unit, enquanto `Requires=` e `Wants=` controlam relações de
dependência. Nenhum deles substitui uma verificação de prontidão do processo,
retry de conexão ou tratamento de indisponibilidade na aplicação.

`condition: service_healthy` também não deve ser convertido simplesmente em
`After=`. A aplicação dependente deve ter uma estratégia própria para aguardar
o serviço necessário, ou a unit deve ser complementada com uma condição
operacional que seja realmente compatível com o serviço.

### Secrets e configs

Compose possui objetos próprios para `secrets` e `configs`, mas a segurança
real depende da implementação. Quadlet não cria uma camada universal de
secret management. Um arquivo `EnvironmentFile=` pode ser adequado para uma
configuração protegida em um host controlado, mas não deve substituir um
secret manager quando há requisitos de rotação, auditoria, distribuição ou
separação de privilégios.

### Profiles e escala

Profiles Compose são uma forma de selecionar partes de uma aplicação. Em
systemd, a seleção pode ser modelada com units separadas, targets, templates ou
enablement por usuário. A decisão deve ser explícita, porque o systemd não
interpreta `profiles`.

Da mesma forma, várias instâncias de uma unit podem ser úteis em um host, mas
isso não equivale a `scale` em um cluster. Não use templates systemd para
simular scheduling, distribuição de tráfego, placement ou failover entre nós.

## Operação e observabilidade

No Compose, o projeto é normalmente a unidade de inspeção. Em Quadlet, a unit
systemd e o container são duas visões do mesmo serviço:

| Pergunta | Compose | Quadlet |
| --- | --- | --- |
| O serviço está ativo? | `docker compose ps` | `systemctl status web.service` |
| O container existe? | `docker ps` | `podman ps` |
| Onde estão os logs? | `docker compose logs` | `journalctl -u web.service` |
| Qual é a configuração declarada? | `compose.yaml` | `web.container` e arquivos relacionados |
| Quem reinicia o processo? | Compose e engine | systemd e Podman |
| Como verificar dependências? | modelo Compose e engine | `systemctl list-dependencies` |

A separação entre unit e container evita um diagnóstico incompleto. Uma unit
ativa pode ter iniciado um container que terminou logo depois, e um container
existente pode não estar sendo gerenciado pela unit que a equipe considera a
fonte de verdade.

## Rootless, rootful e diretórios

Compose normalmente começa pelo projeto e pelo engine selecionado. Quadlet
precisa de uma decisão adicional sobre o escopo do systemd:

| Escopo | Local típico | Operação |
| --- | --- | --- |
| Rootless | `~/.config/containers/systemd/` | `systemctl --user` |
| Rootful | `/etc/containers/systemd/` | `systemctl` |

O escopo rootless reduz privilégios e combina bem com serviços de usuário, mas
exige atenção a linger, portas privilegiadas, permissões de bind mounts,
subuid, subgid e disponibilidade do socket do Podman. O escopo rootful pode
ser necessário para portas baixas, mounts protegidos ou integração com
serviços do sistema, mas amplia o impacto de uma configuração incorreta.

Quadlet exige cgroups v2. Imagens que precisam ser baixadas ou construídas na
ativação também podem ultrapassar o timeout padrão de inicialização do
systemd. Em produção, prefira pre-pull ou configure `TimeoutStartSec=` de
forma deliberada.

## Quando escolher cada um

Compose é uma escolha natural quando a unidade de trabalho é uma aplicação
multi-container portátil, principalmente em desenvolvimento, testes, CI ou um
host em que a equipe já opera o ciclo de vida pelo Compose.

Quadlet é uma escolha natural quando a unidade de trabalho é um serviço de um
host Linux e o systemd já deve controlar inicialização, dependências, logs,
reinício, permissões e integração com o boot. Ele também é interessante para
containers rootless e para configurações versionadas próximas do sistema que
as executa.

Quando a necessidade é operar vários hosts, reconciliar estado desejado,
distribuir workloads, executar rollouts progressivos ou reagir à falha de um
nó, a pergunta deixa de ser Compose versus Quadlet. Nesse ponto deve-se
comparar uma plataforma de orquestração adequada ao cenário.

Não mantenha Compose e Quadlet simultaneamente como fontes de verdade para os
mesmos containers. Se a migração for gradual, defina qual ferramenta possui a
responsabilidade de cada serviço, evite nomes e volumes compartilhados por
acidente e documente a janela em que o serviço ficará sob controle de cada
modelo.

## Relações

- [Compose Specification](../../containers/compose/specification.md) define o modelo declarativo de aplicações compostas.
- [Docker Compose](../../containers/compose/docker-compose.md) explica o uso do modelo com Docker.
- [Podman Compose](../../containers/compose/podman-compose.md) explica o wrapper e o provedor externo.
- [Podman Quadlets](../../podman-quadlets.md) explica a integração declarativa entre Podman e systemd.
- [Systemd: units, timers e dependências](../../systemd-units-timers-e-dependencias.md) explica as primitives que o Quadlet reutiliza.
- [Serviços em um único host](../../cenarios/execucao/single-node.md) compara Compose, Quadlet e outras opções no cenário single-node.

## Fontes primárias

- [Compose Specification](https://compose-spec.github.io/compose-spec/00-overview.html)
- [Docker Compose](https://docs.docker.com/compose/)
- [Podman systemd units e Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Podman Quadlet](https://docs.podman.io/en/latest/markdown/podman-quadlet.1.html)
- [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html)
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
