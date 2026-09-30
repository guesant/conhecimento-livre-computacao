# Mapa de WAL e capacidade no PostgreSQL

O Write-Ahead Log, ou WAL, registra alterações antes que as páginas de dados sejam consideradas persistidas. Ele permite recuperação após crash, replicação física, arquivamento contínuo e recuperação para um ponto no tempo.

O WAL é necessário, mas não é ilimitado. Uma falha de arquivamento, uma réplica atrasada, um slot abandonado ou uma operação de grande volume pode impedir a reciclagem de segmentos. Quando isso acontece, o diretório `pg_wal` cresce no mesmo volume do cluster e pode preencher o disco rapidamente.

Se o filesystem que contém `pg_wal` ficar cheio, o PostgreSQL pode entrar em shutdown de emergência. A causa não é resolvida removendo arquivos manualmente: a correção precisa liberar o consumidor que está retendo WAL ou restaurar o caminho de arquivamento.

## O ciclo do WAL

O PostgreSQL grava registros em segmentos, normalmente de 16 MB. Sem arquivamento, segmentos antigos podem ser reciclados quando já não são necessários para recuperação local. Com arquivamento, o segmento precisa ser enviado com sucesso ao destino antes de poder ser reutilizado conforme as outras necessidades do cluster.

Streaming replication envia WAL para réplicas. Replication slots fazem uma promessa mais forte: o primary conserva WAL até que o consumidor alcance a posição necessária. Essa proteção evita que o consumidor perca dados, mas um consumidor parado pode reter WAL indefinidamente.

Uma base backup para PITR também cria uma dependência de WAL arquivado. É preciso preservar uma sequência suficiente desde o backup base até o ponto de recuperação desejado. A retenção não pode ser calculada somente olhando o tamanho atual do diretório.

## Fontes de crescimento

### Arquivamento falho

O `archive_command` ou `archive_library` pode falhar por destino indisponível, falta de espaço, credencial inválida, erro de permissão, rede, versão incompatível do pgBackRest ou configuração incorreta. O PostgreSQL tenta novamente e conserva os segmentos locais.

O comando de arquivamento deve retornar sucesso somente quando o segmento estiver realmente armazenado. Retornar zero antes da persistência cria um backup incompleto; retornar erro quando o arquivo idêntico já existe pode causar retry desnecessário. O comportamento precisa ser validado pelo mecanismo escolhido.

### Replication slots

Slots físicos e lógicos retêm WAL por razões diferentes. Um slot físico serve uma réplica. Um slot lógico serve um consumidor de decodificação ou CDC. Um slot que ficou inativo sem um proprietário identificado é um risco de capacidade.

Não remova um slot apenas porque `active` está falso. Antes, confirme se ele pertence a uma réplica que será recuperada, a uma assinatura lógica, a um conector de CDC ou a uma ferramenta de migração. Remover o slot pode obrigar o consumidor a fazer uma cópia inicial novamente.

Quando suportado pela versão, `max_slot_wal_keep_size` pode limitar a retenção causada por slots. O limite é uma barreira de segurança: ao ultrapassá-lo, o consumidor pode perder a posição e precisar de ressincronização. Ele não substitui alertas nem correção do consumidor.

### Réplica atrasada

Uma réplica pode estar conectada e ainda assim não acompanhar o primary. Rede, disco lento, CPU, replay serializado, consultas longas no standby ou conflito com recovery podem aumentar a fila.

Para cada réplica, acompanhe o atraso de envio, escrita, flush e replay. Uma réplica que não é atual o bastante não deve receber leituras que exigem read-after-write nem ser promovida sem avaliar o risco de perda.

### Operações de grande volume

Backfills, `UPDATE` em massa, `DELETE`, criação de índices, migrations e cargas podem gerar muito WAL em pouco tempo. O volume de WAL depende das páginas e índices afetados, não somente da quantidade de linhas lógica.

Divida operações grandes em lotes, limite concorrência, faça commits frequentes, monitore o crescimento e permita pausa. Uma única transação grande também pode atrasar vacuum e dificultar a recuperação se falhar no final.

### Retenção legítima

WAL também cresce porque está sendo preservado corretamente para um backup ou uma política de PITR. A solução não é apagar segmentos até o volume parecer saudável. Primeiro confirme quais backups e pontos de recuperação precisam deles e quais cadeias já expiraram pela política.

## Diagnóstico

### Arquivamento

Consulte o estado do archiver:

```sql
SELECT
  archived_count,
  failed_count,
  last_archived_wal,
  last_archived_time,
  last_failed_wal,
  last_failed_time,
  stats_reset
FROM pg_stat_archiver;
```

`failed_count` crescente, falha recente ou ausência de arquivamento em um sistema que está gerando WAL exigem investigação. Relacione a view com logs do PostgreSQL e do pgBackRest, espaço do destino e permissões do processo.

### Slots

