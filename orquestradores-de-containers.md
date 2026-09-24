# Orquestração de containers

Docker Compose, Docker Swarm e Kubernetes resolvem o mesmo problema geral, rodar múltiplos containers coordenados, em escopos diferentes: um único host para desenvolvimento, um pequeno cluster de poucos hosts, ou uma plataforma de produção escalável.

**Compose** é uma ferramenta de desenvolvimento, não de produção, tudo rodando na mesma máquina coordenado por um único comando; não oferece escalabilidade além de um host, alta disponibilidade, nem os conceitos de rede overlay e service discovery que Swarm e Kubernetes introduzem para múltiplos hosts.

**Swarm** estende o modelo do Compose para múltiplos hosts coordenados por um quorum de managers, com sintaxe próxima (`docker service create` em vez de `docker compose up`); é uma escolha razoável para equipes pequenas já familiarizadas com Compose, clusters de poucas dezenas de nós, sem autoscaling automático, RBAC granular, namespaces nem service mesh, recursos que Kubernetes trata como parte do modelo central.

**Kubernetes** declara o estado desejado em manifests e reconcilia continuamente, com namespaces, RBAC granular, ingress controllers plugáveis e um driver CSI para armazenamento; vale o investimento quando o cluster precisa crescer sem redesenho, quando automação e multi-tenancy são requisitos reais, ou quando o ambiente já se integra ao ecossistema cloud native.

A escolha entre Swarm e Kubernetes especificamente depende do cenário, não de qual é objetivamente melhor. Swarm instala com um comando e estende Docker Compose com curva de aprendizado baixa, mas autoscaling é manual, a rede é overlay com mesh ingress, e a escala testada fica na casa de centenas de nós; Kubernetes exige alguns minutos de setup e introduz conceitos novos (Pods, Services, namespaces), mas oferece HPA automático, CSI integrado e CNI plugável, testado em milhares de nós.

Swarm é suficiente para uma equipe pequena, um cluster de poucas dezenas de nós, sem necessidade de HPA, RBAC granular ou um driver CSI avançado, o exemplo típico sendo três máquinas rodando API, banco e cache. Kubernetes se torna necessário quando a escala precisa crescer de dezenas para milhares de nós sem redesenho, quando a stack de destino já gira em torno dele, ou quando um fluxo GitOps com Argo CD pressupõe sua API.

Não é incomum combinar as duas por ambiente, Swarm ou Compose para staging e testes rápidos, Kubernetes para produção; migrar de Swarm para Kubernetes depois é uma trajetória comum, não um erro de decisão inicial, já que os dois falam a linguagem de containers e a migração reaproveita a maior parte do conhecimento adquirido.

Para quem está começando um projeto novo hoje, aprender Kubernetes diretamente (via K3s, que reduz especificamente o custo de operá-lo em ambientes pequenos) costuma valer mais o investimento do que passar por Swarm primeiro, porque o conhecimento se transfere diretamente para qualquer cluster de produção depois.

## Como o Swarm coordena managers e roteia tráfego

Por trás da API estendida do Compose, o Swarm usa o mesmo tipo de consenso distribuído (Raft) que o etcd embarcado do K3s usa entre servidores, aqui entre managers em vez de servidores Kubernetes: um manager participa da eleição e mantém o estado do cluster (serviços, tarefas, secrets, configs), um worker só executa e reporta tarefas sem nunca participar desse consenso, o que o torna livremente substituível sem risco ao control plane.

A regra de quorum é a mesma, três managers toleram a perda de um, cinco toleram a perda de dois, um número par não ganha tolerância adicional sobre o ímpar imediatamente anterior.

Duas peças de rede resolvem problemas complementares. Uma rede overlay encapsula o tráfego entre containers de um mesmo serviço espalhados por hosts diferentes (tipicamente sobre VXLAN), fazendo-os se enxergarem como se estivessem na mesma rede local independentemente de onde rodam de fato.

Um ingress routing mesh publica a porta de um serviço em todo nó do cluster, mesmo os que não executam nenhuma réplica dele, roteando qualquer requisição recebida até uma réplica disponível em algum lugar, o que dá um balanceamento básico de entrada sem exigir que quem chama saiba em qual host físico o serviço está rodando naquele momento.

