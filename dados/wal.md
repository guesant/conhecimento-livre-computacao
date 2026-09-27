# Write-Ahead Logging

WAL é o log de escrita antecipada usado por bancos como PostgreSQL para proteger a integridade. A descrição da alteração é persistida no log antes que as páginas de tabela e índice sejam consideradas persistidas. Em uma falha, o banco refaz alterações confirmadas que ainda não chegaram às páginas de dados.

WAL participa de replicação física, arquivamento contínuo, recuperação para um ponto no tempo, backup físico online e decodificação lógica. A sequência precisa estar disponível desde o backup base para que o PITR funcione.

WAL não é backup completo, histórico editorial, auditoria legível por usuário ou mecanismo de recuperação de uma única linha. Uma exclusão confirmada é uma alteração legítima e normalmente será propagada para réplicas. Recuperar o estado anterior exige PITR, backup lógico, revisão de domínio ou outra cópia adequada.

O crescimento do WAL precisa ser acompanhado por arquivamento, replication slots, réplicas atrasadas, operações grandes, retenção e espaço em disco. A política deve definir limites e alertas antes que o volume preencha o armazenamento.

## Fontes primárias

- [PostgreSQL, Write-Ahead Logging](https://www.postgresql.org/docs/current/wal-intro.html)
- [PostgreSQL, MVCC](https://www.postgresql.org/docs/current/mvcc-intro.html)
- [PostgreSQL, continuous archiving e PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [PostgreSQL, logical decoding](https://www.postgresql.org/docs/current/logicaldecoding.html)
