# Interfaces, rotas e camada 2 no Linux

Todo pacote que um host Linux envia ou recebe passa por três decisões em sequência: por qual interface ele entra ou sai, por qual rota o kernel escolhe encaminhá-lo, e como ele chega ao vizinho de camada 2 mais próximo nesse caminho. Esta página segue essa ordem, da interface mais próxima do hardware até a rota que decide o próximo salto.

## Interfaces físicas e virtuais

Para o kernel, uma interface de rede é uma estrutura de dados com nome, índice numérico e um conjunto de propriedades, exista ou não hardware físico por trás. `eth0` e `enp3s0` (o nome mais comum hoje, que codifica a localização física do dispositivo em vez de numerar sequencialmente) representam placas físicas reais, assim como `wlan0` para uma placa sem fio.

`lo` é a interface de loopback, sempre presente, usada para tráfego que nunca sai da própria máquina. `veth0`, `br0` e outras interfaces puramente virtuais são criadas e destruídas por software, sem nenhum dispositivo físico correspondente.

Do ponto de vista da pilha de rede, uma interface virtual se comporta como qualquer outra: recebe endereço, aparece na tabela de rotas como destino possível, pode entrar numa bridge. Essa uniformidade é o que permite a containers, VPNs e redes overlay funcionarem sem hardware dedicado, cada um criando as interfaces virtuais de que precisa.

`ip link show` lista as interfaces do host com seu estado, que aparece na saída como `UP` ou `DOWN`. Esse estado combina duas informações distintas: o estado administrativo, que reflete se alguém pediu para ativar a interface, e o estado operacional, que reflete se existe portadora física ou lógica de fato.

O estado operacional aparece no campo `LOWER_UP`, indicando um cabo conectado, um link WiFi associado ou o par de um veth presente do outro lado. Uma interface pode estar administrativamente `UP` e ainda assim sem `LOWER_UP`, o padrão de um cabo desconectado sem que ninguém tenha desativado a interface no sistema.

O MTU de uma interface define o maior payload, em bytes, que ela envia num único quadro sem fragmentação, tipicamente 1500 bytes numa Ethernet física. Quando uma interface encapsula tráfego dentro de outra, como o backend VXLAN do Flannel discutido adiante, o cabeçalho extra consome parte desse orçamento.

Se o MTU da interface física e o MTU esperado dentro do túnel não estiverem coordenados, o resultado é fragmentação silenciosa ou descarte de pacotes maiores que o limite real. Esse sintoma se parece com conexão instável, não com falha total de conectividade, o que costuma atrasar o diagnóstico.

## `ip link` e `ip address`: o par de comandos

`ip link` opera na camada de enlace: mostra e altera estado, MTU, endereço MAC e tipo de interface (veth, bridge, VLAN, entre dezenas de outros). `ip address` opera uma camada acima, mostrando, adicionando e removendo endereços IP de uma interface já existente. A separação reflete a separação real de camadas: uma interface pode existir, estar `UP`, e ainda não ter nenhum endereço, o estado normal logo após ser criada.

```bash
ip link show
ip link show eth0
sudo ip link set eth0 up
sudo ip link set eth0 down
sudo ip link set eth0 mtu 1450
ip address show
sudo ip address add 192.0.2.10/24 dev eth0
sudo ip address del 192.0.2.10/24 dev eth0
```

Uma interface pode carregar mais de um endereço simultaneamente, sem hierarquia entre eles e sem a sintaxe de alias que versões antigas de configuração exigiam, como `eth0:0` e `eth0:1`.

Cada endereço tem seu próprio escopo: `global` para o alcançável fora da máquina, `link` para o válido só dentro do segmento de rede local, e `host` para o que só o próprio host usa, como o endereço da interface de loopback.

O comando `ip`, do pacote `iproute2`, substituiu o antigo `ifconfig` porque este não lida nativamente com tipos de interface virtual modernos, como veth, VXLAN e WireGuard, nem expõe a base de dados de política de rotas usada pelo policy routing descrito mais adiante.

O `ifconfig` também trata múltiplos endereços por interface através da sintaxe de alias já mencionada, um modelo mais limitado do que o kernel oferece hoje. O `ip` foi desenhado contra a API netlink do kernel, mais recente, e por isso cobre o que o kernel expõe de forma mais completa.

## Vizinhança e camada 2

