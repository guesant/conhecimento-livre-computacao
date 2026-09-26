# Mutex

Mutex, de mutual exclusion, é um mecanismo que permite que somente um proprietário por
vez entre em uma seção crítica. O proprietário adquire o mutex, acessa o estado protegido
e o libera. Enquanto ele permanece adquirido, outros participantes esperam ou falham,
conforme a API.

Mutex é apropriado para uma invariável dentro de um processo, como uma estrutura em
memória, uma fila local ou um recurso de uma biblioteca. Um mutex comum não coordena
processos em hosts diferentes. Para isso, é necessário um mecanismo compartilhado com
semântica de lease, fencing e recuperação de participante morto.

## Propriedades importantes

- ownership: quem adquiriu deve liberar, ou o protocolo precisa tratar abandono;
- atomicidade da aquisição: dois participantes não podem acreditar que venceram;
- escopo: thread, processo, host, cluster ou recurso lógico;
- fairness: se há fila ou uma atividade pode esperar indefinidamente;
- reentrância: se o mesmo proprietário pode adquirir novamente;
- timeout: quanto tempo esperar antes de desistir;
- memória: quais leituras e escritas ficam visíveis depois da aquisição e antes da liberação.

Um mutex reentrante evita que a mesma thread bloqueie a si própria, mas pode esconder
recursão acidental e tornar a contagem de liberações difícil. Um mutex não reentrante
expõe melhor algumas violações de protocolo.

## Seção crítica

A seção crítica deve ser pequena e conter somente o acesso que precisa de exclusão. Não
faça dentro dela chamadas HTTP, espera de fila, I/O lento, logging bloqueante ou código que
possa adquirir um segundo lock sem uma ordem definida.

O mutex não deve proteger uma cópia que é enviada a outro processo depois da liberação.
Se a operação externa precisa ser coordenada, use uma transação, outbox, lease ou uma
confirmação no recurso compartilhado.

## Mutex distribuído

Um lock distribuído pode usar banco, Redis, serviço de coordenação ou lease do
orquestrador. O protocolo precisa definir expiração, renovação, identidade do proprietário,
fencing token e comportamento em partição de rede.

Um TTL sozinho não impede que o antigo proprietário continue trabalhando depois de perder
o lock. O recurso protegido deve rejeitar tokens antigos ou aceitar somente uma versão
monotônica. Sem fencing, dois participantes podem acreditar que possuem a autorização em
momentos diferentes e ainda produzir escritas conflitantes.

## Alternativas

Use uma constraint e uma operação atômica quando a invariável é de dados. Use semáforo
quando há capacidade para vários participantes. Use fila quando a espera pode ser
persistida e o trabalho não precisa ocorrer na mesma chamada. Use controle otimista quando
o conflito é raro e a operação pode ser repetida.

## Relações

- [Condição de corrida](race-condition.md) explica o problema que o mutex pode evitar.
- [Semáforos](semaforos.md) permitem capacidade maior que um e sinalização.
- [Deadlock](deadlock.md) explica espera circular entre mutexes.
- [TTL](../../dados/ttl.md) explica expiração, que não substitui fencing.

## Fontes

- [POSIX threads, mutexes](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutex_lock.html)
- [Linux man-pages, pthread mutex](https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3p.html)
