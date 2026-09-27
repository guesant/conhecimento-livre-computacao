# Java

Java é uma linguagem de propósito geral, estaticamente tipada e orientada a
objetos, projetada para compilar código fonte em bytecode executado por uma
Java Virtual Machine. O ecossistema inclui a linguagem, as bibliotecas da
plataforma Java, ferramentas do JDK e implementações da JVM. Esses elementos
possuem ciclos de versão e responsabilidades diferentes.

## Linguagem

O compilador verifica tipos, resolve sobrecargas e produz arquivos de classe.
Interfaces, classes, records, generics, annotations, exceptions e módulos
permitem modelar aplicações grandes. O sistema de tipos não impede todos os
erros de runtime: nullability, concorrência, recursos externos e invariantes
de negócio ainda precisam ser tratados pela aplicação.

A biblioteca padrão fornece coleções, I/O, rede, concorrência, criptografia,
reflexão, serialização e ferramentas de data e hora. Dependências externas
devem ser avaliadas por compatibilidade, manutenção, segurança e custo de
inicialização, não somente pela quantidade de funcionalidades.

## Execução

O `javac` transforma fontes em bytecode. A JVM carrega classes, verifica
formatos e executa instruções. Ela pode interpretar caminhos inicialmente e
compilar métodos quentes com JIT. O garbage collector recupera objetos não
alcançáveis, mas não fecha automaticamente arquivos, sockets, transações ou
locks.

O desempenho depende de heap, pausas de GC, threads, class loading, alocações,
compilação e chamadas externas. Um benchmark precisa representar warmup,
concorrência, tamanho de dados e comportamento de produção.

## Concorrência

Threads, executors, futures, locks, atomics e estruturas concorrentes permitem
compor trabalho paralelo e concorrente. `synchronized` protege regiões e
invariantes, mas pode produzir contenção ou deadlock. APIs assíncronas e pools
precisam de limites, shutdown e propagação de cancelamento.

Mais threads não significam mais capacidade. O limite pode estar na CPU, no
banco, nos sockets, no pool de conexões ou no serviço externo. Meça fila,
tempo de espera e trabalho efetivo.

## Empacotamento e operação

O JDK fornece compilador, ferramentas e runtime de desenvolvimento. Uma
aplicação pode ser distribuída como classpath, módulo, imagem de container,
fat jar ou imagem nativa produzida por ferramentas específicas. O artefato
precisa declarar a versão da JVM, flags, locale, timezone, memória e
certificados esperados.

Em produção, monitore heap, pausas, threads, class loading, erros, filas,
latência e chamadas externas. Atualizações de JDK podem mudar defaults, TLS,
garbage collector e APIs removidas, portanto devem ser validadas em staging.

## Relações

- [JVM](jvm.md) explica a máquina virtual que executa o bytecode.
- [Kotlin](kotlin.md) usa a JVM e interoperabilidade com Java.
- [Threads](../engenharia-software/concorrencia/threads.md) e [virtual
  threads](../engenharia-software/concorrencia/virtual-threads.md) tratam os
  modelos de execução.

## Fontes primárias

- [Java documentation](https://docs.oracle.com/en/java/)
- [Java SE documentation](https://docs.oracle.com/en/java/javase/)
- [OpenJDK](https://openjdk.org/)
