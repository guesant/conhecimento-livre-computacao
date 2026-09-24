# Modelos OSI/TCP-IP e endereçamento IP

Quando alguém diz que um balanceador de carga opera em "camada 4" e um reverse proxy como o Traefik opera em "camada 7", está usando o vocabulário do modelo OSI para descrever uma pilha que, na prática, é implementada segundo o modelo TCP/IP.

O OSI, formalizado pela ISO na década de 1980 (ISO/IEC 7498-1), define sete camadas como referência abstrata e independente de implementação; nenhuma pilha em uso amplo hoje o implementa à risca, e ele sobreviveu como vocabulário, não como arquitetura. O TCP/IP, descrito em RFCs como a 1122, nasceu do trabalho prático de construir a internet, com quatro camadas (acesso à rede, internet, transporte, aplicação) que correspondem a protocolos reais em código.

O mapeamento entre os dois não é exato: as camadas 5, 6 e 7 do OSI (sessão, apresentação, aplicação) colapsam todas na camada de aplicação do TCP/IP, porque essa distinção raramente aparece como protocolos separados na prática.

Um balanceador de "camada 4" decide para onde encaminhar um pacote olhando IP de destino e porta, sem entender o protocolo transportado; um proxy de "camada 7" lê o conteúdo da requisição (host, caminho, cabeçalhos) para decidir a rota, o que exige entender o protocolo de aplicação inteiro.

Essa numeração também organiza a rede de um host Linux: interfaces e endereçamento físico em camadas 1 e 2 (bridges, veth pairs), roteamento entre redes em camada 3, portas de transporte em camada 4.

Vale usar essa numeração para comunicar rápido em que nível um problema ou uma ferramenta opera, como comparar um firewall de borda de camada 3/4 com um web application firewall de camada 7, ou diagnosticar uma falha, um veth pair desconectado é camada 2 e não se resolve mexendo em regra de camada 7.

Não é necessário memorizar as sete camadas do OSI em detalhe para operar uma infraestrutura; o que importa é reconhecer, diante de um termo como L4 ou L7, qual conjunto de decisões aquela camada realmente tem disponível. Essa mesma numeração volta a aparecer mais adiante, na diferença entre terminar TLS e apenas encaminhar seus bytes cifrados, ou entre um proxy que só olha porta e um que lê o conteúdo da requisição.

## IPv4: de classes a CIDR

Um endereço IPv4 tem 32 bits, escrito como quatro octetos decimais. O esquema antigo de classes fixas (A, B, C) desperdiçava endereços com facilidade; o CIDR (RFC 4632) substituiu isso por um prefixo variável `/N`, onde N bits pertencem à rede e os restantes a hosts.

`192.168.1.0/24` reserva 24 bits para a rede, sobrando 256 endereços (254 utilizáveis); `10.0.0.0/8` reserva só 8 bits, sobrando mais de 16 milhões.

O endereço de rede vem de um AND lógico entre endereço e máscara; o de broadcast, de um OR entre o endereço de rede e o complemento da máscara; hosts utilizáveis são `2^(32-prefixo) - 2`. Dividir uma rede em sub-redes (subnetting) significa aumentar o prefixo, emprestando bits de host para a porção de rede; cada bit emprestado dobra o número de sub-redes e reduz à metade os hosts por sub-rede.

A tabela abaixo resume os blocos IPv4 reservados por RFC, para uso privado ou só como exemplo em documentação.

