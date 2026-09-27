# Haskell

Haskell é uma linguagem funcional de tipagem estática, forte e expressiva. Seu
modelo favorece funções puras, tipos algébricos, typeclasses e avaliação lazy.
O compilador mais utilizado é o GHC, que produz código nativo, bytecode ou
outros artefatos conforme o alvo e a configuração.

A linguagem não é apenas uma coleção de funções sem estado. Efeitos como I/O,
concorrência e mutação controlada são modelados por bibliotecas e tipos, o que
permite separar a descrição de uma operação de sua execução.

## Tipos e pureza

Uma função pura produz o mesmo resultado para as mesmas entradas e não altera
estado observável. Essa propriedade facilita testes, raciocínio local e
paralelização, mas não significa que todo programa Haskell seja automaticamente
rápido ou livre de efeitos.

Tipos algébricos e pattern matching permitem representar estados válidos e
falhas explicitamente. Typeclasses descrevem capacidades comuns sem exigir
herança nominal. O desenho do modelo de tipos pode reduzir estados inválidos,
mas tipos excessivamente complexos também aumentam o custo de aprendizado e de
diagnóstico.

## Avaliação lazy

A avaliação lazy adia o cálculo até que o valor seja necessário. Isso permite
compor estruturas potencialmente infinitas e pipelines declarativos. Também
pode acumular thunks, que são computações pendentes ocupando memória, quando o
programa não força os resultados no momento adequado.

Problemas de espaço devem ser analisados observando alocações, retenção,
strictness e garbage collection. Inserir avaliação estrita indiscriminadamente
pode alterar semântica, enquanto deixar tudo lazy pode aumentar latência e
memória. O caminho correto é medir e escolher a avaliação adequada para cada
estrutura.

## Efeitos, I/O e concorrência

O tipo `IO` representa ações que o runtime executará, em vez de afirmar que o
programa é puro no sentido de não realizar I/O. Monads, applicatives e outras
abstrações compõem essas operações. O runtime do GHC oferece threads leves,
MVars, STM e bibliotecas para concorrência e comunicação.

Concorrência ainda exige limites, cancelamento, timeouts, backpressure e
tratamento de exceções. Um tipo sofisticado não impede deadlocks, starvation,
contenção ou saturação de um serviço externo.

## Toolchain

O projeto pode usar GHC, Cabal, Stack, Hackage e ferramentas de linguagem. A
reprodutibilidade depende de fixar a versão do compilador, o solver, os
pacotes, flags, sistema operacional e bibliotecas nativas. Registre o plano de
dependências e teste os artefatos na arquitetura de produção.

## Escolha

Haskell é útil quando modelagem funcional, correção local, abstrações de tipos e
composição são prioridades. É uma escolha mais exigente quando a equipe não
domina lazy evaluation, profiling e o ecossistema de build. A decisão deve
considerar manutenção de longo prazo, contratação, observabilidade, integração
com bibliotecas C e requisitos de latência.

## Relações

- [Scala](scala.md) combina recursos funcionais e orientados a objetos na JVM.
- [Elixir](elixir.md) e [Erlang](erlang.md) usam o modelo de processos da BEAM,
  que é diferente do runtime do GHC.
- [Rust](rust.md) e [Go](go.md) oferecem alternativas compiladas com outros
  modelos de memória e concorrência.

## Fontes primárias

- [Haskell documentation](https://www.haskell.org/documentation/)
- [Haskell language](https://www.haskell.org/)
- [GHC User's Guide](https://downloads.haskell.org/ghc/latest/docs/users_guide/)
- [Haskell 2010 Language Report](https://www.haskell.org/onlinereport/haskell2010/)
