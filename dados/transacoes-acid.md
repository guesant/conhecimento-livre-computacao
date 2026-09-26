# Transações e ACID

ACID é o conjunto de propriedades normalmente associado a transações de bancos
relacionais: atomicidade, consistência, isolamento e durabilidade. O modelo ajuda a
descrever o que o banco garante dentro de um limite transacional. Ele não transforma uma
sequência que atravessa serviços, APIs, filas e bancos diferentes em uma transação única.

## Atomicidade

Atomicidade significa tudo ou nada dentro da transação. Se uma transação atualiza saldo,
lança o registro correspondente e falha antes do commit, o banco pode desfazer o conjunto
de alterações. Depois do commit, as alterações tornam-se visíveis conforme as regras do
banco.

Atomicidade não significa que um sistema externo participou da mesma decisão. Enviar um
email antes do rollback não é desfeito por um `ROLLBACK` local. Para esse caso, use outbox,
reconciliação ou compensação.

## Consistência

Consistência significa que uma transação válida preserva as regras declaradas pelo banco
e pelo modelo. Primary keys, unique constraints, foreign keys, checks, triggers e regras
de aplicação podem participar da invariância.

ACID não descobre todas as regras de negócio. Uma condição que depende de várias leituras
concorrentes pode exigir uma constraint, lock ou nível de isolamento mais forte. Se a
aplicação calcula a regra sem considerar concorrência, a transação pode terminar em um
estado inválido mesmo que o SQL seja sintaticamente correto.

## Isolamento

Isolamento define o que uma transação pode observar enquanto outras executam. Níveis mais
fortes reduzem anomalias, mas podem aumentar bloqueios, abortos, retry e custo de
concorrência.

Os fenômenos relevantes incluem dirty read, non-repeatable read, phantom read e conflitos
de escrita. PostgreSQL implementa seus níveis com MVCC e locks; o comportamento exato
precisa ser consultado na documentação do banco, não inferido apenas pelo nome do nível.

`READ COMMITTED` é comum e permite que statements sucessivos observem commits diferentes.
`REPEATABLE READ` mantém uma visão mais estável. `SERIALIZABLE` oferece a promessa mais
forte e pode abortar transações concorrentes para preservar o resultado serializável.

Mais isolamento não é sempre melhor. Uma consulta analítica longa em `SERIALIZABLE` pode
gerar abortos que o chamador precisa repetir. A operação deve definir a invariável e o
comportamento aceitável antes de escolher o nível.

## Durabilidade

Durabilidade significa que, depois de o banco confirmar uma transação, seu resultado não
deve desaparecer por uma falha normal prevista pelo mecanismo. O banco usa log de escrita,
flush, WAL, replicação ou mecanismos equivalentes conforme sua configuração.

Durabilidade do commit não substitui backup. Um `DELETE` confirmado, uma migração errada
ou ransomware podem ser duráveis e replicados corretamente. Backup, retenção e teste de
restauração protegem contra outro tipo de falha.

Também é preciso considerar o que o cliente recebeu. Se a conexão cair depois de o banco
confirmar e antes da resposta chegar, o cliente pode não saber o resultado. A operação
precisa de consulta por identificador, idempotency key ou reconciliação.

## Limite da transação

Mantenha a transação curta o suficiente para liberar locks e conexões, mas completa o
suficiente para proteger a invariável. Não mantenha uma transação aberta durante chamada
HTTP lenta, espera de usuário ou processamento que não precisa de snapshot estável.

Uma transação local pode cobrir múltiplas tabelas do mesmo banco. Ela normalmente não
abrange outro cluster, serviço ou provedor externo. Distribuir o limite exige 2PC, saga,
outbox ou outra coordenação, cada qual com custos e failure modes próprios.

## ACID e consistência eventual

Em sistemas distribuídos, cada serviço pode manter transações ACID locais e propagar
eventos. O estado global torna-se eventualmente consistente, e o sistema precisa tolerar
atraso, duplicação, reordenação e falha de consumidor.

Isso não é uma versão inferior de ACID. É uma escolha de limite e comportamento. Uma
transferência financeira pode exigir uma autoridade transacional forte; uma projeção de
busca pode aceitar atraso e reconstrução.

## Atomicidade e idempotência

Atomicidade impede que parte da transação local fique visível. Idempotência torna seguro
repetir uma operação. Uma propriedade não substitui a outra.

Uma transação pode ser atômica e ainda ser executada duas vezes por um retry depois de
um timeout. Uma operação pode ser idempotente e ainda deixar uma transação parcial se não
houver rollback ou compensação.

## Boas práticas

- defina a invariável antes do `BEGIN`;
- use constraints no banco para regras que exigem proteção concorrente;
- escolha isolamento pelo problema, não por preferência abstrata;
- mantenha o limite transacional explícito;
- não faça chamadas externas lentas dentro da transação sem necessidade;
- combine outbox e consumidores idempotentes quando publicar eventos após commit;
- teste rollback, timeout, conflito, crash e restauração;
- monitore locks, duração, abortos, deadlocks e crescimento do WAL.

## Fontes

- [PostgreSQL, transações](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [PostgreSQL, níveis de isolamento](https://www.postgresql.org/docs/current/transaction-iso.html)
- [PostgreSQL, COMMIT](https://www.postgresql.org/docs/current/sql-commit.html)
- [PostgreSQL, consistência no nível da aplicação](https://www.postgresql.org/docs/current/applevel-consistency.html)
