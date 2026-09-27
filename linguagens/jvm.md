# Java Virtual Machine

JVM é uma máquina virtual que define um modelo de execução para bytecode de
classes. Java é a linguagem mais conhecida nesse ecossistema, mas não é a
única. Kotlin, Scala, Groovy, Clojure e outras linguagens podem produzir
bytecode compatível ou interagir com bibliotecas Java.

## Class files e carregamento

O compilador produz class files com bytecode, tabela de constantes, metadados
e informações de métodos. Class loaders localizam e carregam classes segundo
uma estratégia de delegação. Verificação, linking e inicialização acontecem em
etapas diferentes e podem falhar em momentos distintos.

Isso torna importante separar erro de compilação, classe ausente, conflito de
versão, erro de inicialização estática e incompatibilidade binária. Um fat jar
ou um classpath que funciona localmente ainda pode carregar outra versão em
produção.

## Memória e execução

A JVM administra heaps de objetos, áreas de metadados, stacks de threads e
buffers nativos. O garbage collector identifica objetos não alcançáveis, mas
recursos fora do heap precisam de fechamento explícito. A JVM pode interpretar
bytecode e compilar métodos quentes com JIT, usando informações observadas
durante a execução.

Flags de heap, collector, thread stacks, metaspace e direct buffers devem ser
dimensionadas em relação ao limite de memória do container. O processo pode
ser encerrado pelo kernel antes de a JVM produzir um erro de falta de heap se
o consumo nativo exceder o limite do cgroup.

## Threads e observabilidade

Threads de aplicação, pools, garbage collector, compilador e bibliotecas nativas
competem por CPU. Thread dump, heap dump, JFR, métricas de GC e logs de
class loading respondem perguntas diferentes. Colete-os com controle de
acesso, porque dumps podem conter dados sensíveis.

O diagnóstico deve separar CPU consumida, tempo bloqueado, espera por lock,
fila do executor, I/O e pausa de GC. Aumentar heap ou threads sem observar o
causal pode apenas deslocar o gargalo.

## Compatibilidade

Uma aplicação depende da versão da linguagem, do bytecode, da JVM, das
bibliotecas e do sistema operacional. APIs internas e flags experimentais
podem quebrar em atualizações. Prefira APIs documentadas, registre o target de
compilação e teste a combinação de runtime e dependências em uma imagem
reproduzível.

## Relações

- [Java](java.md) explica a linguagem mais associada à JVM.
- [Kotlin](kotlin.md) explica uma linguagem moderna com alvo JVM.
- [V8](../sistemas/runtime/v8.md) é uma engine JavaScript, não uma JVM.
- [Runtime](../sistemas/runtime/index.md) compara engine, bibliotecas e host.

## Fontes primárias

- [Java Virtual Machine Specification](https://docs.oracle.com/javase/specs/)
- [OpenJDK HotSpot](https://openjdk.org/groups/hotspot/)
- [Java Flight Recorder](https://docs.oracle.com/javacomponents/jmc-8/jfr-runtime-guide/)