Antes de entregar um quadro a outro host na mesma rede local, é preciso traduzir o endereço IP de destino para o endereço MAC correspondente, sem o qual a camada de enlace não sabe para qual porta encaminhar o quadro. Em IPv4 essa tradução é responsabilidade do ARP; em IPv6, do NDP, que roda sobre ICMPv6. O resultado de ambas fica na tabela de vizinhança do kernel, inspecionável com `ip neigh`.

Cada entrada dessa tabela carrega um estado que descreve a confiança do kernel naquela associação, de uma resolução recém-confirmada até uma que falhou. A tabela abaixo resume os quatro estados possíveis.

| Estado | Significado |
| --- | --- |
| `REACHABLE` | a vizinhança foi confirmada recentemente, dentro da janela de validade |
| `STALE` | a entrada ainda é usada, mas já passou tempo suficiente para ser considerada suspeita |
| `INCOMPLETE` | a resolução ainda está em andamento |
| `FAILED` | as tentativas de confirmação se esgotaram sem resposta |

O kernel reconfirma essas entradas periodicamente, um mecanismo chamado Neighbor Unreachability Detection. Isso explica por que um vizinho que muda de endereço MAC, como uma VM recriada, volta a funcionar sozinho depois de um intervalo, sem que o operador precise limpar a tabela manualmente.

Uma interface TUN opera em camada 3: entrega e recebe pacotes IP, sem cabeçalho de enlace nenhum. É o modelo mais comum para VPNs de acesso remoto e para o WireGuard, porque o único objetivo é rotear tráfego IP através do túnel, sem necessidade de simular uma rede Ethernet completa.

Uma interface TAP opera em camada 2, entregando quadros Ethernet inteiros com seus endereços MAC, o que permite que protocolos dependentes de broadcast funcionem através do túnel como se as duas pontas estivessem no mesmo segmento físico. O custo é mais overhead por pacote e mais complexidade de configuração: uma TAP normalmente só tem utilidade real conectada a uma bridge, o equivalente em software a um switch de camada 2.

Um veth pair são dois pontos de uma mesma interface virtual ligados um ao outro, como as duas pontas de um cabo. `ip link add veth-host type veth peer name veth-container` cria os dois já ligados de uma vez.

Uma ponta é movida para dentro do namespace de rede do container, a outra permanece no host, conectada a uma bridge com `ip link set veth-host master <bridge>`. Essa combinação, veth pair mais bridge, é o que qualquer runtime de container ou CNI monta por baixo para dar a cada Pod uma interface própria, como a [rede interna do cluster](rede-interna-do-cluster.md) usa na prática.

A bridge não encaminha por adivinhação: mantém sua própria tabela de aprendizado, a FDB, populada conforme quadros chegam por cada porta. `bridge fdb show` lista essa tabela, os endereços MAC já vistos e a porta associada a cada um; `bridge link show` mostra o estado de cada porta participante.

Quando o MAC de destino já apareceu na FDB, a bridge encaminha só para a porta correspondente. Quando ainda é desconhecido, ela inunda o quadro para todas as portas, como um switch físico não gerenciado faria antes de aprender a topologia.

## VLAN e VXLAN: segmentar ou estender uma camada 2

Uma VLAN (IEEE 802.1Q) marca um quadro Ethernet com uma tag de 12 bits, permitindo que um único switch físico carregue múltiplos domínios de broadcast isolados entre si, sem cabeamento separado para cada um. Uma porta em modo access pertence a uma única VLAN e não vê a tag; uma porta em modo trunk carrega várias simultaneamente, cada quadro identificado pela sua tag.

O limite de 12 bits permite no máximo 4094 VLANs, suficiente para a maioria das redes, mas insuficiente para provedores multi-tenant que precisam de um segmento isolado por cliente. Uma VLAN sozinha nunca atravessa um roteador: os dois lados precisam de adjacência física de camada 2.

VXLAN, definido na RFC 7348, resolve as duas limitações que a VLAN não resolve: em vez de uma tag dentro do quadro, encapsula o quadro Ethernet completo dentro de um pacote UDP/IP, usando a porta 4789 padrão da IANA. Cada rede virtual é identificada por um VNI de 24 bits, mais de 16 milhões de segmentos possíveis.

O resultado é uma camada 2 que se estende por cima de uma rede de camada 3 já roteada, inclusive entre datacenters diferentes, sem que os switches físicos no caminho precisem saber nada sobre a rede virtual transportada; para eles, é só mais um pacote UDP.