Esse comportamento padrão tem uma saída deliberada, o modo host de publicação de porta, que restringe a resposta apenas aos hosts que realmente executam o container, deixando os demais em silêncio na mesma porta; vale a pena quando um serviço com estado precisa de afinidade a um host específico, algo que o balanceamento transparente do modo padrão atrapalharia em vez de ajudar.

Cada peça desse tráfego usa uma porta própria, e o firewall entre managers e entre managers e workers precisa liberar as três para o cluster funcionar:

| Porta | Protocolo | Uso |
| --- | --- | --- |
| 2377 | TCP | Consenso Raft entre managers e entrada de novos nós no cluster. |
| 7946 | TCP/UDP | Gossip de descoberta de nós entre todo o cluster. |
| 4789 | UDP | Encapsulamento VXLAN do tráfego da rede overlay. |

| Identificador | Papel |
| --- | --- |
| `docker network create --driver overlay <nome>` | Cria a rede overlay que um service usa para conectar réplicas entre hosts. |
| `docker service create --publish <porta>:<porta>` | Publica a porta pelo ingress routing mesh, em todo nó do cluster. |
| `docker service create --publish mode=host,target=<porta>,published=<porta>` | Publica a porta só nos hosts que executam o container, contornando o mesh. |
| `docker node ls` | Lista os nós do cluster, papel e status de alcançabilidade. |

O nome de um serviço funciona como hostname dentro da rede overlay: o DNS interno do Swarm converte esse nome num VIP (endereço IP virtual único), e um container de outro serviço na mesma rede alcança qualquer réplica chamando diretamente esse nome, sem saber em qual host físico ela está.

Essa resolução só existe para serviços conectados à mesma rede overlay, um serviço fora dela não é alcançável por nome, e a rede overlay continua sendo o único mecanismo de descoberta que o Swarm oferece nesse cenário.

## Secrets e configs como primitivos nativos, não um Secret do Kubernetes

Secrets e configs no Swarm são primitivos de mais baixo nível que um `Secret` do Kubernetes: ambos são geridos pelos managers e entregues a um container como um arquivo num volume em memória, a diferença entre os dois é só que um secret é cifrado em repouso no armazenamento Raft do manager e uma config não é, pensada para dado não sensível como uma versão ou um endpoint.

Nenhum dos dois tem rotação automática, controle de acesso por secret individual dentro do mesmo serviço, nem log de auditoria de quem acessou o quê; atualizar um valor significa criar um novo objeto e forçar um redeploy do serviço para que ele passe a referenciá-lo, os containers já em execução continuam com a versão antiga até serem substituídos.

Essa simplicidade deliberada, sem RBAC fino, sem log de auditoria, sem rotação, é consistente com o restante do modelo do Swarm: ele resolve o problema de coordenar containers em múltiplos hosts sem tentar cobrir o espaço de controle de acesso e observabilidade que um [secret store externo](secret-store-externo.md) ou o RBAC do Kubernetes cobrem.

| Identificador | Papel |
| --- | --- |
| `docker secret create <nome> <arquivo>` / `docker secret ls` | Cria um secret cifrado em repouso, e lista os secrets já criados. |
| `docker config create <nome> <arquivo>` | Cria uma config em texto claro, sem cifragem. |
| `docker service create --secret <nome>` | Anexa um secret existente a um service. |
| `/run/secrets/<nome>` e `/run/configs/<nome>` | Caminho onde o valor chega dentro do container, montado em memória. |
| `docker service update --secret-rm <antigo> --secret-add <novo>` | Troca qual secret um service referencia, forçando redeploy das tasks. |

## Promover um nó, dados persistentes e atualização no Swarm

Promover um worker para manager (ou rebaixar um manager para worker) muda o total de managers imediatamente, e com ele o próprio critério de quorum descrito acima: promover o segundo manager de um cluster que tinha só um faz o cluster passar a exigir os dois ativos ao mesmo tempo para continuar operando, porque dois é o total e nenhum sozinho forma maioria.

Planejar essa transição pensando no número ímpar final (três ou cinco), sem promover um nó de cada vez sem calcular o efeito, evita criar um cluster temporariamente mais frágil do que antes da promoção.

| Identificador | Papel |
| --- | --- |
| `docker node promote` / `docker node demote <node_id>` | Muda o papel de um nó entre worker e manager, alterando o quorum. |
| `docker swarm leave` | Um nó sai do cluster por conta própria, antes de ser removido do registro. |
| `docker node rm --force <node_id>` | Remove do registro um nó que não está mais alcançável para sair sozinho. |
| `docker swarm join-token worker` / `docker swarm join-token manager` | Recupera o token de entrada para um novo worker ou manager. |

