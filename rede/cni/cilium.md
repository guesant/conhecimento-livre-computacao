# Cilium

Cilium é uma plataforma de conectividade, segurança e observabilidade para
workloads. Em Kubernetes, sua forma mais comum de instalação é como CNI, mas o
produto também pode assumir responsabilidades de roteamento, balanceamento de
Services, enforcement de políticas, firewall do host, integração com Gateway
API, service mesh, criptografia e observabilidade.

Essas responsabilidades são independentes. Um cluster pode usar Cilium apenas
como CNI e para NetworkPolicy, ou pode habilitar um conjunto muito maior de
funções. Portanto, "modo de operação do Cilium" não é uma opção única. É a
combinação de decisões sobre dataplane, IPAM, roteamento, policy, Services,
segurança e observabilidade.

## O que ele é e o que não é

Cilium é uma implementação de rede e segurança que usa eBPF para executar
parte da lógica próxima ao kernel Linux. Em Kubernetes, o agente é executado
em cada nó e o operador cuida de tarefas que não precisam ser executadas em
todos os nós.

Cilium não é apenas:

- um plugin CNI;
- um substituto obrigatório do kube-proxy;
- um service mesh;
- um sistema de métricas;
- um coletor de logs;
- um sistema de tracing de aplicação.

Essas funções podem ser compostas, mas habilitar Cilium como CNI não habilita
automaticamente todos esses componentes.

## Modelo mental da arquitetura

Uma instalação Kubernetes normalmente possui os seguintes componentes:

| Componente | Responsabilidade |
| --- | --- |
| CNI plugin | Conecta um Pod à rede quando ele é criado ou removido. |
| Cilium agent | Executa em cada nó, programa o dataplane e aplica políticas locais. |
| eBPF maps e programas | Mantêm identidades, Services, rotas, NAT, policy e eventos. |
| Cilium operator | Executa tarefas de escopo do cluster, como parte do IPAM e reconciliações. |
| Envoy integrado | Processa tráfego L7 quando uma função exige proxy. |
| Hubble | Expõe fluxos e decisões observados pelo dataplane. |
| Cilium CLI e Helm chart | Instalam, validam e configuram os componentes. |

O agente não é um controlador de aplicação. Ele observa endpoints e identidades
de rede, instala programas e mantém o estado necessário para encaminhar e
proteger tráfego.

## eBPF e dataplane

eBPF permite carregar programas verificados no kernel Linux e conectá-los a
hooks de rede, socket, cgroup e tracing. Cilium usa essa capacidade para
encaminhar pacotes, fazer load balancing, aplicar policy, observar fluxos e
interagir com o stack de rede do host.

O dataplane normalmente usa tabelas e programas eBPF para evitar que cada
decisão dependa de uma longa cadeia de regras iptables. Isso pode reduzir
latência e custo de atualização em clusters grandes, mas aumenta a importância
da versão do kernel, dos drivers e da compatibilidade entre recursos.

eBPF não substitui todos os componentes do kernel. Cilium continua dependendo
de interfaces Linux, rotas, dispositivos, namespaces, sockets, conntrack em
alguns caminhos e funcionalidades do kernel que variam entre distribuições.

A página de [eBPF](ebpf.md) explica a tecnologia independentemente do Cilium.

## Dimensões de operação

As subseções seguintes descrevem decisões que podem ser combinadas. Elas não
formam uma lista de perfis mutuamente exclusivos.

### CNI e rede de Pods

No modo CNI, o plugin recebe a chamada de criação do runtime e configura a
interface do Pod, seu endereço, rotas e regras necessárias para que o endpoint
participe do dataplane. O agente acompanha o ciclo de vida do endpoint depois
da criação.

Esse é o núcleo mínimo para usar Cilium em Kubernetes. Mesmo quando outras
funções ficam desabilitadas, ainda é preciso decidir IPAM, roteamento entre
nós, acesso a Services e políticas de segurança.

### Encapsulamento

No modo encapsulado, os nós formam uma rede overlay usando VXLAN ou Geneve. O
pacote do Pod é transportado dentro de um pacote entre nós.

Esse modo reduz a quantidade de conhecimento que a rede física precisa ter
sobre os prefixes de Pods. Ele é útil quando os nós conseguem se alcançar, mas
a infraestrutura não oferece roteamento direto dos CIDRs de Pods.

Os custos são overhead de cabeçalho, menor MTU efetiva, necessidade de liberar
o protocolo e a porta do túnel e uma camada adicional para diagnosticar. O
modo VXLAN usa normalmente UDP 8472 e Geneve usa normalmente UDP 6081, mas a
configuração efetiva e os firewalls do ambiente devem ser verificados.

