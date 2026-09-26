# Software de rede

O hardware apenas fornece interfaces, memória, processamento e meios físicos. A rede funciona porque firmware, sistemas operacionais, drivers, protocolos, serviços e ferramentas de gerenciamento implementam as decisões de encaminhamento, controle e observabilidade.

## Camadas do software

### Firmware e drivers

Firmware inicializa o equipamento, controla ASICs, rádios, transceptores, sensores e fontes e oferece a base para a atualização segura. Drivers fazem a interface entre o sistema operacional e NICs, rádios, aceleradores e outras partes do hardware.

### Sistema operacional de rede

Um sistema operacional de rede fornece modelo de configuração, processos de controle, tabelas de encaminhamento, interfaces de gerenciamento e integração com hardware. Pode ser um sistema proprietário, uma distribuição Linux especializada, um sistema baseado em BSD ou um sistema desagregado que combina software e hardware de fornecedores diferentes.

### Protocolos de enlace e rede

Ethernet, Wi-Fi, VLAN, STP, LACP, ARP, NDP, IPv4 e IPv6 implementam a conectividade local e o encaminhamento. Roteamento estático, OSPF, IS-IS e BGP distribuem informações de alcançabilidade. DHCP e SLAAC configuram hosts. DNS associa nomes a serviços e endereços.

### Serviços de transporte e aplicação

TCP, UDP e QUIC transportam fluxos ou datagramas. TLS protege sessões. HTTP, HTTP/2, HTTP/3, SMTP, SSH, SFTP, DNS e outros protocolos oferecem serviços aos usuários e aplicações. Na Web, servidores, proxies, CDNs, balanceadores e aplicações compõem uma cadeia acima do roteamento IP.

### Gerenciamento e automação

SNMP, syslog, streaming telemetry, NETCONF, RESTCONF, gNMI, APIs, agentes e ferramentas de configuração automatizam operação e diagnóstico. O gerenciamento não deve depender apenas de acesso manual ao equipamento, porque mudanças precisam ser auditáveis, reproduzíveis e recuperáveis.

## Plano de dados, controle e gerenciamento

O plano de dados encaminha tráfego. O plano de controle constrói as tabelas e mantém vizinhanças, sessões e protocolos. O plano de gerenciamento recebe intenção, aplica configuração e expõe estado. Uma falha em um plano pode existir sem que os outros pareçam indisponíveis.

Por exemplo, um switch pode responder ao painel de administração enquanto uma VLAN está errada no plano de dados. Um roteador pode ter BGP estabelecido, mas instalar uma rota indesejada. Um AP pode estar online, mas com rádio saturado. Métricas e testes precisam observar o comportamento real, não somente o processo de gerenciamento.

## Rede definida por software

Em SDN, controladores, agentes e APIs podem separar a intenção de rede da implementação em equipamentos. Isso facilita padronização e automação, mas cria dependência do controlador, de seu modelo de estado e da disponibilidade do canal de controle. Desagregar software e hardware também desloca responsabilidades para integração, ciclo de atualização e compatibilidade.

## Segurança da cadeia de software

Firmware e sistemas de rede precisam de origem verificável, atualizações assinadas, controle de acesso, logs, backup de configuração e possibilidade de recuperação. Uma rede crítica não deve tratar a imagem do equipamento como um detalhe descartável, porque ela contém a implementação dos protocolos e das políticas que protegem o tráfego.

## Fontes primárias

- [RFC 1122, requisitos de software de hosts](https://datatracker.ietf.org/doc/html/rfc1122)
- [RFC 1812, requisitos de roteadores](https://datatracker.ietf.org/doc/html/rfc1812)
- [IEEE 802 LAN/MAN Standards Committee](https://www.ieee802.org/)
