# Mapa de algoritmos e estruturas de dados

Algoritmos e estruturas de dados são duas faces do mesmo desenho. A estrutura determina como o estado é organizado e quais operações podem ser eficientes; o algoritmo determina como esse estado é percorrido, transformado ou combinado. A frase do título do livro *Algorithms + Data Structures = Programs*, de Niklaus Wirth, resume uma ideia de engenharia: um programa não é apenas uma sequência de instruções, mas uma escolha explícita de representação e de procedimento.

Wirth publicou o livro em 1976. A formulação não significa que todo programa possa ser reduzido a uma equação, nem que a estrutura seja independente do domínio. Ela chama atenção para o fato de que uma representação inadequada pode tornar um algoritmo simples caro, enquanto uma boa representação pode eliminar trabalho desnecessário.

## Como classificar uma estrutura

Não existe uma lista finita que esgote todas as estruturas de dados. Há estruturas elementares, composições, variantes especializadas, índices persistentes, estruturas probabilísticas e representações adaptadas a hardware, paralelismo ou armazenamento externo. Um mapa útil começa pelas operações exigidas:

| Família | Operação favorecida | Exemplos |
| --- | --- | --- |
| Sequencial contígua | acesso por posição e localidade de memória | array fixo, array dinâmico |
| Sequencial encadeada | inserção e remoção com referência ao nó | lista ligada simples, dupla ou circular |
| Restrição de acesso | último ou primeiro elemento | pilha, fila, deque |
| Associação por chave | busca, inserção e remoção por chave | tabela hash, mapa, conjunto |
| Ordenação | sucessor, predecessor e intervalos | árvore de busca, skip list |
| Prioridade | obter o menor ou maior item | heap, fila de prioridade |
| Hierarquia | representação de relações pai-filho | árvore, trie, B-tree, B+tree |
| Relação geral | caminhos, conectividade e dependências | grafo por lista, matriz ou arestas |
| Partição | unir grupos e consultar conectividade | union-find, disjoint set |
| Intervalo ou geometria | consulta espacial ou de faixa | árvore de segmentos, intervalo, R-tree |
| Probabilística | resposta aproximada com pouco espaço | Bloom filter, Count-Min Sketch |
| Persistência | preservar versões ou compartilhar estrutura | árvore persistente, vetor imutável |

### Sequências

Arrays fixos ocupam uma região contígua com capacidade definida. Arrays dinâmicos usam um buffer contíguo, mas podem realocá-lo quando a capacidade se esgota. Listas ligadas distribuem nós na memória e conectam esses nós por referências. Pilhas expõem a política last in, first out; filas expõem first in, first out; deques permitem operações nas duas extremidades.

### Associação e prioridade

Uma tabela hash usa uma função de dispersão para mapear chaves a posições. Ela normalmente oferece custo esperado constante, mas depende da qualidade da função, da taxa de ocupação e do tratamento de colisões. Uma árvore de busca mantém uma relação de ordenação e permite consultas por intervalo, sucessor e predecessor. Um heap mantém apenas a propriedade necessária para obter uma prioridade, não uma ordenação completa.

### Árvores e índices

Árvores binárias de busca podem degenerar em listas se não forem balanceadas. AVL e red-black mantêm limites de altura por invariantes diferentes. B-tree e B+tree foram desenhadas para reduzir acessos a armazenamento externo e aparecem em índices de bancos de dados. Tries organizam chaves por prefixos e são úteis quando a representação dos símbolos é mais importante que a comparação inteira da chave.

### Grafos

Um grafo pode ser armazenado como lista de adjacência, matriz de adjacência ou lista de arestas. A lista é econômica em grafos esparsos; a matriz simplifica consultas diretas de adjacência em grafos densos. A escolha afeta busca em largura, busca em profundidade, caminhos mínimos, ordenação topológica, fluxo e detecção de componentes.

## Famílias de algoritmos

Algoritmos de busca e travessia visitam elementos, estados ou vértices. Busca linear não exige ordenação; busca binária troca a exigência de ordenação por um número logarítmico de comparações. BFS e DFS percorrem grafos com propriedades diferentes, mesmo quando ambos têm custo linear no tamanho da representação.

Algoritmos de ordenação incluem inserção, seleção, merge sort, quicksort, heapsort, counting sort e radix sort. Eles diferem em estabilidade, memória auxiliar, localidade, sensibilidade à distribuição dos dados e garantias de pior caso. Algoritmos de seleção encontram estatísticas de ordem sem necessariamente ordenar toda a entrada.

Divisão e conquista separa o problema em subproblemas, resolve cada um e combina os resultados. Algoritmos gulosos tomam decisões locais que só são corretas quando uma propriedade de troca ou outra prova sustenta a estratégia. Programação dinâmica armazena resultados de subproblemas sobrepostos e exige uma decomposição correta do estado. Backtracking explora uma árvore de escolhas e poda caminhos incompatíveis; branch and bound acrescenta limites para reduzir a busca em problemas de otimização.

Há ainda algoritmos aleatorizados, online, aproximados, distribuídos, paralelos e heurísticos. A classificação deve descrever o contrato do algoritmo, não apenas a implementação. Um algoritmo online recebe entradas sem conhecer o futuro; um algoritmo aproximado declara uma garantia de qualidade; um algoritmo heurístico pode ser útil sem oferecer uma prova geral de optimalidade.

## Critérios de escolha

Comece listando as operações, a frequência de cada operação, o tamanho dos dados, a necessidade de ordenação, a mutabilidade, a localidade de memória, o custo de cópia, a persistência, a concorrência e a tolerância a respostas aproximadas. Em seguida, declare os invariantes que devem permanecer verdadeiros e os casos extremos que serão testados.

Uma estrutura rápida em memória pode ser inadequada quando os dados não cabem na RAM, quando a ordem precisa sobreviver a reinícios ou quando o padrão de acesso causa contenção. Da mesma forma, uma estrutura teoricamente boa pode perder para outra mais simples por causa de constantes, cache da CPU, alocações, coletor de lixo e custo de serialização.

As páginas de [análise de complexidade](analise-de-complexidade.md) e [arrays fixos e dinâmicos](arrays-fixos-e-dinamicos.md) tratam esses custos em mais detalhe. Cursos, livros e artigos acadêmicos oferecem fontes complementares para aprofundamento.

## Fontes

- [Algorithms + Data Structures = Programs, Niklaus Wirth, 1976](https://people.inf.ethz.ch/~wirth/AD.pdf)
- [Introduction to Algorithms, MIT Press](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
- [Algorithms, Princeton](https://algs4.cs.princeton.edu/home/)
- [MIT 6.006, Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
- [The Algorithm Design Manual](https://www.algorist.com/)
