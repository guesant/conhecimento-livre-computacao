# Tipos de firewall

Firewall é uma política de controle de tráfego entre zonas de confiança. Ele pode
permitir, rejeitar, descartar ou inspecionar fluxos conforme endereços, portas,
protocolos, estado da conexão, identidade, aplicação ou conteúdo. Não é um produto
único nem uma substituição para autenticação, autorização, atualização, segmentação ou
segurança da aplicação.

Os tipos abaixo se sobrepõem. Um firewall pode ser, por exemplo, um appliance de rede
stateful com inspeção de aplicação e funções de próxima geração, enquanto outro pode
ser um filtro stateless no kernel de um host.

## Por onde o firewall atua

### Firewall de host

Roda no próprio servidor ou endpoint e controla tráfego de entrada, saída e, em alguns
casos, encaminhado pelo host. O benefício é conhecer interfaces, processos, usuários,
namespaces e redes locais. O custo é administrar políticas em muitos hosts e lidar com
ordens de regra diferentes em cada sistema.

`nftables`, `iptables`, `firewalld`, UFW, Windows Defender Firewall e PF são exemplos
de mecanismos ou interfaces usados nesse espaço. [Netfilter](netfilter.md) e [nftables](nftables.md)
explica o caminho do pacote no Linux.

### Firewall de rede

Fica entre redes ou segmentos e aplica uma política centralizada para muitos clientes.
Pode ser um appliance físico, uma máquina virtual, um serviço de nuvem ou um conjunto
distribuído de agentes. É útil para controlar zonas, egress, VPN, NAT e entrada
perimetral, mas não observa necessariamente o processo que abriu a conexão.

### Firewall distribuído

Distribui a política nos nós que hospedam workloads. Kubernetes NetworkPolicy, Cilium
NetworkPolicy, security groups distribuídos e agentes de endpoint se aproximam desse
modelo. A política acompanha a identidade ou o workload, reduzindo a dependência de
um único ponto de passagem, mas exige uma fonte de verdade e observabilidade
consistentes.

### Firewall pessoal ou de endpoint

É uma forma de firewall de host voltada ao usuário final. Além de portas e interfaces,
pode perguntar se um aplicativo pode escutar ou sair para a rede. O controle é útil
contra software inesperado no endpoint, mas pode gerar decisões ruins quando o usuário
aceita prompts sem entender a origem.

## Como a decisão é tomada

### Filtro stateless de pacotes

Examina cada pacote de forma independente. Regras normalmente usam endereço de origem,
destino, protocolo, porta, interface e direção. É previsível, simples e barato, mas
não sabe se um pacote pertence a uma conexão válida. A política precisa expressar
explicitamente o tráfego de retorno.

Stateless é adequado para ACLs simples, filtros de borda, roteadores e regras que
precisam de alto desempenho e comportamento facilmente auditável. Ele não é inferior em
qualquer cenário; apenas não oferece o contexto de uma conexão.

### Stateful firewall

Mantém estado dos fluxos, geralmente por meio de connection tracking. Pode permitir
respostas de conexões iniciadas de forma válida sem abrir todas as portas de retorno.
Também pode acompanhar protocolos que criam fluxos relacionados, embora protocolos
complexos possam exigir helpers e aumentar a superfície de erro.

O estado consome memória e precisa de limites. Uma inundação de conexões pode esgotar
a tabela de acompanhamento mesmo que a CPU ainda esteja disponível. Timeout, limite de
entradas, política para conexões incompletas e observabilidade fazem parte da operação.

### Circuit-level gateway

Intermedeia a sessão em nível de conexão, sem necessariamente interpretar o conteúdo
da aplicação. SOCKS é um exemplo de mecanismo que pode ser usado nessa posição. O
gateway esconde a conexão entre origem e destino, mas não oferece a validação semântica
de um proxy que compreende HTTP ou SMTP.

### Proxy ou application gateway

Termina a conexão do cliente e abre outra conexão para o destino. Por compreender a
aplicação, pode aplicar política por host HTTP, caminho, método, cabeçalho, identidade,
comando ou operação. O custo é a necessidade de terminar e reconstruir protocolos, o
risco de incompatibilidade e uma maior dependência do proxy.

Reverse proxies e API gateways podem exercer funções de firewall de aplicação, mas
não devem ser chamados de firewall apenas por estarem na frente do serviço. A
responsabilidade concreta é determinada pelas políticas que realmente aplicam.

