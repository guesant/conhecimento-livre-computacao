# F Sharp

F# é uma linguagem funcional-first que executa no .NET. Ela combina funções,
imutabilidade e tipos algébricos com acesso às bibliotecas, ferramentas e
runtime do ecossistema .NET. O estilo funcional é uma forma de estruturar o
domínio, não uma garantia de que toda biblioteca chamada pelo programa seja
imutável ou livre de efeitos.

## Modelagem

Inferência de tipos, records, discriminated unions, pattern matching e funções
de primeira classe permitem representar estados válidos de forma explícita.
Uma union pode separar estados como carregando, sucesso e falha sem recorrer a
combinações ambíguas de flags.

Imutabilidade reduz alterações acidentais e facilita raciocínio sobre
concorrência, mas I/O, banco, relógio e rede continuam sendo efeitos. Separe
funções puras das bordas do sistema e injete dependências que representam esses
efeitos.

## Interoperabilidade

F# pode consumir assemblies .NET, APIs C# e bibliotecas do runtime. Diferenças
de convenção, overloads, nullability, mutabilidade e representação podem
exigir adapters. Um domínio F# não deve aceitar automaticamente tipos mutáveis
de qualquer camada sem definir onde a conversão ocorre.

Async, tasks e bibliotecas de concorrência precisam ser compostos com atenção
ao cancellation token, exceções e scheduler. Uma função assíncrona pode ser
correta em isolamento e ainda produzir concorrência ilimitada quando usada em
um `map` sem limite.

## Casos de uso

F# é adequado para regras de negócio ricas, análise de dados, ferramentas e
serviços .NET que se beneficiam de tipos expressivos. A interoperabilidade
permite adoção gradual em uma solução existente. O custo aparece quando a
equipe não conhece o modelo funcional, quando bibliotecas assumem APIs
imperativas ou quando o toolchain e as convenções não são compartilhados.

## Fontes primárias

- [F# documentation](https://learn.microsoft.com/en-us/dotnet/fsharp/)
- [F# language reference](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/)
- [F# style guide](https://learn.microsoft.com/en-us/dotnet/fsharp/style-guide/)
