# Kotlin Flow

Kotlin Flow é uma abstração de fluxo assíncrono do ecossistema `kotlinx.coroutines`. Ele
representa valores emitidos ao longo do tempo, integra suspensão e cancelamento
estruturado e oferece operadores para transformar, combinar e controlar a coleta.

Flow não é banco, fila durável nem transporte de rede. Ele vive no processo, embora possa
adaptar uma API, callback, socket, banco ou broker para um modelo de consumo Kotlin.

## Modelo básico

Uma fonte produz valores e um collector os recebe. Operadores intermediários transformam o
fluxo e operadores terminais, como `collect`, iniciam a execução.

```kotlin
fun numbers(): Flow<Int> = flow {
  emit(1)
  emit(2)
}

suspend fun consume() {
  numbers().collect { value ->
    println(value)
  }
}
```

O builder `flow` normalmente representa um fluxo cold. O bloco não executa apenas porque a
função foi chamada; ele executa quando existe um collector. Cada collector pode iniciar
uma nova execução independente. A documentação de [Flow](https://kotlinlang.org/docs/flow.html)
detalha essa distinção.

## Cold e hot

Um cold Flow representa uma receita de produção. Se três componentes coletam a mesma fonte,
a operação upstream pode ser executada três vezes. Isso é adequado para uma consulta que
deve ser independente por consumidor, mas pode gerar requisições ou trabalho duplicado.

Um hot flow existe independentemente dos collectors e compartilha emissões. Em Kotlin,
`SharedFlow` transmite valores aos collectors e `StateFlow` representa um estado atual com
um valor inicial e a emissão mais recente.

| Tipo | Sem collector | Novo collector | Uso comum |
| --- | --- | --- | --- |
| Cold `Flow` | Normalmente não produz | Inicia uma execução | Consulta, transformação, operação sob demanda |
| `SharedFlow` | Pode emitir conforme a política | Recebe replay configurado e novos valores | Eventos e broadcast em memória |
| `StateFlow` | Mantém estado atual | Recebe imediatamente o estado atual | Estado de tela, sessão ou modelo |

Hot não significa durável. Se todos os collectors forem cancelados, eventos podem ser
perdidos conforme a política de replay. Para durabilidade, use banco, outbox, fila ou
stream apropriado.

## StateFlow

`StateFlow` é um `SharedFlow` especializado em estado. Ele exige um valor inicial, mantém
o valor atual e conflui atualizações iguais de acordo com `equals`. O consumidor pode ler
o valor atual e também coletar suas mudanças.

Exponha uma interface somente leitura e mantenha a mutabilidade no dono do estado:

```kotlin
private val mutableState = MutableStateFlow(ScreenState.Loading)
val state: StateFlow<ScreenState> = mutableState.asStateFlow()
```

Use `StateFlow` quando o significado for "qual é o estado agora?". Para eventos de
navegação, toast, erro consumível ou comando que não deve ser reemitido como estado atual,
`SharedFlow` ou outra abstração de evento pode ser mais adequada.

O valor inicial precisa ser semanticamente válido. Usar uma lista vazia ou `null` sem
distinguir carregando, vazio, erro e sucesso pode fazer a interface exibir "sem dados"
antes de a consulta terminar.

## SharedFlow

`SharedFlow` transmite emissões para vários collectors. Seus parâmetros definem replay,
buffer e comportamento quando consumidores são lentos. Um `replay` maior aumenta a
informação entregue a novos collectors, mas também pode repetir eventos que não deveriam
ser repetidos.

Use-o para eventos em memória, atualizações compartilhadas, sinais de sessão ou adaptação
de uma fonte que deve ser coletada uma vez. Não trate `SharedFlow` como garantia de entrega
quando o processo pode ser reiniciado ou quando um consumer pode ficar ausente durante o
evento.

## Operadores e composição

Os operadores de Flow incluem transformação, filtragem, combinação, janela, tratamento de
erro, retry, compartilhamento e agregação. Operadores intermediários são normalmente
lazy; a cadeia só produz quando um operador terminal coleta.

Algumas decisões importantes são:

- `map` transforma um valor sem alterar a frequência;
- `flatMapLatest` cancela a operação anterior quando chega uma nova entrada;
- `combine` compõe os valores mais recentes de fontes;
- `zip` espera valores correspondentes de cada fonte;
- `debounce` reduz chamadas durante uma sequência rápida de entradas;
- `distinctUntilChanged` evita atualizações repetidas;
- `catch` trata falhas upstream conforme o ponto em que é aplicado;
- `retry` repete falhas que realmente podem ser transitórias;
- `stateIn` compartilha um cold flow como `StateFlow`;
- `shareIn` compartilha um cold flow como `SharedFlow`.

`flatMapLatest` é útil para busca conforme o usuário digita, mas somente se a operação
anterior puder ser cancelada com segurança. Cancelar a coleta não desfaz automaticamente
uma gravação já aceita pelo servidor.

## Contexto e dispatchers

Flow preserva o contexto de emissão de modo restritivo. Use `flowOn` para mover a parte
upstream para outro dispatcher, em vez de alterar o contexto de emissão dentro do builder
de maneira incompatível.

Escolha dispatcher pelo trabalho:

- `Dispatchers.IO` para bloqueio de I/O que não possui API suspensiva;
- `Dispatchers.Default` para CPU;
- dispatcher da interface somente para atualização que precisa dele;
- contexto próprio quando a biblioteca ou o domínio exigir serialização.

Mudar dispatcher não cria capacidade infinita. Pool saturada, banco bloqueado e rede lenta
continuam sendo limites. Observe filas, tempo de espera e cancelamentos.

## Backpressure, buffer e conflation

Um producer pode emitir mais rápido que o consumer. Flow oferece suspensão, buffer,
conflation e operadores de controle para representar a política.

- `buffer` permite que upstream e downstream avancem de modo concorrente, dentro de um
  limite;
- `conflate` descarta valores intermediários e preserva uma atualização mais recente;
- `collectLatest` cancela o processamento do valor anterior quando chega outro;
- processamento sequencial mantém ordem e limita concorrência;
- `flatMapMerge` pode aumentar concorrência e precisa de limite explícito.

Escolha pela semântica do valor. Para estado visual, descartar intermediários pode ser
correto. Para pagamentos, auditoria ou comandos, perder uma emissão é normalmente um
defeito. Buffer sem limite converte lentidão em pressão de memória.

## Erros, retry e cancelamento

Exceções podem encerrar a coleta. `catch` trata falhas da parte upstream que está dentro de
seu escopo; colocar o operador no lugar errado pode deixar falhas downstream escaparem.

Use `retry` com limite, backoff e filtro de erros transitórios. Não repita autenticação
rejeitada, validação inválida ou uma operação não idempotente sem uma chave de deduplicação.
O retry de uma consulta pode ser aceitável; o retry de uma gravação exige contrato.

Cancelamento é parte do lifecycle da coroutine. Colete no escopo do componente, tela ou
request e cancele quando esse dono desaparecer. Um `Flow` coletado no escopo global pode
manter recursos e listeners vivos depois que a interface foi destruída.

## Integração com callbacks, APIs e banco

`callbackFlow` adapta uma API baseada em callbacks a um Flow. A adaptação deve remover o
listener ao cancelar e fechar o canal quando a fonte terminar. A ausência dessa limpeza
causa vazamento de listeners e trabalho duplicado.

Uma chamada HTTP sob demanda pode ser um cold Flow ou simplesmente uma função suspensa.
Use Flow quando houver múltiplos valores, cancelamento de stream, composição ou observação
contínua. Um único resultado não precisa ser transformado em Flow apenas por uniformidade.

Um listener de banco em tempo real pode ser exposto como Flow, mas o adapter precisa
preservar reconexão, resync, autorização, duplicidade e estado pendente. `StateFlow` pode
representar o estado já carregado no processo, mas não substitui a fonte de verdade nem o
log de eventos do banco.

## Lifecycle e UI

Em uma UI, coletar de um lifecycle apropriado evita atualizar uma tela que não está mais
ativa. A estratégia exata depende do toolkit, mas a regra é geral: o owner do collector
deve controlar sua duração.

Separe estado durável de evento momentâneo. Estado deve poder ser coletado novamente e
reconstruir a tela. Um evento de navegação ou mensagem deve ter uma política clara para
replay, consumo e rotação de configuração.

## Testes

Teste emissões, ordem, conclusão, erros, cancelamento, retry e concorrência. Verifique que:

- cold flows executam a quantidade esperada de vezes;
- `stateIn` possui estado inicial correto;
- `SharedFlow` tem replay e buffer esperados;
- collectors são cancelados com o lifecycle;
- callbacks são removidos;
- retries não duplicam efeitos;
- debounce, timeout e operadores temporais têm comportamento determinístico.

Ferramentas como Turbine podem facilitar asserções sobre emissões, mas não substituem testes
de integração da fonte real, do banco ou do transporte.

## Relação com ReactiveX

Flow e ReactiveX compartilham ideias como streams, operators, cold e hot, erros e
cancelamento. Eles não possuem contratos idênticos. Flow integra suspensão e structured
concurrency; ReactiveX tradicionalmente expressa concorrência por Observables, schedulers,
Disposable e variantes com backpressure.

Ao migrar entre os modelos, revise:

- quem inicia a execução;
- se o stream é cold ou hot;
- como cancelar a fonte;
- se existe demanda ou somente buffer;
- onde erros terminam;
- como schedulers viram dispatchers;
- como replay, estado e eventos são preservados;
- como a interoperabilidade trata blocos e backpressure.

## Fontes primárias

- [Kotlin Flow](https://kotlinlang.org/docs/flow.html)
- [Kotlin coroutines and Flow](https://kotlinlang.org/docs/coroutines-flow.html)
- [Flow API](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/)
- [StateFlow API](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/)
- [SharedFlow API](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-shared-flow/)
- [shareIn](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/share-in.html)
- [ReactiveX](https://reactivex.io/)
