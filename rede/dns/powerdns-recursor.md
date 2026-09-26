# PowerDNS Recursor

PowerDNS Recursor é um resolvedor recursivo e cacheador separado do PowerDNS
Authoritative Server. Ele recebe consultas de clientes autorizados, segue a
hierarquia DNS ou consulta forwarders, valida respostas conforme a política e
reutiliza dados enquanto os TTLs permitirem.

## Recursão e encaminhamento

No modo recursivo, o serviço consulta root servers, TLDs e autoridades até
obter uma resposta. Em uma rede interna, ele também pode encaminhar zonas ou
todo o tráfego para resolvers upstream. Forwarding reduz o trabalho local, mas
cria dependência de privacidade, disponibilidade e política do upstream.

O cache é parte central do desempenho. TTL, prefetch, cache negativo, limite
de memória, concorrência e comportamento diante de falhas upstream devem ser
observados. Um cache aquecido reduz latência e carga, mas pode servir uma
resposta até a expiração permitida pelo DNS.

## Aplicações

- resolver interno para estações, servidores e workloads;
- resolver de alta capacidade na borda de uma organização;
- validação DNSSEC para clientes que não executam a validação;
- políticas de encaminhamento por domínio;
- separação entre zonas internas, autoridades públicas e Internet;
- camada recursiva atrás de dnsdist ou de balanceadores.

PowerDNS Recursor não é o catálogo autoritativo das zonas. Para publicar
domínios, use o Authoritative Server, BIND, CoreDNS ou outra autoridade. É
possível compor os processos na mesma máquina, mas a separação de portas,
ACLs, logs e domínios de falha deve ser explícita.

## Segurança

Permita recursão apenas para redes autorizadas. Um resolver aberto pode ser
abusado para amplificação e pode expor consultas de terceiros. Restrinja
interfaces de escuta, aplique ACLs, acompanhe taxas de consulta, habilite
DNSSEC quando o cenário exigir e proteja a interface de gerenciamento.

DoT e DoH podem proteger o trecho entre cliente e resolver quando habilitados
e suportados pela implantação. Eles não tornam automaticamente confiáveis os
upstreams nem substituem autenticação e autorização das aplicações.

## Diagnóstico

Compare uma resposta em cache com uma consulta iterativa ou encaminhada,
observe flags como `AD`, `RD` e `RA`, e diferencie `NXDOMAIN`, resposta vazia,
`SERVFAIL` e timeout. Meça hit rate, latência, falhas de validação DNSSEC,
erros de upstream, uso de memória e saturação de sockets.

## Relações

- [PowerDNS Authoritative Server](powerdns-authoritative.md) publica zonas.
- [Resolver](resolver.md) explica o papel recursivo em termos gerais.
- [DNSSEC](dnssec.md) explica a validação de autenticidade.
- [Reverse DNS](reverse-dns.md) explica consultas PTR.

## Fontes primárias

- [PowerDNS Recursor documentation](https://docs.powerdns.com/recursor/)
- [PowerDNS project](https://www.powerdns.com/)
