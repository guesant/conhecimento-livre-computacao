# Replicação em cascata

Replicação em cascata, também chamada de replicação hierárquica, usa uma réplica como
origem de outras réplicas. O primary mantém uma conexão direta com uma réplica de
primeiro nível. Essa réplica recebe as alterações, aplica o log e também o disponibiliza
para réplicas downstream.

A réplica de primeiro nível continua sendo uma standby durante a operação normal. Ela
assume o papel de primary somente depois de uma promoção controlada ou de um failover.
Enquanto não é promovida, o termo mais preciso é relay, cascading standby ou upstream
standby, e não um segundo primary.

## Primary, replica e upstream

O primary possui a autoridade de escrita. A réplica recebe e aplica mudanças de acordo
com o protocolo do produto. Quando uma réplica também aceita conexões de replicação de
outras réplicas, ela possui duas responsabilidades:

1. consumir alterações do seu upstream;
2. disponibilizar essas alterações aos seus downstreams.

| Papel | Recebe alterações de | Envia alterações para | Responsabilidade |
| --- | --- | --- | --- |
| Primary | clientes de escrita | réplicas de primeiro nível | Autoridade de escrita e origem do log. |
| Relay ou upstream standby | primary ou outro upstream | réplicas downstream | Aplicar e retransmitir o log. |
| Downstream standby | relay ou primary | nenhum membro de replicação | Aplicar o log e atender leituras ou failover. |

Uma topologia direta possui uma conexão do primary para cada réplica. Uma topologia em
cascata organiza os membros em níveis, com um relay atendendo várias réplicas próximas.
O ganho principal é limitar conexões e tráfego direto no primary, especialmente quando
as réplicas estão em outra região, rede ou zona de custo diferente.

## Quando a cascata ajuda

Uma réplica upstream pode reduzir o fan-out de conexões no primary, concentrar o tráfego
entre regiões e criar um ponto de distribuição próximo dos consumidores. Isso é útil
quando há muitas réplicas de leitura, quando a origem tem limites de conexões ou quando
o custo de transportar o log pela rede é diferente entre os sites.

O ganho não é uma redução mágica do volume total de dados. Cada downstream ainda precisa
receber e aplicar as alterações. A cascata muda o caminho e o domínio do tráfego, não a
quantidade de WAL ou eventos que cada cópia precisa processar.

Uma topologia direta pode ser mais simples e ter menor atraso acumulado. A cascata fica
mais interessante quando a redução de fan-out, a proximidade geográfica ou a separação
de redes compensa a dependência adicional.

## Topologias

| Topologia | Conexões no primary | Dependência principal | Uso típico |
| --- | ---: | --- | --- |
| Direta | Uma por réplica | Primary | Poucas réplicas e menor complexidade. |
| Um relay | Uma por relay | Primary e relay | Distribuição regional ou redução de fan-out. |
| Vários relays | Uma por grupo de distribuição | Primary, relay de cada grupo | Sites, regiões ou domínios de falha diferentes. |
| Cadeia longa | Uma por nível | Todos os upstreams anteriores | Cenários específicos, com atenção ao lag acumulado. |

Cada standby normalmente possui um único upstream. Uma árvore pode ter vários downstreams
por relay, mas o desenho deve evitar uma dependência única quando o relay for crítico.
Em alguns ambientes é útil manter um caminho de reconfiguração direta para situações de
emergência, desde que a mudança não crie duas fontes de escrita ou duas autoridades de
replicação ao mesmo tempo.

## Promoção do relay

Durante um failover, o relay mais atualizado pode ser promovido a novo primary. As
réplicas downstream precisam então reconhecer a nova timeline ou o novo identificador
de autoridade e passar a consumir do promoted primary. Isso é diferente de simplesmente
continuar retransmitindo dados enquanto o relay ainda é standby.

O processo seguro precisa definir:

- como o primary antigo é isolado, usando fencing ou uma autoridade externa;
- como o melhor candidato é escolhido considerando o lag;
- como o endpoint de escrita passa ao promoted primary;
- como downstreams alteram seu upstream;
- como clientes descartam conexões antigas;
- como o antigo primary é reconstruído antes de voltar ao grupo;
- como divergências de timeline são detectadas e corrigidas.

Sem fencing, a promoção pode produzir split brain. Sem reconfiguração das réplicas, o
downstream pode continuar consultando um nó antigo ou ficar sem origem. Sem uma política
de recuperação, uma promoção manual pode parecer concluída enquanto parte da topologia
continua em uma linha de dados diferente.

## PostgreSQL

