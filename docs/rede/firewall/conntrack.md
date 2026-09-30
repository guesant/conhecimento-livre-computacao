# conntrack

Conntrack é o subsistema de acompanhamento de conexões do kernel Linux. Ele
mantém uma tabela de fluxos e associa pacotes a estados como `NEW`, `ESTABLISHED`,
`RELATED` e `INVALID`. Netfilter, nftables, firewalls, NAT e kube-proxy podem
usar essa informação para tomar decisões coerentes sobre pacotes que pertencem
à mesma conexão.

## Fluxo e estado

Para TCP, conntrack observa flags e transições, mas não substitui a máquina de
estados completa da aplicação. UDP não possui handshake equivalente; o kernel
usa temporizadores e tráfego observado para manter uma associação. ICMP pode
ser relacionado a um fluxo original por informações transportadas no erro.

`RELATED` representa tráfego associado a uma conexão principal, quando um helper
ou o protocolo permite essa relação. `INVALID` indica que o pacote não pode ser
associado com segurança ao estado conhecido. Aceitar tudo que está marcado como
`ESTABLISHED` sem restringir a interface, endereço e política pode abrir mais
tráfego que o esperado.

## Tabela e consumo

Cada entrada consome memória. Muitos clientes, scans, conexões curtas e ataques
de exaustão podem preencher a tabela antes de saturar CPU. Monitore contagem,
limite, inserções, expirações e descartes. Aumentar o limite sem dimensionar
memória ou investigar a origem apenas move a falha.

O timeout precisa refletir o protocolo. Um timeout muito curto encerra sessões
legítimas; um timeout muito longo mantém entradas inúteis. TCP keepalive,
retries de aplicações, WebSocket, NAT e serviços com long polling alteram o
perfil de ocupação.

## NAT e Kubernetes

Quando NAT altera endereços ou portas, conntrack mantém a relação entre os dois
lados. O mesmo host pode aparecer com IP diferente em logs antes e depois da
tradução. Em Kubernetes, kube-proxy, CNI e NetworkPolicy podem instalar regras
que dependem de conntrack. O diagnóstico deve separar o estado do kernel no nó,
o fluxo do Pod e o endereço observado no serviço.

## Diagnóstico

`conntrack -L` lista entradas quando a ferramenta está instalada e autorizada;
`conntrack -S` mostra contadores. `nft list ruleset` revela as regras que usam
ct state. Para um incidente, capture interface, zona de rede, tuple original,
tradução, estado e timeout. Limpar a tabela em produção derruba conexões e não
deve ser usado como tentativa genérica de recuperação.

## Relações

- [Netfilter](netfilter.md) explica hooks e decisões de filtragem.
- [nftables](nftables.md) usa expressões de estado e NAT.
- [Kube-proxy](../../kubernetes/networking/kube-proxy.md) pode depender do estado do nó.

## Fontes primárias

- [Netfilter connection tracking](https://www.netfilter.org/projects/conntrack-tools/)
- [nf_conntrack no kernel Linux](https://www.kernel.org/doc/html/latest/networking/nf_conntrack-sysctl.html)
- [conntrack-tools](https://conntrack-tools.netfilter.org/)
