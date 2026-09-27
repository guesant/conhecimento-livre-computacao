# Kotlin

Kotlin é uma linguagem estaticamente tipada, concisa e interoperável com Java.
Ela pode produzir bytecode para a JVM e também possui alvos para JavaScript,
WebAssembly e código nativo conforme o projeto e a biblioteca usados. A
linguagem não deve ser confundida com Kotlin Flow, Android ou um framework
web: esses são partes diferentes do ecossistema.

## Tipos e modelagem

Null safety, inferência de tipos, data classes, sealed classes, extension
functions, generics e pattern matching por `when` ajudam a representar estados
de domínio. O compilador reduz uma classe de erros, mas valores externos,
reflexão, interoperabilidade Java e tipos platform ainda exigem validação.

Imutabilidade é uma prática útil, não uma propriedade automática de todos os
objetos. `val` impede reatribuição da referência, mas não torna um objeto
profundamente imutável. APIs de domínio devem definir quem pode alterar estado
e em qual transação.

## Coroutines

Coroutines representam trabalho suspensível sem exigir uma thread por operação.
Scopes estruturados associam o ciclo de vida do trabalho a um owner. Dispatchers
escolhem onde o trabalho executa, mas não transformam um cálculo CPU-bound em
I/O nem eliminam limites de CPU, rede ou banco.

`Flow` modela uma sequência assíncrona e pode ser cold ou compartilhado por
`StateFlow` e `SharedFlow`. A coleta precisa respeitar cancelamento, backpressure,
retry e lifecycle. O documento de [Kotlin Flow](../comunicacao/kotlin-flow.md)
trata essa composição em detalhe.

## Interoperabilidade e build

Kotlin pode chamar APIs Java e ser chamado por código Java, mas diferenças de
nullability, nomes gerados, properties, checked exceptions e coroutines podem
afetar a integração. O build deve fixar versão do compilador, plugin, target de
bytecode, JDK e dependências.

Em projetos multiplataforma, uma abstração comum não elimina as diferenças de
filesystem, threads, memória, APIs de rede e distribuição. O código específico
de cada alvo precisa ser testado no próprio runtime.

## Casos de uso e limites

Kotlin é usado em Android, serviços JVM, ferramentas, aplicações server-side e
projetos multiplataforma. É uma boa escolha quando interoperabilidade com Java,
coroutines e expressividade reduzem custo do domínio. Pode ser inadequado
quando o tamanho mínimo do runtime, toolchain muito simples ou integração com
uma ABI C específica forem prioridades maiores.

## Fontes primárias

- [Kotlin documentation](https://kotlinlang.org/docs/home.html)
- [Kotlin language reference](https://kotlinlang.org/spec/introduction.html)
- [Kotlin coroutines](https://kotlinlang.org/docs/coroutines-overview.html)
