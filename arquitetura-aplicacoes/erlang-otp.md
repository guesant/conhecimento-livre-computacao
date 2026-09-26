# Erlang/OTP

Erlang/OTP é uma plataforma para construir sistemas concorrentes e tolerantes a falhas.
Erlang é a linguagem e a máquina virtual BEAM executa processos leves que se comunicam
por mensagens. OTP fornece comportamentos, supervisores e convenções para organizar
esses processos.

O modelo não é o mesmo que criar um processo do sistema operacional para cada tarefa.
Processos da BEAM são isolados dentro da máquina virtual, têm mailbox próprio e podem ser
criados em grande quantidade. Eles não compartilham estado mutável diretamente. A
comunicação acontece por passagem de mensagens.

## Processos e mensagens

Um processo recebe mensagens, mantém seu estado e decide como responder. O isolamento
limita o efeito de uma falha local: a terminação de um processo não precisa encerrar toda
a aplicação. O processo pode ser monitorado ou ligado a outros processos para que a
falha seja observada e tratada.

A mailbox é uma fila de mensagens do processo. Se o produtor enviar mais mensagens do
que o consumidor consegue processar, a memória pode crescer. O modelo de mensagens não
elimina backpressure. Filas limitadas, protocolos de confirmação, particionamento e
controle de ritmo continuam sendo necessários.

## `gen_server`

`gen_server` é um comportamento OTP para servidores genéricos que mantêm estado e
respondem a mensagens. O módulo de callback implementa operações como inicialização,
chamada síncrona, mensagem assíncrona, mensagens gerais e encerramento.

Os padrões principais são:

- `gen_server:call`, uma requisição síncrona que espera uma resposta;
- `gen_server:cast`, uma mensagem assíncrona sem resposta obrigatória;
- `handle_info`, para mensagens que não foram enviadas por `call` ou `cast`;
- `init`, que cria o estado inicial e pode solicitar ações posteriores.

Um servidor de OTP não deve ser tratado apenas como uma classe com métodos. O contrato
inclui o tipo de mensagem, o estado, o comportamento em falhas, o timeout e a relação
com seu supervisor.

## Supervisão

Uma árvore de supervisão organiza supervisores e workers. O supervisor inicia processos
filhos e aplica uma estratégia quando um deles termina. Dependendo da configuração, ele
pode reiniciar apenas o filho que falhou, reiniciar os demais ou reiniciar o próprio
grupo.

Essa estrutura torna explícita a pergunta: qual conjunto de processos precisa falhar e
reiniciar junto? Um cache local pode ter uma política diferente de um processo que mantém
uma conexão com um sistema externo.

A supervisão não corrige um erro lógico. Se um processo reinicia imediatamente com o
mesmo estado inválido, a árvore pode entrar em falha repetida. Limites de reinício,
estratégias adequadas, telemetria e uma forma de remover ou corrigir a causa continuam
sendo necessários.

## Outros comportamentos OTP

`gen_server` é adequado para um servidor orientado a mensagens e estado. Outros
comportamentos modelam problemas diferentes:

- `gen_statem` organiza máquinas de estados e transições explícitas;
- `gen_event` coordena handlers de eventos em um gerenciador de eventos;
- `supervisor` descreve a relação de supervisão e as políticas de reinício;
- `application` define como uma parte do sistema inicia e se integra à árvore principal.

Escolher um comportamento não substitui o desenho do protocolo. O estado, as mensagens,
os timeouts e as garantias de entrega ainda precisam ser definidos.

## Concorrência e distribuição

Vários processos da BEAM podem executar no mesmo nó sem que exista comunicação de rede.
Isso permite organizar um sistema concorrente e modular dentro de uma única máquina
virtual. O uso de processos não significa que a aplicação seja composta por
microsserviços.

Erlang também pode conectar nós e enviar mensagens entre máquinas virtuais. Nesse ponto
entram falhas de rede, particionamento, atraso, nós indisponíveis e descoberta de
serviço. A semântica distribuída não deve ser confundida com a semântica local de uma
mailbox.

Uma aplicação pode, portanto, ser um único release com muitos processos internos, vários
releases no mesmo nó ou vários nós Erlang. A unidade de deploy e a unidade de concorrência
são dimensões diferentes.

## Nós Erlang

Um nó Erlang é uma instância da máquina virtual BEAM com um nome próprio. O nome permite
que processos em nós diferentes sejam endereçados. Em uma configuração com nomes longos,
um nó pode ser identificado por algo como `worker-a@example.internal`; com nomes curtos,
o nome é limitado ao domínio local configurado.

