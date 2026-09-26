# Netfilter

Esta página fica com a parte que os fundamentos de [firewall no Linux](firewalld.md) deixam para trás por design: o mecanismo interno do netfilter, como uma conexão inteira é rastreada, o que muda entre a arquitetura antiga de `iptables` e a atual de `nftables`, e a ordem prática de investigar um problema de rede quando algo dá errado.

## Prioridade de chain e rastreamento de conexão

Um hook do netfilter não está limitado a uma única chain. Várias ferramentas, como o firewall do host, o CNI de um cluster e o Docker, podem registrar suas próprias chains no mesmo hook, e o kernel precisa de um critério para decidir a ordem de execução.

Esse critério é a prioridade, um número inteiro associado a cada chain de base, a que está de fato presa a um hook. Chains de prioridade mais baixa executam primeiro, o que explica por que uma regra de NAT do Docker pode processar um pacote antes que a política de bloqueio do UFW o veja.

Um firewall que decide cada pacote isoladamente não consegue expressar uma regra tão básica quanto aceitar o tráfego de resposta de uma conexão já iniciada pelo próprio host. O conntrack resolve isso mantendo uma tabela de estado: para cada fluxo observado, o kernel registra endereços, portas, protocolo e uma fase da conexão. A tabela abaixo resume os quatro estados possíveis desse rastreamento.

| Estado | Significado |
| --- | --- |
| `NEW` | primeiro pacote observado de um fluxo ainda não confirmado |
| `ESTABLISHED` | o fluxo já teve tráfego confirmado nos dois sentidos |
| `RELATED` | um fluxo secundário ligado a uma conexão já rastreada, como o canal de dados do FTP |
| `INVALID` | um pacote que não corresponde a nenhum padrão esperado |

Esse estado é o que permite escrever uma política declarando aceitar tudo que for `ESTABLISHED` ou `RELATED` e rejeitar o resto por padrão, em vez de enumerar manualmente cada porta de resposta possível. É também o que sustenta o masquerading: sem saber que um pacote de resposta pertence a uma conexão já traduzida, o kernel não saberia para qual endereço interno reencaminhá-lo depois de desfazer o NAT.

## nftables: uma máquina virtual dentro do kernel

A diferença estrutural entre `iptables` e `nftables` não é de sintaxe, é de arquitetura interna. O `iptables` original embute lógica específica de protocolo diretamente no kernel, duplicada para cada família de endereço.

Uma implementação cobre IPv4, outra IPv6, outra ARP e outra bridging Ethernet, cada uma com seu próprio código em C no kernel, sem compartilhar a lógica de filtragem entre si. A tabela abaixo lista o comando de cada família.

| Família | Comando |
| --- | --- |
| IPv4 | `iptables` |
| IPv6 | `ip6tables` |
| ARP | `arptables` |
| Bridging Ethernet | `ebtables` |

O `nftables`, introduzido no kernel 3.13, substitui isso por uma máquina virtual genérica que executa bytecode: as regras escritas pelo operador são compiladas para esse bytecode, e uma única engine processa pacotes de qualquer família de endereço.

O resultado é um kernel mais simples de manter, uma ferramenta de espaço de usuário unificada, `nft`, no lugar de quatro comandos separados, e a possibilidade de substituir o ruleset inteiro numa única transação atômica, sem a janela em que um firewall parcialmente aplicado deixaria passar tráfego indevido.

Dentro dessa arquitetura, tabelas são o contêiner de mais alto nível, cada uma associada a uma família de endereço. A tabela abaixo lista as famílias que o `nftables` reconhece.

| Família | Cobre |
| --- | --- |
| `ip` | IPv4 |
| `ip6` | IPv6 |
| `inet` | IPv4 e IPv6 ao mesmo tempo |
| `arp` | ARP |
| `bridge` | bridging Ethernet |
| `netdev` | ganchos por dispositivo de rede |

Chains vivem dentro de uma tabela, de base, presas a um hook com a prioridade já descrita, ou regulares, só alcançáveis por `jump` a partir de outra chain, um recurso de organização que o modelo antigo não oferecia da mesma forma. O modelo é declarativo e composicional, tabelas contendo chains contendo regras, em vez das tabelas fixas predefinidas que o `iptables` impõe.

