# dnsmasq

dnsmasq é um serviço leve que combina DNS cacheador e encaminhador com DHCP.
Também pode oferecer DHCPv6, Router Advertisements, nomes locais, autoridade
para domínios simples, TFTP e suporte a PXE. Ele foi desenhado para redes
pequenas, roteadores, appliances, laboratórios e sistemas embarcados.

## Modelo operacional

dnsmasq lê hosts locais, leases DHCP e configurações de domínio. Para nomes
que não conhece, pode responder do cache ou encaminhar a resolvers upstream.
Quando configurado como autoridade para um domínio local, pode responder por
esses nomes sem transformar o serviço em uma plataforma completa de hospedagem
de zonas públicas.

O acoplamento entre DHCP e DNS é uma vantagem em uma LAN, pois leases podem
ser associados a nomes. Também cria uma responsabilidade combinada: uma
mudança de interface, escopo DHCP ou lista de hosts pode alterar a resolução
dos clientes.

## Aplicações

- gateway doméstico e roteador de pequena rede;
- OpenWrt e appliances com pouca memória;
- laboratório com DHCP, nomes locais e cache DNS;
- rede temporária ou de instalação;
- PXE, TFTP e boot de hosts quando o fluxo é simples;
- encaminhamento condicional para resolver interno ou externo.

dnsmasq não é normalmente a escolha para uma autoridade pública com muitas
zonas, DNSSEC operacional complexo, backend relacional, múltiplos operadores
ou exigência de API rica. Para esses casos, compare BIND, PowerDNS ou um
serviço DNS gerenciado.

## Segurança

Prenda o serviço às interfaces corretas, limite clientes, não exponha
recursão, restrinja DHCP a segmentos sob seu controle e proteja arquivos de
leases e configuração. Um servidor DHCP inesperado pode alterar gateway, DNS e
rotas de toda a rede. Em uma rede existente, habilitar `dhcp-authoritative` sem
ter certeza da topologia pode causar conflito com outro servidor DHCP.

Quando TFTP ou PXE forem usados, trate os arquivos de boot como artefatos de
infraestrutura: controle origem, integridade, permissões e substituição. TFTP
não oferece a mesma proteção de transporte que HTTPS ou SSH.

## Diagnóstico

Verifique interfaces de escuta, leases, `resolv-file`, `server` e `address`,
ordem das fontes locais, upstreams, cache e logs. Para DHCP, confirme que há
um único servidor responsável pelo segmento. Para DNS, compare uma consulta
local com uma consulta ao upstream e observe se a resposta veio de uma zona
local, do cache ou de encaminhamento.

## Relações

- [Resolver](resolver.md) explica cache e recursão.
- [BIND 9](bind.md) atende cenários de autoridade e recursão mais amplos.
- [CoreDNS](coredns.md) usa plugins e integração forte com Kubernetes.
- [Instalação pela rede](../../sistemas/boot/network-install.md) explica PXE,
  DHCP, TFTP e HTTP.

## Fonte primária

- [dnsmasq manual](https://thekelleys.org.uk/dnsmasq/docs/dnsmasq-man.html)
