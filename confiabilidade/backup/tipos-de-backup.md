# Tipos de backup

Os termos full, differential e incremental descrevem como uma cópia se relaciona com
outras cópias. Eles não dizem, sozinhos, se o backup é físico ou lógico, se pode restaurar
um ponto no tempo ou se está protegido contra a perda do servidor original.

Uma estratégia deve combinar tipo de cópia, frequência, retenção, localização, segurança,
RPO, RTO e teste de restauração. Uma cadeia curta e rápida de restaurar pode ser melhor
que uma cadeia muito econômica que ninguém consegue reconstruir sob pressão.

## Backup full

Um backup full contém uma representação completa do escopo escolhido no momento da cópia.
Ele é a base mais simples para restauração porque não depende de outra cópia do mesmo
conjunto.

O custo é maior em leitura, rede, storage e tempo de execução. Um backup full também pode
gerar carga no banco e consumir espaço temporário. Full não significa imutável, externo ou
testado. Um único full apagado, corrompido ou armazenado no mesmo host não é uma política
de recuperação suficiente.

## Backup differential

Um backup differential contém as mudanças ocorridas desde o último full correspondente.
Cada diferencial tende a crescer até que um novo full seja criado. Para restaurar, a cadeia
normal precisa do full e do diferencial escolhido.

O diferencial troca espaço por simplicidade: normalmente exige apenas duas peças na
restauração e pode ser mais rápido que reaplicar muitos incrementais. Ele pode crescer
consideravelmente quando o próximo full é adiado.

O significado de differential precisa ser confirmado na ferramenta. Alguns produtos usam
o termo para uma relação diferente, e a unidade pode ser arquivo, página, bloco, objeto
ou WAL. No pgBackRest, o differential depende do full mais recente da mesma stanza.

## Backup incremental

Um backup incremental contém somente o que mudou desde a referência incremental definida
pelo produto. Essa referência pode ser o último full, o último differential ou o último
incremental.

Incremental reduz a janela e o volume de cada cópia, mas cria uma cadeia mais sensível a
perdas. Para restaurar, pode ser necessário o full e todos os incrementais intermediários,
ou o conjunto específico que a ferramenta documentar.

No pgBackRest, um incremental depende do backup mais recente, independentemente de ele ser
full, differential ou incremental. Não se deve apagar uma peça da cadeia apenas porque o
nome da cópia parece antigo.

## Log de transações e WAL

O log de transações registra alterações em uma sequência que pode ser reaplicada. No
PostgreSQL, o WAL arquivado, combinado com um backup base, permite recuperação para um
ponto no tempo quando o arquivamento e a retenção foram mantidos corretamente.

WAL não é substituto de backup base. Ele descreve mudanças e depende de uma base a partir
da qual essas mudanças possam ser reaplicadas. Também não é um backup histórico por si só
se os segmentos foram reciclados ou se o destino de arquivamento não é recuperável.

## Backup físico e lógico

Backup físico copia o armazenamento ou uma representação física do cluster. Ele costuma
ser adequado para recuperação completa, réplica física e PITR, mas depende da versão,
arquitetura, sistema operacional, extensão e compatibilidade do cluster.

Backup lógico exporta objetos e dados em comandos ou registros lógicos, como ocorre com
`pg_dump`. Ele permite restaurar tabelas, schemas ou dados selecionados e facilita
migrações entre versões, mas pode ser muito mais lento para grandes volumes e não
representa todo o estado físico necessário para um failover imediato.

Um backup físico não deve ser usado como se fosse uma exportação seletiva. Um backup
lógico não deve ser tratado como uma réplica pronta para assumir o tráfego.

## Snapshot de storage

Snapshot registra o estado de volumes ou objetos conforme a semântica do storage. Ele pode
ser rápido e útil para recuperação operacional, mas precisa de coordenação com o banco.
Snapshot de um volume sem garantir consistência entre dados, WAL, tablespaces e metadados
pode produzir uma cópia que não restaura.

