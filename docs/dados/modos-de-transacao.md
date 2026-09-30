# Transações de banco de dados

Uma transação agrupa operações que precisam obedecer a um contrato de consistência. O banco só consegue garantir esse contrato se a aplicação delimitar corretamente o início, o commit e o rollback, além de escolher um isolamento compatível com a concorrência esperada.

## Autocommit

No modo autocommit, cada statement bem-sucedido é confirmado separadamente. Esse modo é adequado para leituras independentes e alterações simples, mas não protege uma sequência que precisa ser observada como uma unidade. Uma falha entre dois statements pode deixar o processo parcialmente concluído.

## Transação explícita e savepoints

Uma transação explícita permite agrupar leituras e escritas e desfazer tudo quando uma pré-condição falha. Savepoints criam pontos intermediários de retorno, úteis quando uma parte opcional pode falhar sem invalidar o trabalho anterior. Quanto mais longa a transação, maior o tempo de retenção de locks e versões antigas.

## Modos e isolamento

Os níveis de isolamento controlam quais efeitos de outras transações podem ser observados. `Read committed`, `repeatable read`, `snapshot isolation` e `serializable` têm nomes e detalhes diferentes entre bancos. A escolha deve partir do fenômeno que precisa ser evitado, como leitura suja, leitura não repetível, phantom read ou conflito de serialização.

Retries de serialização e deadlock só são seguros quando a unidade de trabalho é idempotente ou pode ser repetida sem duplicar efeitos externos.

## DDL e transações

Alguns bancos executam DDL dentro de transações e outros fazem commit implícito em determinadas operações. Mesmo quando o DDL é transacional, o lock pode durar até o commit. Por isso uma migration deve separar mudanças rápidas de backfills e operações de validação longa.

## Fontes

- [PostgreSQL, controle de concorrência](https://www.postgresql.org/docs/current/mvcc.html)
- [PostgreSQL, níveis de isolamento](https://www.postgresql.org/docs/current/transaction-iso.html)
- [MySQL, níveis de isolamento](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html)
- [MariaDB, transações](https://mariadb.com/kb/en/transactions/)
