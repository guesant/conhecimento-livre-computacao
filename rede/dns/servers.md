# Servidores DNS

Um servidor autoritativo e um resolvedor recursivo resolvem problemas de
engenharia opostos. O autoritativo responde a partir de dados que controla;
o recursivo navega uma cadeia de servidores externos e precisa validar e
armazenar respostas com segurança.

Separar os papéis reduz a superfície de risco e torna a operação previsível.
Misturar os dois é aceitável em ambientes pequenos quando a simplicidade
compensa a superfície combinada, mas a escolha precisa ser explícita.

## Implementações

[PowerDNS Authoritative Server](powerdns-authoritative.md) e [PowerDNS
Recursor](powerdns-recursor.md) são componentes distintos. O primeiro armazena
zonas em backends plugáveis, inclusive bancos relacionais; o segundo é focado
em resolução recursiva e cache.

Unbound é um resolvedor recursivo leve, com validação DNSSEC e sem a função de
administrar zonas autoritativas. BIND pode operar nos dois papéis e continua
sendo uma referência para zonas e para a configuração `named.conf`, mas sua
dupla função deve ser avaliada com cuidado.

[Technitium DNS](technitium.md) combina autoridade, recursão, bloqueio de
domínios e DoT/DoH em um único processo com interface web. Isso favorece
homelabs, nos quais um painel integrado pode ser mais valioso que a separação
de processos.

[CoreDNS](coredns.md) é o servidor usado pelo Kubernetes, inclusive pelo K3s.
Ele funciona como um pipeline de plugins. O plugin `kubernetes` resolve a zona
`cluster.local` a partir do estado do cluster e o plugin `forward` encaminha
consultas para a Internet ou para outro resolvedor.

[dnsmasq](dnsmasq.md) combina DNS local e cacheador, DHCP, Router
Advertisements, TFTP e PXE com baixo consumo de recursos. Ele é apropriado
para redes pequenas e appliances, não para substituir uma autoridade pública
ou um sistema de zonas de grande escala.

## Critérios de escolha

O primeiro critério é o papel necessário, autoritativo, recursivo ou ambos. O
segundo é a capacidade de operação da equipe. O terceiro é a exposição do
serviço: um resolvedor acessível a clientes não confiáveis exige hardening
diferente de uma autoridade interna. Nenhum servidor é superior em todos os
cenários.

## Continue por aqui

[Resolver](resolver.md) e [servidor autoritativo](authoritative.md) detalham
os dois papéis. [BIND 9](bind.md) aprofunda uma implementação que pode exercer
ambos.
