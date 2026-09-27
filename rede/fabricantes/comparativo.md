# Comparação de fabricantes e plataformas de rede

Este comparativo não define uma marca vencedora. Ele separa cenários e critérios para que a decisão considere o problema real, o ciclo de vida e a capacidade da equipe.

| Plataforma | Plano mais forte | Gerenciamento | Hardware ou execução | Suporte e operação |
| --- | --- | --- | --- | --- |
| Cisco | campus, data center, WAN, segurança e ambientes corporativos | CLI, APIs, plataformas Catalyst, Meraki e ferramentas específicas | amplo portfólio de switches, roteadores, wireless e segurança | ecossistema empresarial, parceiros e contratos de suporte |
| TP-Link e Omada | SMB, Wi-Fi administrado e filiais | controladores locais, software ou nuvem, conforme a linha | gateways, switches, EAP, controladores e produtos domésticos | operação simples, suporte por linha e região, validar ciclo de firmware |
| pfSense | firewall, roteamento, VPN e serviços de borda | interface web, console, pacotes, APIs e automação limitada pelo desenho | hardware genérico, VM e appliances | comunidade e suporte comercial via Netgate ou parceiros |
| Netgate | appliances pfSense Plus e edge routing com TNSR | conforme pfSense Plus ou TNSR | appliances desktop, rack, bare metal, VM e nuvem | TAC, treinamento e serviços comerciais |
| MikroTik | flexibilidade de roteamento, BGP, WISP e equipamentos compactos | RouterOS, CLI, WinBox, WebFig, API e scripts | hAP, hEX, CCR, CRS, wireless, LTE/5G, x86 e CHR | documentação, fórum, distribuidores, consultores e treinamento |
| Ubiquiti | redes integradas, multi-site e WISP | UniFi, UISP e consoles associados | gateways, switches, Wi-Fi, segurança física e rádios | experiência integrada, comunidade e suporte por produto |

## Escolha por cenário

| Cenário | Candidatos plausíveis | Perguntas que podem mudar a decisão |
| --- | --- | --- |
| residência e homelab | pfSense, MikroTik, Omada, UniFi e OpenWrt | silêncio, consumo, VLAN, VPN, manutenção e possibilidade de recuperação local |
| pequeno escritório | Omada, UniFi, MikroTik, pfSense e Netgate | operação multi-site, PoE, Wi-Fi, suporte e custo total |
| firewall de borda | pfSense, Netgate, Cisco e MikroTik | inspeção, VPN, alta disponibilidade, throughput, suporte e logs |
| campus corporativo | Cisco, UniFi, Omada e combinações com firewall dedicado | identidade, roaming, redundância, automação, telemetria e SLA |
| data center | Cisco Nexus, Cisco routing, MikroTik CCR e soluções especializadas | fabric, EVPN, latência, escala, BGP, automação e suporte |
| WISP ou enlace externo | MikroTik e Ubiquiti UISP, além de soluções de rádio especializadas | espectro, capacidade, CPE, interferência, monitoramento e redundância |
| rede de câmeras e PoE | Omada, UniFi e Cisco | orçamento PoE, isolamento, gravação, retenção e falha do controlador |

## Critérios que devem ser medidos

Não use apenas a largura de banda nominal. Meça ou valide o perfil de tráfego esperado, número de regras, conexões simultâneas, tamanho de tabelas, desempenho com VPN, inspeção, QoS, IPv6, logs e telemetria. Para wireless, densidade, roaming, interferência e desenho de canais importam mais que a taxa PHY anunciada.

Também compare o custo operacional: assinatura, controlador, licenças, contratos, energia, peças, tempo de atualização, treinamento e recuperação. Um equipamento barato pode ser mais caro quando exige intervenção manual frequente ou não oferece exportação confiável de configuração.

## Interoperabilidade e dependência

Uma composição multi-vendor pode reduzir dependência, mas exige testes de VLAN, LACP, STP, LLDP, MTU, PoE, AAA, SNMP, syslog, roteamento dinâmico e APIs. Uma composição de um único ecossistema simplifica o plano de controle, mas aumenta a dependência de seu controlador, formato de configuração, ciclo de suporte e política comercial.

O critério correto não é evitar qualquer dependência. É escolher uma dependência conhecida, recuperável e compatível com as restrições do ambiente.

## Fontes primárias

- [Cisco products](https://www.cisco.com/site/us/en/products/index.html)
- [TP-Link Omada](https://www.tp-link.com/us/business-networking/omada/)
- [pfSense documentation](https://docs.netgate.com/pfsense/en/latest/)
- [Netgate appliances](https://www.netgate.com/appliances)
- [MikroTik products](https://mikrotik.com/products)
- [Ubiquiti](https://www.ui.com/)