Esse mecanismo aparece no próprio cluster deste notebook: o backend VXLAN do Flannel, padrão do K3s para a [rede interna do cluster](rede-interna-do-cluster.md) e detalhado em [topologias de rede e falhas em K3s multinó](topologias-rede-e-falhas-em-k3s-multino.md), encapsula o tráfego entre Pods de nós diferentes exatamente dessa forma. No Linux, esse backend usa UDP/8472, não a porta 4789 da IANA, valor herdado do módulo VXLAN do kernel Linux desde antes da padronização; no Windows, o mesmo backend usa 4789.

O Proxmox VE SDN permite declarar zonas de rede inteiras no nível do cluster de hipervisores, não host a host. Uma zona `VLAN` mapeia para o modelo 802.1Q tradicional; uma zona `VXLAN` cria uma camada 2 em túnel UDP entre os nós do cluster; e uma zona `EVPN` combina VXLAN com [BGP](tls-mtls-e-confianca-de-rede.md) para prover roteamento de camada 3 entre as redes virtuais, distribuindo essa configuração a partir de um único lugar.

## Roteamento local e longest prefix match

A tabela de roteamento é a estrutura que o kernel consulta para decidir por qual interface e gateway um pacote sai: uma lista de prefixos de rede, cada um associado a uma interface e, quando necessário, a um gateway. `ip route show` lista o conteúdo da tabela principal. Quando mais de uma rota poderia servir ao mesmo destino, o kernel escolhe a mais específica, o prefixo mais longo que ainda cobre esse destino, o critério chamado longest prefix match.

Um host com as rotas `10.0.0.0/8` e `10.1.0.0/16`, ao enviar um pacote para `10.1.5.20`, usa a rota mais específica, porque ela descreve o destino com mais precisão, mesmo as duas cobrindo tecnicamente o mesmo endereço.

A rota `default`, equivalente a `0.0.0.0/0` em IPv4, é o caso extremo desse critério: o prefixo menos específico possível, usado só quando nenhuma rota mais longa corresponde. É por isso que ela funciona como saída para qualquer destino sem rota melhor.

O kernel mantém três tabelas de roteamento por padrão, cada uma com uma prioridade numérica que decide a ordem de consulta. A tabela abaixo lista as três e a prioridade de cada uma.

| Tabela | Prioridade | Papel |
| --- | --- | --- |
| `local` | 0 | rotas de controle para endereços locais e de broadcast, mantida pelo kernel |
| `main` | 32766 | onde `ip route add` insere rotas por padrão |
| `default` | 32767 | vazia, reservada para pós-processamento |

Um administrador pode criar tabelas de roteamento adicionais, nomeadas em `/etc/iproute2/rt_tables` ou referenciadas por número, para o caso em que a decisão de rota precisa depender de algo além do destino, como o endereço de origem, o protocolo ou a porta.

Esse problema, chamado policy routing, é resolvido por duas peças trabalhando juntas: as tabelas adicionais já descritas, e a RPDB, consultada via `ip rule`, que decide qual tabela usar para cada pacote antes de qualquer tabela individual ser consultada. `ip rule add` direciona pacotes que casam um seletor, como o endereço de origem ou a interface de entrada, para uma tabela específica em vez da `main`.

O exemplo mais motivador é um host com duas saídas de rede, uma interface para a rede interna e outra para uma rede de gerência ou um segundo provedor. Sem policy routing, o host tem uma única rota padrão na `main`, então todo tráfego de saída sem rota mais específica usa o mesmo gateway.

Isso é um problema quando a resposta a uma conexão recebida por outra interface deveria, por simetria, sair por ela, e não pelo gateway da rota padrão. A solução é criar uma tabela extra por interface, com sua própria rota padrão apontando para o gateway daquela rede.

Uma regra como `ip rule add from <endereço-da-interface> table <tabela>` garante que a conexão responda pela mesma interface por onde chegou, independentemente do que a rota padrão da `main` diria para o mesmo destino.

## Continue por aqui

[Netfilter, nftables e diagnóstico de rede](netfilter-nftables-e-diagnostico.md) cobre o que decide se um pacote, já roteado pela lógica descrita aqui, é aceito ou descartado, e a ordem prática de investigar um problema de rede. [Rede interna do cluster](rede-interna-do-cluster.md) mostra bridge, veth pair e VXLAN aplicados à CNI real deste cluster, e o [cookbook de comandos de rede e DNS](../referencia/comandos-de-rede-e-dns.md) reúne a sintaxe rápida de diagnóstico e rota.
