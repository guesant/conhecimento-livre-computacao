# Análise de complexidade

Análise de complexidade descreve como o custo de um algoritmo varia quando o tamanho da entrada cresce. Ela ajuda a comparar alternativas antes de medir uma implementação, mas não substitui medições. Constantes, alocações, cache, compilador, armazenamento, rede, paralelismo e distribuição dos dados podem alterar o resultado observado.

## Notação assintótica

Big O expressa um limite superior assintótico. Dizer que um algoritmo é `O(n)` significa que, a partir de algum tamanho, seu custo cresce no máximo proporcionalmente a `n`, ignorando constantes e termos de ordem menor. Theta, escrita `Theta(n)`, descreve um limite assintoticamente justo. Omega, escrita `Omega(n)`, descreve um limite inferior.

As classes mais comuns, em ordem aproximada de crescimento, são `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n²)`, `O(2^n)` e `O(n!)`. A ordem não é uma promessa de desempenho absoluto. Um `O(n)` com uma operação cara pode perder para um `O(n log n)` com uma operação simples em entradas pequenas.

## Melhor, pior e caso médio

O melhor caso descreve a entrada mais favorável. O pior caso descreve a entrada mais desfavorável dentro do contrato. O caso médio depende de uma distribuição de entradas e de uma hipótese de probabilidade. Sem declarar essa distribuição, “médio” pode ser apenas uma intuição não verificável.

Busca linear em uma sequência tem melhor caso `O(1)`, quando o item está no primeiro elemento, e pior caso `O(n)`, quando está no fim ou ausente. Sob uma distribuição uniforme simples, o número esperado de comparações também cresce linearmente. Busca binária tem `O(1)` no melhor caso e `O(log n)` no pior caso, mas exige dados ordenados e acesso eficiente ao meio.

Uma tabela hash costuma ter busca, inserção e remoção em `O(1)` esperado. Colisões, uma função de dispersão ruim ou uma carga excessiva podem elevar o custo, e o pior caso pode chegar a `O(n)`. Uma árvore balanceada oferece `O(log n)` no pior caso para operações fundamentais. A garantia pior pode ser preferível quando latência previsível importa mais que uma média menor.

## Tempo, espaço e outros modelos

O custo temporal conta operações de acordo com um modelo. O custo espacial pode contar memória auxiliar, memória total, tamanho da pilha ou espaço de saída. Em sistemas de dados, também é necessário distinguir CPU, leituras de disco, acessos ao cache, bytes transferidos e chamadas remotas. Um algoritmo com boa complexidade de CPU pode ser inadequado se fizer muitas requisições de rede.

Para algoritmos paralelos, considere trabalho total e caminho crítico. Para estruturas persistentes, considere alocações e compartilhamento. Para bancos de dados, considere páginas, seletividade, cardinalidade, plano de execução e custo de I/O, em vez de aplicar apenas a complexidade de uma estrutura em memória.

## Complexidade amortizada

Complexidade amortizada não é o mesmo que caso médio. Ela garante o custo médio por operação em uma sequência, mesmo sem assumir uma distribuição probabilística de entradas. A sequência pode conter operações caras, desde que o custo total seja limitado por uma soma favorável.

Um array dinâmico pode precisar copiar todos os elementos quando aumenta a capacidade. Essa operação isolada custa `O(n)`, mas, quando a capacidade cresce geometricamente, o custo total de várias inserções é `O(n)`. Assim, a inserção no fim tem custo amortizado `O(1)`, embora algumas inserções individuais continuem custando `O(n)`.

Os métodos clássicos são análise agregada, método contábil e método do potencial. A análise agregada calcula o custo total da sequência. O método contábil atribui créditos às operações baratas para pagar operações futuras. O método do potencial associa uma função ao estado da estrutura e transforma a mudança dessa função em crédito ou débito.

## Como usar a análise

Uma análise útil começa definindo o tamanho da entrada. Para uma busca em grafo, pode ser `V + E`; para uma string, pode ser o número de símbolos; para um banco, pode ser o número de linhas, páginas ou bytes. Depois, conte o laço dominante, considere chamadas recursivas e verifique se a estrutura usada realmente oferece a operação assumida.

Registre separadamente melhor caso, pior caso, hipótese de caso médio e custo amortizado. Se o algoritmo depende de ordenação, balanceamento, dispersão ou cache, escreva essa condição. A análise deixa de ser confiável quando essas premissas ficam implícitas.

## Fontes

- [Introduction to Algorithms, MIT Press](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
- [MIT 6.006, Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- [Asymptotic analysis, Wikipedia](https://en.wikipedia.org/wiki/Asymptotic_analysis)
- [Amortized analysis, Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis)
- [Princeton Algorithms](https://algs4.cs.princeton.edu/home/)
