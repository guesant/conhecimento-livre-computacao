# Replicação

Replicação mantém uma ou mais cópias de um estado para aumentar disponibilidade, permitir
failover, distribuir leituras ou aproximar dados de consumidores. Neste documento,
`primary` é o componente que recebe a autoridade de escrita e `replica` é uma cópia que
recebe alterações conforme um protocolo de replicação.

Os nomes master e slave devem ser evitados. Além de serem menos precisos, não explicam se
uma instância é somente leitura, candidata a failover, síncrona, assíncrona ou uma fonte
de leitura derivada.

## Primary e replicas

Em uma topologia primary-replica, as escritas são direcionadas ao primary. Replicas
recebem o log ou alterações e podem atender leituras. O roteador de conexão precisa saber
quando uma réplica é elegível para leitura e quando uma troca de primary ocorreu.

Uma réplica pode ser:

- síncrona, quando a confirmação depende de uma cópia definida;
- assíncrona, quando a origem confirma antes de todas as cópias receberem a alteração;
- somente leitura, quando não pode aceitar alterações locais;
- candidata, quando pode ser promovida após uma falha;
- lógica, quando recebe mudanças em entidades ou operações selecionadas;
- física, quando reproduz estruturas ou páginas do armazenamento conforme o mecanismo.

Os termos variam entre produtos. Consulte a semântica do sistema antes de assumir que
"replica" significa failover automático ou consistência imediata.

## Lag e read-after-write

Em replicação assíncrona, uma leitura na réplica pode não ver uma escrita recém-confirmada
no primary. Esse lag pode ser pequeno em operação normal e crescer quando a rede, disco,
CPU ou consumidor de WAL está sob pressão.

Se o usuário precisa ver imediatamente sua própria alteração, leia do primary, use uma
réplica que tenha alcançado uma posição mínima ou carregue uma garantia de leitura. Uma
aplicação que alterna aleatoriamente entre primary e replicas pode produzir resultados
aparentemente regressivos.

## Failover

Promover uma réplica exige decidir se ela possui todas as alterações confirmadas, como
redirecionar clientes, como impedir que o primary antigo volte a escrever e como recuperar
o atraso perdido. Fencing evita split brain, no qual dois nós aceitam escritas como
autoridade.

Failover automático reduz tempo de recuperação, mas pode promover uma cópia atrasada ou
tomar uma decisão errada durante uma partição. A política precisa definir quorum, lease,
DNS, conexões antigas, revalidação de credenciais e como o nó antigo será reintegrado.

Uma réplica também pode ser configurada como upstream de outras réplicas. Essa é a
[replicação em cascata](replicacao-em-cascata.md): o relay recebe alterações do primary
e as disponibiliza aos downstreams. Se o relay for promovido, os downstreams precisam
ser reconfigurados para acompanhá-lo como novo primary.

## Replicação não é backup

Uma alteração errada, `DELETE`, corrupção lógica ou ransomware pode ser replicado para
todas as cópias. Backup preserva pontos históricos e permite voltar antes do incidente.
Snapshot pode acelerar recuperação, mas continua sujeito à retenção e ao domínio de falha
do storage onde está guardado.

Replicação protege principalmente continuidade e disponibilidade; backup protege
recuperação histórica. Uma arquitetura madura pode precisar dos dois.

## Replicação e transações

Uma confirmação no primary garante propriedades da transação naquele banco e naquela
configuração. Ela não garante que uma API externa, uma réplica assíncrona, um cache ou um
consumidor de evento já tenha observado a alteração.

Ao publicar uma alteração para outros componentes, use outbox, eventos duráveis ou uma
estratégia explícita de reconciliação. Consumidores devem tolerar atraso, duplicação e
reordenação quando essas propriedades fizerem parte do transporte.

## Métricas e operação

Monitore lag por tempo e posição, taxa de replay, WAL ou log acumulado, atraso de
consumidores, estado de conexão, erros de aplicação, capacidade de disco e elegibilidade
para failover. Teste promoção, perda de rede, atraso de disco, retorno do primary antigo
e restauração a partir de backup.

Não direcione leituras para qualquer réplica apenas porque ela está conectada. Verifique
se está saudável, autorizada, suficientemente atualizada e capaz de atender o contrato
da operação.

## Relações

- [Replicação para continuidade](../confiabilidade/backup/replicacao.md) diferencia
  disponibilidade de backup.
- [Transações e ACID](transacoes-acid.md) define o limite da confirmação local.
- [Cache](cache.md) trata cópias derivadas, não cópias autoritativas.
- [Backup](../confiabilidade/backup/backup.md) trata pontos históricos e restauração.

## Fontes

- [PostgreSQL, alta disponibilidade](https://www.postgresql.org/docs/current/high-availability.html)
- [PostgreSQL, warm standby](https://www.postgresql.org/docs/current/warm-standby.html)
- [PostgreSQL, replicação lógica](https://www.postgresql.org/docs/current/logical-replication.html)
