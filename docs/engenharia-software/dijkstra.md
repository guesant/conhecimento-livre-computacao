# Edsger W. Dijkstra

Edsger Wybe Dijkstra foi um cientista da computação neerlandês cuja influência atravessa
algoritmos, linguagens, sistemas operacionais, concorrência, sistemas distribuídos,
verificação formal e educação em programação. Sua relevância não está somente em um
algoritmo de caminhos mínimos. Ela está na mudança de como programas podem ser projetados:
como objetos estruturados, argumentáveis e derivados de invariantes, em vez de mecanismos
que são apenas testados até parecerem funcionar.

O [arquivo de Dijkstra mantido pela Universidade do Texas](https://www.cs.utexas.edu/~EWD/)
organiza manuscritos, relatórios, notas técnicas e transcrições que mostram a amplitude
desse trabalho. A lista abaixo cobre as linhas principais de contribuição, não cada artigo
ou cada algoritmo que ele publicou.

## Por que ele é relevante

Dijkstra ajudou a consolidar a computação como uma disciplina de raciocínio. Em uma época
em que programas eram frequentemente descritos como sequências de instruções e depurados
por tentativa, ele insistiu que estrutura, invariantes, provas e abstrações matemáticas
deveriam participar da construção do programa.

Essa atitude produz consequências práticas atuais:

- um fluxo com menos estados implícitos é mais fácil de testar e revisar;
- uma invariável explícita revela quais concorrências são permitidas;
- uma prova ou argumento formal pode encontrar falha antes de uma execução;
- uma abstração só vale se preservar a propriedade que o sistema precisa;
- simplicidade reduz estados possíveis e, com eles, caminhos de falha.

O reconhecimento institucional inclui o ACM Turing Award de 1972 por contribuições
fundamentais ao desenvolvimento de linguagens de programação. O [ACM Turing
Award](https://amturing.acm.org/?pg=awards.html) reconhece contribuições de importância
duradoura para a computação.

## Algoritmo de Dijkstra

O algoritmo de Dijkstra resolve caminhos mínimos de uma origem para os vértices alcançáveis
de um grafo com pesos não negativos. Ele mantém uma estimativa para cada vértice,
seleciona o vértice não finalizado com menor estimativa e relaxa suas arestas.

Quando a menor estimativa é escolhida, ela é definitiva porque nenhum caminho futuro com
pesos não negativos pode chegar a uma distância menor. Essa propriedade deixa de ser válida
com pesos negativos. Para esses casos, Bellman-Ford ou outro método apropriado responde a
uma pergunta diferente.

A estrutura de dados altera o custo: uma busca linear do menor vértice, um heap binário,
um heap de Fibonacci e estruturas especializadas produzem trade-offs diferentes. A ideia
algorítmica não deve ser confundida com uma implementação única.

Dijkstra também publicou algoritmos relacionados a árvores geradoras mínimas. O próprio
arquivo registra que ele publicou algoritmos de caminho mínimo e árvore geradora mínima;
as páginas [EWD 1000](https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1000.html) e
[EWD 316](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD316.7.html) preservam
parte desse material.

## Estruturação de programas

Em *Notes on Structured Programming*, Dijkstra tratou estrutura como uma ferramenta de
compreensão e derivação. A programação estruturada não é apenas uma regra estética de
evitar `goto`. Ela procura construir fluxos com composição, seleção, repetição, escopo e
invariantes que possam ser compreendidos localmente.

O resultado prático é reduzir a distância entre a especificação e o código. Um loop deve
ter uma condição de entrada, uma invariável que permanece verdadeira e uma medida que
ajuda a argumentar sobre terminação. Uma função deve deixar claro quais estados recebe e
quais propriedades produz.

O artigo [Notes on Structured Programming](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html)
trata composição passo a passo, prova de correção e limites da compreensão humana.

## Correção formal e weakest precondition

Dijkstra formulou o cálculo de predicate transformers e a ideia de weakest precondition.
Para um programa `S` e uma pós-condição `R`, `wp(S, R)` é a condição mais fraca sobre o
estado inicial que garante que `S` termina corretamente deixando `R` verdadeira.

Isso inverte o hábito de começar pelo código e tentar adivinhar se ele funciona. Começa-se
pela propriedade desejada, deriva-se a condição necessária e verifica-se se a entrada
realmente a satisfaz. A abordagem apoia provas, geração de programas, verificação de
invariantes e raciocínio sobre loops.

O conceito não significa que toda aplicação deva ser formalmente provada. Ele oferece uma
linguagem para discutir precisão, pré-condições, pós-condições, terminação e o que uma
refatoração preserva. O [EWD 209](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD209.html)
e o [EWD 418](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD418.html) mostram
essa linha de trabalho.

## Guarded commands e não determinismo

Guarded commands descrevem alternativas protegidas por condições. Quando mais de uma
guarda está habilitada, a escolha pode ser não determinística. Isso separa a especificação
da política acidental de escolher o primeiro ramo textual.

O não determinismo pode ser útil para provar que qualquer escolha válida preserva uma
propriedade. Também pode revelar que a especificação esqueceu fairness, prioridade ou
terminação. Em sistemas reais, a implementação precisa decidir como lidar com starvation,
ordem, timeout e observabilidade.

## Concorrência e semáforos

Dijkstra contribuiu para os fundamentos de processos sequenciais cooperantes, exclusão
mútua e semáforos. As operações P e V fornecem uma abstração para esperar uma condição,
consumir uma permissão e sinalizar disponibilidade. Um semáforo binário pode proteger uma
seção crítica; um contador pode representar capacidade.

O valor dessa contribuição não é recomendar semáforos para qualquer programa. É fornecer
um modelo para falar sobre interleavings, estados protegidos, espera e sinalização. O
[EWD 123](https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD123-2.html) e o
[EWD 209](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD209.html) mostram como
esses mecanismos aparecem no raciocínio sobre processos concorrentes.

## Deadlock, terminação e sistemas distribuídos

O problema dos filósofos jantando, mutual exclusion, fairness e deadlock tornaram-se
exemplos duradouros de como componentes localmente simples podem formar um sistema sem
progresso. Dijkstra também trabalhou em terminação de computações distribuídas, incluindo
o trabalho com C. S. Scholten sobre detecção de terminação em computações difusas.

Em autoestabilização, uma configuração arbitrária pode convergir para um estado legítimo
depois de um número finito de passos. Essa ideia é útil quando não é realista garantir que
todo estado inicial ou todo estado após uma falha seja correto. O domínio aparece hoje em
protocolos de rede, control loops e sistemas que precisam se recuperar de estados
inconsistentes.

O [arquivo de Dijkstra](https://www.cs.utexas.edu/~EWD/) resume a influência de seu trabalho
em semáforos, mutual exclusion, deadlock, raciocínio sobre concorrência e
self-stabilization. Esta coleção também trata de
[autoestabilização](../arquitetura-aplicacoes/self-stabilization.md).

## Sistemas operacionais e linguagens

Dijkstra participou do desenvolvimento de sistemas operacionais e de ferramentas para
programação, incluindo o sistema THE, cuja estrutura hierárquica foi usada para organizar
níveis de abstração e concorrência. Também trabalhou com linguagens e compiladores, e
defendeu que a linguagem deveria permitir expressar estruturas que pudessem ser
compreendidas e verificadas.

Essas contribuições não devem ser reduzidas à frase "Dijkstra era contra uma construção
específica". O ponto mais amplo era controlar a complexidade acidental e evitar que o
programador dependesse de uma visão global impossível de manter.

## Educação e estilo de trabalho

Dijkstra escreveu extensamente sobre ensinar programação, matemática e ciência da
computação. Ele defendia generalização, abstração e argumentos curtos que expõem a razão
de uma construção. Sua influência também é metodológica: formular o problema, escolher
uma representação, derivar uma solução e só então implementar.

Esse método não elimina experimentos, testes ou medições. Ele evita usar testes como único
argumento de correção e evita medir um programa cuja especificação ainda está ambígua.

## O que não deve ser atribuído a ele

O nome de Dijkstra aparece em vários algoritmos e técnicas que não foram necessariamente
inventados por ele. O algoritmo de Dijkstra é específico para caminhos mínimos com pesos
não negativos. O método de weakest precondition não é a mesma coisa que toda verificação
formal. Estruturado não significa automaticamente correto. E um semáforo não é sinônimo de
mutex, fila ou transação.

## Relações

- [Concorrência e sincronização](concorrencia/index.md) organiza race conditions, mutexes,
  semáforos e deadlocks.
- [Autoestabilização](../arquitetura-aplicacoes/self-stabilization.md) trata convergência
  após estados arbitrários.
- [Algoritmos e estruturas de dados](algoritmos-e-estruturas-de-dados.md) trata custo,
  representação e escolha de estruturas.
- [Clean Code](clean-code.md) trata legibilidade e manutenção sem substituir argumentos
  de correção.

## Fontes

- [E. W. Dijkstra Archive](https://www.cs.utexas.edu/~EWD/)
- [ACM A. M. Turing Award](https://amturing.acm.org/?pg=awardees.html)
- [Notes on Structured Programming, EWD 249](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html)
- [A constructive approach to the problem of program correctness, EWD 209](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD209.html)
- [Guarded commands, non-determinacy and a calculus for the derivation of programs, EWD 418](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD418.html)