Snapshots também herdam, em muitos casos, o domínio de falha, as credenciais e a política
de exclusão do storage original. Use cópia externa, imutabilidade e teste de restauração
quando a ameaça incluir ransomware ou perda do cluster.

## Cadeias de restauração

Uma cadeia pode ser descrita assim:

```text
full -> differential -> WAL
full -> incremental -> incremental -> WAL
full -> differential -> incremental -> WAL
```

O desenho exato depende da ferramenta. O importante é saber quais artefatos são necessários
para cada ponto de restauração, qual é o primeiro backup válido da cadeia, quando os WAL
podem ser descartados e como verificar a integridade sem esperar um incidente.

Uma política deve responder:

- qual full é a raiz de cada diferencial ou incremental;
- quais arquivos ou objetos são necessários para restaurar um ponto específico;
- qual é o tempo para baixar, preparar e aplicar a cadeia;
- como o sistema detecta uma peça ausente ou corrompida;
- como uma cadeia antiga é expirada sem quebrar outra ainda válida;
- onde existe uma cópia independente do cluster e do repositório primário.

## Full, differential e incremental no PostgreSQL

No PostgreSQL, `pg_basebackup` produz uma base física. Ferramentas como pgBackRest e
Barman acrescentam retenção, compressão, verificação, catalogação, cópias diferenciais ou
incrementais e integração com WAL. `pg_dump` e `pg_dumpall` operam no nível lógico.

O PostgreSQL não transforma automaticamente qualquer cópia de diretório em um backup
restaurável. A cópia precisa respeitar consistência, tablespaces, WAL, permissões,
extensões e o método de recuperação escolhido.

Para uma estratégia com PITR, combine um backup base físico, arquivamento contínuo do WAL,
retenção suficiente, destino independente e teste de recuperação. Para migração seletiva
ou mudança de major, um dump lógico pode ser mais apropriado, mesmo que seja mais lento.

## Comparação operacional

| Tipo | Volume de cada cópia | Dependências na restauração | Uso comum |
| --- | --- | --- | --- |
| Full | Alto | A própria cópia | Base de recuperação e simplificação da cadeia. |
| Differential | Cresce desde o full | Full mais recente e diferencial escolhido | Restauração com menos peças e custo intermediário. |
| Incremental | Baixo por execução | Full e cadeia exigida pela ferramenta | Janelas curtas e grande volume de dados. |
| WAL ou log | Relativo ao volume de alterações | Backup base e sequência contínua | PITR e recuperação de alterações após a base. |
| Snapshot | Depende do storage e dos blocos alterados | Snapshot, storage e coordenação do banco | Recuperação rápida ou cópia operacional. |
| Lógico | Depende dos objetos exportados | Arquivo lógico e compatibilidade do destino | Migração seletiva, auditoria e mudança de versão. |

Não escolha incremental somente porque ele é menor. O tempo total de restauração, a
complexidade de validação e o risco de uma cadeia incompleta fazem parte do custo.

## Relação com checkpoints

Checkpoint ajuda o PostgreSQL a organizar a recuperação após crash, mas não finaliza uma
cadeia de backup. O backup físico ainda precisa do método correto de cópia e do WAL
necessário. Consulte [Checkpoints no PostgreSQL](../../dados/postgresql-checkpoints.md) e
[PostgreSQL: WAL e capacidade](../../dados/postgresql-wal-e-capacidade.md).

## Fontes

- [PostgreSQL, backup e restore](https://www.postgresql.org/docs/current/backup.html)
- [PostgreSQL, continuous archiving e PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [PostgreSQL, `pg_basebackup`](https://www.postgresql.org/docs/current/app-pgbasebackup.html)
- [PostgreSQL, `pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html)
- [pgBackRest, tipos de backup](https://pgbackrest.org/user-guide.html#backup-types)
