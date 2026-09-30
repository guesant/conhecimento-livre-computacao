# pgBackRest

pgBackRest é uma ferramenta de backup e recuperação para PostgreSQL. Ela organiza stanzas, repositórios, backups full, differential e incremental, retenção, compressão, criptografia, arquivamento de WAL e restauração, inclusive recuperação para um ponto no tempo.

pgBackRest não é uma réplica de leitura nem um substituto para streaming replication. Uma réplica mantém continuidade ou aproxima o estado atual; pgBackRest preserva cópias e WAL suficientes para recuperar um cluster depois de corrupção, exclusão lógica, erro operacional ou perda de infraestrutura.

## Modelo de funcionamento

Uma stanza identifica um cluster e sua configuração de backup. O repositório pode estar no mesmo host, em outro servidor ou em storage compatível com objeto. O repositório precisa pertencer a um domínio de falha diferente quando a meta for sobreviver à perda do servidor PostgreSQL.

Um backup full é independente para restauração. Um differential depende do full correspondente. Um incremental depende da cadeia de backups anteriores. A retenção deve preservar uma cadeia inteira que seja realmente restaurável, não somente apagar arquivos antigos pelo nome.

O WAL arquivado completa o caminho para PITR. Depois de restaurar o backup base, o PostgreSQL reproduz os segmentos WAL até o momento escolhido. O conjunto de WAL necessário depende do backup e do ponto de recuperação; uma limpeza sem entender a cadeia pode tornar um backup aparentemente existente inutilizável.

## Arquivamento de WAL

O PostgreSQL entrega segmentos concluídos para `archive_command` ou `archive_library`. O pgBackRest pode ser usado nesse caminho para enviar os segmentos ao repositório. O comando de arquivamento só deve retornar sucesso quando o segmento estiver realmente persistido no destino.

Se o arquivamento falhar, o PostgreSQL tenta novamente e conserva mais segmentos em `pg_wal`. Isso é uma proteção de integridade, não um vazamento que deve ser resolvido apagando arquivos manualmente. Se o destino ficar indisponível ou sem espaço, o volume local pode ser preenchido até o PostgreSQL entrar em shutdown de emergência.

Configure alertas para a falha de arquivamento e para o crescimento do `pg_wal`. Um backup que ainda existe no repositório não prova que o arquivamento corrente está saudável.

## Retenção

A retenção precisa responder duas perguntas diferentes:

- por quanto tempo deve ser possível restaurar um backup base;
- até qual ponto no tempo o WAL deve estar disponível.

Retenção de backup e retenção de archive precisam ser compatíveis com o RPO, o RTO, a cadeia de dependências e a capacidade do repositório. Repositório cheio não deve ser resolvido com uma exclusão manual de WAL; ajuste a política de retenção e execute a expiração pelo próprio pgBackRest depois de confirmar que os backups restantes podem ser restaurados.

Mantenha espaço livre reservado no volume do banco e no repositório. O crescimento diário de WAL deve ser medido em períodos normais e durante jobs de carga, índices, backfills e migrations, porque o pico pode ser várias vezes maior que a média.

## Verificação e restauração

Operações importantes incluem:

- `stanza-create` para registrar a configuração inicial;
- `check` para verificar a configuração e o caminho de arquivamento;
- `info` para inspecionar backups e cadeias;
- `backup` para criar cópias;
- `expire` para aplicar retenção;
- `verify` para validar o conteúdo do repositório;
- `restore` para recuperar o cluster.

O comando não substitui um teste de restauração. Restaure periodicamente em um cluster separado, confirme permissões, schema, dados, extensões, WAL necessário, tempo total e comportamento da aplicação. Registre o LSN e o horário alcançado para comparar com o RPO pretendido.

## Segurança

O repositório contém o banco inteiro e seus WALs. Use criptografia do repositório, credenciais de menor privilégio, separação de acesso entre operação e aplicação, retenção contra exclusão acidental quando disponível e logs sem segredos.

O arquivo de configuração deve proteger chaves, paths e credenciais. Um repositório no mesmo disco do PostgreSQL pode simplificar o teste, mas não oferece proteção suficiente contra perda do host, corrupção do volume ou ransomware.

## WAL e capacidade

O diretório `pg_wal` pode crescer por falha de arquivamento, slot abandonado, réplica atrasada, backfill, migration, índice ou retenção necessária para PITR. O diagnóstico detalhado, incluindo consultas para `pg_stat_archiver`, `pg_replication_slots` e `pg_stat_replication`, está em [PostgreSQL: WAL e capacidade](../../dados/postgresql-wal-e-capacidade.md).

Não remova arquivos manualmente de `pg_wal`, não desligue o arquivamento para esconder o crescimento e não remova slots sem identificar seus consumidores. Corrija a causa, confirme que o WAL voltou a ser reciclado e valide que a cadeia de backup continua restaurável.

## Relações

- [Backup do CloudNativePG](../../confiabilidade/backup/cloudnative-pg.md) relaciona backup base, WAL e PITR.
- [Replicação](../../dados/replicacao.md) explica réplicas, lag e failover.
- [PostgreSQL: `pg_stat`, índices e otimização](../../dados/postgresql-pg-stat-indices-e-otimizacao.md) cobre estatísticas, I/O e observabilidade de consultas.
- [Migrações de schema, locks e transações](../../dados/migracoes-schema-locking.md) trata migrations que geram carga, locks e WAL.

## Fontes

- [PostgreSQL, continuous archiving e PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [PostgreSQL, configuração de WAL e replicação](https://www.postgresql.org/docs/current/runtime-config-replication.html)
- [PostgreSQL, replication slots](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION-SLOTS)
- [PostgreSQL, estatísticas de slots](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-SLOTS)
- [pgBackRest, User Guide](https://pgbackrest.org/user-guide.html)
- [Pgpool-II, documentação oficial](https://www.pgpool.net/docs/latest/en/html/)