O Swarm não orquestra volumes entre hosts: um volume é local ao host onde o container roda, e se o Swarm reagenda esse container para outro host, por falha, atualização ou rebalanceamento, o volume antigo fica para trás e o container reinicia com dados vazios no host novo.

Três respostas existem para isso, cada uma com um custo diferente. A primeira é aceitar o volume local, adequado só quando a própria aplicação já replica seus dados entre réplicas ou quando a perda é tolerável.

A segunda é um driver de volume externo (NFS, iSCSI, um plugin de nuvem), que desacopla o dado do host ao custo de depender de um backend compartilhado adicional.

A terceira é fixar o container a um host específico por uma constraint de posicionamento, o que resolve o problema evitando o reagendamento por completo, mas transforma a perda daquele host específico numa indisponibilidade garantida do serviço, uma troca de disponibilidade por simplicidade, não uma solução real ao problema de fundo.

| Abordagem | Identificador |
| --- | --- |
| Volume local (padrão) | `--mount type=volume,source=<nome>,target=<caminho>` |
| Driver de volume externo | `docker volume create --driver nfs --opt addr=<servidor> <nome>` |
| Constraint de placement | `--constraint node.hostname==<host>` |

Uma atualização de serviço no Swarm avança uma réplica de cada vez, respeitando um intervalo configurável entre cada uma, e pode ser configurada para pausar automaticamente se uma réplica nova falhar um health check antes de tocar nas demais.

O ponto que engana quem espera um comportamento parecido ao de outros orquestradores é que essa pausa não é um rollback: o Swarm simplesmente para de avançar e devolve a decisão ao operador, que precisa observar o resultado e decidir manualmente entre continuar o rollout ou reverter para a versão anterior; nada volta sozinho, mesmo com o critério de falha configurado para pausar automaticamente.

Uma alternativa que troca simplicidade por um rollback instantâneo é manter duas versões completas rodando ao mesmo tempo (um padrão chamado blue-green), alternando qual delas recebe tráfego externo através do próprio balanceador em vez de substituir réplicas gradualmente; o custo é rodar a capacidade de duas versões completas simultaneamente durante a transição, e depender de algo fora do Swarm para alternar o tráfego entre as duas.

| Identificador | Papel |
| --- | --- |
| `--update-parallelism` / `--update-delay` | Quantas réplicas mudam por vez, e o intervalo de espera entre elas. |
| `--update-failure-action pause` | Pausa o rollout se uma réplica nova falhar o health check. |
| `docker service update --image <imagem> <service>` | Dispara o rolling update para a imagem informada. |
| `docker service rollback <service>` / `--rollback-parallelism` | Reverte o service para a configuração anterior, uma réplica por vez ou em paralelo. |
| `--publish-rm` / `--publish-add` | Tira ou dá a publicação de porta a um service, base do switchover blue-green. |

## De service a tasks: deploy, scheduling e health checks

Um `service` é a declaração de quantas réplicas de uma imagem devem rodar e sob quais condições, e o Swarm mantém essa declaração satisfeita reagendando tasks sempre que a realidade diverge dela; uma task é a instância agendada num nó específico, e o container é o processo real que ela executa ali.

O mesmo arquivo Compose usado em desenvolvimento pode virar uma stack sem conversão, declarando vários services de uma vez e reduzindo a distância entre o ambiente local e o cluster de produção.

Um health check declarado no service dá ao Swarm um critério objetivo para decidir se uma task está saudável, e depois de um número configurável de falhas consecutivas o Swarm mata essa task e agenda uma substituta, sem esperar o operador perceber o problema manualmente.

Uma constraint de placement restringe em quais nós um service pode ser agendado, e serve dois propósitos bem diferentes: fixar um container a um host específico, já visto acima para persistência local, ou direcionar um service para nós com uma característica desejável marcada por um rótulo, como um disco SSD.

| Identificador | Papel |
| --- | --- |
| `--health-cmd` / `--health-interval` / `--health-timeout` / `--health-retries` | Comando de verificação, intervalo entre checagens, tempo limite de cada uma e número de falhas até matar a task. |
| `--constraint node.labels.<chave>==<valor>` | Direciona o service para nós com esse rótulo. |
| `docker node update --label-add <chave>=<valor> <node_id>` | Aplica o rótulo que a constraint acima consulta. |
| `docker service ls` / `docker service ps <service>` | Lista services e as tasks, com o nó onde cada uma roda. |

