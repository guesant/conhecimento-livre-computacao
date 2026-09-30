# Switch

Um switch conecta dispositivos em uma rede comutada e encaminha quadros de camada 2 a partir de endereços MAC. Ele aprende quais endereços estão associados a cada porta e envia o quadro somente para a porta apropriada quando conhece o destino. Quadros broadcast, multicast ou destinos desconhecidos seguem regras próprias.

## Hardware

Switches usam memória para tabelas MAC e buffers, ASICs ou processadores especializados para encaminhamento, interfaces de diferentes velocidades, transceptores e, em modelos de data center, recursos de alta densidade e baixa latência. PoE adiciona alimentação elétrica para APs, câmeras, telefones e outros dispositivos.

## Switch não gerenciável e gerenciável

Um switch não gerenciável costuma operar com configuração mínima. Um switch gerenciável acrescenta administração, telemetria e protocolos para controlar topologia e segmentação. Entre as funções comuns estão VLAN, portas access e trunk, STP, LACP, QoS, espelhamento, LLDP, 802.1X, ACL e, em alguns modelos, roteamento IP.

VLAN separa domínios lógicos, mas não é por si só uma política completa de segurança. A comunicação entre VLANs passa por um roteador ou switch de camada 3, onde regras podem ser aplicadas.

## Topologia e loops

Redes comutadas precisam evitar loops de camada 2. STP e suas variantes permitem redundância controlada, mas uma topologia mal configurada pode produzir broadcast storm, MAC flapping e perda de conectividade. LACP agrega enlaces quando os dois lados concordam com a configuração.

## Plano de controle e gerenciamento

O switch precisa ser administrado com credenciais protegidas, firmware atualizado, acesso de gerenciamento separado e logs enviados para um destino confiável. Configurações devem registrar VLANs, trunks, MTU, PoE, filtros, spanning tree e dependências de uplink.

## Fontes primárias

- [IEEE 802.1Q, bridges e VLANs](https://standards.ieee.org/ieee/802.1Q/10323/)
- [IEEE 802 LAN/MAN Standards Committee](https://www.ieee802.org/)
