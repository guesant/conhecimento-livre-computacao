# Escopos de rede

LAN, MAN e WAN classificam redes principalmente pelo alcance e pelo domínio de operação. Os limites não são números universais. Uma organização pode chamar de MAN uma rede metropolitana que outra chama de WAN regional. O valor da classificação está em comunicar propriedade, latência esperada, meio de transporte, fronteiras administrativas e modelo de operação.

## Comparação

| Escopo | Alcance típico | Operação comum | Exemplos |
| --- | --- | --- | --- |
| [LAN](lan.md) | Sala, prédio, residência ou campus | Uma organização ou uma unidade local | Ethernet, Wi-Fi, VLAN |
| [MAN](man.md) | Vários prédios ou uma região metropolitana | Organização, operadora, universidade ou IXP | Fibra metropolitana, anel urbano, metro Ethernet |
| [WAN](../conectividade/wan.md) | Cidades, estados, países ou continentes | Operadora, empresa ou consórcio | MPLS, Internet, SD-WAN, enlaces privados |

## Escopo não define protocolo

LAN não significa necessariamente Ethernet, MAN não significa necessariamente fibra e WAN não significa necessariamente Internet pública. Os termos descrevem o alcance e a operação; os protocolos e meios precisam ser especificados separadamente.

Uma WLAN é uma LAN sem fio. Uma VLAN é uma separação lógica, não uma área geográfica. Uma VPN pode criar uma rede lógica sobre uma WAN. Um backbone pode atravessar várias MANs e WANs.

## Propriedade e fronteira

Em uma LAN, a mesma equipe pode controlar hosts, switches, APs, DHCP e firewall. Em uma WAN, o caminho pode atravessar múltiplos provedores e sistemas autônomos. Essa mudança de propriedade altera observabilidade, contratos, SLA, segurança, diagnóstico e capacidade de aplicar mudanças.

## Fontes primárias

- [IEEE 802 LAN/MAN Standards Committee](https://www.ieee802.org/)
- [IEEE 802 overview and architecture](https://www.ieee802.org/secmail/pdfocSP2xXA6d.pdf)
