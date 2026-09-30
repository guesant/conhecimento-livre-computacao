# Concorrência

Concorrência é a capacidade de uma aplicação organizar várias atividades que
podem avançar na mesma janela de tempo. Ela não exige que duas instruções sejam
executadas fisicamente ao mesmo tempo. Um sistema com um único processador
pode intercalar tarefas, suspender uma enquanto espera I/O e continuar outra.

O conceito trata principalmente de composição e coordenação. As atividades
podem ser threads, processos, tarefas assíncronas, callbacks, requisições,
workers ou atores. O que importa é que seus passos podem se intercalar e que a
ordem observada não deve quebrar as invariantes do sistema.

## Exemplo sem paralelismo

Considere uma aplicação com um único event loop:

```text
tarefa A: inicia leitura de arquivo
tarefa B: inicia consulta HTTP
tarefa A: espera o disco
tarefa B: recebe resposta e processa dados
tarefa A: recebe dados do disco e continua
```

As tarefas são concorrentes porque podem progredir alternadamente, mas não há
duas instruções da aplicação executando no mesmo instante nesse único loop.
Quando uma tarefa espera uma operação não bloqueante, o runtime aproveita o
tempo para executar outra.

## Formas de concorrência

### Memória compartilhada

Threads e processos que compartilham dados precisam de uma disciplina para
leituras, escritas e visibilidade. Mutexes, semáforos, operações atômicas e
variáveis de condição protegem invariantes, mas também podem produzir espera,
contenção e deadlock.

### Passagem de mensagens

Uma atividade envia uma mensagem para outra em vez de modificar diretamente o
estado dela. Filas, canais e atores podem simplificar a propriedade dos dados,
mas introduzem filas cheias, mensagens duplicadas, ordenação, cancelamento e
políticas de backpressure.

### Concorrência assíncrona

Uma tarefa entrega uma operação ao runtime e retorna enquanto aguarda o
resultado. O scheduler ou event loop retoma a continuação quando há um evento.
Esse modelo reduz threads bloqueadas em I/O, mas não torna automaticamente o
trabalho de CPU assíncrono nem elimina a necessidade de limites.

### Concorrência distribuída

Em processos ou máquinas diferentes, não existe memória compartilhada com
visibilidade imediata. Relógios podem divergir, mensagens podem atrasar ou
duplicar e participantes podem falhar independentemente. Locks locais não
protegem uma invariável distribuída; transações, leases, consenso ou desenho
idempotente podem ser necessários.

## Segurança e progresso

Uma implementação concorrente precisa tratar duas classes de propriedade:

- safety, nada incorreto deve acontecer, como duas operações consumirem o
  mesmo recurso exclusivo;
- liveness, algo correto deve eventualmente acontecer, como uma tarefa não
  ficar esperando para sempre.

Exclusão mútua pode preservar safety e ainda produzir starvation. A ordem
correta de aquisição de locks pode evitar deadlock, mas não resolve uma fila
sem limite. Timeout, cancelamento, retry e idempotência devem fazer parte do
protocolo, não ser adicionados depois que a concorrência já existe.

## Limites

Concorrência sem limite costuma apenas mover o problema para outro recurso:

- tarefas acumulam na memória;
- conexões ocupam o pool do banco;
- requisições excedem o rate limit de uma dependência;
- workers disputam CPU;
- retries amplificam uma falha;
- filas crescem até o processo ser encerrado.

Pools, filas limitadas, semáforos de capacidade e rate limits transformam
concorrência em uma quantidade observável. Backpressure informa ao produtor
que o consumidor não consegue acompanhar. Fire and forget sem retenção,
confirmação ou limite não é uma estratégia de confiabilidade.

## Concorrência e threads

Threads são uma forma de executar atividades concorrentes, mas não são a única.
Uma aplicação pode usar event loop, corrotinas, atores, processos, filas ou
uma combinação deles. Também é possível criar muitas threads concorrentes que
passam a maior parte do tempo bloqueadas em I/O e poucas que executam código.

[Threads](../threads.md) explica a unidade de execução do processo, enquanto
[virtual threads](../virtual-threads.md) explica como um runtime pode manter
muitas tarefas lógicas sobre menos threads de plataforma.

## Relações

- [Paralelismo](paralelismo.md) trata execução física simultânea.
- [Comparação entre concorrência e paralelismo](../../../comparacoes/engenharia-software/concorrencia-paralelismo.md) contrasta os objetivos e os custos.
- [Condição de corrida](../race-condition.md) trata resultados dependentes de ordem.
- [Mutex](../mutex.md), [semáforos](../semaforos.md) e [deadlock](../deadlock.md) tratam coordenação e falhas.
- [Event loop](../../../sistemas/runtime/event-loop.md) trata o modelo de execução orientado a eventos.

## Fontes primárias

- [Python, asyncio](https://docs.python.org/3/library/asyncio.html)
- [Oracle, concurrency in Java](https://docs.oracle.com/javase/tutorial/essential/concurrency/)
- [Linux kernel, scheduler](https://docs.kernel.org/scheduler/index.html)
