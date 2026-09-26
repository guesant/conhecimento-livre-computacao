# Checkpoints no PostgreSQL

Checkpoint é um ponto de recuperação interno do PostgreSQL. Durante um checkpoint, o
servidor garante que páginas de dados modificadas que precisam estar persistidas sejam
escritas no armazenamento e registra no WAL informações que permitem ao processo de
recovery começar de uma posição conhecida depois de uma falha.

Checkpoint não é backup, snapshot nem commit. Um commit confirma uma transação segundo
as regras de durabilidade configuradas. Um checkpoint organiza a persistência das páginas
e reduz o trecho de WAL que precisa ser reaplicado durante a recuperação. Um backup é uma
cópia recuperável que precisa sobreviver ao problema contra o qual foi projetada.

## O que acontece em um checkpoint

O PostgreSQL mantém páginas modificadas em buffers de memória. Antes de uma página de
dados ser considerada segura para recovery, o WAL correspondente precisa estar persistido
segundo as regras do servidor. O checkpoint percorre esse estado e faz com que páginas
necessárias sejam gravadas nos arquivos de dados, registra o checkpoint no WAL e atualiza
o estado usado na próxima inicialização.

O processo não precisa escrever todas as páginas do cluster a cada vez. Ele trabalha sobre
as páginas sujas e sobre o estado acumulado desde o checkpoint anterior. A quantidade de
dados, o ritmo de escrita, o cache, o storage e a estratégia de sincronização influenciam
o tempo e o volume de I/O.

Um checkpoint reduz o trabalho potencial de crash recovery, mas gera escrita adicional.
Se muitos dados forem descarregados em uma janela curta, a latência da aplicação pode
aumentar. Se o trabalho for espalhado ao longo do intervalo, o pico tende a ser menor,
mas o PostgreSQL precisa manter mais WAL e páginas sujas em circulação.

## O que dispara checkpoints

Checkpoints podem ser iniciados por:

- expiração de `checkpoint_timeout`;
- crescimento de WAL até o limite operacional de `max_wal_size`;
- shutdown que precisa deixar o cluster em estado consistente;
- execução explícita de `CHECKPOINT`;
- ações administrativas ou de recuperação que exigem um novo ponto de controle.

`max_wal_size` é um alvo flexível, não um limite físico absoluto. Uma transação longa,
uma carga intensa, uma réplica atrasada, retenção de slot ou falha de arquivamento podem
fazer o armazenamento crescer além da expectativa antes que o PostgreSQL consiga reciclar
segmentos.

## Checkpoint e restartpoint

Em um primary, o processo executa checkpoints. Em uma réplica em recovery, ele executa
restartpoints, que cumprem papel semelhante para que a réplica possa reiniciar a
recuperação de uma posição recente. Restartpoints dependem da chegada de registros de
checkpoint pelo WAL e podem ocorrer com frequência diferente da origem.

Isso importa para operação de réplicas: um standby pode estar recebendo WAL e ainda ter
um ritmo de escrita, replay ou flush incompatível com a origem. Checkpoint não prova que a
réplica está atualizada nem que ela é uma candidata segura para promoção.

## Configurações principais

Os nomes e defaults devem ser verificados na versão instalada, mas os papéis são:

| Parâmetro | Papel | Trade-off |
| --- | --- | --- |
| `checkpoint_timeout` | Intervalo máximo entre checkpoints automáticos | Intervalo menor reduz recovery potencial, mas aumenta frequência de escrita. |
| `max_wal_size` | Quantidade aproximada de WAL que orienta a criação de checkpoint | Valor maior reduz checkpoints por volume, mas exige espaço para WAL e pode aumentar recovery. |
| `checkpoint_completion_target` | Fração do intervalo usada para espalhar a escrita | Valor alto reduz picos, mas mantém o trabalho ativo por mais tempo. |
| `full_page_writes` | Registra imagens completas de páginas após checkpoints para proteger contra torn writes | Desligar reduz WAL, mas aumenta risco de corrupção após falha de página parcial. |
| `checkpoint_flush_after` | Orienta quando dados escritos devem ser enviados ao storage | Pode reduzir rajadas de flush, dependendo do kernel e do dispositivo. |

Não escolha parâmetros olhando apenas para a quantidade de checkpoints. O objetivo é
equilibrar taxa de WAL, latência, capacidade, tempo de recovery e comportamento do
storage.

