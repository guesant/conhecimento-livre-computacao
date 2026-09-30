# Netfilter

Netfilter é a infraestrutura do kernel Linux que permite observar e transformar
pacotes em pontos definidos do caminho de rede. Ele fornece hooks, rastreamento
de conexões, NAT e mecanismos de filtragem, mas não é uma política pronta nem o
comando que o operador necessariamente usa para configurar o host.

## Hooks e prioridade

Um hook do Netfilter pode receber chains de várias fontes, incluindo o firewall
do host, um CNI de Kubernetes e o Docker. Cada chain de base possui uma
prioridade inteira. Valores menores executam primeiro, por isso a posição de uma
regra no arquivo de uma ferramenta não basta para explicar a ordem final.

Ao investigar o caminho de um pacote, considere interface de entrada, roteamento,
decisão de encaminhamento, NAT, interface de saída e a prioridade de todas as
chains registradas no hook. O ruleset final do kernel é a fonte de verdade, não
uma configuração isolada de UFW, firewalld ou Docker.

## Rastreamento de conexão

O conntrack mantém estado dos fluxos observados. Para cada conexão, registra
endereços, portas, protocolo e fase do fluxo. Os estados mais usados são:

| Estado | Significado |
| --- | --- |
| `NEW` | primeiro pacote de um fluxo ainda não confirmado |
| `ESTABLISHED` | fluxo confirmado com tráfego relacionado nos dois sentidos |
| `RELATED` | fluxo secundário relacionado a uma conexão existente |
| `INVALID` | pacote que não corresponde a um estado esperado |

Esse estado permite aceitar respostas de conexões iniciadas de forma válida sem
abrir manualmente todas as portas de retorno. Ele também sustenta NAT, pois o
kernel precisa associar a resposta à tradução original antes de encaminhá-la.
Conntrack consome memória e possui limites. Uma inundação de conexões pode
esgotar a tabela mesmo quando ainda há CPU disponível, portanto timeouts,
contadores e alertas fazem parte da política de firewall.

## Interfaces que usam Netfilter

`iptables`, `ip6tables`, `arptables` e `ebtables` foram interfaces tradicionais
para famílias de protocolo diferentes. O [nftables](nftables.md) fornece uma
interface unificada e um modelo mais recente sobre a mesma infraestrutura do
kernel. UFW e firewalld são interfaces de nível mais alto que geram regras para
esse subsistema.

O Docker, o kube-proxy e os plugins de rede podem instalar regras próprias. Isso
não significa que exista uma única política coordenada entre eles. O operador
precisa definir quem é responsável por cada cadeia e verificar colisões de
prioridade, NAT, encaminhamento e limpeza de regras antigas.

## Diagnóstico

Comece pelo ruleset efetivo com `nft list ruleset` e pelos contadores de cada
regra. Relacione o resultado com `ip route`, interfaces, conntrack e captura de
pacotes. Um pacote pode ser descartado antes da regra que o operador está
observando, ou pode ser aceito e depois falhar no serviço por causa de rota,
TLS, autorização ou processo ausente.

[Diagnóstico de rede](../../diagnostico/rede.md) organiza a sequência de
investigação. [Firewalld](../../firewalld.md) e [UFW](../../ufw-e-portas-publicadas-pelo-docker.md)
explicam as interfaces de alto nível que configuram o mecanismo.

## Fontes primárias

- [Linux kernel Netfilter documentation](https://www.netfilter.org/documentation/)
- [Netfilter hooks](https://wiki.nftables.org/wiki-nftables/index.php/Netfilter_hooks)
- [Conntrack tools](https://conntrack-tools.netfilter.org/)
