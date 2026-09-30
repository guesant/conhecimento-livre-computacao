# BIND 9

BIND 9 é uma implementação de servidor DNS. O mesmo daemon pode atuar como autoritativo para determinadas zonas, como secundário para outras e como resolver recursivo e cacheador para clientes autorizados. Esses papéis são logicamente diferentes e frequentemente devem ser separados por instância, rede ou política.

## Hardware e forma de execução

BIND 9 pode rodar em servidores físicos, máquinas virtuais, containers e
equipamentos de diferentes arquiteturas. O limite prático normalmente vem de
memória, número de zonas, taxa de consultas, tamanho do cache, DNSSEC,
transferências e latência de armazenamento, não de um requisito de hardware
fixo do projeto.

## Autoridade e recursão

Quando BIND é autoritativo, ele responde pelos dados das zonas que administra. Quando é recursivo, recebe uma consulta de um cliente e percorre a hierarquia DNS, armazenando respostas conforme TTL. Expor recursão para a Internet sem controle cria um risco de abuso e amplificação.

Uma configuração segura define explicitamente quais clientes podem consultar recursão, quais zonas são autoritativas, quais transferências são permitidas e quais views devem ser usadas. Um servidor autoritativo público geralmente desabilita recursão para reduzir sua superfície.

Views permitem respostas diferentes conforme a origem da consulta, o que pode
ser útil em split-horizon DNS. Elas aumentam a capacidade de expressar a
política, mas também aumentam o risco de publicar uma zona incorreta para um
cliente. Use ACLs, TSIG, `rndc`, logs e validação de configuração para tornar
as mudanças auditáveis.

## Configuração e operação

`named.conf` reúne opções, zonas, ACLs, views, logging e controles de transferência. A zona precisa de SOA, NS e registros coerentes. Alterar dados exige atualizar o serial de acordo com a estratégia de publicação e verificar sintaxe antes de recarregar.

DNSSEC adiciona assinaturas e validação, mas não corrige uma delegação errada, uma zona inconsistente ou uma política de recursão aberta. Monitorar respostas, expiração de zonas, transferências e erros de validação é parte da operação.

## Relação com identidade

FreeIPA pode integrar BIND para administrar nomes do domínio de identidade. Nesse cenário, DNS participa da descoberta de KDCs, LDAP e outros serviços. Uma falha de DNS pode aparecer como falha de login Kerberos, mesmo que o diretório e o KDC estejam funcionando.

## Quando usar

Use BIND quando a compatibilidade, o controle de zonas, a integração com ambientes Unix e a operação autoritativa ou recursiva forem requisitos. Separe BIND autoritativo e recursivo quando os clientes, níveis de confiança e políticas de exposição forem diferentes.

BIND é adequado para autoridades públicas, servidores secundários, DNS
interno, recursão controlada, DNSSEC, integração com FreeIPA e ambientes que
precisam de ampla compatibilidade. Para um roteador simples, dnsmasq pode ser
menor; para DNS Kubernetes orientado a plugins, CoreDNS pode se encaixar
melhor; para backend relacional e API de zonas, PowerDNS pode reduzir trabalho
de integração.

## Relações

- [Servidor DNS autoritativo](authoritative.md) define o papel, independentemente da implementação.
- [Resolver](resolver.md) explica recursão e cache.
- [PowerDNS Authoritative Server](powerdns-authoritative.md) e [PowerDNS
  Recursor](powerdns-recursor.md) separam os papéis em processos distintos.
- [CoreDNS](coredns.md) usa uma cadeia de plugins, especialmente em Kubernetes.
- [Technitium DNS](technitium.md) combina autoridade, recursão e console web.
- [dnsmasq](dnsmasq.md) atende redes pequenas com DNS, DHCP e boot de rede.
- [Zona DNS](zone.md) e [Registros DNS](records.md) explicam os dados publicados.
- [FreeIPA](../../seguranca/identidade/freeipa.md) documenta a integração com identidade.

## Fontes primárias

- [BIND 9 Administrator Reference Manual](https://bind9.readthedocs.io/en/stable/)
- [ISC BIND](https://www.isc.org/bind/)
