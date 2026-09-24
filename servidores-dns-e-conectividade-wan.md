# Servidores DNS e conectividade WAN

## Implementações de servidor DNS: papéis opostos, softwares diferentes

Um servidor autoritativo e um resolvedor recursivo resolvem problemas de engenharia opostos. O autoritativo precisa responder rápido e de forma previsível a partir de dados que ele mesmo controla, sem confiar em outro servidor; o risco que gerencia é sobretudo de disponibilidade e exatidão dos próprios dados. O recursivo precisa navegar uma cadeia de servidores que não controla e se defender de respostas forjadas ao longo do caminho.

O risco que o recursivo gerencia é sobretudo de segurança e cache envenenado. Separar os dois softwares, cada um endurecido para seu próprio papel, é a prática mais comum em operações de porte real. Misturar os dois no mesmo processo é mais comum em ambientes pequenos, onde a superfície de risco extra é aceitável em troca de simplicidade operacional.

O PowerDNS torna essa separação literal em vez de apenas recomendada. O projeto distribui dois produtos completamente distintos sob o mesmo projeto guarda-chuva, o Authoritative Server e o Recursor, cada um com base de código, processo e configuração próprios. Um operador que só precisa de autoridade sobre zonas roda apenas o primeiro; um que só precisa de resolução recursiva roda apenas o segundo, sem compartilhar processo nem estado entre os dois.

O Authoritative Server se destaca por armazenar zonas em backends plugáveis, incluindo bancos de dados relacionais. Isso facilita integração com provisionamento automatizado quando o número de zonas geridas cresce além do que editar arquivos manualmente comporta.

Unbound é um resolvedor recursivo validador, leve e focado só nesse papel. Não administra zonas próprias como autoridade, e prioriza segurança e validação DNSSEC por padrão. É a escolha comum quando o objetivo é só um resolvedor confiável e privado na rede local.

BIND, o servidor DNS mais antigo em uso contínuo, é o único capaz de operar nos dois papéis no mesmo software. A própria documentação do projeto recomenda separá-los, pelo mesmo motivo de superfície de risco já descrito. Grande parte do vocabulário operacional do DNS, como arquivo de zona e o arquivo `named.conf`, vem do BIND, que continua sendo a base autoritativa de infraestrutura crítica em muitas organizações.

Technitium representa a escolha oposta à separação do PowerDNS: um único processo com interface web de administração, cobrindo autoritativo, recursivo, bloqueio de domínios e suporte a DoT/DoH no mesmo pacote. Essa integração é o que o torna atrativo para homelab, onde um operador solo gerenciando poucos domínios internos e uma rede doméstica ganha mais com um painel único do que perderia com a superfície de risco combinada. DoT e DoH, mecanismos de transporte cifrado cobertos em [DNSSEC, mDNS e registro de domínio](dnssec-mdns-e-registro-de-dominio.md), vêm suportados nativamente pelo Technitium, sem exigir um proxy adicional.

CoreDNS é o servidor DNS padrão de qualquer cluster Kubernetes, incluindo o K3s, rodando como um pipeline de plugins encadeados em vez de um monólito com configuração fixa. O plugin `kubernetes` é o que o torna autoritativo para a zona `cluster.local`, resolvendo Services e Pods a partir do estado do cluster em tempo real.

Essa arquitetura de plugins é o motivo pelo qual o mesmo binário consegue ser autoritativo de uma zona e recursivo, ou forwarder, para o resto da internet na mesma instância, através do plugin `forward`. Isso acontece sem misturar responsabilidades da forma arriscada descrita no início desta seção: cada zona configurada delega explicitamente a um plugin específico.

Três critérios práticos decidem melhor que uma preferência abstrata pelo servidor mais popular. O primeiro é qual papel é realmente necessário, recursivo, autoritativo ou os dois. O segundo é quem vai operar o servidor no dia a dia, já que um operador solo em homelab ganha mais com um painel integrado do que uma equipe com múltiplas zonas ganharia com ele.

O terceiro é qual é a exposição do servidor, porque um recursivo exposto a clientes não confiáveis exige hardening que um autoritativo interno não precisa da mesma forma. Nenhum destes softwares é estritamente superior aos outros fora de um contexto específico. O erro mais comum é adotar um servidor monolítico com todos os recursos ligados por padrão quando o papel real exigido era só um dos dois.

## Conectividade WAN: de onde vem a instabilidade de endereço

Toda resolução DNS presume que um host já tem acesso à internet. Isso esconde uma decisão anterior, tomada uma única vez na configuração do roteador de borda: como esse roteador obtém seu próprio endereço IP público. Essa decisão, mais do que qualquer configuração de DNS em si, é o que determina se um operador precisa de DNS dinâmico para expor um serviço, o problema que um [túnel de rede](rede/conectividade/tunel.md) pode contornar.

Existem três modos possíveis de obter esse endereço, e a diferença entre eles não é de desempenho, é de estabilidade. PPPoE (Point-to-Point Protocol over Ethernet, RFC 2516) é o protocolo que muitos provedores de fibra e DSL exigem na porta WAN antes de entregar qualquer endereço IP. O roteador do cliente autentica com usuário e senha fornecidos pelo provedor, encapsulando quadros PPP dentro de Ethernet.

