# Threads

Uma thread é uma unidade de execução que pode ser escalonada independentemente
dentro de um processo. Threads do mesmo processo compartilham o espaço de
endereçamento, arquivos abertos e outros recursos do processo, mas cada uma
mantém seu próprio contador de programa, registradores, pilha de chamadas e
estado de execução.

Essa combinação torna a comunicação entre threads barata, porque elas podem
acessar a mesma memória, mas também torna a memória compartilhada uma fonte de
condições de corrida. Uma thread não é uma unidade de isolamento equivalente a
um processo e não é automaticamente uma unidade de paralelismo.

## Concorrência e paralelismo

Concorrência significa que várias atividades podem avançar durante a mesma
janela de tempo. Paralelismo significa que mais de uma atividade executa
fisicamente ao mesmo tempo. Um sistema operacional pode intercalar dez threads
em um único processador, produzindo concorrência sem paralelismo. Com vários
processadores lógicos, algumas delas podem executar em paralelo.

O número de threads não deve ser confundido com o número de [cores](../../sistemas/cpu/cores.md).
Uma aplicação pode ter milhares de threads bloqueadas em I/O e poucas threads
executando computação. Criar threads indiscriminadamente para trabalho de CPU,
por outro lado, aumenta trocas de contexto e disputa pelo processador.

## Thread de sistema operacional

Em um modelo tradicional, a thread criada pela biblioteca de execução é
associada a uma thread do kernel. O scheduler do sistema operacional coloca a
thread em uma fila de execução, escolhe quando ela recebe um processador lógico
e pode interrompê-la para executar outra.

Uma troca de contexto salva registradores e metadados da atividade atual e
restaura os da próxima. Ela tem custo de CPU e pode degradar a localidade de
cache, mas é necessária para compartilhar o processador entre processos e
threads. Bloqueios de I/O retiram a thread da execução até que o evento possa
continuar, permitindo que o processador trabalhe em outra atividade.

## Memória compartilhada

Como threads acessam o mesmo heap, uma operação que parece simples no código
fonte pode envolver várias leituras e escritas. O compilador, o runtime e o
processador também podem reordenar operações quando o modelo de memória permite.
Mutexes, semáforos, operações atômicas e canais estabelecem as regras de
visibilidade e exclusão necessárias.

Locks não corrigem um desenho por si só. Um lock deve proteger a invariável que
precisa permanecer verdadeira, ter um escopo claro e ser liberado em todos os
caminhos. Locks em excesso reduzem paralelismo; locks ausentes produzem corrida;
locks adquiridos em ordens diferentes podem produzir [deadlock](deadlock.md).

## Pools

Um pool limita a quantidade de threads de plataforma e reutiliza threads para
diversas tarefas. Isso evita o custo repetido de criação e destruição, além de
funcionar como um limite de concorrência. O tamanho adequado depende do tipo de
trabalho:

- trabalho de CPU deve ser próximo da capacidade de execução disponível;
- trabalho de I/O pode ter mais atividades pendentes, desde que conexões,
  memória e filas também tenham limites;
- mistura de CPU e I/O costuma exigir pools ou filas separados.

Um pool sem fila limitada apenas desloca a falta de capacidade para a memória.
Uma fila limitada permite aplicar backpressure, rejeitar trabalho ou responder
com atraso controlado.

## Threads em containers

Uma thread continua sendo uma thread do kernel do host mesmo quando o processo
está em um container. Namespaces isolam visibilidade e cgroups limitam recursos,
mas não criam um conjunto independente de cores. Um processo com muitas threads
pode consumir toda a cota de CPU do container e ser estrangulado pelo cgroup.

No Kubernetes, requests e limits são declarados por container. O [CPU no Kubernetes](../../kubernetes/recursos/cpu.md)
explica como essa cota é convertida em tempo de CPU, e a página de [cgroups](../../sistemas/linux/cgroups.md)
explica o mecanismo de controle no kernel.

## Relações

- [Virtual threads](virtual-threads.md) implementa muitas threads lógicas sobre
  um conjunto menor de threads de plataforma.
- [Condição de corrida](race-condition.md) descreve um erro de ordem entre
  atividades concorrentes.
- [Mutex](mutex.md) e [semáforos](semaforos.md) coordenam acesso e capacidade.
- [Processo Linux](../../sistemas/linux/process.md) explica a unidade de
  isolamento que contém threads.

## Fontes primárias

- [pthreads(7)](https://man7.org/linux/man-pages/man7/pthreads.7.html)
- [Linux scheduler](https://docs.kernel.org/scheduler/index.html)
- [The Linux Kernel documentation, scheduler](https://docs.kernel.org/scheduler/sched-design-CFS.html)
