# Streams reativos

Streams reativos representam sequências de valores ao longo do tempo, com operações para transformar, combinar, cancelar e observar esse fluxo. A categoria trata o modelo de composição e lifecycle do stream, não um protocolo de rede específico.

## Implementações

- [ReactiveX e Rx](../reactivex.md) define Observable, Observer, operadores, schedulers, hot e cold streams e backpressure.
- [Kotlin Flow](../kotlin-flow.md) integra streams suspensos ao modelo de coroutines do Kotlin.

Um stream pode ser frio, quando cada consumidor inicia seu próprio trabalho, ou quente, quando vários consumidores observam uma fonte compartilhada. Cancelamento e backpressure são parte do contrato. Um consumidor lento não deve produzir crescimento ilimitado de memória ou bloquear uma fonte crítica sem uma política explícita.

## Não confundir

Streams reativos não são o mesmo que event streaming. Um broker pode fornecer eventos duráveis e replayáveis, enquanto uma abstração reativa normalmente vive no processo e coordena valores em memória. Eles podem ser compostos, mas a durabilidade precisa vir de uma fila, log ou banco apropriado.