A maioria das distribuições atuais, incluindo o Debian desde a versão 10, não elimina o comando `iptables`: substitui o que ele faz por baixo. O `iptables-nft` aceita exatamente a mesma sintaxe de linha de comando de sempre, mas traduz cada regra para o subsistema `nf_tables` do kernel.

Scripts, ferramentas e até UFW e firewalld continuam funcionando sem alteração, e o que efetivamente filtra o tráfego, por baixo, já é `nftables`. `update-alternatives --display iptables` mostra qual backend está ativo no sistema.

## Escolher entre `nftables` e `iptables`

Nenhuma das duas interfaces é estritamente superior; as duas configuram o mesmo netfilter por baixo, com modelos de sintaxe e organização diferentes. O `iptables` legado usa tabelas fixas predefinidas pelo kernel e avaliação sequencial, cada regra comparada uma a uma até uma decisão terminal. O `nftables` usa tabelas e chains declaradas pelo operador, e pode usar estruturas de mapa, os verdict maps, para lookup em tempo constante em vez de percorrer regra por regra.

O caso concreto que torna essa diferença mensurável é o kube-proxy do Kubernetes, que gera uma regra de encaminhamento para cada combinação de IP e porta de cada Service do cluster. No modo `iptables`, essa avaliação cresce linearmente com o número de Services, e em clusters com milhares deles a travessia já aparece mensurável na latência de cada pacote.

O modo `nftables`, geralmente disponível desde a versão 1.31 do Kubernetes, troca isso por um único verdict map consultado em tempo aproximadamente constante, independentemente do tamanho do cluster.

Medições publicadas pelo próprio projeto Kubernetes mostram que, em clusters com cinco a dez mil Services, a latência mediana do modo `nftables` já se aproxima da latência de melhor caso do modo `iptables`, uma diferença que se acentua em clusters ainda maiores. Apesar disso, `iptables` continua sendo o modo padrão do kube-proxy por compatibilidade; migrar exige troca explícita de configuração, não acontece sozinho numa atualização de versão.

Manter regras em `iptables-nft` continua sendo a escolha mais simples quando um host já tem scripts ou playbooks escritos nessa sintaxe, e o volume de regras é pequeno o bastante para a diferença de desempenho nunca aparecer na prática, o caso da maioria dos hosts de borda e nós de cluster deste notebook.

Migrar para `nft` nativo faz mais sentido quando o ruleset já é grande o bastante para a avaliação sequencial virar um gargalo mensurável, ou quando a distribuição em uso já trata o modelo novo como o caminho recomendado para configuração nova.

Um host com regras escritas diretamente em `nft` e, ao mesmo tempo, ferramentas que ainda chamam `iptables`, mesmo traduzido, tem duas fontes de regra coexistindo no mesmo ruleset do kernel, sem que nenhuma das duas tenha visão completa do que a outra configurou.

Depurar um firewall nessas condições exige inspecionar o ruleset final com `nft list ruleset`, porque nem `iptables -L` nem um arquivo de regras isolado mostram o quadro completo quando as duas convivem.

O Docker usa `iptables` por padrão, mas oferece suporte experimental a um backend `nftables` nativo, selecionável pela opção `firewall-backend` do daemon, ainda documentado como experimental.

O Kubernetes, via kube-proxy, oferece os dois modos já descritos, com `iptables` ainda como padrão hoje. Nenhum dos dois força a migração: um cluster ou host pode continuar rodando inteiramente sobre `iptables-nft` sem perder funcionalidade.

O procedimento de diagnóstico foi extraído para [diagnóstico de rede](diagnostico/rede.md), porque investigar conectividade é uma responsabilidade diferente de explicar o funcionamento do Netfilter.

## Continue por aqui

[Interfaces, rotas e camada 2 no Linux](interfaces-rotas-e-l2-no-linux.md) cobre as peças do caminho de rede. [Firewalld](firewalld.md) cobre a camada de mais alto nível que UFW e firewalld configuram por cima deste mesmo Netfilter.
