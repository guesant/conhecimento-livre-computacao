# pthread

POSIX threads, pthreads, é a API para criar e coordenar threads dentro de um
processo. Cada thread compartilha o espaço de endereçamento, arquivos abertos
e muitos recursos do processo, mas possui stack, registradores, estado de
agendamento e identidade próprios.

## Ciclo de vida

`pthread_create` inicia uma função; `pthread_join` aguarda e recolhe seu
resultado; `pthread_detach` informa que os recursos serão recolhidos quando a
thread terminar. Misturar join e detach, perder uma referência ou deixar uma
thread acessar dados destruídos produz vazamentos, use-after-free e encerramento
prematuro.

A stack de cada thread tem limite configurável. Recursão, arrays locais e
callbacks profundos podem esgotá-la independentemente da memória heap do
processo.

## Sincronização

Mutex protege exclusão mútua; condition variable coordena espera por uma
condição; read-write lock separa leitores e escritores; barrier sincroniza uma
fase; semáforo limita contagem. A primitiva não define a regra de posse dos
dados. O código precisa declarar invariantes, ordem de aquisição e o que pode
ser acessado fora do lock.

Deadlock surge quando threads mantêm locks em ordem circular. Starvation surge
quando uma thread não obtém tempo ou lock. Race condition pode existir sem
deadlock e pode produzir resultado incorreto mesmo que o processo nunca pare.

## Memória e cancelamento

Uma thread que publica um ponteiro precisa de uma relação de happens-before
adequada. Volatile não substitui sincronização. Cancelamento assíncrono pode
interromper uma thread no meio de um lock ou atualização; pontos de cancelamento
cooperativos são mais previsíveis.

## Relações

- [Mutex](../../engenharia-software/concorrencia/mutex.md) explica uma primitiva específica.
- [Event loop](../runtime/event-loop.md) contrasta concorrência cooperativa e threads.
- [malloc](malloc.md) trata o heap compartilhado.

## Fontes primárias

- [POSIX threads](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)
- [pthreads(7)](https://man7.org/linux/man-pages/man7/pthreads.7.html)
- [pthread_create(3)](https://man7.org/linux/man-pages/man3/pthread_create.3.html)