| RFC | Blocos reservados | Uso |
| --- | --- | --- |
| RFC 1918 | `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | endereçamento privado, nunca roteado na internet pública |
| RFC 5737 | `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` | exemplos de documentação, não sugerem um host real |

Qualquer rede doméstica ou interna usa endereços do bloco RFC 1918, e um host que só tem endereço privado precisa de NAT para iniciar conexões para fora, o roteador de borda reescrevendo o endereço de origem antes de enviar e desfazendo a tradução na resposta.

K3s aplica a mesma lógica dentro do cluster: por padrão o Flannel aloca Pods e Services a partir dos blocos `10.42.0.0/16` e `10.43.0.0/16`, configuráveis por flag na inicialização do k3s.

Nem todo mapeamento de porta através do NAT depende do operador editar a configuração do roteador: os protocolos UPnP e PCP permitem que o próprio dispositivo da rede local peça a abertura de uma porta, sem intervenção humana.

O perfil IGD do UPnP não implementa nenhuma autenticação por padrão, então qualquer dispositivo da rede, incluindo malware, pode solicitar o mesmo mapeamento que uma aplicação legítima pediria; falhas de implementação já documentadas permitiram abusar disso para amplificação de DDoS. O PCP, sucessor do NAT-PMP, tem desenho mais restrito e mais fácil de auditar, mas o risco permanece: qualquer dispositivo interno pode pedir exposição para fora sem aprovação do operador.

## IPv6: não é IPv4 com mais bits

Um endereço IPv6 tem 128 bits, escrito em oito grupos hexadecimais separados por dois-pontos, com zeros à esquerda de cada grupo omissíveis e uma única sequência de grupos zerados substituível por `::` (`2001:db8::1`). A RFC 3849 reserva o prefixo `2001:db8::/32` para documentação, o equivalente em IPv6 dos blocos TEST-NET do IPv4 já vistos na tabela acima.

Todo host Linux moderno já vem com essa pilha habilitada por padrão, o que significa que um serviço pode estar acessível por IPv6 mesmo quando o operador só pensou em configurar IPv4, e um firewall que cobre só a família IPv4 deixa essa rota de acesso sem filtro nenhum.

O espaço de 128 bits existe porque o IPv4 se esgotou como alocação livre; isso muda a arquitetura em duas direções: NAT deixa de ser necessidade estrutural, já que há endereços suficientes para cada host ter um endereço global roteável, e redes IPv6 tendem a depender de firewall com negação por padrão, não de NAT, para controlar conexões de entrada.

A configuração de endereço ganha um mecanismo automático nativo: SLAAC permite a um host gerar seu próprio endereço global a partir do prefixo anunciado pelo roteador, sem precisar de um servidor DHCP. DHCPv6 continua existindo como alternativa com estado, útil quando a rede precisa de controle centralizado sobre quais endereços são distribuídos. As duas formas não se excluem: uma rede real pode combinar SLAAC para o endereço principal com DHCPv6 só para opções auxiliares, como servidores DNS.

O erro mais comum de quem chega ao IPv6 é tratá-lo como IPv4 com endereço maior, o que gera diferenças estruturais reais: não existe broadcast (tudo foi redesenhado sobre multicast); ARP não existe, substituído por NDP sobre ICMPv6, então bloquear ICMPv6 inteiro quebra a própria descoberta de vizinhos e rotas; só a origem fragmenta um pacote, e a rede depende de Path MTU Discovery, que também depende de ICMPv6.

O roteador padrão nunca vem do DHCP, só de Router Advertisement; o cabeçalho não tem checksum, porque essa responsabilidade passou para camadas superiores; múltiplos endereços por interface é o normal, não a exceção.

O bloco ULA (`fc00::/7`, na prática `fd00::/8`) não nasceu de escassez de endereços como o RFC 1918 nasceu, e sim para dar a uma rede interna uma identidade estável e não roteável globalmente. Nada impede, tecnicamente, que a mesma rede também tenha endereços públicos ao mesmo tempo, porque múltiplos endereços por interface já é o normal em IPv6.

Cada ULA é gerado uma única vez por um algoritmo pseudoaleatório (RFC 4193) que produz um identificador de site sem depender de nenhum registro central, o que faz dele um bom candidato a identidade permanente quando o prefixo público de uma rede pode mudar.

Subnetting em IPv6 raramente é feito bit a bit: a convenção fixa os últimos 64 bits de qualquer endereço unicast global como identificador de interface, e um site tipicamente recebe da operadora um prefixo de rede menor que isso, geralmente entre 48 e 56 bits.

Um site assim tem liberdade para criar `2^16` sub-redes `/64` a partir do prefixo alocado, cada uma ainda grande demais para esgotar por uso normal. Essa abundância é o que torna plausível dar a cada Pod de um cluster um endereço global roteável, uma opção que nunca existiu de verdade em IPv4.

Kubernetes trata dual stack como estável desde a versão 1.23, com o mesmo par de flags de cluster e de Service descrito abaixo aceitando um valor de cada família, e cada Service declarando sua `ipFamilyPolicy` e sua lista de `ipFamilies`.

## Dual stack

Dual stack é a configuração em que um host ou um cluster mantém IPv4 e IPv6 simultaneamente ativos, em vez de migrar de um para o outro de uma vez; é o estado mais comum hoje, porque a internet pública ainda depende fortemente de IPv4 para conectividade universal. K3s aceita dual stack nativamente: `--cluster-cidr` e `--service-cidr` recebem um valor IPv4 e um valor IPv6 separados por vírgula, e o cluster passa a alocar um endereço de cada família por Pod e por Service. Na prática, dual stack aumenta a superfície de configuração, porque cada regra de firewall e cada suposição sobre qual é o IP de um host precisa considerar que existem dois endereços válidos e, potencialmente, duas rotas diferentes até o mesmo destino.

Um Pod pode ter só um endereço ULA (equivalente em escopo ao `10.42.0.0/16` atual), só um endereço global roteável (conectividade fim a fim sem tradução, mas exigindo postura de negação explícita por firewall/NetworkPolicy já que não há NAT escondendo topologia), ou os dois ao mesmo tempo.

Quando o prefixo público delegado por um provedor pode rotacionar, como é comum em conexões residenciais, não vale amarrar cluster-cidr, service-cidr ou NetworkPolicy a esse prefixo: o plano interno fica em ULA, estável porque gerado uma vez por um algoritmo pseudoaleatório (RFC 4193) sem depender de delegação externa.

A exposição pública, quando necessária, é resolvida na borda com NPTv6 (RFC 6296), uma tradução de prefixo sem estado que absorve a rotação sem tocar em nenhum host interno.

## Continue por aqui

[TLS, mTLS e confiança de rede](tls-mtls-e-confianca-de-rede.md) cobre a camada de segurança acima do transporte que este texto pressupõe; [VPNs, túneis e bordas de rede](vpns-tuneis-e-bordas-de-rede.md) cobre os mecanismos de acesso e exposição construídos sobre esse endereçamento.