Só depois dessa autenticação bem-sucedida o roteador recebe um endereço, tipicamente por um mecanismo de configuração dentro do próprio PPP, não por um DHCP separado. Sem credenciais corretas configuradas no roteador, a conexão nunca sobe, mesmo com o cabeamento físico perfeito. Provedores que usam PPPoE costumam fazer isso para controlar acesso por assinante já na camada de enlace, antes de qualquer endereçamento IP entrar em jogo.

DHCP (Dynamic Host Configuration Protocol, RFC 2131) é o modo automático mais comum em conexões a cabo, e cada vez mais comum em fibra também. O roteador de borda pede um endereço na porta WAN sem autenticação de usuário e senha na camada de enlace, e o provedor responde com IP, máscara, gateway e servidores DNS recomendados. A diferença central entre DHCP e PPPoE não é técnica de endereçamento, é de controle de acesso.

DHCP identifica o assinante por outros meios, como o endereço MAC registrado ou autenticação na própria infraestrutura física do provedor. PPPoE, em vez disso, exige uma credencial explícita configurada no equipamento do cliente. Nenhum dos dois garante que o endereço público permaneça o mesmo entre reconexões, o cerne do problema que DNS dinâmico resolve.

O terceiro modo não depende de negociação nenhuma: o provedor atribui contratualmente um endereço fixo, configurado manualmente no roteador ou entregue sempre igual via DHCP. É o único dos três modos em que o endereço público nunca muda sem aviso, e por isso é o único que dispensa DDNS por completo. Se o problema que o DDNS resolve é o IP mudando sem o registro DNS acompanhar, um endereço que nunca muda elimina o problema pela raiz, não apenas o mitiga.

PPPoE e DHCP entregam um endereço que pode mudar sem aviso, o que exige DDNS sempre que o operador precisa de alcançabilidade direta e estável a partir de fora da rede. Essa mesma lógica se aplica ao endereçamento IPv6 delegado por DHCPv6-PD, coberto em [modelos OSI/TCP-IP e endereçamento IP](osi-tcpip-e-enderecamento-ip.md#ipv6-nao-e-ipv4-com-mais-bits): um prefixo IPv6 que o provedor pode reatribuir é, na prática, o mesmo problema de um IPv4 dinâmico, só que em escala de bloco em vez de endereço único.

Em ambos os casos a resposta operacional é a mesma. Ou o plano interno se apoia em algo que não muda com a WAN, um ULA no caso do IPv6 ou um registro DNS atualizado dinamicamente no caso geral, ou o operador aceita a instabilidade e resolve alcançabilidade de outra forma. Um [túnel de exposição](rede/conectividade/tunel.md), por exemplo, nunca depende do IP público do lado exposto permanecer o mesmo.

SFP+ é um padrão de transceptor óptico, ou elétrico com um módulo específico, usado para uplinks de 10 Gigabit Ethernet. É comum em roteadores de borda dedicados e switches de homelab mais sérios, ao lado das portas RJ45 tradicionais. [Appliances de borda](rede/conectividade/borda.md), como RouterOS e pfSense, costumam oferecer uma porta SFP+ justamente para o uplink WAN de maior capacidade, quando o provedor entrega fibra mais rápida do que uma porta Gigabit comum comporta.

O ponto relevante aqui é só reconhecer o termo e seu papel: uma camada puramente física, independente de qual dos três modos, PPPoE, DHCP ou IP estático, opera sobre ela.

## Pontos de troca de tráfego: onde as redes se encontram

Um provedor de acesso não carrega sozinho todo o tráfego de seus assinantes até qualquer destino na internet. Ele estabelece conexões diretas, chamadas de peering, com outras redes especificamente para trocar tráfego entre si sem depender de um terceiro no meio. Um ponto de troca de tráfego (Internet Exchange Point, IXP) é a infraestrutura física e lógica que concentra esse peering entre muitas redes num único local, cada uma conectando um único link a um switch compartilhado.

Isso resolve um problema de escala: sem um ponto de troca comum, N redes que quisessem trocar tráfego diretamente entre si precisariam de uma conexão para cada par, um custo que cresce muito mais rápido que o número de redes. Com o ponto de troca, cada rede paga só a conexão até ele.

O IX.br, mantido pelo NIC.br, a mesma entidade que administra o registro de domínios `.br`, é a rede de pontos de troca de tráfego mais distribuída do mundo em número de participantes, presente em dezenas de cidades brasileiras. Sua existência é uma das razões práticas pelas quais o tráfego entre dois provedores brasileiros costuma ter latência baixa. Na maioria dos casos, esse tráfego nem precisa sair do país para ser trocado.

Um serviço como o Cloudflare Radar (radar.cloudflare.com) publica, a partir da posição de observação de uma rede que atende uma fração grande do tráfego global, dados agregados sobre tráfego de internet, adoção de protocolo e incidentes de conectividade por região. É uma forma pública de enxergar, de fora, o efeito agregado dessa malha de peering e roteamento sem precisar operar rede nenhuma.

Nenhum desses dois serviços substitui o diagnóstico direto de uma conexão específica. Servem para entender o contexto mais amplo em que a conectividade WAN de um roteador de borda se insere.

## Continue por aqui

[Resolução, zonas e registros DNS](resolucao-zonas-e-registros-dns.md) e [DNSSEC, mDNS e registro de domínio](dnssec-mdns-e-registro-de-dominio.md) cobrem os papéis conceituais e as garantias que os softwares aqui listados implementam; [VPNs, túneis e bordas de rede](vpns-tuneis-e-bordas-de-rede.md) cobre o DDNS e os túneis de exposição que a instabilidade de endereço WAN torna necessários.
