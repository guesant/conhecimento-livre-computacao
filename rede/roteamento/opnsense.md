# OPNsense

OPNsense é uma distribuição de firewall e roteamento baseada em FreeBSD, com interface administrativa, filtragem de tráfego, NAT, VPN, DNS e recursos de observabilidade. Ele combina configuração de rede com políticas de segurança no perímetro.

## Quando usar

OPNsense é adequado quando se deseja um appliance administrável, com recursos de firewall e extensões pela interface e por plugins. O desenho precisa considerar alta disponibilidade, backup da configuração e como recuperar o acesso quando uma regra bloquear a rede de administração.

## Segurança

Restrinja a interface de administração, use MFA quando disponível, mantenha o sistema atualizado e trate backups como material sensível. Regras devem ter origem, destino, serviço e justificativa claros, evitando permissões amplas que apenas escondem problemas de conectividade.

## Relações

- [pfSense](pfsense.md) é uma alternativa próxima.
- [OpenWrt](openwrt.md) é mais orientado a roteadores e equipamentos com recursos limitados.
- [Provider OPNsense](../../iac/providers/opnsense.md) automatiza parte da API do produto.

## Fonte primária

- [OPNsense documentation](https://docs.opnsense.org/)
