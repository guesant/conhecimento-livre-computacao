# Complexidade cognitiva

Complexidade cognitiva estima o esforço mental necessário para entender o fluxo de um código. A métrica foi criada pela SonarSource para complementar a complexidade ciclomática: duas funções podem ter quantidade parecida de caminhos, mas uma pode exigir muito mais esforço por causa de aninhamento, saltos e decisões espalhadas.

## O que a métrica observa

A contagem costuma aumentar quando há quebras no fluxo linear, como condicionais, loops, `catch`, operadores de curto-circuito e chamadas recursivas. Aninhamento adiciona peso porque uma decisão dentro de outra exige manter mais contexto mental. Estruturas que são idiomáticas e fáceis de ler podem receber tratamento diferente conforme a linguagem e o analisador.

Uma cadeia profundamente aninhada pode ser difícil de entender mesmo que tenha poucos caminhos independentes. Uma sequência plana de guard clauses pode ter decisões equivalentes e ser mais legível. A métrica tenta refletir essa diferença, mas continua sendo uma aproximação baseada em regras, não uma leitura completa da intenção do programa.

## Comparação com complexidade ciclomática

Complexidade ciclomática pergunta quantos caminhos de controle independentes existem e é útil para raciocinar sobre testes. Complexidade cognitiva pergunta quanta estrutura e contexto uma pessoa precisa acompanhar para compreender o fluxo.

| Situação | Ciclomática | Cognitiva | Interpretação |
| --- | ---: | ---: | --- |
| Muitos casos simples em uma tabela clara | pode subir | pode permanecer moderada | há caminhos, mas a estrutura pode ser previsível |
| Condicionais profundamente aninhadas | sobe | sobe mais | caminhos e contexto mental se acumulam |
| Guard clauses sequenciais | sobe | tende a ser menor | decisões sem empilhamento de contexto |
| Muitas chamadas delegadas | pode parecer baixa | pode esconder custo | o leitor precisa atravessar vários arquivos |

As duas métricas são sinais, não veredictos. Uma arquitetura que espalha uma decisão simples em dez classes pode reduzir a métrica de uma função e aumentar a dificuldade de compreensão do sistema.

## Como usar

Use a métrica por função para encontrar pontos de revisão. Leia o código, entenda o domínio, examine testes e verifique se a função possui mais de uma responsabilidade. Extraia uma decisão quando ela representar uma regra coerente, dê nome ao conceito e preserve o fluxo principal. Use tipos discriminados, tabelas de decisão ou máquinas de estado quando eles tornarem estados e transições mais explícitos.

Não use uma função delegada apenas para diminuir a contagem. `process()` que chama `processInternal()` não ficou melhor se a segunda função continua com a mesma responsabilidade e o leitor precisa saltar para outro arquivo. A redução legítima muda a coesão, o acoplamento, o nível de abstração ou a testabilidade.

## Limites e qualidade gates

Um limite deve ser calibrado pela linguagem, pelo tipo de código e pelo risco. Handlers de entrada, renderizadores, parsers e regras de domínio podem ter necessidades diferentes. Um limite baixo pode detectar cedo uma mistura de responsabilidades; um limite alto pode evitar ruído em código declarativo ou em uma máquina de estados legítima.

Antes de bloquear o CI, rode a métrica no corpus existente, categorize os achados e confirme que a regra mede o problema desejado. Depois fixe o limite, acompanhe tendência e permita exceções raras com justificativa explícita. Nunca transforme o número em objetivo isolado nem aceite uma refatoração que apenas distribui a mesma complexidade.

## Relação com design

Complexidade cognitiva é afetada por nomes, domínio, coesão, dependências, tamanho de abstrações, repetição, acoplamento e consistência. Uma função curta pode ser difícil porque usa nomes vagos ou efeitos implícitos. Uma função longa pode ser relativamente compreensível se representar uma tabela de dados linear e bem nomeada, embora ainda deva ser revisada por manutenção e testes.

Combine a métrica com revisão humana, cobertura, complexidade ciclomática, tamanho de função, duplicação, dependências e histórico de defeitos. A pergunta final não é “qual é o número?”, mas “quanto contexto uma pessoa precisa manter para alterar este comportamento com segurança?”.

## Relações

- [Complexidade ciclomática](complexidade-ciclomatica.md) mede caminhos de controle.
- [Clean Code](clean-code.md) discute nomes, funções, comentários, testes e refatoração.
- [Arquitetura Limpa](arquitetura-limpa.md) discute dependências entre políticas e detalhes.
- [Análise de complexidade](analise-de-complexidade.md) trata custo assintótico de algoritmos.

## Fontes

- [SonarSource, Cognitive Complexity](https://www.sonarsource.com/resources/cognitive-complexity/)
- [SonarQube, definições de métricas](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/code-metrics/metrics-definition)
- [Validação empírica da complexidade cognitiva](https://arxiv.org/abs/2007.12520)
