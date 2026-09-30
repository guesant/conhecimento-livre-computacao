# Mapa de quorum, consenso e Raft

Cluster, replicação e consenso são conceitos relacionados, mas não são sinônimos. Um
cluster é um conjunto de nós tratado como uma unidade operacional. Replicação mantém
cópias de dados ou de um log. Consenso coordena decisões para que os nós concordem sobre
uma sequência de valores ou comandos, mesmo quando alguns nós falham.

Essa distinção é importante porque uma topologia com um primary e várias réplicas pode
ter replicação sem consenso entre os nós. O primary continua sendo uma autoridade única,
enquanto as réplicas recebem e aplicam suas mudanças. Já um grupo de consenso precisa
decidir qual membro pode liderar, quais entradas do log estão confirmadas e qual estado
deve ser aplicado por todos os participantes.

## Quorum de maioria

Quorum é a quantidade mínima de votos necessária para uma decisão. Em um grupo com `N`
votantes, o quorum de maioria é:

```text
floor(N / 2) + 1
```

Esse número garante que dois grupos que obtiveram maioria sempre tenham pelo menos um
voto em comum. O voto compartilhado impede que duas partições diferentes confirmem
decisões incompatíveis ao mesmo tempo, desde que o protocolo preserve a validade desse
voto e que os nós não sejam Byzantine.

A tolerância a falhas de processo para continuar tomando decisões é:

```text
floor((N - 1) / 2)
```

| Votantes | Quorum | Falhas de votantes toleradas | Observação |
| ---: | ---: | ---: | --- |
| 1 | 1 | 0 | Não há redundância de consenso. |
| 2 | 2 | 0 | Qualquer falha ou partição elimina a maioria. |
| 3 | 2 | 1 | Continua decidindo com um nó indisponível. |
| 4 | 3 | 1 | Custa mais que três e tolera a mesma falha. |
| 5 | 3 | 2 | Continua decidindo com dois nós indisponíveis. |

## Por que três nós são preferíveis a dois

Em um cluster de dois votantes, a maioria é formada pelos dois. Se um nó parar, perder
conectividade ou ficar isolado, o nó restante não sabe se é a única parte viva do grupo
ou se o outro continua aceitando decisões em uma partição diferente. Para preservar a
segurança, ele deve parar de confirmar operações que exigem maioria. O sistema pode
continuar respondendo leituras locais, mas perde a capacidade de avançar com segurança
nas decisões que dependem do quorum.

Com três votantes, a maioria é dois. Um nó pode falhar sem impedir que os outros dois
formem uma maioria. A mesma relação explica por que cinco nós suportam duas falhas e por
que quatro não oferecem mais tolerância que três. Números ímpares aproveitam melhor cada
voto quando a decisão depende de maioria simples.

Isso não significa que todo cluster precise ter um número ímpar de servidores. Quatro
nós podem ser adequados quando a capacidade adicional é necessária ou quando existe uma
política de votação diferente. O ponto é que adicionar um quarto votante a um grupo de
três não aumenta a quantidade de falhas toleradas pela maioria. Também é possível usar
um witness ou arbitrator sem cópia completa dos dados para desempatar uma topologia de
dois nós, mas esse componente não substitui uma réplica completa para durabilidade.

Quorum de votos também não corrige um failure domain compartilhado. Três máquinas no
mesmo host, rack, switch ou domínio elétrico podem cair juntas. Para que a tolerância
seja real, os votantes precisam estar distribuídos conforme as falhas que a arquitetura
pretende suportar, sem introduzir latência que torne o protocolo impraticável.

## Consenso e máquina de estados replicada

Um modelo comum de consenso é a máquina de estados replicada. Os nós mantêm um log de
comandos em uma ordem comum. Cada nó aplica a mesma sequência a uma máquina de estados
determinística e, por isso, chega ao mesmo resultado.

O log não precisa ser uma tabela de banco. Ele pode conter comandos de um armazenamento
chave-valor, alterações de configuração, eleição de um líder ou operações de um
control-plane. O algoritmo de consenso protege a ordem e a confirmação do log; a
aplicação define o significado dos comandos.

Segurança e disponibilidade são propriedades diferentes. Um protocolo pode continuar
seguro e recusar novas decisões quando perdeu a maioria. Essa recusa é preferível a
confirmar uma decisão que outra partição também possa confirmar. O sistema volta a
avançar quando os membros se reencontram, um líder válido é eleito e o log é reconciliado.

## Raft