Escalar um service é sempre uma decisão manual: `docker service scale <service>=<n>` ajusta o número de réplicas para o valor informado, criando ou removendo tasks até esse total, sem HPA nem outra forma de autoscaling automático.

Tirar um nó de circulação para manutenção segue a mesma lógica de dois passos de [cordon e drain](manutencao-de-no-cordon-drain-e-disco.md) do Kubernetes, adaptada ao vocabulário do Swarm: `docker node update --availability drain` move as tasks do nó para outros antes de intervir no host físico, e `--availability active` o devolve ao agendamento depois.

Remover um service com `docker service remove <service>` é destrutivo e imediato: o Swarm encerra todas as tasks associadas sem aviso nem confirmação, e a definição do service (réplicas, constraints, secrets vinculados) desaparece junto, não só os containers em execução.

Volumes locais das tasks removidas não são apagados automaticamente, mas os dados deixam de estar acessíveis pelo service, e recriar o service não os traz de volta ao ponto em que foi removido, apenas cria uma declaração nova a partir do zero.

## Backup e recuperação do estado do cluster

O Swarm guarda todo o estado do cluster, services, tasks, secrets, configs, redes e certificados TLS dos managers, num banco de dados Raft replicado entre eles, armazenado em `/var/lib/docker/swarm/`. Esse diretório é o único artefato que precisa de backup para recuperar a configuração do cluster; ele não inclui dados de volumes, imagens Docker (rebaixadas automaticamente num redeploy) nem logs de containers, efêmeros por natureza.

Como o Raft precisa de um estado interno consistente, o backup mais seguro de `/var/lib/docker/swarm/` requer parar o Docker antes de copiar o diretório e reiniciá-lo em seguida; copiar com o Docker ativo produz um snapshot potencialmente inconsistente, porque o banco de dados pode estar no meio de uma escrita no instante exato da cópia. Rodar esse backup a partir de um único manager já cobre o cluster inteiro, porque o Raft replica o mesmo estado entre todos eles.

Perder um manager enquanto os demais mantêm quorum é o cenário mais simples: o nó offline sai do registro do cluster, é reparado ou substituído, e volta a se juntar como um manager novo, sem precisar de nenhum backup, porque o estado inteiro já sobrevive nos managers restantes. É o mesmo raciocínio por trás da tolerância a falha de um manager em três, ou de dois em cinco: o Raft não perde nada enquanto a maioria continua de pé.

Quando managers suficientes caem ao mesmo tempo para impedir qualquer quorum, o cluster trava e só volta a decidir depois de ser reconstruído a partir de um backup válido de um manager que funcionava antes da queda; sem esse backup, a única saída é recriar o cluster do zero, perdendo services, secrets e configs registrados nele.

A recuperação restaura esse backup num único manager escolhido e roda `docker swarm init --force-new-cluster` ali para criar um cluster novo a partir dele, em vez de retomar o consenso anterior; repetir esse comando em mais de um manager ao mesmo tempo produz dois clusters divergentes a partir do mesmo backup, não um cluster único restaurado. Os demais managers voltam a se juntar a esse cluster recém-criado como se fossem novos, com `docker swarm join --token <token> <ip>:<porta>`.

Confirmar que a recuperação funcionou significa ver, em `docker node ls` e `docker service ls`, os managers reintegrados alcançáveis e os services que existiam antes da perda de quorum reaparecendo com a contagem de réplicas esperada, não apenas ver o cluster respondendo a comandos.

Um service ausente ou com réplicas zeradas indica que o backup usado era anterior à criação dele, ou que não era o mais recente disponível.

Um procedimento de recuperação nunca exercitado fora de uma emergência real não é testado; a mesma disciplina de [RPO e RTO](fundamentos-de-backup-rpo-e-rto.md) que vale para qualquer backup vale aqui, validando o caminho completo, incluindo o force do novo cluster, num servidor descartável antes de depender dele em produção.

## Continue por aqui

[Distribuições Kubernetes](distribuicoes-kubernetes.md) cobre o vocabulário básico (Pod, Deployment, Service) e as opções concretas de distribuição, incluindo o K3s que este cluster usa; [k3s](k3s.md) descreve especificamente essa distribuição.
