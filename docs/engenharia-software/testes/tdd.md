# TDD

Test-driven development, ou TDD, é uma prática de desenvolvimento em que a
equipe escreve primeiro um teste que expressa um comportamento desejado,
observa a falha, implementa a menor mudança que faz o teste passar e depois
refatora o código preservando os testes.

O ciclo costuma ser descrito como:

1. Red, escrever um teste que falha por uma razão relevante.
2. Green, implementar o suficiente para satisfazer o teste.
3. Refactor, melhorar design, nomes, duplicação e acoplamento sem mudar o
   comportamento protegido.

O teste inicial não é somente uma verificação posterior. Ele funciona como uma
pergunta concreta sobre a interface de uma unidade e força a equipe a pensar
em entradas, saídas, estados inválidos e dependências antes de consolidar a
implementação.

## O que TDD ajuda a revelar

Uma unidade difícil de testar pode ter responsabilidades demais, dependências
ocultas, efeitos colaterais acoplados ou uma interface pouco clara. O ciclo
curto torna esses problemas visíveis enquanto a mudança ainda é pequena. A
refatoração transforma essa evidência em um design mais coeso, em vez de
apenas adicionar mais mocks.

TDD também cria uma regressão executável para o comportamento desenvolvido.
Isso não garante que os requisitos foram descobertos corretamente, que a
integração funciona ou que a experiência do usuário é adequada. Para isso são
necessários testes de integração, contrato, segurança e end-to-end.

## O que TDD não é

TDD não significa testar cada linha, escrever testes sem entender o domínio ou
proibir testes manuais. Também não exige que qualquer teste seja unitário. Um
time pode aplicar o ciclo a uma unidade, a um componente ou a um contrato,
desde que o feedback seja rápido o bastante para orientar a mudança.

Um teste que replica detalhes privados da implementação pode passar enquanto
o comportamento visível está errado. Prefira expressar a regra através de
interfaces e resultados observáveis.

## Limites

TDD é menos direto quando o comportamento ainda é desconhecido, quando a
interface depende de exploração visual ou quando o custo de montar o ambiente
é maior que o ciclo de mudança. Nessas situações, protótipos, testes
exploratórios, exemplos e experimentos podem anteceder a especificação
automatizada.

Depois que o comportamento for compreendido, transforme os exemplos relevantes
em testes estáveis. A suíte deve permanecer pequena o bastante para dar
feedback e abrangente o bastante para proteger as decisões importantes.

## Relação com BDD

TDD normalmente opera próximo ao design de unidades e contratos de código.
BDD organiza exemplos em uma linguagem compartilhada com pessoas do negócio e
do produto. As duas práticas podem coexistir. Um cenário BDD não substitui
testes unitários, e um teste unitário não substitui a validação de uma jornada
de negócio.

## Fontes

- [Test-Driven Development, Martin Fowler](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
- [BDD e Gherkin](../requisitos/bdd-e-gherkin.md)
- [Testes de software](index.md)
