# ReactiveX e Rx

ReactiveX é um modelo para compor operações assíncronas e eventos por meio de sequências
observáveis. A família inclui implementações como RxJava, RxJS, Rx.NET, RxSwift e outras.
O nome Rx não identifica um banco, um broker ou um transporte. Ele descreve uma forma de
representar uma sequência, observar seus valores e aplicar operadores.

## Modelo mental

Uma sequência possui uma fonte, operadores e um consumidor. O consumidor assina a
sequência, recebe zero ou mais valores, recebe um erro ou recebe uma conclusão. Uma
assinatura representa um recurso: enquanto ela está ativa, a fonte pode produzir valores e
executar efeitos.

Os sinais conceituais são:

- `onNext`, um valor;
- `onError`, uma falha terminal;
- `onComplete`, uma conclusão normal;
- `dispose` ou cancelamento, a interrupção da assinatura pelo consumidor.

Os nomes e tipos exatos variam entre implementações. A semântica do contrato precisa ser
consultada na implementação utilizada, especialmente para backpressure, concorrência,
cancelamento e tratamento de exceções.

## Observable, Observer e Subscription

O Observable representa a produção de valores. O Observer reage aos sinais. A Subscription
ou Disposable representa o vínculo que pode ser cancelado. Essa separação permite compor
uma sequência sem iniciar necessariamente o trabalho antes da assinatura.

Não confunda criar uma sequência com executar uma operação. Muitas fontes são frias: cada
assinatura inicia uma execução independente. Outras fontes são quentes: uma fonte externa
continua produzindo e cada assinante observa o que estiver disponível a partir de sua
entrada.

Uma função que cria uma requisição HTTP fria pode executá-la para cada assinante. Se o
resultado precisa ser compartilhado, use um operador de compartilhamento apropriado e
defina replay, cache, ciclo de vida e comportamento quando não houver assinantes.

## Operadores

Operadores transformam, filtram, combinam ou controlam uma sequência. Alguns exemplos
conceituais são:

| Família | Exemplos de uso |
| --- | --- |
| Transformação | mapear um valor para outro ou achatar uma sequência interna |
| Filtragem | aceitar somente valores que atendem uma condição |
| Combinação | unir fontes, esperar várias ou trocar para a mais recente |
| Tempo | atrasar, agrupar, limitar frequência ou aplicar janela |
| Estado | compartilhar, reter o último valor ou eliminar duplicatas |
| Erro | capturar, substituir, repetir com limite ou propagar |
| Concorrência | escolher scheduler, paralelizar ou limitar trabalho |
| Acúmulo | reduzir uma sequência a estado, lista ou agregado |

Operadores podem alterar o momento de execução, o número de assinaturas, a ordem e a
quantidade de memória. Uma cadeia curta de operadores não é automaticamente mais eficiente
que um loop explícito; avalie alocação, cancelamento, debugging e clareza.

## Schedulers e concorrência

