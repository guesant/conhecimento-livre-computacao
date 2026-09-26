# Netgate

Netgate é uma empresa de appliances e software de rede associada ao ecossistema pfSense. Seu portfólio não é apenas uma lista de computadores pré-configurados: inclui appliances pfSense Plus, o sistema TNSR para roteamento de alto desempenho, opções bare metal, virtuais e em nuvem, além de suporte técnico, treinamento e serviços profissionais.

## Hardware e plataformas

| Família | Hardware ou software | Responsabilidade |
| --- | --- | --- |
| Appliances desktop | Equipamentos compactos, frequentemente fanless, com múltiplas portas Ethernet | residência, homelab, filial e SMB |
| Appliances de maior capacidade | Equipamentos desktop expandidos ou rackmount, com mais memória, portas e aceleração | média empresa, borda e alta disponibilidade |
| pfSense Plus | Plataforma de firewall, roteamento, NAT, VPN, serviços de rede e pacotes | borda segura e redes multi-WAN |
| TNSR | Plataforma orientada a encaminhamento de alto desempenho e conectividade de borda | throughput elevado, IPsec e conectividade de nuvem |
| Bare metal, VM e cloud | Execução do software em hardware próprio, hipervisor ou provedor | ambientes que não querem appliance físico |

O modelo de appliance exato determina portas, desempenho, aceleração criptográfica, armazenamento, memória, suporte a alta disponibilidade e nível de suporte incluído. Não compare números de firewall ou VPN de modelos diferentes sem conferir o método de teste e o perfil de tráfego.

## Aplicações

Com pfSense Plus, Netgate atende firewall stateful, NAT, roteamento, VLAN, DHCP, DNS, VPN, multi-WAN, alta disponibilidade, shaping, captive portal, monitoramento e prevenção de ataques por pacotes ou integrações. TNSR tem outra orientação, com foco em edge routing de alto desempenho, IPsec site-to-site e conectividade de nuvem.

Essa distinção evita uma decisão incorreta. pfSense Plus prioriza um conjunto integrado de serviços de segurança e administração; TNSR é uma opção para encaminhamento de alto throughput. A escolha deve partir dos requisitos de pacotes por segundo, latência, criptografia, inspeção, operação e suporte, não somente da largura de banda anunciada.

## Casos de uso

- gateway de residência avançada ou laboratório com múltiplas VLANs;
- firewall de filial com VPN e mais de uma conexão de Internet;
- borda de SMB com políticas, DNS, DHCP, portal e relatórios;
- par de appliances para alta disponibilidade;
- firewall virtual em um cluster de virtualização;
- conectividade de nuvem ou site-to-site com requisitos de throughput elevados, quando TNSR for apropriado.

## Suporte e segurança

Netgate oferece documentação do pfSense, planos TAC, serviços profissionais e treinamento. A edição, o appliance e o contrato precisam ser registrados separadamente na decisão operacional. A comunidade do pfSense continua sendo uma fonte útil, mas não substitui um contrato quando há requisito de resposta, escalonamento ou orientação formal.

Proteja console, interface web, SSH, APIs e backups de configuração. Use autenticação centralizada quando o cenário exigir, segmente interfaces de administração, armazene backups fora do appliance e teste restauração. Em alta disponibilidade, documente sincronização de configuração, estados, certificados, chaves e o procedimento para operar quando um membro estiver isolado.

## Relações

- [pfSense](../roteamento/pfsense.md) explica a plataforma de firewall e roteamento.
- [OPNsense](../roteamento/opnsense.md) é uma alternativa próxima, mas não é uma edição da Netgate.
- [VPN](../conectividade/vpn.md) explica o conceito que aparece em várias aplicações do portfólio.

## Fontes primárias

- [Netgate appliances](https://www.netgate.com/appliances)
- [pfSense documentation](https://docs.netgate.com/pfsense/en/latest/)
- [Netgate support](https://www.netgate.com/support)
- [TNSR](https://www.tnsr.com/)
