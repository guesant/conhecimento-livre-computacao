# nftables

nftables é a interface moderna para configurar filtragem, NAT e outras ações
do Netfilter. Ele substitui a família de comandos separados do iptables por uma
linguagem e uma engine unificadas, capazes de trabalhar com IPv4, IPv6, ARP,
bridging e hooks por dispositivo.

## Modelo de execução

O `nft` transforma regras em bytecode executado por uma máquina virtual do kernel.
Tabelas contêm chains, e chains contêm regras. Chains de base ficam ligadas a um
hook e uma prioridade; chains regulares podem ser chamadas por `jump` ou
`goto`. Essa composição deixa a organização explícita e permite trocar um
ruleset em uma transação atômica.

As famílias mais comuns são:

| Família | Cobertura |
| --- | --- |
| `ip` | IPv4 |
| `ip6` | IPv6 |
| `inet` | IPv4 e IPv6 na mesma tabela |
| `arp` | ARP |
| `bridge` | bridging Ethernet |
| `netdev` | hook associado a um dispositivo |

## Relação com iptables

O iptables tradicional possui tabelas e caminhos predefinidos por família. O
`iptables-nft` aceita a sintaxe conhecida, mas traduz as regras para o
subsistema `nf_tables`. Isso permite compatibilidade com scripts antigos sem
significar que o sistema esteja usando o backend legado.

Verifique o backend com `update-alternatives --display iptables` e examine o
estado efetivo com `nft list ruleset`. Misturar regras declaradas diretamente
com regras geradas por iptables, Docker, Kubernetes ou firewalld pode criar uma
política difícil de atribuir a um único arquivo de configuração.

## Escala e operação

Rulesets grandes podem usar sets e verdict maps para consultar conjuntos de
endereços ou serviços sem repetir a mesma regra. Isso é especialmente relevante
quando uma ferramenta gera uma regra para cada Service ou endpoint. O ganho real
depende do caminho de dados, do número de entradas e da versão do kernel.

Use arquivos declarativos, revisão de diff, transações atômicas e rollback. Uma
regra aplicada manualmente pode desaparecer no próximo reload ou ser sobrescrita
por uma ferramenta de mais alto nível. Defina a fonte de verdade antes de
adicionar uma regra ao host.

## Relações

- [Netfilter](netfilter.md) explica os hooks, conntrack e a infraestrutura do
  kernel que executa as regras.
- [Firewalld](../../firewalld.md) fornece uma política baseada em zonas.
- [UFW e portas publicadas pelo Docker](../../ufw-e-portas-publicadas-pelo-docker.md)
  explica a interação entre firewall de host e publicação de portas.
- [Rede interna do cluster](../../rede-interna-do-cluster.md) mostra como
  bridges, interfaces virtuais e encapsulamento aparecem num cluster.

## Fontes primárias

- [nftables wiki](https://wiki.nftables.org/)
- [nftables reference](https://www.netfilter.org/projects/nftables/manpage.html)
- [nftables JSON output](https://wiki.nftables.org/wiki-nftables/index.php/Libnftables_JSON)