### Roteamento nativo

No modo nativo, os pacotes não são encapsulados entre nós. A rede subjacente,
as rotas do host, um roteador ou um protocolo de roteamento precisa saber
alcançar os prefixes de Pods.

O modo costuma reduzir overhead e facilitar a observação do caminho real, mas
transfere responsabilidade para a infraestrutura. É necessário definir o
CIDR de roteamento nativo e garantir que os nós e os roteadores conheçam as
rotas necessárias.

Rotas podem ser distribuídas por rotas estáticas, rotas automáticas em uma
mesma rede L2, integração de provedor cloud ou BGP. A página de [roteamento
nativo](native-routing.md) detalha essa alternativa, e
[encapsulamento](encapsulamento.md) detalha o modelo overlay.

### IPAM por escopo do cluster

No cluster-pool IPAM, o Cilium administra pools de endereços de Pods e entrega
faixas aos nós conforme a necessidade. É um modo comum quando o Cilium pode
ser a autoridade para alocação de endereços.

Esse modelo permite mais de um CIDR de cluster, mas não deve ser confundido
com um banco de endereços externo. A alocação e a saúde dos pools passam a ser
parte do estado que precisa ser monitorado.

### IPAM por escopo do nó

No Kubernetes host-scope IPAM, o Kubernetes associa um PodCIDR a cada nó e o
Cilium aloca os endereços dentro dessa faixa. Esse desenho é adequado quando o
control plane já é a autoridade para os PodCIDRs e a integração com a
distribuição nativa do Kubernetes é desejada.

O nó precisa receber um PodCIDR válido antes que o agente consiga alocar
endereços. A alteração de IPAM em um cluster existente deve seguir uma
migração documentada, porque os endpoints existentes podem sofrer
interrupções.

### Multi-Pool e IPAM por CRD

O Multi-Pool permite administrar mais de um pool de endereços e associar
workloads a pools diferentes. Isso pode ser útil para separar redes, famílias
de endereços, requisitos de egress ou classes de workload.

O IPAM baseado em CRD permite que uma fonte externa ou um controlador forneça
os endereços. Os modos cloud, como AWS ENI, Azure IPAM e integrações com GKE,
delegam parte da alocação à rede do provedor.

