# Technitium DNS Server

Technitium DNS Server é uma implementação multiplataforma, open source,
autoritativa e recursiva, voltada especialmente a DNS local self-hosted,
privacidade, desenvolvimento e redes pequenas ou médias. Ela oferece console
web, API, zonas, recursão, encaminhamento condicional e opções de DoT e DoH.

## Modelo operacional

Uma instalação pode servir zonas autoritativas internas, resolver nomes da
Internet, responder por hosts locais e aplicar políticas de bloqueio. A
interface web e a API concentram tarefas que em BIND exigiriam edição manual
de arquivos ou ferramentas complementares.

Essa integração facilita homelab, filial e rede de desenvolvimento, mas a
configuração continua sendo estado operacional. Faça backup, restrinja a
interface administrativa e documente como reconstruir o servidor sem depender
apenas do armazenamento local.

## Recursos

- zonas autoritativas e secundárias;
- resolução recursiva e forwarders condicionais;
- cache, prefetch e validação DNSSEC;
- listas de bloqueio e políticas por cliente ou zona;
- DNS-over-TLS e DNS-over-HTTPS quando habilitados;
- console web, API e execução em Windows, Linux, macOS ou container;
- integração com DHCP e nomes locais conforme o desenho escolhido.

## Casos de uso

- DNS de uma residência, homelab ou laboratório de desenvolvimento;
- rede pequena ou média que precisa de uma interface operacional integrada;
- resolver local com bloqueio de domínios e políticas por dispositivo;
- zonas internas para serviços, ambientes e dispositivos;
- ambiente de testes que precisa criar zonas sem manter uma cadeia complexa de
  arquivos e ferramentas.

Para uma autoridade pública de grande escala, multi-tenant ou altamente
automatizada, compare com PowerDNS Authoritative e BIND. Para DNS de serviço
em Kubernetes, CoreDNS costuma se integrar melhor ao modelo de descoberta do
cluster.

## Segurança e limites

Não exponha recursão aberta, console web ou API administrativa à Internet.
Separe usuários administrativos, use HTTPS com certificado válido, restrinja
clientes permitidos, preserve logs e mantenha a versão suportada. Listas de
bloqueio não substituem firewall, endpoint security ou autorização da
aplicação.

## Fontes primárias

- [Technitium DNS Server](https://technitium.com/dns/)
- [Technitium DNS help](https://technitium.com/dns/help.html)