Schedulers controlam onde ou quando partes da cadeia executam. Uma implementação pode
oferecer schedulers para thread atual, I/O, computação, temporizadores ou uma pool. A
documentação oficial do [ReactiveX Scheduler](https://reactivex.io/documentation/scheduler.html)
é importante porque operadores diferentes possuem defaults e restrições diferentes.

Separar trabalho de I/O e CPU evita bloquear uma thread inadequada, mas mover tudo para
uma pool não resolve saturação. Defina limites, monitore filas e preserve o contexto de
cancelamento. Uma fonte pode iniciar várias operações concorrentes se cada assinatura ou
cada valor disparar trabalho sem controle.

`subscribeOn` e `observeOn`, quando existem com esses nomes, afetam partes diferentes do
fluxo. Um muda onde a assinatura ou produção começa; o outro muda onde os sinais são
observados depois de um ponto. Não use ambos por hábito sem medir o caminho e verificar o
contrato da implementação.

## Erros e cancelamento

Em geral, um erro encerra a sequência. Isso é diferente de emitir um objeto que representa
erro e continuar normalmente. Escolha o modelo conforme o domínio: falha de uma leitura
pode ser recuperável, enquanto corrupção de estado pode precisar encerrar todo o fluxo.

Retries devem ser limitados, ter backoff e respeitar idempotência. Repetir automaticamente
uma operação que publica cobrança ou grava evento pode duplicar efeitos. O retry também
deve distinguir erro transitório, erro permanente, cancelamento e rejeição de autorização.

Cancelamento deve alcançar a fonte. Cancelar somente a observação enquanto uma chamada
HTTP, leitura de arquivo ou job continua consumindo recursos produz trabalho órfão. Use
timeouts e integração com o mecanismo de cancelamento da biblioteca subjacente.

## Backpressure

Backpressure é a coordenação entre a velocidade de produção e a capacidade de consumo.
Nem toda implementação ReactiveX oferece o mesmo protocolo. Algumas usam `Flowable` ou
equivalente para uma fonte que respeita demanda; outras usam buffer, amostragem, janela,
conflation ou descarte.

Quando o produtor é mais rápido, decida de forma explícita se deve:

- bloquear ou suspender o produtor;
- armazenar uma fila limitada;
- manter somente o valor mais recente;
- agrupar valores;
- descartar os mais antigos ou mais novos;
- rejeitar o produtor;
- escalar consumidores.

Um buffer ilimitado apenas transforma pressão de throughput em falha de memória. Em fluxos
de estado, manter o último valor pode ser correto. Em pagamentos ou eventos de auditoria,
descartar valores normalmente é incorreto.

## Subjects e fontes quentes

Subject, Processor ou tipos equivalentes permitem publicar valores e expor uma sequência.
Eles são úteis para adaptar callbacks e eventos, mas podem esconder ownership, estado
mutável e condições de corrida.

Escolha o tipo de fonte conforme a semântica:

- sequência fria para uma operação que cada consumidor deve iniciar;
- fonte quente para um evento externo que existe independentemente do consumidor;
- estado compartilhado para o valor atual e seus updates;
- stream durável quando consumidores precisam recuperar eventos ausentes.

Um Subject em memória não é uma fila durável. Se o processo cair, valores não consumidos
serão perdidos, a menos que a fonte de verdade exista fora do processo.

## Teste e observabilidade

Teste valores, ordenação, conclusão, erro, cancelamento, retry e concorrência. Use tempo
virtual para operadores baseados em relógio quando a implementação permitir. Verifique
que uma assinatura é encerrada quando a tela, requisição ou componente sai do ciclo de
vida.

Mensure assinaturas ativas, duração, eventos por segundo, backlog, descartes, retries,
erros, cancelamentos e tempo de processamento. Trace o caminho entre a origem e o
consumidor quando o fluxo atravessar rede, banco ou fila.

## Onde usar e onde evitar

ReactiveX é útil quando o domínio realmente envolve streams, composição de eventos,
cancelamento, múltiplas fontes ou transformações assíncronas. Ele aparece em interfaces
reativas, clientes de rede, integração de sensores, pipelines de eventos e processamento
de sinais.

Prefira uma função direta, uma suspensão ou uma fila simples quando há uma única operação
sequencial. Uma cadeia extensa para representar um fluxo trivial dificulta stack traces,
debugging e ownership. Não use ReactiveX para substituir persistência, autorização,
transação ou um broker durável.

## Relação com bancos em tempo real e Kotlin Flow

Um listener de banco pode ser adaptado para Observable, e o consumidor pode transformar o
fluxo antes de renderizá-lo. Essa adaptação deve preservar reconexão, erro, cancelamento,
duplicidade e resync do banco.

[Kotlin Flow](kotlin-flow.md) é a abstração idiomática do ecossistema Kotlin para fluxos
integrados a coroutines. Ela compartilha conceitos com ReactiveX, mas seus contratos de
contexto, suspensão, backpressure, hot flows e lifecycle não são idênticos.

## Fontes primárias

- [ReactiveX](https://reactivex.io/)
- [ReactiveX operators](https://reactivex.io/documentation/operators.html)
- [ReactiveX scheduler](https://reactivex.io/documentation/scheduler.html)
- [Reactive Streams](https://www.reactive-streams.org/)
- [RxJava](https://github.com/ReactiveX/RxJava)
- [RxJS](https://rxjs.dev/)
