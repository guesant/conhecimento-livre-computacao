# Mapa de mudanças de banco

Alterar um banco em produção envolve schema, concorrência e transações. Uma migration curta pode esperar por uma transação antiga, enfileirar consultas e esgotar o pool de conexões.

- [Migrações de schema](migracoes-schema.md) trata de DDL, expand and contract, backfill e alteração online.
- [Locks](locks.md) trata de locks de tabela, linha, metadados, intervalo, intenção e advisory.
- [Transações](modos-de-transacao.md) trata de autocommit, isolamento, savepoints, DDL e rollback.

O plano precisa considerar versão do banco, engine, topologia, réplicas, lag, timeout, idempotência e rollback. Uma operação "online" ainda pode esperar por um lock exclusivo no início ou no commit.
