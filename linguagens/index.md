# Linguagens de programação

Uma linguagem define sintaxe, semântica, tipos, modelo de execução e formas de
composição. Ela não é o mesmo que um runtime, uma biblioteca, um framework ou
uma plataforma de deploy. JavaScript pode executar em V8, SpiderMonkey ou
JavaScriptCore. Java e Kotlin podem executar na JVM. C# e F# normalmente
usam .NET, mas as responsabilidades do compilador, do runtime e da biblioteca
base continuam diferentes.

## Como comparar linguagens

Compare primeiro o tipo de problema e o contrato de execução, não somente a
velocidade de um benchmark. Pergunte se o sistema precisa de controle sobre
memória e representação de dados, coleta automática, interoperabilidade,
concorrência, distribuição, tempo de compilação, portabilidade, tamanho do
runtime, estabilidade de ABI e disponibilidade de bibliotecas.

Também importa o modelo de equipe. Uma linguagem pode ter excelentes
propriedades técnicas, mas ser inadequada se o ecossistema não oferece as
ferramentas de teste, observabilidade, segurança, build e suporte que o
projeto precisa.

## Relações

- [JavaScript](javascript.md) é uma linguagem dinâmica padronizada por
  ECMAScript. O ambiente hospedeiro fornece APIs como DOM, rede e filesystem.
- [Lua](lua.md) é uma linguagem dinâmica e embutível, comum em scripts e
  extensões controladas pelo host.
- [Java](java.md) é uma linguagem estática cujo bytecode normalmente é
  executado pela [JVM](jvm.md).
- [Kotlin](kotlin.md) aproveita a JVM e a interoperabilidade com Java, além de
  possuir alvos multiplataforma.
- [Scala](scala.md) combina orientação a objetos e programação funcional,
  principalmente sobre a JVM.
- [Haskell](haskell.md) organiza a programação em torno de funções, tipos e
  avaliação lazy.
- [Elixir](elixir.md) e [Erlang](erlang.md) usam a BEAM e o ecossistema OTP
  para concorrência, supervisão e distribuição.
- [C#](../dotnet/csharp.md) e [F#](../dotnet/fsharp.md) participam do
  ecossistema .NET. [ASP.NET](../dotnet/asp-net.md) é uma plataforma web, não
  uma linguagem.
- [D](d.md), [Go](go.md), [Rust](rust.md) e [V](v.md) produzem binários
  nativos com modelos diferentes de memória, concorrência e abstração.

## Compilação e execução

Uma linguagem pode ser compilada para código nativo, para bytecode, para
WebAssembly ou interpretada por uma engine. Essas categorias não são
mutuamente exclusivas. V8 pode interpretar e otimizar JavaScript com JIT; a
JVM pode interpretar bytecode e compilá-lo durante a execução; Rust, Go e D
normalmente produzem binários, embora ainda dependam de bibliotecas e do
ambiente operacional.

O artefato executável também não define sozinho o comportamento operacional.
Gerenciamento de memória, threads, event loop, sistema de módulos, carregamento
de plugins, criptografia, logs e configuração pertencem à combinação entre
linguagem, runtime, bibliotecas e aplicação.

## Fontes primárias

- [ECMAScript Language Specification](https://tc39.es/ecma262/)
- [Java documentation](https://docs.oracle.com/en/java/)
- [.NET documentation](https://learn.microsoft.com/en-us/dotnet/)
- [Rust documentation](https://www.rust-lang.org/learn)
- [Go documentation](https://go.dev/doc/)
