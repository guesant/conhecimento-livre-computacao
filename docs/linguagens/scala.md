# Scala

Scala é uma linguagem de tipagem estática que combina orientação a objetos e
programação funcional. Ela é usada principalmente na JVM, interoperando com
Java e com bibliotecas do ecossistema Java. Scala 3 também possui compilação
para JavaScript e WebAssembly em cenários suportados pelo toolchain.

## Tipos e composição

Classes, traits, enums, funções, pattern matching, tipos algébricos e
typeclasses permitem modelar domínios com diferentes estilos. A linguagem
oferece inferência de tipos, mas contratos públicos devem ser explicitados
quando isso melhora a leitura, a estabilidade de APIs e as mensagens de erro.

Recursos como `given`, `using`, extensões e tipos opacos ajudam a compor
abstrações sem expor detalhes de implementação. Eles também podem tornar o
código difícil de entender quando combinados sem convenções. A equipe deve
preferir designs que deixem resolução implícita, efeitos e dependências
visíveis nas fronteiras importantes.

## JVM e interoperabilidade

Na JVM, Scala compartilha garbage collector, threads, classpath, bibliotecas
de sistema e ferramentas de observabilidade com aplicações Java. O bytecode e
as APIs geradas precisam ser compatíveis com a versão do JDK, o framework e o
modelo de módulos usados em produção.

Interoperabilidade não significa que qualquer biblioteca Java terá uma API
idiomática em Scala. Conversões entre coleções, nullability, exceções,
`Future`, tipos funcionais e callbacks devem ser tratadas como fronteiras
explícitas.

## Concorrência e efeitos

A linguagem não impõe um modelo único de concorrência. Aplicações podem usar
threads e executors da JVM, `Future`, actors ou bibliotecas funcionais. A
escolha deve considerar cancelamento, supervisão, ordenação, backpressure,
observabilidade e integração com I/O.

`Future` pode iniciar trabalho imediatamente, enquanto abstrações como `IO`
podem descrever uma operação antes de executá-la. Confundir descrição com
execução pode gerar chamadas duplicadas, tarefas sem dono e testes instáveis.

## Build e versões

Scala possui toolchains e bibliotecas que precisam ser alinhados ao JDK, ao
binary version, ao framework e às dependências transitivas. Fixe versões,
resolva conflitos de classpath e gere artefatos em um ambiente controlado.

Uma migração entre versões major pode exigir mudanças de sintaxe, macros,
derivação, collections e plugins. Faça a migração por etapas, compile todos os
módulos e valide o comportamento em runtime, não apenas a aceitação do
compilador.

## Escolha

Scala é interessante para sistemas que se beneficiam do ecossistema Java e de
abstrações funcionais mais expressivas. O custo está na complexidade da
linguagem, no tempo de compilação, na variedade de estilos e na necessidade de
padronizar bibliotecas de efeitos, logging, testes e concorrência.

## Relações

- [Java](java.md) e [JVM](jvm.md) explicam a plataforma de execução principal.
- [Kotlin](kotlin.md) é outra linguagem JVM com foco em interoperabilidade e
  redução de boilerplate.
- [Haskell](haskell.md) oferece um modelo funcional mais uniforme.

## Fontes primárias

- [Scala documentation](https://docs.scala-lang.org/)
- [Scala 3 reference](https://docs.scala-lang.org/scala3/reference/)
- [Scala language specification](https://scala-lang.org/files/archive/spec/2.13/)
- [Scala source repository](https://github.com/scala/scala3)