## Checkpoint fast e spread

Um checkpoint pode ser executado de forma espalhada ao longo do intervalo normal ou de
forma rápida quando uma operação precisa encerrá-lo sem esperar. Checkpoint rápido grava
mais páginas em menos tempo e pode causar uma rajada de I/O.

Uma ferramenta de backup pode solicitar um checkpoint rápido ou espalhado como parte da
preparação de um backup base. Isso não transforma o checkpoint em uma cópia e não elimina
a necessidade de arquivar o WAL correspondente.

## Checkpoint e backup

Um backup físico precisa de uma base consistente e de WAL suficiente para recuperar as
alterações necessárias depois dela. O checkpoint ajuda o servidor a manter um ponto de
recuperação bem definido, mas a validade do backup depende do método de cópia, do
arquivamento do WAL, da retenção e do teste de restauração.

Um snapshot de volume tirado sem coordenação com o banco não deve ser tratado como backup
consistente. O storage pode capturar páginas em momentos diferentes e não saber se o WAL
necessário está preservado. Use a integração oficial da ferramenta de backup ou uma
estratégia de snapshot que coordene o estado do banco e a cadeia de WAL.

## Checkpoint e WAL

Checkpoints ajudam a limitar a distância de recovery, mas não são o único fator do
crescimento de `pg_wal`. Arquivamento falho, replication slots, réplicas atrasadas,
backfills e transações volumosas também retêm ou produzem WAL.

Uma política que reduz agressivamente checkpoints pode conservar mais WAL e aumentar o
tempo de recovery. Uma política que força checkpoints com muita frequência pode aumentar
I/O e produzir latência. A decisão deve ser baseada em métricas de geração de WAL,
`checkpoint_write_time`, `checkpoint_sync_time`, tempo de recovery e latência da aplicação.

## Observabilidade

As estatísticas relacionadas a checkpoint mudam entre versões. Em versões que expõem a
view dedicada, consulte `pg_stat_checkpointer`. Em versões anteriores, parte das métricas
fica em `pg_stat_bgwriter`.

Indicadores úteis incluem:

- quantidade de checkpoints por tempo;
- checkpoints iniciados por tempo contra checkpoints solicitados por volume;
- tempo de escrita;
- tempo de sincronização;
- buffers escritos por checkpoint;
- WAL gerado entre checkpoints;
- tempo de recuperação observado em testes;
- latência e saturação do storage durante o ciclo.

Um aumento de `checkpoints_req` em relação aos checkpoints por tempo pode indicar que o
volume de WAL ou a taxa de escrita ultrapassou o planejamento atual. A interpretação deve
considerar alterações de carga, migrations, backfills, criação de índices e comportamento
de réplicas.

## Sintomas de configuração inadequada

Checkpoints frequentes podem causar escrita repetitiva, saturação de I/O e picos de
latência. Checkpoints muito espaçados podem acumular páginas sujas, conservar muito WAL e
prolongar a recuperação após crash. Em storage lento, aumentar o tamanho sem medir pode
apenas transferir a latência para outro ponto do ciclo.

Não use `CHECKPOINT` repetidamente para tentar liberar espaço em `pg_wal`. O espaço só
pode ser reciclado quando nenhum backup, réplica, slot ou consumidor de arquivamento ainda
precisa dos segmentos. Investigue o consumidor que está retendo o WAL.

## Relações

- [PostgreSQL: WAL e capacidade](postgresql-wal-e-capacidade.md) trata arquivamento, slots,
  réplicas atrasadas e crescimento do volume.
- [Tipos de backup](../confiabilidade/backup/tipos-de-backup.md) diferencia cópias full,
  differential, incremental, físicas, lógicas e WAL.
- [Locks e transações no PostgreSQL](postgresql-locks-e-transacoes.md) explica o efeito de
  transações longas sobre vacuum, DDL e concorrência.
- [pgBackRest](../ferramentas/bancos/pgbackrest.md) trata backup base, retenção e restauração.

## Fontes

- [PostgreSQL, WAL configuration](https://www.postgresql.org/docs/current/wal-configuration.html)
- [PostgreSQL, reliability and the write-ahead log](https://www.postgresql.org/docs/current/wal-intro.html)
- [PostgreSQL, monitoring statistics](https://www.postgresql.org/docs/current/monitoring-stats.html)
- [PostgreSQL, continuous archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
