# Mapa de BDD e Gherkin

Behavior-Driven Development, BDD, é uma abordagem de descoberta e desenvolvimento baseada
em colaboração, linguagem compartilhada e exemplos concretos de comportamento. Dan North
formulou o termo para aproximar desenvolvimento, testes e entendimento do negócio. O objetivo
não é simplesmente aumentar a quantidade de testes automatizados. É reduzir ambiguidades antes
da implementação e manter exemplos que expliquem o comportamento esperado.

## BDD não é apenas Cucumber

BDD é uma prática de colaboração. Cucumber é uma ferramenta que lê especificações e executa
cenários por meio de definições de passos. Gherkin é a linguagem estruturada usada para escrever
essas especificações. Uma equipe pode praticar BDD com exemplos, workshops e testes sem usar
Cucumber, e pode usar Cucumber sem praticar colaboração real.

O ciclo costuma ser chamado de descoberta por exemplos: discutir o comportamento, formular
exemplos, automatizar os exemplos relevantes, implementar e manter o resultado como documentação
executável. A conversa continua sendo necessária quando um cenário falha ou o domínio muda.

## Estrutura do Gherkin

Gherkin usa palavras-chave como `Feature`, `Rule`, `Scenario`, `Given`, `When`, `Then`, `And`,
`But`, `Background`, `Scenario Outline` e `Examples`. Os nomes podem ser localizados para
outros idiomas, mas os arquivos precisam seguir a gramática reconhecida pelo runner.

```gherkin
Feature: Recuperar uma conta

  Rule: O proprietário precisa provar sua identidade

    Example: Código válido
      Given a pessoa solicitou a recuperação da conta
      When ela informa um código ainda válido
      Then a conta fica disponível para redefinição de senha

    Example: Código expirado
      Given a pessoa solicitou a recuperação da conta
      When ela informa um código expirado
      Then a redefinição é recusada
```

`Given` estabelece o contexto, `When` representa um evento ou ação e `Then` descreve um
resultado observável. `Rule` agrupa cenários que ilustram uma regra de negócio. `Scenario
Outline` combina um cenário com uma tabela de exemplos quando o mesmo comportamento precisa ser
verificado com vários dados.

## Especificação por comportamento

Um cenário deve descrever o que importa para o usuário ou para um sistema externo, não como a
implementação funciona. "Quando o cliente solicita a recuperação" é mais estável que "quando o
cliente clica no botão azul e o navegador chama o endpoint X". A implementação pode mudar sem
que a regra de negócio mude.

O resultado deve ser observável. Verificar diretamente uma linha interna do banco pode ser útil
em um teste de integração, mas frequentemente não é o melhor `Then` de uma especificação de
comportamento. Prefira resposta, mensagem, evento, disponibilidade de recurso ou outro efeito
que um ator consiga observar.

## Three Amigos

A conversa pode reunir quem entende o negócio, quem desenvolve e quem testa. Cada participante
contribui com perguntas diferentes: qual é o valor, qual regra foi esquecida e como obteremos
evidência. O encontro não precisa produzir dezenas de cenários. Ele deve revelar exemplos e
limites que reduzam interpretações divergentes.

## Critérios para bons cenários

- um cenário deve ilustrar uma regra ou comportamento relevante;
- o nome deve explicar o resultado ou a situação importante;
- o texto deve esconder detalhes de interface e infraestrutura desnecessários;
- o contexto deve ser curto e significativo;
- o resultado deve ser observável;
- exemplos devem cobrir sucesso, rejeição, ausência, conflito e limites quando forem relevantes;
- passos repetidos devem ter uma linguagem comum para evitar duplicação semântica;
- tags e fixtures devem organizar a execução sem substituir a compreensão do domínio.

## Cucumber e definições de passos

Cucumber relaciona cada passo a uma definição de código. Essas definições preparam contexto,
disparam uma ação e fazem asserções. Não coloque toda a lógica no arquivo `.feature`. Também
não esconda uma sequência de passos genéricos tão grande que o cenário deixe de explicar o
comportamento.

Arquivos de feature devem ser versionados junto do software e tratados como contrato vivo. A
equipe precisa remover cenários que já não descrevem comportamento válido, corrigir definições
de passos duplicadas e evitar que um teste de interface frágil represente uma regra que poderia
ser verificada em nível mais estável.

## BDD, TDD e testes

BDD e TDD se relacionam, mas operam em níveis diferentes. TDD normalmente conduz o desenho de
unidades por ciclos de teste, implementação e refatoração. BDD começa pelo comportamento e pela
linguagem compartilhada, podendo resultar em testes de aceitação, integração ou contrato. Um
cenário BDD não substitui testes unitários, de integração, segurança, desempenho ou operação.

## Quando não usar Cucumber

Cucumber pode custar caro quando o domínio é simples, quando ninguém participa da manutenção
dos cenários ou quando os arquivos viram scripts detalhados de interface. Um teste de contrato,
uma tabela de decisão ou um teste de unidade pode expressar melhor uma regra local. O critério
é o valor da linguagem compartilhada e da especificação, não a quantidade de palavras-chave
`Given` e `Then`.

## Relações

- [Use Cases](use-cases.md) organiza objetivos, atores e fluxos.
- [Requisitos funcionais e regras de negócio](requisitos-funcionais-e-regras-de-negocio.md)
  define comportamentos e políticas.
- [Engenharia de requisitos](engenharia-de-requisitos.md) trata elicitação e validação.
- [Backlog e hierarquia de trabalho](backlog-e-hierarquia.md) explica como exemplos entram no
  planejamento sem confundir feature de BDD com item de backlog.

## Fontes primárias

- [Cucumber](https://cucumber.io/docs/)
- [Referência do Gherkin](https://cucumber.io/docs/gherkin/reference/)
- [Quem faz o quê em Cucumber](https://cucumber.io/docs/bdd/who-does-what/)
- [Gherkin orientado a comportamento](https://cucumber.io/docs/bdd/better-gherkin/)