## Profundidade de inspeção

### Firewall de camada 3 e 4

Decide com base em IP, protocolo, porta, interface, direção e estado. É o modelo
tradicional de ACL e firewall stateful. Não precisa decodificar HTTP, mas também não
consegue distinguir dois caminhos diferentes no mesmo servidor TCP.

### Firewall de camada 7

Interpreta o protocolo da aplicação, como HTTP, DNS, SMTP ou Kafka. Pode reconhecer
comandos, métodos, hosts, tipos de conteúdo e padrões de abuso. O modelo é mais
expressivo e mais caro, depende da correta implementação do protocolo e pode precisar
de descriptografia TLS para inspecionar o conteúdo.

### WAF

Web Application Firewall é especializado em aplicações web. Ele pode procurar padrões
de exploração, aplicar regras para HTTP e limitar comportamentos de bots. Um WAF não
substitui validação de entrada, autorização ou correção do código. Também pode produzir
falsos positivos quando trata payloads legítimos como ataques.

### NGFW

Next-generation firewall combina funções tradicionais com identidade, inspeção de
aplicação, prevenção de intrusão, reputação, categorização e integração com diretórios.
O nome é comercialmente amplo, então compare as funções concretas: quais protocolos são
entendidos, onde TLS é terminado, qual telemetria é preservada e qual é o custo de
processamento.

### IPS e IDS

IDS detecta e alerta. IPS está no caminho ou tem capacidade de bloquear. A distinção é
de efeito operacional, não de algoritmo. Um mecanismo pode oferecer ambos os modos.
Bloqueio automático exige calibrar falsos positivos, modo de falha, atualização das
assinaturas e possibilidade de bypass controlado durante um incidente.

## Onde é executado

| Tipo | Posição | Pergunta principal |
| --- | --- | --- |
| Host | Servidor ou endpoint | Este processo ou fluxo pode usar esta interface? |
| Perímetro | Entre redes | Esta zona pode conversar com aquela? |
| Egress | Saída de uma rede | Para onde workloads podem enviar dados? |
| Ingress | Entrada de uma rede | Quem pode alcançar um serviço exposto? |
| Leste-oeste | Entre workloads | Um serviço pode chamar outro dentro da mesma rede? |
| Cloud | Serviço gerenciado ou security group | Qual identidade, subnet ou recurso pode comunicar? |
| WAF | Frente da aplicação web | Esta requisição HTTP parece permitida? |
| Service mesh | Proxy ou datapath do workload | Esta identidade pode executar esta operação? |

## Políticas e modo de falha

Uma política precisa ter dono, escopo, precedência, logging, prazo de revisão e
critério de remoção. `deny by default` reduz exposição, mas requer allowlist completa
para DNS, atualização, identidade, observabilidade e dependências da aplicação.

O modo de falha também é uma decisão. Fail-closed preserva o bloqueio quando o
componente de política falha, mas pode interromper serviços legítimos. Fail-open mantém
disponibilidade durante uma falha de controle, mas pode liberar tráfego não autorizado.
O modo adequado depende da função, do risco e da capacidade de recuperação.

Não acumule firewalld, UFW, scripts diretos de `nftables`, Docker e regras da CNI sem
entender a ordem final. Vários donos escrevendo no mesmo datapath produzem políticas
difíceis de explicar e de depurar.

## Relações

- [Firewalld](../../firewalld.md) explica uma interface de zonas para firewall Linux.
- [Netfilter](netfilter.md) explica o datapath e [nftables](nftables.md) explica a interface
  do kernel Linux.
- [UFW e portas publicadas pelo Docker](../../ufw-e-portas-publicadas-pelo-docker.md)
  trata a interação entre firewall do host e NAT de containers.
- [NetworkPolicy](../../kubernetes/networking/network-policy.md) aplica segmentação
  declarativa a workloads Kubernetes.
- [HAProxy](../proxy/haproxy.md) explica o proxy e balanceador que pode compor uma
  borda, mas não substitui a política de firewall.

## Fontes

- [nftables wiki](https://wiki.nftables.org/)
- [Linux kernel Netfilter documentation](https://www.netfilter.org/documentation/)
- [Cilium NetworkPolicy](https://docs.cilium.io/en/stable/network/kubernetes/policy/)
- [OWASP Web Application Firewall](https://owasp.org/www-community/Web_Application_Firewall)
