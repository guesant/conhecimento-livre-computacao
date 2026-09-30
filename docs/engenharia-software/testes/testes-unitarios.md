# Testes unitários

Teste unitário verifica uma unidade coerente de comportamento em isolamento
controlado. A unidade pode ser uma função, uma classe, um módulo ou outra
fronteira pequena definida pelo design. O tamanho físico não é o critério
principal. O importante é que o teste tenha uma hipótese clara e consiga
localizar a causa provável de uma falha.

Um teste unitário normalmente prepara entradas, executa a operação e verifica
um resultado ou uma mudança observável. Dependências externas, como banco,
rede, relógio, filesystem e serviços remotos, podem ser substituídas por
colaboradores controlados quando o objetivo é testar a regra local.

## Isolamento sem falsidade

Mock, stub, fake e spy são técnicas diferentes para controlar ou observar uma
dependência. O isolamento deve reduzir ruído, não esconder um contrato
importante. Se o comportamento depende de SQL, serialização, transação ou
configuração real, um teste unitário não deve ser a única evidência.

Mocks excessivos tornam o teste acoplado à implementação. Uma refatoração
interna passa a exigir alterações mesmo quando o comportamento público não
mudou. Prefira verificar resultados, efeitos e chamadas que fazem parte do
contrato, deixando detalhes privados fora da asserção.

## Propriedades de uma boa unidade

Um teste unitário útil é determinístico, rápido, isolado, legível e específico
quando falha. Ele deve controlar tempo, aleatoriedade, locale, timezone e
ordem dos dados quando esses elementos não fazem parte da hipótese.

Casos importantes incluem valores normais, limites, ausência de dados, entradas
inválidas, permissões, erros de dependência e idempotência. Não confunda
quantidade de casos com qualidade: o conjunto deve representar as decisões e
os riscos da unidade.

## Relação com outras camadas

Teste unitário não demonstra que uma aplicação consegue iniciar, consultar o
banco ou renderizar uma jornada no navegador. Testes de integração cobrem
fronteiras reais. Testes de componente verificam a composição imediata.
Testes end-to-end protegem fluxos críticos. A escolha da camada deve refletir
o defeito que se quer detectar e o tempo de feedback aceitável.

## TDD

TDD usa frequentemente testes unitários porque eles permitem o ciclo Red,
Green, Refactor com feedback curto. Isso é uma consequência do custo e do
isolamento, não uma exigência de que todo TDD produza apenas testes unitários.

## Diagnóstico de testes frágeis

Um teste que falha apenas por ordem de execução, horário, rede, animação,
texto incidental ou estado deixado por outro caso não está protegendo uma
hipótese estável. Corrija a causa, isole os dados e torne o relógio ou a
aleatoriedade explícitos quando forem relevantes ao comportamento.
