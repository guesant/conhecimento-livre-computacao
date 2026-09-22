# Executar serviços em um único host

Um único host pode executar aplicações de várias formas corretas. A decisão não é "Docker ou Kubernetes?" isoladamente: primeiro é preciso identificar quais propriedades da plataforma são realmente necessárias.

## Premissas do cenário

Há um único failure domain físico. Portanto, nenhuma ferramenta executada somente nesse host cria alta disponibilidade contra a perda do host. Kubernetes single-node pode reconciliar processos depois de uma falha de aplicação, mas não mantém o serviço disponível se a máquina, disco, energia ou rede do host falhar.

Essa distinção elimina uma justificativa comum mas incorreta: adicionar um orquestrador local não transforma um host em infraestrutura altamente disponível.

## Padrão 1: processo nativo + systemd

É o desenho de menor número de camadas quando a aplicação já é distribuída como binário ou pacote adequado ao sistema operacional.

Use quando há poucos serviços, isolamento por container não é requisito e integração direta com systemd, filesystem e ferramentas do host é desejável.

O custo é maior acoplamento ao sistema operacional e menor portabilidade do empacotamento. Dependências da aplicação precisam ser geridas cuidadosamente para não contaminar o host.

## Padrão 2: Podman + Quadlet + systemd

Containers fornecem empacotamento e isolamento; Quadlet transforma a declaração dos containers em units geradas e deixa ciclo de vida, dependências e logs sob systemd.

É um bom encaixe quando existe um único host, a quantidade de serviços é administrável e o objetivo é ter containers declarativos sem introduzir uma API de cluster.

Uma composição típica é: imagens OCI + Podman rootless quando possível + Quadlets versionados + systemd + journal + backup explícito dos volumes.

Evite recriar manualmente containers que deveriam ser geridos por Quadlet. Isso cria duas fontes de verdade.

## Padrão 3: Docker/Compose

Compose descreve uma aplicação multi-container de forma compacta e possui ecossistema amplo. Em um único host ele pode ser suficiente para aplicações pequenas e stacks de terceiros que já publicam um Compose mantido.

É especialmente conveniente quando o artefato upstream já é Compose e não existe benefício claro em traduzi-lo para outra plataforma.

O ponto fraco não é "Compose não pode rodar produção" como regra absoluta. O limite é o conjunto de propriedades oferecido: um host, modelo de reconciliação e rollout mais simples, menor isolamento administrativo e menos APIs de plataforma que Kubernetes.

## Padrão 4: Kubernetes single-node

K3s, MicroK8s e outras distribuições tornam Kubernetes viável em uma máquina. O benefício não é HA local; é usar a API e o ecossistema Kubernetes: controllers, CRDs, Helm, operators, policies, GitOps e uma interface operacional transferível para clusters maiores.

Faz sentido quando esses recursos são requisitos reais, quando as aplicações já dependem de operators/CRDs, quando o ambiente serve também como plataforma de aprendizado/validação Kubernetes ou quando existe intenção concreta de compartilhar o mesmo modelo operacional com outros clusters.

O custo é maior quantidade de componentes, certificados, control plane, CNI, storage abstractions e conhecimento necessário para diagnosticar falhas.

## E Portainer?

Portainer é uma interface de administração, não um substituto para runtime ou orquestrador. Ele pode administrar Docker, ambientes Podman em capacidades suportadas e Kubernetes conforme produto/configuração. A pergunta correta é se uma UI administrativa agrega valor ao padrão escolhido, não "Portainer ou Kubernetes?".

Uma UI não deve virar a única fonte de configuração. Mudanças importantes feitas somente por clique tendem a criar estado que não pode ser reconstruído.

## Comparação contextual

| Propriedade | systemd nativo | Podman + Quadlet | Docker Compose | K3s single-node |
| --- | --- | --- | --- | --- |
| empacotamento OCI | não necessário | sim | sim | sim |
| número de camadas | baixo | baixo/médio | baixo/médio | alto |
| API Kubernetes | não | não | não | sim |
| Helm/operators/CRDs | não | não | não | sim |
| integração systemd | direta | direta | indireta | cluster |
| HA contra perda do host | não | não | não | não |
| caminho operacional para multi-node Kubernetes | indireto | indireto | indireto | direto |

## Sinais para escolher o desenho mais simples

Poucos serviços, uma única equipe, ausência de CRDs/operators, baixa frequência de deploy e nenhuma necessidade de scheduling entre nós favorecem systemd, Quadlet ou Compose.

Isso não significa que Kubernetes seja "errado". Significa que seu custo precisa comprar uma propriedade que o cenário valoriza.

## Sinais para Kubernetes mesmo com um nó

Dependência de APIs Kubernetes, GitOps baseado em reconciliação de recursos, operators, políticas Kubernetes, necessidade de reproduzir a mesma plataforma usada em outros ambientes ou expectativa concreta de expansão são justificativas melhores que "é padrão da indústria".

## Caminhos de evolução

Compose ou Quadlet -> Kubernetes não precisa ser tratado como fracasso. Imagens OCI, health checks, configuração externa, volumes bem definidos e observabilidade portável reduzem custo de migração.

Kubernetes single-node -> multi-node também exige trabalho: storage, quorum/control plane, load balancing, failure domains e políticas que eram irrelevantes num único host passam a importar.

## Anti-patterns

Não use Kubernetes para simular HA em um único host. Não adicione Portainer para esconder uma plataforma que ninguém sabe operar por CLI/API. Não escolha Compose apenas porque o YAML é menor se a aplicação depende de primitives Kubernetes. Não escolha Kubernetes apenas para executar três containers independentes quando nenhuma de suas propriedades adicionais será usada.

## Continue por aqui

[Podman Quadlets](../../podman-quadlets.md), [K3s](../../k3s.md), [orquestradores de containers](../../orquestradores-de-containers.md) e [systemd](../../systemd-units-timers-e-dependencias.md) aprofundam as peças.