```sql
SELECT
  slot_name,
  slot_type,
  active,
  restart_lsn,
  confirmed_flush_lsn,
  wal_status,
  safe_wal_size,
  inactive_since
FROM pg_replication_slots;
```

`restart_lsn` indica a posição mais antiga que o consumidor ainda pode exigir. Compare essa posição com a posição atual e monitore a diferença ao longo do tempo. Os campos disponíveis variam conforme a versão do PostgreSQL; a consulta deve ser adaptada ao servidor real.

### Réplicas

No primary:

```sql
SELECT
  application_name,
  client_addr,
  state,
  sync_state,
  sent_lsn,
  write_lsn,
  flush_lsn,
  replay_lsn,
  pg_wal_lsn_diff(sent_lsn, replay_lsn) AS bytes_behind
FROM pg_stat_replication;
```

O atraso deve ser medido em bytes e tempo. Também é necessário verificar se o standby recebe dados, grava no disco e reproduz os registros. Uma conexão estabelecida não garante que a réplica esteja saudável ou elegível para failover.

### Volume e taxa

O LSN absoluto não representa espaço. Colete a posição em dois instantes e calcule a diferença, ou monitore o tamanho do volume e do diretório `pg_wal` com uma ferramenta de infraestrutura. A taxa de geração deve ser medida em períodos normais e durante migrations, backfills, jobs e cargas de índice.

Use alertas graduais para:

- crescimento anormal de `pg_wal`;
- falha ou atraso de arquivamento;
- slot antigo ou inativo com retenção crescente;
- réplica com lag acima do contrato;
- repositório pgBackRest próximo do limite;
- volume do cluster próximo de ficar sem espaço.

O alerta precisa chegar antes do limite de emergência. Reserve espaço para logs, checkpoints, temporários, operações de manutenção e a correção do incidente.

## Prevenção

Uma política segura combina:

1. arquivamento testado e observado continuamente;
2. pgBackRest ou mecanismo equivalente com repositório fora do domínio de falha do banco;
3. retenção baseada em RPO, RTO e cadeias restauráveis;
4. inventário de todos os replication slots;
5. limite explícito para retenção por slot quando a versão suportar;
6. alertas de crescimento, falha e espaço;
7. base backups em frequência compatível com o volume de WAL e o tempo de replay;
8. backfills e migrations pausáveis e idempotentes;
9. testes de restauração e de recuperação quando o arquivamento está atrasado;
10. volume e capacidade dimensionados para sobreviver à intervenção sem desligar o banco.

`archive_timeout` pode forçar a troca de segmento em ambientes de baixo tráfego para reduzir a idade do WAL arquivado, mas um valor muito baixo cria muitos segmentos parcialmente preenchidos e aumenta o armazenamento. Use-o somente com uma meta de RPO clara.

## Como responder a crescimento rápido

1. Confirme o crescimento no volume e identifique se o consumo está em `pg_wal`, no repositório ou em ambos.
2. Consulte `pg_stat_archiver` e os logs para verificar falhas de arquivamento.
3. Liste slots e encontre o maior `restart_lsn` retido.
4. Verifique lag de réplicas, consumidores lógicos e conexões de CDC.
5. Identifique migrations, backfills, índices ou jobs iniciados recentemente.
6. Pause o produtor pesado se o RPO e a invariável da operação permitirem.
7. Corrija o arquivamento ou o consumidor antes de remover dados de retenção.
8. Confirme que o WAL volta a ser reciclado e que o backup continua restaurável.
9. Registre o pico, a taxa, a causa e o tempo necessário para recuperação.

Não execute `rm` em `pg_wal`, não desative o arquivamento para esconder o crescimento e não remova slots sem identificar seus consumidores. Se o disco estiver perto do limite, trate a situação como incidente de capacidade e preserve o espaço de emergência.

## Relações

- [pgBackRest](../ferramentas/bancos/pgbackrest.md) cobre backup, archive, retenção e restauração.
- [Backup do CloudNativePG](../confiabilidade/backup/cloudnative-pg.md) relaciona backup base, WAL e PITR.
- [Checkpoints no PostgreSQL](postgresql-checkpoints.md) explica como páginas sujas, WAL e recovery se relacionam.
- [Replicação](replicacao.md) explica lag, failover e cópias do estado.
- [PostgreSQL: `pg_stat`, índices e otimização](postgresql-pg-stat-indices-e-otimizacao.md) cobre observabilidade de consultas e I/O.
- [Migrações de schema, locks e transações](migracoes-schema-locking.md) trata operações que podem gerar carga e WAL.

## Fontes

- [PostgreSQL, continuous archiving e PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [PostgreSQL, configuração de WAL e replicação](https://www.postgresql.org/docs/current/runtime-config-replication.html)
- [PostgreSQL, replication slots](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION-SLOTS)
- [PostgreSQL, estatísticas de replication slots](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-SLOTS)
- [pgBackRest, User Guide](https://pgbackrest.org/user-guide.html)
