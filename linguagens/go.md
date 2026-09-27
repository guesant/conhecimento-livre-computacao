# Go

Go é uma linguagem compilada, estaticamente tipada e orientada a uma sintaxe
pequena, builds rápidos e bibliotecas de rede e concorrência. O compilador
produz um binário que inclui grande parte do runtime necessário, embora ainda
dependa do sistema operacional, libc em alguns cenários, certificados e
arquivos externos.

## Modelo de execução

Goroutines representam unidades leves de execução gerenciadas pelo runtime.
Canais podem comunicar goroutines, mas não substituem invariantes, transações
ou controle de backpressure. O scheduler distribui goroutines sobre threads do
processo e o desempenho depende também de bloqueios, syscalls, GC e recursos
externos.

Contextos carregam cancelamento, deadline e escopo de request. Eles não devem
ser usados como um saco genérico de parâmetros. Propague o contexto até o
banco, cliente HTTP e worker, e trate o cancelamento para liberar sockets,
locks e trabalho pendente.

## Tipos e composição

Interfaces são satisfeitas implicitamente. Isso facilita adapters pequenos,
mas pode esconder dependências quando uma interface grande é usada em várias
camadas. Structs, métodos e composição normalmente substituem hierarquias de
herança.

Erros são valores e devem receber contexto, classificação e tratamento
coerente. `panic` é apropriado para invariantes impossíveis ou falhas de
inicialização muito específicas, não para erro esperado de rede ou validação.

## Toolchain e operação

O toolchain inclui `go`, modules, testes, benchmark, vet, formatting e suporte
a profiling. Fixe a versão do Go e o checksum das dependências. Reproduzir o
build exige controlar flags, ambiente, base image e arquivos incorporados.

Limites de goroutines, conexões, filas e workers precisam ser explícitos. Uma
aplicação pode parecer leve até receber uma goroutine por request sem limite ou
uma fila interna sem backpressure.

## Fontes primárias

- [Go documentation](https://go.dev/doc/)
- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [Effective Go](https://go.dev/doc/effective_go)
- [Go memory model](https://go.dev/ref/mem)
