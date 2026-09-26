# MikroTik

MikroTik combina hardware de rede com RouterOS, um sistema operacional que transforma equipamentos compactos, switches, roteadores, pontos de acesso e dispositivos wireless externos em plataformas programáveis de encaminhamento. Também existem produtos com SwOS e versões de RouterOS para execução em x86 ou como Cloud Hosted Router.

## Hardware e famílias

| Família | Hardware e função | Ambiente típico |
| --- | --- | --- |
| hAP e hEX | Roteadores compactos com Ethernet e wireless em alguns modelos | residência, laboratório e pequena filial |
| CCR | Cloud Core Routers com maior capacidade de CPU, memória e interfaces | borda, agregação, BGP e provedores |
| CRS e switches | Switches com recursos de camada 2 e, conforme o modelo, funções L3 e RouterOS | acesso, agregação e data center pequeno |
| cAP, wAP e mAP | Pontos de acesso internos, externos e dispositivos compactos | WLAN, IoT e ambientes industriais ou externos |
| Chateau e LTE/5G | Gateways com modem celular, Wi-Fi e Ethernet | backup de WAN, áreas remotas e mobilidade |
| LHG, SXT e wireless externo | CPEs, enlaces direcionais e conectividade outdoor | WISP, ponto a ponto e ponto-multiponto |
| RouterBOARD e x86/CHR | Plataformas de hardware ou execução virtual do RouterOS | appliances próprios, virtualização e nuvem |

A nomenclatura da MikroTik tem muitas combinações de CPU, memória, rádio, portas, PoE, SFP, licença e gabinete. O produto exato deve ser conferido no catálogo e no manual, principalmente quando o desenho depende de aceleração IPsec, capacidade de bridge, filas, tabela BGP ou rádio externo.

## Aplicações

RouterOS oferece roteamento estático e dinâmico, BGP, OSPF, VLAN, bridge, firewall, NAT, VPN, QoS, filas, MPLS, bonding, VRF em cenários suportados, monitoramento, automação e wireless. O ecossistema também inclui WinBox, WebFig, CLI, APIs, scripts, SNMP e ferramentas móveis.

A plataforma permite uma grande variedade de topologias, mas flexibilidade aumenta a responsabilidade da operação. Uma configuração que funciona em um laboratório pode ser inadequada para um backbone, e recursos com nomes semelhantes podem possuir limites distintos conforme a arquitetura do hardware.

## Casos de uso

- roteador doméstico ou de laboratório com VLANs, VPN e controle de banda;
- pequena empresa com firewall, múltiplos links e Wi-Fi;
- borda de provedor com BGP, filtros, redundância e agregação;
- WISP com CPEs, enlaces wireless e gestão de clientes;
- enlaces ponto a ponto em áreas sem infraestrutura cabeada;
- conectividade LTE ou 5G para backup, telemetria e locais remotos;
- switches de baixo custo com uplinks SFP ou SFP+ e administração centralizada por automação própria.

## Suporte e segurança

MikroTik oferece manuais, changelogs, avisos de segurança, fórum, consultores, treinamento e distribuidores. O suporte comercial e o nível de serviço dependem do canal e do contrato, portanto uma organização que precisa de resposta garantida deve validar esse compromisso antes da compra.

Restrinja WinBox, WebFig, API e SSH às redes de administração, altere credenciais padrão, use chaves ou AAA quando apropriado, desative serviços não utilizados, filtre tráfego da própria caixa e mantenha RouterOS dentro de uma versão suportada. Exporte configurações, proteja os arquivos de backup e teste o retorno a uma versão anterior antes de atualizar uma frota inteira.

## Fontes primárias

- [MikroTik products](https://mikrotik.com/products)
- [RouterOS documentation](https://help.mikrotik.com/docs/display/ROS/RouterOS)
- [MikroTik manuals](https://manual.mikrotik.com/)
- [MikroTik security](https://mikrotik.com/security)
- [MikroTik forum](https://forum.mikrotik.com/)
