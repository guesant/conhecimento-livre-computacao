# Deadlock

Deadlock é uma situação em que atividades ficam bloqueadas porque cada uma espera um
recurso mantido por outra. O sistema não progride sem intervenção externa, mesmo que
todos os processos estejam vivos.

As quatro condições clássicas são:

1. exclusão mútua, algum recurso não pode ser compartilhado simultaneamente;
2. hold and wait, uma atividade mantém um recurso enquanto espera outro;
3. no preemption, o recurso não pode ser retirado à força sem quebrar a operação;
4. espera circular, existe um ciclo de dependências entre proprietários e recursos.

Remover qualquer uma reduz ou elimina a classe de deadlock. Na prática, a estratégia mais
comum é impor uma ordem global de aquisição, manter transações curtas e abortar uma
atividade quando o sistema detectar um ciclo.

## Exemplo

Uma thread adquire `A` e espera `B`. Outra adquire `B` e espera `A`. Nenhuma consegue
liberar o primeiro recurso porque a execução está parada antes da seção que faria a
liberação.

O mesmo padrão aparece em bancos, filas e serviços distribuídos. Uma transação pode
segurar uma linha enquanto espera outra; um worker pode possuir um lease enquanto espera
uma resposta; dois serviços podem esperar callbacks que nunca serão enviados.

## Prevenção

- adquira mutexes, tabelas e linhas em uma ordem determinística;
- ordene IDs antes de bloquear vários recursos;
- não misture locks locais e remotos sem um protocolo de ordem;
- mantenha a transação curta;
- use `NOWAIT` ou timeout quando esperar não for aceitável;
- evite chamada externa dentro da seção crítica;
- reserve todos os recursos necessários antes de iniciar trabalho irreversível;
- prefira operação atômica ou constraint quando a invariável puder ser expressa no storage.

Prevenção reduz deadlocks, mas pode diminuir paralelismo. Um lock global usado para evitar
qualquer ciclo pode apenas transformar a aplicação em uma fila lenta.

## Detecção e recuperação

Um banco pode construir um grafo de espera e abortar uma transação. O PostgreSQL reporta
`deadlock detected`; o InnoDB escolhe uma vítima; outros sistemas usam timeout ou um
coordenador.

O retry deve repetir a transação ou operação inteira, não apenas a última instrução. O
cliente precisa limitar tentativas, aplicar backoff com jitter e diferenciar deadlock de
erro permanente. Se a transação chamou um sistema externo, idempotência ou compensação
continua necessária.

## Deadlock distribuído

Em múltiplos processos, o ciclo pode atravessar bancos, filas, APIs e leases. Nem sempre
existe um observador com visão completa. Timeouts quebram a espera, mas não garantem que o
trabalho abandonado não continuará em outro participante.

Use correlation ID, lease com fencing, cancelamento, deadlines e estados recuperáveis.
Uma mensagem que expirou deve deixar claro se o efeito foi aplicado, desconhecido ou ainda
pendente.

## Deadlock, livelock e starvation

Deadlock é ausência de progresso por espera circular. Livelock é atividade contínua sem
progresso útil, como duas transações que sempre detectam conflito e repetem ao mesmo
tempo. Starvation é quando uma atividade pode progredir em teoria, mas nunca recebe
recurso por prioridade ou fairness inadequada.

As métricas precisam distinguir os três. Aumentar retries pode piorar livelock, e uma
fila sem fairness pode esconder starvation mesmo sem locks aparentes.

## Relações

- [Mutex](mutex.md) trata ownership local.
- [Semáforos](semaforos.md) trata capacidade e sinalização.
- [Locks e transações no PostgreSQL](../../dados/postgresql-locks-e-transacoes.md)
  trata deadlocks e timeouts no banco.
- [Condição de corrida](race-condition.md) trata ordem incorreta sem necessariamente
  haver bloqueio.

## Fontes

- [PostgreSQL, explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- [MySQL, deadlocks e retry](https://dev.mysql.com/doc/refman/8.4/en/innodb-deadlocks.html)
- [EWD 209, processos cooperantes e semáforos](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD209.html)
