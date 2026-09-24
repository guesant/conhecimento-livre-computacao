# pfSense

pfSense é uma distribuição de firewall e roteamento baseada em FreeBSD. Ela oferece filtragem stateful, NAT, VPN, serviços de rede e administração por interface web, com extensões conforme a edição e os pacotes instalados.

## Quando usar

pfSense é uma opção madura para appliances de borda e redes tradicionais. Antes de escolhê-lo, confirme o modelo de licenciamento, a disponibilidade dos recursos necessários e o suporte do hardware ao throughput e às funções de inspeção.

## Operação

Faça backup versionado da configuração, mantenha console ou acesso físico para recuperação e teste mudanças de firewall em uma janela controlada. Documente a separação entre roteamento, filtragem, DNS, DHCP e túneis para que uma única regra não se torne um ponto de falha oculto.

## Relações

- [OPNsense](opnsense.md) possui origem próxima e um ecossistema próprio.
- [OpenWrt](openwrt.md) atende melhor a muitos roteadores embarcados.
- [Rede](../index.md) situa a responsabilidade de filtragem na topologia.

## Fonte primária

- [pfSense documentation](https://docs.netgate.com/pfsense/en/latest/)
