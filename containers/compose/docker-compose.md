# Docker Compose

Docker Compose é uma implementação para definir e operar uma aplicação composta por serviços, redes, volumes, configs e secrets a partir de um arquivo compatível com a [Compose Specification](specification.md). Ele coordena containers no escopo de um projeto local e não é um scheduler de cluster.

## Modelo de projeto

Um projeto Compose agrupa recursos por um nome e cria uma rede padrão na qual os serviços podem se encontrar pelo nome do serviço. O serviço declara uma imagem ou um build, portas, volumes, variáveis e dependências. A rede interna não transforma o nome do serviço em um endereço estável fora do projeto e não substitui DNS, ingress ou service discovery de um cluster.

Volumes nomeados podem sobreviver à recriação do container, mas continuam sujeitos ao ciclo de vida e à política de backup do host. Um volume local não é automaticamente replicado, versionado ou protegido contra falha do disco.

## Ciclo de vida

Compose torna explícitas operações como build, pull, create, start, stop, restart e remoção do projeto. A ordenação de dependências pode controlar quando uma operação começa, mas não transforma uma verificação de processo em prova de que a aplicação está pronta. Healthchecks e lógica de retry continuam sendo responsabilidades da composição e da própria aplicação.

## Limites

Compose é apropriado para desenvolvimento, testes, automação local e serviços pequenos em um host. Ele não oferece por si só scheduling entre vários nós, reconciliação contínua do estado desejado, rollout progressivo, autoscaling distribuído ou failover de volumes. Quando essas necessidades aparecem, a decisão deve considerar um scheduler ou uma plataforma que possua essas propriedades, em vez de acumular scripts em torno do Compose.

## Relações

- [Compose Specification](specification.md) define o modelo compartilhado.
- [Podman Compose](podman-compose.md) usa um provedor externo para operar uma composição no Podman.
- [Quando Kubernetes faz sentido](../../cenarios/execucao/quando-kubernetes.md) compara o custo da plataforma com as necessidades do cenário.
- [Imagem de container](../image.md) é a unidade distribuída que um serviço pode consumir.

## Fontes primárias

- [Docker Compose documentation](https://docs.docker.com/compose/)
- [Compose Specification](https://github.com/compose-spec/compose-spec)
