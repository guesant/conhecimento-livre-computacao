# Redes

Esta área organiza fundamentos de comunicação, resolução de nomes, conectividade privada, filtragem, proxies e redes de cluster.

## Arquitetura e escopos

[Arquitetura física e lógica da Internet](arquitetura/index.md) explica como meios físicos, redes de acesso, agregação, backbones, sistemas autônomos e serviços de aplicação formam uma cadeia. [Equipamentos de rede](equipamentos/index.md) diferencia access points, modems, switches, roteadores e funções combinadas. [Escopos de rede](escopos/index.md) compara LAN, MAN e WAN.

## Fundamentos

[OSI](fundamentos/osi.md) e [TCP/IP](fundamentos/tcp-ip.md) fornecem o vocabulário de camadas e endereçamento. Interfaces, rotas e camada 2 explicam como um host alcança outros destinos.

## DNS

DNS deve ser aprendido em camadas: resolução e [registros](dns/records.md); servidores autoritativos e recursivos; [BIND](dns/bind.md); [DNSSEC](dns/dnssec.md); [mDNS](dns/mdns.md); e [registro de domínio](dns/registro-de-dominio.md). Esses assuntos se relacionam, mas resolvem problemas diferentes.

Correio eletrônico compõe [SMTP](email/smtp.md), [POP3](email/pop3.md), [IMAP](email/imap.md), [DKIM](email/dkim.md), [SPF](email/spf.md) e [DMARC](email/dmarc.md). Transporte, acesso à caixa e autenticação de domínio são responsabilidades distintas.

## Governança e organizações

[Organizações da Internet no Brasil e na América Latina](governanca/index.md) explica a diferença entre governança multissetorial, operação técnica, registro de nomes, recursos de numeração, interconexão e proteção de dados. A categoria separa [CGI.br](governanca/cgi-br.md), [NIC.br](governanca/nic-br.md), [Registro.br](governanca/registro-br.md), [IX.br](governanca/ix-br.md), [LACNIC](governanca/lacnic.md) e [ANPD](governanca/anpd.md).

## Filtragem e proxies

[Tipos de firewall](firewall/index.md) separa filtragem stateless, stateful, host,
rede, camada de aplicação, WAF, NGFW, IDS e IPS. [Proxies](proxy/index.md) explica
forward proxy, reverse proxy e balanceamento, incluindo [HAProxy](proxy/haproxy.md).

## Conectividade privada

[VPN](conectividade/vpn.md) cria conectividade protegida entre participantes. [Túnel](conectividade/tunel.md) encapsula tráfego por outro canal. [Borda de rede](conectividade/borda.md) descreve o ponto de encontro entre redes e políticas, não um protocolo específico.

## Fabricantes e plataformas

[Fabricantes e plataformas de rede](fabricantes/index.md) compara equipamentos, sistemas operacionais de rede, controladores e appliances. A distinção é importante: Cisco, TP-Link e Ubiquiti são portfólios de hardware e software; pfSense e RouterOS são plataformas; Netgate combina appliances, software e suporte comercial.

## Continue por aqui

Para nomes, comece por resolução DNS. Para conectividade privada, compare VPN e túnel antes de escolher uma implementação.