O nó é uma unidade de runtime, não necessariamente uma unidade de negócio. Uma aplicação
OTP pode executar em um nó, em vários nós do mesmo host ou em vários hosts. O release,
os módulos carregados e as configurações precisam ser compatíveis quando os nós forem
interagir diretamente.

Para conectar nós, a VM precisa conhecer o endereço e a porta do outro nó. O mecanismo
tradicional usa o EPMD para descobrir a porta de distribuição associada ao nome do nó.
Em ambientes controlados, a descoberta e a faixa de portas devem ser explicitamente
configuradas para que firewall, containers e redes Kubernetes não transformem a conexão
em uma dependência implícita.

Uma conexão pode ser testada com o ping distribuído do OTP. O sucesso indica que os nós
conseguiram estabelecer a conexão e aceitar a autenticação básica. Não significa que a
aplicação remota esteja saudável ou que uma operação de negócio possa ser concluída.

## Mensagens entre nós

Depois que dois nós estão conectados, um processo pode enviar uma mensagem para um PID
remoto ou para um nome registrado. O código que envia a mensagem pode se parecer com o
código de comunicação local, mas as garantias são diferentes.

Uma mensagem remota depende da conexão, pode esperar por buffers e pode deixar de chegar
quando o nó ou a rede falhar. O modelo não fornece entrega exatamente uma vez por padrão.
Se a operação não puder ser perdida, o protocolo precisa de confirmação, identificador de
operação, persistência e processamento idempotente.

Chamadas RPC podem esconder ainda mais a rede. Uma chamada para um módulo remoto pode
bloquear, expirar ou falhar porque o nó está indisponível. Use um timeout explícito e
trate a chamada remota como uma integração distribuída, mesmo que o código tenha a mesma
forma de uma função local.

Também é possível iniciar um processo em outro nó, mas isso não elimina a necessidade de
definir ownership, ciclo de vida, supervisão e capacidade. Um processo criado remotamente
precisa ter o código disponível no nó de destino e uma política clara para quando a
conexão for perdida.

## Links e monitors distribuídos

Links e monitors podem atravessar nós. Um monitor remoto informa que o processo ou nó
observado terminou. Um link pode propagar uma falha para o processo ligado, conforme a
semântica de trapping exits e da supervisão.

Essa propriedade permite construir supervisão envolvendo processos remotos, mas aumenta
o custo de falhas. Uma desconexão pode parecer uma terminação do processo, embora o
processo remoto continue executando. O sistema precisa distinguir falha do processo,
falha do nó e perda de conectividade.

Uma árvore de supervisão local não deve assumir que um worker remoto será reiniciado com
sucesso. A recuperação pode exigir redescoberta do serviço, reconexão, reenvio de uma
operação pendente ou eleição de outro processo responsável.

## Autenticação e segurança

Nós Erlang tradicionalmente usam um cookie compartilhado para autenticar a conexão de
distribuição. O cookie é uma credencial de cluster, não uma autorização detalhada por
operação. Quem consegue participar da distribuição pode ter capacidades muito amplas,
portanto o cookie deve ser tratado como um segredo de alta sensibilidade.

A porta de distribuição e o EPMD não devem ser expostos à Internet. Restrinja os
endereços de origem com firewall ou NetworkPolicy, use nomes e portas previsíveis apenas
quando necessário e proteja o armazenamento do cookie. Em redes não confiáveis, configure
distribuição sobre TLS e valide certificados conforme a topologia de confiança adotada.

Criptografar a conexão não substitui autenticação de usuário, autorização de negócio ou
isolamento entre ambientes. Um nó de desenvolvimento não deve compartilhar o cookie do
cluster de produção.

## Falhas e particionamento

O estado de um nó conectado não é automaticamente consistente com o estado dos demais.
Uma partição de rede pode produzir dois grupos que continuam aceitando trabalho local.
Quando a conexão voltar, mensagens atrasadas, operações duplicadas e decisões conflitantes
podem aparecer.

Distribuição Erlang não é, por si só, um algoritmo de consenso nem um banco replicado.
Se a aplicação precisa de uma única autoridade para uma decisão, deve usar um protocolo
de coordenação ou um armazenamento apropriado, com regras para quorum, fencing e
recuperação.

Considere pelo menos estes estados em um protocolo distribuído:

- nó conectado e processo disponível;
- nó conectado, mas serviço sobrecarregado;
- conexão perdida com processo ainda executando;
- nó encerrado e processo perdido;
- partição em que mais de um grupo acredita ser responsável;
- reconexão com mensagens antigas ou operações já aplicadas.

