# Locks de banco de dados

Um lock coordena operações concorrentes sobre um recurso. Ele não é sinônimo de transação: uma transação pode adquirir muitos locks, e alguns locks existem fora de uma transação explícita. O efeito correto depende do recurso protegido, da compatibilidade entre modos e do tempo de retenção.

## Locks de tabela e de linha

Locks de tabela protegem uma relação inteira ou uma operação estrutural. Locks de linha protegem registros específicos durante atualizações, exclusões ou leituras que pedem bloqueio. Um lock de tabela pode impedir DDL ou escrita mesmo quando a consulta que o aguarda pretende tocar poucas linhas.

No PostgreSQL, `FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE` e `FOR KEY SHARE` expressam intenções diferentes sobre as linhas. No InnoDB, a combinação de locks de registro, gap e next-key também pode proteger intervalos de índices e impedir inserções concorrentes.

## Metadata, intervalo e intenção

Locks de metadata aparecem em alterações de schema e podem esperar por sessões que mantêm uma tabela aberta. Locks de intervalo protegem uma faixa indexada, mesmo quando não existe um registro correspondente. Locks de intenção permitem que o mecanismo combine proteção em níveis diferentes, como tabela e linha.

## Advisory locks

Advisory locks são contratos definidos pela aplicação. Eles são úteis para eleger um único worker, serializar uma tarefa ou evitar que duas rotinas processem o mesmo recurso. A aplicação precisa definir a chave, a duração e o comportamento quando o lock não estiver disponível. O banco não conhece o significado da chave.

## Diagnóstico

Investigue sessões bloqueadoras e bloqueadas, duração da transação, consulta atual, idade da transação e plano de execução. Defina timeouts de lock para falhar de modo previsível, mas não use o timeout como substituto para reduzir transações longas ou corrigir a ordem de aquisição.

## Fontes

- [PostgreSQL, concorrência e locks](https://www.postgresql.org/docs/current/explicit-locking.html)
- [PostgreSQL, locking clauses](https://www.postgresql.org/docs/current/sql-select.html)
- [MySQL, locks InnoDB](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking.html)
- [MariaDB, locks](https://mariadb.com/kb/en/metadata-locking/)