Não se deve escolher o modo apenas pelo nome. A tabela de compatibilidade entre
IPAM, roteamento, IPv4, IPv6, multi-pool e integração cloud precisa ser
consultada antes da instalação. A [documentação de IPAM do
Cilium](https://docs.cilium.io/en/stable/network/concepts/ipam/) mantém essa
matriz atualizada.

### BPF host routing e caminho pelo kernel

Cilium pode encaminhar tráfego de Pod usando BPF host routing, reduzindo a
passagem por camadas tradicionais do stack de rede. Também existem caminhos
legados ou compatibilidades em que o tráfego continua usando mais partes do
stack do host.

Essa escolha afeta performance, suporte de kernel, comportamento de MTU,
integrações com firewall e troubleshooting. Não é correto comparar duas
instalações Cilium sem informar o caminho de host, o encapsulamento e o
hardware de rede.

### Kube-proxy replacement

Com kube-proxy replacement, o Cilium implementa no dataplane as funções
necessárias para Services Kubernetes. Dependendo da configuração, isso inclui
load balancing de ClusterIP, NodePort, LoadBalancer, ExternalIP, HostPort,
redirecionamento de socket, NAT e caminhos de entrada e saída.

O replacement pode ser mantido desabilitado, habilitado em uma configuração
compatível ou usado como substituição completa, conforme a versão e os
recursos escolhidos. Não se deve presumir que "parcial" e "strict" tenham o
mesmo significado em todas as versões. A configuração instalada e os testes
de compatibilidade são a autoridade.

O modo completo pode remover a dependência de kube-proxy, mas altera uma peça
central do cluster. Antes de adotá-lo, valide Services, NodePort, DSR, host
network, health checks, integração com service mesh e o plano de rollback. A
página de [kube-proxy replacement](kube-proxy-replacement.md) resume a
decisão.

### Load balancing de Services

Cilium pode fazer balanceamento leste-oeste entre Pods e norte-sul entre nós e
serviços externos. Conforme o caminho configurado, ele pode usar socket-level
load balancing, NAT, XDP, Direct Server Return e Maglev consistente.

Esses recursos podem reduzir o custo de encaminhamento e manter distribuição
estável, mas exigem validação de compatibilidade com o kernel, com o NIC, com
health checks, com clientes que preservam o IP de origem e com proxies.

### NetworkPolicy do Kubernetes

Cilium implementa NetworkPolicy de Kubernetes para controlar tráfego entre
endpoints, namespaces, portas e protocolos. O modelo básico é L3/L4 e pode
usar selectors de Pod, namespace, identidade ou CIDR.

A policy é aplicada no dataplane. Um fluxo permitido pela rede ainda precisa
ser autorizado pela aplicação, pelo protocolo e pelo controle de acesso do
serviço de destino.

### CiliumNetworkPolicy e CiliumClusterwideNetworkPolicy

As APIs próprias do Cilium ampliam o modelo Kubernetes. Elas permitem
selectors por identidade, entidades como host e world, regras DNS/FQDN,
portas, CIDRs, opções de ingress e egress, regras L7 e políticas de escopo
cluster-wide.

Essas APIs também permitem expressar dependências de serviço com mais
precisão, mas aumentam o acoplamento ao Cilium. Um cluster que pretende trocar
de CNI deve separar o que é essencial do modelo Kubernetes do que depende dos
CRDs do Cilium.

### Policy baseada em identidade

O Cilium associa identidades de segurança aos endpoints a partir de labels,
namespace, service account e outros atributos. As políticas podem selecionar
essa identidade em vez de depender apenas do IP.

Isso é importante porque Pods são efêmeros e seus IPs mudam. A identidade
reduz a necessidade de reprogramar regras quando um workload é recriado, mas
torna os labels e a sincronização do estado de identidade parte do domínio
de segurança.

### Policy DNS e FQDN

Políticas FQDN podem limitar egress para nomes resolvidos, em vez de permitir
qualquer destino externo. O Cilium observa as respostas DNS e associa os
endereços observados ao conjunto permitido dentro das regras do produto.

Esse modo precisa ser tratado com cuidado em ambientes com CDN, baixa duração
de TTL, múltiplos resolvers, DNS criptografado e destinos que mudam
rapidamente. Não é equivalente a validar a identidade criptográfica do
servidor.

### Visibilidade e policy L7

Quando uma policy L7 direciona o tráfego para o proxy compatível, Cilium pode
aplicar e observar operações de protocolos suportados, como DNS e HTTP. A
visibilidade L7 não aparece automaticamente para todo o tráfego: ela exige o
proxy e a configuração correspondente.

Habilitar L7 pode impor restrições, alterar o caminho do tráfego e aumentar
CPU, memória e exposição de dados sensíveis. Query strings, cabeçalhos,
credenciais e parâmetros podem aparecer nos eventos se a redação não estiver
configurada.

### Firewall do host

O host firewall aplica políticas ao tráfego que entra ou sai do próprio nó,
além das políticas de endpoints. Ele pode proteger interfaces, tráfego entre
host e Pods, e acessos administrativos.

O firewall do host exige inventário das interfaces e dos serviços legítimos do
nó. Uma policy default-deny mal planejada pode bloquear SSH, DNS, o runtime,
o control plane ou a própria comunicação do Cilium.

### BGP control plane

O BGP control plane anuncia prefixes e serviços para roteadores externos e
aprende ou publica rotas conforme a topologia. Ele é útil quando a rede física
já usa BGP e quando o cluster precisa participar dessa topologia sem depender
de um overlay.

BGP não é necessário para todo cluster nativo. Ele introduz sessões,
políticas de anúncio, autenticação, convergência e failure modes que precisam
ser operados como parte da rede. Não substitui automaticamente o IPAM, a
policy ou o balanceamento do Cilium.

### Criptografia transparente

Cilium pode criptografar tráfego entre nós e endpoints usando WireGuard ou
IPsec, conforme o modo e a plataforma. A criptografia é transparente para as
aplicações, mas pode alterar MTU, CPU, observabilidade e suporte a certos
caminhos de aceleração.

É importante separar criptografia em trânsito de autenticação de aplicação.
WireGuard ou IPsec protege o caminho definido pelo Cilium; não substitui TLS,
mTLS, validação de identidade do serviço ou autorização HTTP.

### Bandwidth Manager

O Bandwidth Manager usa eBPF e EDT, Earliest Departure Time, para controlar
bandwidth de Pods e reduzir filas no host. Ele pode respeitar as anotações de
ingress e egress do Kubernetes e servir de base para uso de BBR em Pods,
conforme os requisitos da plataforma.

Esse recurso é uma política de capacidade, não uma garantia de throughput.
Deve ser medido junto com o NIC, o caminho de host, o congestionamento
externo e a qualidade do workload.

### Gateway API e Ingress

Cilium pode atuar como implementação de Ingress e Gateway API. Nessa função,
ele recebe tráfego norte-sul, escolhe Services, executa regras de rota e pode
integrar TLS, políticas e proxies.

Gateway API oferece recursos e papéis mais explícitos do que o modelo
tradicional de Ingress. Usar Cilium como Gateway não exige adotar service mesh
para tráfego leste-oeste.

### Service mesh e Envoy

Cilium pode participar de uma arquitetura de service mesh usando proxy e
recursos L7. O benefício é aproximar conectividade, policy e observabilidade;
o custo é concentrar mais responsabilidades e introduzir interação com o
proxy, certificados, retries, timeouts e telemetria.

Cilium como CNI não é sinônimo de Cilium Service Mesh. A página de [Cilium
Service Mesh](../service-mesh/cilium-service-mesh.md) trata a composição e a
página de [service mesh](../service-mesh/index.md) apresenta a categoria.

### Cluster Mesh

Cluster Mesh conecta múltiplos clusters Cilium, permitindo conectividade entre
workloads, descoberta de serviços globais, load balancing entre clusters e
políticas baseadas em identidade compartilhada.

Os clusters precisam ter endereçamento sem conflitos, conectividade entre nós,
compatibilidade de versões e modo de dataplane compatível. Cluster Mesh não é
uma VPN genérica nem elimina a necessidade de definir limites de confiança,
firewalls, observabilidade e failure domains.

### Hubble

Hubble é a camada de observabilidade que lê eventos produzidos pelo Cilium e
os oferece em nível local, por Relay, pela UI, por métricas ou pelo CLI.
Pode ficar desabilitado, habilitado apenas nos agentes ou exposto de forma
centralizada. A página de [Hubble](hubble.md) descreve esses modos em detalhe.

## Capacidades agrupadas por objetivo

| Objetivo | Recursos possíveis |
| --- | --- |
| Conectar workloads | CNI, IPAM, encapsulamento, roteamento nativo, cloud IPAM. |
| Encaminhar tráfego | eBPF host routing, rotas do host, kube-proxy replacement, socket LB. |
| Publicar serviços | ClusterIP, NodePort, LoadBalancer, DSR, XDP, Maglev. |
| Controlar rede | NetworkPolicy, CiliumNetworkPolicy, políticas cluster-wide. |
| Controlar aplicação | Proxy L7, regras HTTP, DNS e protocolos suportados. |
| Proteger o host | Host firewall, entidades de host, políticas de entrada e saída. |
| Proteger transporte | WireGuard, IPsec, criptografia transparente. |
| Integrar rede externa | BGP, L2 announcements, cloud networking. |
| Expor aplicações | Ingress, Gateway API, TLS e integração com Envoy. |
| Conectar clusters | Cluster Mesh, serviços globais e identidade entre clusters. |
| Controlar capacidade | Bandwidth Manager, EDT e BBR em ambientes suportados. |
| Observar tráfego | Hubble local, Relay, UI, CLI, métricas e exportação. |

## Combinações práticas

### CNI mínimo

Use Cilium para criar a rede dos Pods e aplicar NetworkPolicy Kubernetes.
Mantenha kube-proxy, encapsulamento e observabilidade em configurações
conhecidas para reduzir o número de mudanças simultâneas.

### CNI com diagnóstico

Adicione Hubble nos agentes e, se necessário, Relay para investigar fluxos
entre nós. Esse desenho é útil quando o problema é conectividade, policy, DNS
ou Service, sem introduzir L7 para todo o tráfego.

### Dataplane sem kube-proxy

Combine BPF load balancing com kube-proxy replacement depois de validar
Services, NodePort, host network, health checks e integrações. O benefício é
reduzir uma camada, mas o rollback precisa ser testado antes.

### Rede integrada ao roteamento do ambiente

Use native routing com IPAM compatível e, quando a rede exigir, BGP. Essa
combinação pode evitar overlay, mas exige operação coordenada entre o cluster
e os roteadores.

### Plataforma com entrada e policy L7

Combine Gateway API ou Ingress, Envoy, CiliumNetworkPolicy, Hubble e métricas.
Esse desenho é adequado quando uma plataforma precisa controlar entrada,
identidade, autorização de rede e diagnóstico em um mesmo conjunto de
componentes.

### Vários clusters

Combine Cluster Mesh, endereçamento não conflitante, identidade compartilhada,
serviços globais e observabilidade Relay. A composição deve declarar quais
serviços podem atravessar clusters e qual é o domínio de falha aceito.

## O que escolher em cada cenário

| Cenário | Começo conservador | Recursos que exigem justificativa adicional |
| --- | --- | --- |
| Cluster pequeno | CNI, policy Kubernetes e Hubble sob demanda. | BGP, mesh, L7 global e Cluster Mesh. |
| Rede overlay simples | Encapsulamento com MTU validada. | Native routing sem rotas preparadas. |
| Rede corporativa roteada | Native routing, IPAM compatível e integração de rotas. | Overlay concorrente com a rede existente. |
| Kubernetes gerenciado | Integração de IPAM e load balancer do provedor. | Substituir mecanismos gerenciados sem suporte oficial. |
| Exigência de isolamento | Identidade, default-deny e policies explícitas. | FQDN ou L7 sem inventário de dependências. |
| Entrada HTTP | Gateway API ou Ingress com TLS e observabilidade. | Tratar Gateway como autorização de negócio. |
| Multi-cluster | Cluster Mesh com endereçamento e confiança documentados. | Conectar clusters sem limites de identidade. |

## Performance e operação

O custo do Cilium depende do número de endpoints, identidades, Services,
políticas, regras L7, eventos Hubble, métricas e conexões simultâneas. A
mesma instalação pode ter comportamento muito diferente quando Hubble L7,
proxy, criptografia e métricas de alta cardinalidade são habilitados.

Monitore o agente, o operador, o Envoy, os mapas eBPF, a pressão de memória,
os erros de policy, a saúde dos nós e a latência de Services. Hubble ajuda a
explicar o tráfego, mas não substitui métricas de saturação do dataplane.

Fixe o modo de roteamento, documente MTU, registre os requisitos de kernel e
teste upgrades em um cluster representativo. Mudanças de IPAM, kube-proxy
replacement, criptografia, host firewall e BGP devem ser tratadas como
mudanças de rede, com plano de reversão.

## Limitações e falhas comuns

- Encapsulamento quebrado por firewall ou MTU incorreta.
- Native routing sem rotas para todos os prefixes.
- IPAM esgotado ou incompatível com o roteamento escolhido.
- kube-proxy replacement incompatível com uma integração de proxy.
- Policy baseada em labels que não representam corretamente a confiança.
- FQDN policy afetada por DNS, CDN ou mudanças rápidas de endereço.
- L7 expondo dados sensíveis ou aumentando o custo sem necessidade.
- Host firewall bloqueando acesso administrativo ou componentes do cluster.
- BGP anunciando rotas mais amplas do que o domínio pretendido.
- Cluster Mesh com CIDRs conflitantes ou conectividade parcial entre clusters.
- Hubble, Prometheus ou UI consumindo recursos sem retenção e cardinalidade planejadas.

## O que Cilium não deve substituir

Cilium não substitui autenticação de aplicação, autorização de negócio, TLS
entre clientes externos, logs de auditoria, tracing distribuído, inventário de
ativos, backup, gestão de vulnerabilidades ou testes de disponibilidade.

Ele pode fornecer sinais importantes para esses sistemas, mas a fronteira de
rede não conhece sozinha o significado de uma operação de negócio.

## Fontes primárias

- [Cilium documentation](https://docs.cilium.io/)
- [Introduction to Cilium and Hubble](https://docs.cilium.io/en/stable/overview/intro/)
- [Networking concepts](https://docs.cilium.io/en/stable/network/concepts/)
- [Routing](https://docs.cilium.io/en/stable/network/concepts/routing/)
- [IPAM](https://docs.cilium.io/en/stable/network/concepts/ipam/)
- [Kubernetes without kube-proxy](https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/)
- [Network policy](https://docs.cilium.io/en/stable/security/policy/)
- [Gateway API](https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/gateway-api/)
- [Cluster Mesh](https://docs.cilium.io/en/stable/network/clustermesh/)
- [Bandwidth Manager](https://docs.cilium.io/en/stable/network/kubernetes/bandwidth-manager/)
- [Monitoring and metrics](https://docs.cilium.io/en/stable/observability/metrics/)

## Continue por aqui

[CNI](index.md) explica a categoria. [eBPF](ebpf.md) explica a tecnologia do
dataplane. [Hubble](hubble.md) detalha a observabilidade. [Cilium e
Calico](../../comparacoes/rede/cilium-calico.md) compara implementações.
[CNI, Service, Gateway e service mesh](../../composicoes/kubernetes/rede-e-trafego.md)
mostra como as responsabilidades se relacionam.
