# pfSense

pfSense é uma plataforma de firewall e roteamento baseada em FreeBSD. Ela oferece filtragem stateful, NAT, VPN, serviços de rede e administração por interface web, com extensões conforme a edição e os pacotes instalados. Pode ser executada em hardware compatível, máquina virtual, nuvem ou appliances Netgate.

## Hardware e formas de execução

| Forma | Características | Cuidados |
| --- | --- | --- |
| Hardware x86 genérico | Permite escolher CPU, memória, armazenamento e interfaces de rede | validar drivers, aceleração criptográfica, estabilidade e suporte da plataforma |
| Appliance Netgate | Hardware integrado, quantidade de portas conhecida e suporte associado | conferir edição, contrato, desempenho medido e ciclo do modelo |
| Máquina virtual | Integra-se a um hypervisor e facilita snapshots controlados e movimentação | reservar interfaces, CPU, memória e acesso de recuperação fora do próprio firewall |
| Nuvem | Usa imagens ou instalações compatíveis com o provedor | validar interfaces virtuais, throughput, custos, IPs e recuperação de acesso |

O desempenho depende do número de regras, conexões, tamanho de pacotes, VPN, inspeção, shaping e drivers. A capacidade nominal da interface não representa automaticamente o throughput com firewall e IPsec ativos.

## Aplicações

pfSense pode atuar como firewall de borda, roteador, gateway multi-WAN, concentrador de VPN, servidor DHCP e DNS, terminador de VLAN, captive portal, plataforma de shaping e membro de uma configuração de alta disponibilidade. Pacotes adicionais podem ampliar o uso, mas também adicionam ciclo de atualização, consumo de recursos e superfície de administração.

## Casos de uso

- residência avançada ou homelab com segmentação, VPN e múltiplos links;
- pequena empresa com regras de saída, redes de convidados, DNS, DHCP e acesso remoto;
- filial com VPN site-to-site e failover de Internet;
- ambiente virtualizado que precisa de uma borda lógica separada dos workloads;
- laboratório para estudar firewall, roteamento, VLAN, NAT e operação de serviços de rede.

Para data centers de alto throughput, roteamento dinâmico muito grande ou requisitos específicos de inspeção, compare pfSense com TNSR, appliances comerciais, Linux e plataformas de roteamento dedicadas. A interface amigável não elimina a necessidade de desenhar domínios de falha, backups e acesso de emergência.

## Quando usar

pfSense é uma opção madura para appliances de borda e redes tradicionais. Antes de escolhê-lo, confirme o modelo de licenciamento, a disponibilidade dos recursos necessários e o suporte do hardware ao throughput e às funções de inspeção.

## Operação

Faça backup versionado da configuração, mantenha console ou acesso físico para recuperação e teste mudanças de firewall em uma janela controlada. Documente a separação entre roteamento, filtragem, DNS, DHCP e túneis para que uma única regra não se torne um ponto de falha oculto.

## Relações

- [OPNsense](opnsense.md) possui origem próxima e um ecossistema próprio.
- [OpenWrt](openwrt.md) atende melhor a muitos roteadores embarcados.
- [Fabricantes e plataformas de rede](../fabricantes/index.md) compara pfSense com Cisco, TP-Link, Netgate, MikroTik e Ubiquiti.
- [Rede](../index.md) situa a responsabilidade de filtragem na topologia.

## Fonte primária

- [pfSense documentation](https://docs.netgate.com/pfsense/en/latest/)