Retries precisam de backoff e de uma chave de idempotência. Reenviar uma mensagem que
cria um recurso, cobra uma operação ou altera uma configuração pode produzir efeitos
duplicados se o receptor não reconhecer operações já concluídas.

## Topologias

Uma topologia pequena pode ter um nó por componente, desde que cada processo tenha uma
responsabilidade clara. Em uma topologia maior, conectar todos os nós entre si aumenta o
número de conexões, os caminhos de falha e a dificuldade de diagnosticar partições.

Os nós podem ser organizados por zona, domínio de falha ou função. Essa escolha deve
considerar latência, quantidade de tráfego, necessidade de comunicação direta e como a
aplicação se recupera quando uma zona desaparece. Conectar nós de regiões muito distantes
como se fossem uma única memória distribuída costuma produzir timeouts e dependências
frágeis.

Um serviço externo ou um broker pode ser uma escolha melhor quando a topologia precisa de
retenção, consumidores independentes, replay, controle de acesso mais granular ou
isolamento de ciclos de vida.

## Diagnóstico

Ao investigar uma falha de distribuição, separe as camadas:

1. resolução do nome e conectividade entre endereços;
2. abertura da porta de distribuição e descoberta do EPMD;
3. autenticação pelo cookie;
4. compatibilidade de versão, release e protocolo;
5. estado da conexão entre os nós;
6. disponibilidade e capacidade do processo remoto;
7. confirmação da operação de negócio.

Um ping bem-sucedido cobre apenas parte dessas camadas. Logs de conexão, métricas de
mailbox, contadores de timeout, notificações de `nodedown` e identificadores de operação
são necessários para diferenciar uma falha de rede de uma falha no handler.

## `call`, `cast` e eventos

`call` é apropriado quando o consumidor precisa de uma resposta e pode tolerar o tempo de
espera. Timeouts precisam fazer parte do contrato, porque um servidor pode estar ocupado,
terminando ou isolado.

`cast` é útil para uma notificação ou alteração cujo resultado não será retornado ao
remetente. Ele não deve ser usado para esconder uma operação que exige confirmação. Se a
mensagem for importante, o sistema precisa definir como detectar perda, duplicidade e
falha do processamento.

Eventos podem ser representados como mensagens para vários processos. O produtor não
deve depender de uma ordem acidental entre consumidores. Cada consumidor precisa ser
idempotente quando uma mensagem puder ser redeliverada ou reenviada após uma falha.

## Modelo de falhas

O princípio de deixar o processo falhar funciona quando o supervisor possui contexto para
reiniciar o processo e quando o estado pode ser reconstruído. Ele não significa ignorar
erros ou reiniciar indefinidamente.

Considere, pelo menos:

- estado volátil, que pode ser reconstruído a partir de uma fonte durável;
- estado durável, que precisa de confirmação e recuperação;
- falhas permanentes, como uma configuração inválida;
- falhas transitórias, como timeout de um serviço externo;
- falhas de protocolo, como mensagens incompatíveis;
- falhas de capacidade, como mailbox ou pool de conexões crescendo sem limite.

Supervisionar uma conexão externa não remove a necessidade de timeout, circuit breaker,
backoff e limites. Reiniciar o worker pode ser correto, mas insistir instantaneamente
pode piorar a indisponibilidade do sistema externo.

## Relação com um monólito modular

Um monólito modular Java normalmente usa pacotes, interfaces, chamadas e eventos no
mesmo processo. Erlang/OTP usa processos leves, mensagens e supervisão como abstrações
centrais. Os dois modelos podem ter fronteiras internas fortes, mas suas garantias e
formas de falha são diferentes.

Um módulo Java não ganha isolamento de falha equivalente apenas por usar um event bus.
Uma exceção pode continuar derrubando a requisição ou a transação. Da mesma forma, um
processo Erlang não vira automaticamente um serviço independente: ele pode continuar
fazendo parte do mesmo release e da mesma máquina virtual.

## Fontes

- [Erlang/OTP, `gen_server`](https://www.erlang.org/docs/26/man/gen_server.html)
- [Erlang/OTP, princípios de desenho](https://www.erlang.org/docs/27/system/design_principles.html)
- [Erlang/OTP, distribuição](https://www.erlang.org/doc/system/distributed.html)
- [Erlang/OTP, distribuição segura](https://www.erlang.org/doc/system/ssl_distribution.html)
- [Erlang/OTP, documentação](https://www.erlang.org/docs)
- [Erlang, processos](https://www.erlang.org/doc/system/processes.html)
