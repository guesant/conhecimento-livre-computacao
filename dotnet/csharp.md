# C Sharp

C# é uma linguagem estaticamente tipada do ecossistema .NET. Ela compila para
IL, que é executado por um runtime .NET, normalmente com JIT ou com uma forma
de publicação nativa conforme o projeto. A linguagem oferece orientação a
objetos, records, pattern matching, generics, delegates, async/await, LINQ e
recursos funcionais.

## Tipos e memória

Value types e reference types têm custos e semânticas diferentes. Boxing,
alocações, cópias, closures e iteradores podem alterar o desempenho de um
caminho aparentemente simples. O garbage collector administra objetos
gerenciados, mas streams, sockets, handles e transações continuam exigindo
`Dispose` ou `using`.

Nullable reference types melhoram a análise estática, mas não validam dados que
chegam da rede, do banco ou de reflection. Validação de entrada e invariantes
de domínio permanecem responsabilidade da aplicação.

## Async e concorrência

`Task` representa trabalho assíncrono. `async` e `await` evitam bloquear uma
thread enquanto uma operação suspensível aguarda, mas não tornam um cálculo
CPU-bound paralelo. Use cancellation tokens, limites de concorrência e
timeouts. Evite bloquear `Task` com `.Result` ou `.Wait()` em caminhos que
possam causar starvation ou deadlock.

LINQ facilita transformações, mas enumeração tardia pode repetir consultas,
reter estado ou executar código em um momento diferente do esperado. Em
consulta de banco, deixe claro o limite entre expressão traduzida pelo
provider e processamento local.

## Plataforma e operação

O SDK compila, testa, empacota e publica. O runtime executa a aplicação e as
bibliotecas base definem APIs comuns. Uma aplicação pode ser publicada
dependente do runtime ou self-contained, com impacto diferente em tamanho,
patching e responsabilidade operacional.

Monitore heap, GC, threads, filas, sockets, exceções, tempo de request e
dependências externas. Em containers, alinhe GC, memória e CPU aos limites do
cgroup.

## Relações

- [.NET](index.md) é a plataforma de execução e bibliotecas.
- [ASP.NET](asp-net.md) fornece a pilha web.
- [F#](fsharp.md) é outra linguagem do .NET.
- [Polly](polly.md) trata resiliência em aplicações .NET.

## Fontes primárias

- [C# guide](https://learn.microsoft.com/en-us/dotnet/csharp/)
- [C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/)
- [.NET documentation](https://learn.microsoft.com/en-us/dotnet/)
