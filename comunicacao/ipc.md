# Interprocess Communication

Interprocess Communication, IPC, é o conjunto de mecanismos usados por
processos para trocar dados, sincronizar execução e transferir direitos ou
descritores dentro de um sistema. O processo pode estar no mesmo host, em
namespaces diferentes ou, em alguns casos, sob um supervisor que controla sua
permissão de comunicação.

IPC não é sinônimo de RPC. Uma chamada RPC pode usar IPC quando cliente e
servidor estão no mesmo host, mas também pode atravessar uma rede. IPC também
inclui mecanismos que não parecem chamadas, como sinais, semáforos e memória
compartilhada.

## Mecanismos principais no Linux

| Mecanismo | Modelo | Força | Risco ou limitação |
| --- | --- | --- | --- |
| Pipe anônimo | Fluxo unidirecional entre processos relacionados | Simples e integrado ao shell | Depende do ciclo de vida dos descritores |
| FIFO | Pipe nomeado no filesystem | Permite processos independentes | Fluxo limitado e sincronização explícita |
| Unix socket | Stream ou datagram no host | Bidirecional, credenciais e passing de file descriptor | Permissões e ciclo de vida do socket |
| Memória compartilhada | Região comum de memória | Alto throughput e baixa cópia | Exige sincronização e cuidado com corrupção |
| Fila de mensagens | Mensagens discretas com ordenação e limites | Fronteira clara entre mensagens | Capacidade e semântica de persistência limitadas |
| Semáforo | Contador ou sinal de sincronização | Coordena acesso a recurso | Não transporta o dado principal |
| Sinal | Notificação curta para um processo | Útil para interrupção e controle | Pouca informação e tratamento delicado |
| D-Bus | Barramento nomeado, métodos e sinais | Descoberta e contratos de serviços | Escopo e políticas do barramento |

System V IPC e POSIX IPC possuem APIs e ciclos de vida diferentes. Memória
compartilhada, filas e semáforos podem sobreviver ao processo criador até que
sejam removidos explicitamente, portanto limpeza e observabilidade importam.

## Pipes e FIFOs

Pipes representam um fluxo de bytes. O consumidor precisa definir framing se
mais de uma mensagem for enviada, porque uma leitura pode devolver parte de
uma mensagem ou mais de uma mensagem de uma vez.

Um FIFO possui um nome no filesystem e permite conectar processos que não
compartilham parentesco. Permissões do arquivo controlam a abertura, mas a
semântica de bloqueio, fechamento e ausência do produtor precisa fazer parte
do protocolo.

## Unix sockets

Unix domain sockets oferecem comunicação local orientada a stream ou
datagram. Eles podem transportar credenciais do processo e file descriptors,
o que permite ativar um serviço, compartilhar uma conexão ou transferir um
recurso aberto sem expor o arquivo por nome.

Um socket Unix é frequentemente uma boa base para um daemon local. Ainda é
necessário proteger o caminho, definir ownership, permissões, autenticação
adicional e limpeza do endpoint quando o servidor termina.

## Memória compartilhada

Memória compartilhada permite que processos mapeiem a mesma região e troquem
dados sem copiar cada mensagem por um pipe. O ganho de throughput vem com um
custo: os processos passam a compartilhar invariantes de memória.

O protocolo precisa definir ownership, layout, alinhamento, versão, barreiras,
locks, semáforos, detecção de produtor morto e recuperação de uma região
parcialmente escrita. Sem isso, uma estrutura mais rápida pode apenas tornar
uma corrupção mais difícil de reproduzir.

## Filas, semáforos e sinais

Filas de mensagens preservam unidades discretas e podem oferecer prioridade,
mas não são automaticamente um broker durável. Semáforos coordenam acesso,
mas não substituem a proteção de dados. Sinais são apropriados para eventos
curtos, como terminar, recarregar ou interromper, e não para transportar
payloads grandes.

Quando o trabalho precisa sobreviver a reinício, ser reprocessado ou ser
consumido por vários hosts, use uma tecnologia de mensageria projetada para
essa finalidade.

## D-Bus

D-Bus é um barramento IPC com nomes, objetos, interfaces, métodos, sinais e
erros. Ele permite que serviços do sistema e aplicações descubram e chamem
componentes sem conhecer diretamente o PID que implementa o serviço.

O barramento de sistema e o barramento de sessão possuem fronteiras e
políticas distintas. D-Bus fornece uma arquitetura de IPC e autorização, mas
não substitui a política de negócio do serviço. Consulte [D-Bus](../sistemas/systemd/dbus.md)
para os detalhes de sua relação com systemd e desktop Linux.

## Segurança e isolamento

Processos normalmente possuem identidade, UID, GID, credenciais, capabilities,
namespaces e limites diferentes. Um processo com acesso ao socket de outro
serviço pode executar operações tão importantes quanto um cliente de rede.

Proteja endpoints IPC como APIs:

- use ownership e permissões mínimos;
- valide credenciais do processo quando o mecanismo fornecer essa informação;
- limite namespaces, cgroups e capabilities;
- valide tamanho, framing e versões da mensagem;
- evite desserialização executável;
- defina timeout e cancelamento;
- remova recursos nomeados durante shutdown e recuperação;
- registre operações administrativas relevantes.

Um Unix socket com permissão ampla não é privado apenas porque não usa TCP.
Memória compartilhada não é segura porque não passa pela rede. O domínio de
confiança continua sendo uma decisão explícita.

## IPC e containers

Containers separados não são automaticamente incapazes de usar IPC. Namespaces
de IPC isolam identificadores System V e POSIX, mas configurações como
`hostIPC`, montagens de sockets, volumes compartilhados e permissões do host
podem remover essa separação.

Antes de permitir IPC entre workloads, defina se a comunicação é parte de um
contrato suportado ou apenas um atalho. Um socket compartilhado reduz latência,
mas acopla ciclo de vida, identidade, versão e domínio de falha dos processos.

## Escolha do mecanismo

Use pipe para composição simples de processos e fluxo curto. Use Unix socket
para um daemon local ou para RPC dentro do host. Use memória compartilhada
quando a taxa de dados justifica a complexidade de sincronização. Use D-Bus
quando descoberta, métodos e sinais entre serviços do sistema fazem parte do
modelo.

Use rede, RPC ou mensageria quando a fronteira precisa sobreviver a hosts,
deployments e domínios de administração distintos.

## Fontes

- [Linux `pipe(7)`](https://man7.org/linux/man-pages/man7/pipe.7.html)
- [Linux Unix domain sockets](https://man7.org/linux/man-pages/man7/unix.7.html)
- [Linux System V IPC](https://man7.org/linux/man-pages/man7/svipc.7.html)
- [Linux POSIX shared memory](https://man7.org/linux/man-pages/man7/shm_overview.7.html)
- [Linux POSIX message queues](https://man7.org/linux/man-pages/man7/mq_overview.7.html)
- [D-Bus specification](https://dbus.freedesktop.org/doc/dbus-specification.html)

## Continue por aqui

[RPC](rpc.md) explica chamadas entre processos. [gRPC](grpc.md) mostra uma
implementação baseada em transporte de rede. [Namespaces](../sistemas/linux/namespaces.md)
explica uma das fronteiras de isolamento que afetam IPC.
