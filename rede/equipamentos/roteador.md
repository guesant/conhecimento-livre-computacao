# Roteador

Um roteador encaminha pacotes entre redes IP. Ele examina o endereço de destino, consulta uma tabela de encaminhamento e escolhe uma interface ou próximo salto. Ao atravessar uma rede diferente, o pacote recebe um novo enquadramento de camada de enlace.

## Roteamento e encaminhamento

Roteamento é o processo de aprender ou calcular caminhos. Encaminhamento é a aplicação rápida dessa decisão a cada pacote. Rotas podem vir de configuração estática, de protocolos internos como OSPF e IS-IS, de BGP ou de controladores e agentes especializados.

Um roteador de residência, um roteador de campus, um roteador de data center e um roteador de backbone exercem a mesma função fundamental, mas possuem escalas, tabelas, interfaces, disponibilidade e políticas muito diferentes.

## Funções que costumam ser combinadas

Produtos de borda frequentemente adicionam:

- NAT e state tracking;
- firewall e ACL;
- DHCP e relay;
- DNS encaminhador ou cache;
- VPN e túneis;
- QoS e controle de congestionamento;
- autenticação de acesso;
- telemetria, syslog e APIs;
- alta disponibilidade e redundância.

Essas funções não são parte obrigatória do roteamento IP. Um roteador pode apenas encaminhar pacotes, enquanto firewall, NAT, DNS e DHCP ficam em serviços separados.

## Roteador, gateway e firewall

Gateway é um termo contextual para o próximo sistema que permite alcançar outra rede. Em uma LAN, o gateway padrão costuma ser o roteador local. Um firewall pode executar roteamento, mas seu critério principal é a política de segurança. Um proxy ou API gateway opera em camadas superiores e não deve ser confundido com um roteador IP.

## Escala global

Roteadores de backbone e de provedores precisam de alta disponibilidade, convergência controlada, capacidade de memória e processamento, interfaces de alta velocidade e operação remota. BGP permite trocar informações de alcançabilidade entre sistemas autônomos, mas a segurança depende de filtros, políticas, RPKI, monitoramento e controle de mudanças.

## Fontes primárias

- [RFC 1812, requisitos para roteadores IPv4](https://datatracker.ietf.org/doc/html/rfc1812)
- [RFC 4271, BGP-4](https://datatracker.ietf.org/doc/html/rfc4271)
- [RFC 1122, arquitetura de hosts e gateways](https://datatracker.ietf.org/doc/html/rfc1122)
