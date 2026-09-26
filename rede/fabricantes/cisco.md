# Cisco

Cisco é um portfólio amplo de redes, segurança, data center, colaboração e observabilidade. Dentro de redes, a marca atende desde acesso corporativo e wireless até data centers, WAN, ambientes industriais e conectividade em grande escala. Portanto, “usar Cisco” não identifica um único sistema operacional, controlador ou modelo de suporte.

## Hardware e famílias

| Família | Hardware e função | Ambiente típico |
| --- | --- | --- |
| Catalyst switching | Switches de acesso, distribuição e campus, com opções PoE, uplinks de alta velocidade e recursos de segmentação | escritórios, escolas, hospitais e campus corporativo |
| Catalyst wireless | Pontos de acesso e componentes de gerenciamento de WLAN | Wi-Fi corporativo, mobilidade e alta densidade |
| Enterprise routing | Roteadores para filiais, WAN, SD-WAN, conectividade de borda e agregação | filiais, redes distribuídas e provedores |
| Nexus | Switches e plataformas para data center, fabric, leaf-spine e ambientes de alta densidade | data center e nuvem privada |
| Industrial networking | Switches, roteadores e wireless reforçados para ambientes industriais | automação, energia, transporte e IoT industrial |
| Secure Firewall | Appliances e software de firewall, VPN, controle de acesso e prevenção de ameaças | borda, data center e segurança de filiais |
| Meraki | Appliances, switches, pontos de acesso e dispositivos gerenciados por dashboard em nuvem | filiais e operações que priorizam implantação simplificada |

Os nomes de famílias e a disponibilidade de modelos mudam conforme região e ciclo de produto. Um inventário deve usar o datasheet e a matriz de compatibilidade do modelo exato, especialmente para PoE, uplinks, licenças, capacidade de tabela e suporte a protocolos.

## Aplicações

Cisco é usado para switching de acesso, roteamento inter-VLAN, Wi-Fi corporativo, SD-WAN, redes de data center, VPN, firewall, controle de acesso à rede, telemetria e automação. A operação pode envolver IOS XE, NX-OS, software de segurança, plataformas Catalyst Center, Meraki Dashboard, APIs, NETCONF, RESTCONF, SNMP, syslog e ferramentas da Cisco DevNet.

A escolha do plano de gerenciamento é parte da arquitetura. Uma rede baseada em CLI e automação declarativa tem necessidades diferentes de uma implantação centrada em dashboard. Linhas tradicionais, data center, segurança e Meraki também podem possuir modelos diferentes de assinatura, atualização e suporte.

## Casos de uso

- campus corporativo com acesso com fio, Wi-Fi, segmentação e controle de identidade;
- filiais conectadas por SD-WAN e políticas centralizadas;
- data centers com fabrics de baixa latência e integração com virtualização;
- redes industriais que exigem equipamentos reforçados e telemetria;
- ambientes regulados que precisam de suporte comercial, advisories e processos formais de ciclo de vida;
- grandes redes de provedores e organizações com equipes dedicadas de operação.

Para uma residência ou laboratório pequeno, Cisco pode ser tecnicamente adequado, mas o custo de aquisição, assinatura, energia, ruído e complexidade operacional costuma ser desproporcional. Equipamentos usados também exigem cuidado com licenças, contratos, firmware e fim de suporte.

## Suporte e segurança

O ecossistema inclui documentação, Cisco Community, parceiros, treinamentos, advisories e suporte TAC condicionado ao contrato aplicável. O ciclo de vida deve ser consultado por produto, porque fim de venda, fim de manutenção, versão de software e necessidade de assinatura podem afetar a operação.

A superfície de administração deve ser isolada. Use AAA centralizado, MFA quando suportado pelo plano de gerenciamento, administração fora da rede de usuários, controle de acesso às APIs, logging remoto, backups de configuração e uma política explícita para imagens de software. Não trate o dashboard ou o controlador como um detalhe: sua indisponibilidade pode limitar mudanças mesmo quando o plano de dados continua encaminhando tráfego.

## Fontes primárias

- [Cisco products](https://www.cisco.com/site/us/en/products/index.html)
- [Cisco product documentation](https://www.cisco.com/c/en/us/support/index.html)
- [Cisco DevNet](https://developer.cisco.com/)
- [Cisco end-of-life policy](https://www.cisco.com/c/en/us/products/collateral/general/end-of-life-policy.html)