[Raft](https://raft.github.io/) é um algoritmo de consenso para gerenciar um log
replicado. Ele foi projetado para ser compreensível e separa o problema em eleição de
líder, replicação do log, segurança e alteração de membros. O artigo
[In Search of an Understandable Consensus Algorithm](https://raft.github.io/raft.pdf)
descreve o algoritmo e suas propriedades.

Cada servidor assume um de três papéis:

- `leader`, que recebe comandos dos clientes e coordena a replicação;
- `follower`, que aceita entradas e responde às mensagens do líder;
- `candidate`, que tenta ser eleito quando deixa de receber heartbeats.

O tempo é dividido em termos. Quando um follower não recebe um heartbeat dentro de seu
timeout de eleição, ele inicia uma eleição, incrementa o termo e solicita votos. Um
candidate só se torna leader depois de obter maioria. Os timeouts aleatórios reduzem a
probabilidade de todos os nós iniciarem a eleição simultaneamente.

O líder acrescenta uma entrada ao próprio log e envia essa entrada aos followers. Uma
entrada só é considerada comprometida quando está replicada na maioria exigida pelo
protocolo. Depois disso, os servidores aplicam a entrada em suas máquinas de estado na
mesma ordem. Um follower com entradas divergentes remove o sufixo incompatível antes de
aceitar o log correto do líder.

As propriedades de segurança de Raft impedem que dois líderes de termos diferentes
confirmem logs incompatíveis na mesma posição. Se uma partição deixa o líder sem
maioria, a minoria pode permanecer disponível para algumas leituras, mas não consegue
comprometer novas entradas. A partição que contém a maioria pode eleger um novo líder e
continuar avançando.

Raft também define a alteração de membros por maiorias sobrepostas. Durante a transição,
as configurações antiga e nova precisam compartilhar uma maioria compatível, evitando
que uma mudança de composição crie duas decisões válidas e incompatíveis. A alteração
de membros deve ser tratada como uma operação de consenso, não como uma simples edição
independente em cada servidor.

## O que Raft não resolve

Raft não transforma automaticamente um banco primary-replica em um cluster de consenso.
Ele é um algoritmo que uma implementação pode usar para replicar um log ou controlar
metadados. O banco ainda precisa definir como persistir dados, aplicar comandos,
reconstruir um membro, expor o endpoint, fazer fencing e operar o failover.

Raft também não tolera automaticamente comportamento Byzantine, como um nó que mente de
forma coordenada ou envia respostas diferentes para participantes diferentes. A análise
normal considera falhas de parada, perda de mensagens, atrasos, reinícios e partições,
com recuperação baseada em armazenamento persistente e reentrada controlada no grupo.

Não confunda consenso com balanceamento de leitura, replicação assíncrona, quorum de
armazenamento ou uma fila. Esses mecanismos podem usar ideias semelhantes, mas possuem
objetivos e garantias diferentes.

## Operação e failure domains

Antes de escolher o tamanho do grupo, defina quais falhas precisam ser toleradas. Um
grupo de três nós no mesmo domínio de falha não oferece a mesma proteção que três nós
em domínios independentes. Também é necessário definir:

- como clientes descobrem o líder;
- como o líder antigo é isolado antes da promoção de outro;
- como membros atrasados recuperam o log;
- como o disco persistente é protegido;
- como mudanças de configuração são auditadas;
- como o cluster é restaurado quando a maioria foi perdida;
- como latência e perda de pacotes afetam o timeout de eleição.

Em sistemas de banco, monitore a saúde do primary ou líder, o atraso das réplicas, o
estado do quorum, a retenção de WAL ou log, a capacidade do disco e a elegibilidade dos
candidatos. Um nó conectado, mas atrasado ou sem armazenamento confiável, não deve ser
promovido apenas porque responde a um health check superficial.

## Relações

- [Clustering, redundância e distribuição](clustering-redundancia-e-distribuicao.md)
  apresenta os modelos de cluster de bancos.
- [Replicação](replicacao.md) explica primary, réplica, lag e failover.
- [Replicação em cascata](replicacao-em-cascata.md) explica relays e upstreams entre
  réplicas.
- [Quorum do control plane](../kubernetes/control-plane/quorum.md) aplica o conceito ao
  control plane Kubernetes e ao datastore que o sustenta.
- [Sistemas distribuídos](../arquitetura-aplicacoes/sistemas-distribuidos.md) trata
  coordenação, falhas e comunicação entre processos em uma perspectiva mais ampla.

## Fontes

- [Raft Consensus Algorithm](https://raft.github.io/)
- [In Search of an Understandable Consensus Algorithm](https://raft.github.io/raft.pdf)
- [PostgreSQL, log-shipping standby servers](https://www.postgresql.org/docs/current/warm-standby.html)
- [etcd, learning about distributed systems](https://etcd.io/docs/v3.6/learning/)