O PostgreSQL documenta essa arquitetura como cascading replication. Um standby pode
aceitar conexões de replicação e transmitir registros WAL para outros standbys. O
standby que recebe e envia é chamado de cascading standby. Os membros mais próximos do
primary são upstream e os mais distantes são downstream.

No downstream, `primary_conninfo` aponta para o cascading standby. O relay precisa estar
configurado para aceitar conexões, com `max_wal_senders`, `hot_standby` e autenticação
adequados. A documentação do PostgreSQL informa que a cascata pode reduzir conexões
diretas no primary e o uso de banda entre sites.

No PostgreSQL atual, a replicação em cascata é assíncrona. Configurações de replicação
síncrona do primary não transformam automaticamente o caminho cascaded em uma confirmação
síncrona de ponta a ponta. O primary também não conhece downstreams como candidatos
diretos de confirmação síncrona.

O PostgreSQL permite que um cascading standby envie WAL recebido do primary e WAL
restaurado do archive. Por isso, uma interrupção da conexão upstream não interrompe
imediatamente o downstream se ainda houver WAL disponível para envio. Essa característica
reduz algumas interrupções, mas não elimina o risco de esgotar o WAL disponível.

Quando um upstream é promovido, downstreams podem continuar a partir da nova timeline
com `recovery_target_timeline` configurado como `latest`, que é o padrão documentado.
Isso não substitui a automação de promoção, endpoint e fencing.

## WAL, slots e retenção

Cada nível precisa acompanhar o ritmo de geração e aplicação do WAL. O operador deve
observar o atraso entre geração, envio, recebimento e replay. Um relay pode estar
conectado ao primary e ainda assim não conseguir alimentar seus downstreams na mesma
velocidade.

Replication slots ajudam a impedir que o primary remova WAL antes de um consumidor ter
recebido os segmentos necessários. Em uma árvore, slots ou mecanismos equivalentes devem
ser dimensionados para cada consumidor, inclusive os relays. Um relay parado pode fazer
o upstream reter WAL por tempo indefinido e preencher o disco.

Use limites de retenção, alertas e procedimentos de remoção de slots abandonados. Não
apague um slot apenas para liberar espaço sem confirmar que o consumidor será
reinicializado ou recuperado por outro caminho. A perda do WAL necessário pode obrigar
um novo base backup para reconstruir a réplica.

## Custos e failure modes

O principal custo da cascata é a dependência adicional. Um relay indisponível pode
isolar todos os downstreams, mesmo que o primary esteja saudável. O atraso também pode
se acumular em cada nível, especialmente quando o relay está ocupado com consultas,
replay, compressão, armazenamento lento ou limites de rede.

Outros problemas comuns são:

- relay configurado para receber, mas não para enviar;
- autenticação de replicação permitida no primary, mas não no relay;
- `max_wal_senders` insuficiente;
- downstream apontando para um endpoint antigo depois da promoção;
- timeline divergente depois de failover;
- slots esquecidos retendo WAL;
- relay usado como ponto único de falha sem caminho de recuperação;
- leitura do downstream sem considerar read-after-write e lag.

## Não é consenso nem backup

Uma árvore de primary e réplicas continua sendo uma topologia de replicação. Ela não
fornece, por si só, consenso entre múltiplos escritores nem a eleição segura de uma
autoridade. A promoção pode ser coordenada por um operador, um controlador ou outro
protocolo, mas o mecanismo de cascata não resolve essa decisão.

Também não é backup. Um erro lógico, exclusão acidental ou corrupção que chega ao
primary pode percorrer toda a árvore. Mantenha backups independentes, retenção histórica
e testes de restauração fora do domínio de falha da replicação.

## Relações

- [Replicação](replicacao.md) apresenta primary, réplicas, lag e failover.
- [Quorum e consenso](quorum-e-consenso.md) diferencia maioria, consenso e replicação.
- [Clustering, redundância e distribuição](clustering-redundancia-e-distribuicao.md)
  compara topologias de bancos.
- [PostgreSQL e capacidade de WAL](postgresql-wal-e-capacidade.md) trata retenção,
  armazenamento e risco de preencher o disco.
- [Backup e restauração](../confiabilidade/backup/backup.md) trata recuperação histórica.

## Fontes

- [PostgreSQL, log-shipping standby servers](https://www.postgresql.org/docs/current/warm-standby.html)
- [PostgreSQL, cascading replication](https://www.postgresql.org/docs/current/warm-standby.html#CASCADING-REPLICATION)
- [PostgreSQL, streaming replication](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION)
- [PostgreSQL, replication slots](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION-SLOTS)
