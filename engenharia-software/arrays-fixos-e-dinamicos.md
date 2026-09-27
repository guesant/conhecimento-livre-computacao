# Comparação entre arrays fixos e dinâmicos

Um array armazena elementos em posições indexadas. A distinção entre array fixo e dinâmico não é apenas uma diferença de sintaxe: ela define como a capacidade é administrada, quando os elementos podem ser movidos e qual previsibilidade de memória a estrutura oferece.

## Array de tamanho fixo

Um array fixo reserva uma capacidade determinada no momento da criação ou pelo tipo. Em uma região contígua, o endereço de `a[i]` pode ser calculado por deslocamento, por isso o acesso por índice é `O(1)`. A localidade de memória costuma favorecer iteração, pré-busca e uso do cache da CPU.

A capacidade não cresce automaticamente. Inserir no meio exige deslocar elementos e custa `O(n)` no pior caso. Remover pode exigir compactação. A estrutura é adequada quando o limite é conhecido, quando o tamanho não muda ou quando alocação previsível e interoperabilidade com hardware são mais importantes que flexibilidade.

## Array de tamanho dinâmico

Um array dinâmico mantém pelo menos tamanho lógico e capacidade física. Enquanto há espaço livre, adicionar ao final altera apenas o tamanho. Quando a capacidade acaba, a implementação reserva um buffer maior, copia ou move os elementos e libera o buffer anterior. O acesso por índice continua `O(1)` e a inserção no final é `O(1)` amortizado, mas a realocação individual é `O(n)`.

Inserção ou remoção no meio continua exigindo deslocamento e custa `O(n)`. A memória não é exatamente igual ao número de elementos: existe capacidade excedente para evitar realocações frequentes. A estratégia de crescimento é parte do comportamento da biblioteca, não uma regra universal para toda aplicação.

## Crescimento geométrico

Se a capacidade cresce adicionando uma quantidade fixa, uma sequência de inserções pode copiar aproximadamente `1 + 2 + 3 + ... + n` elementos e custar `O(n²)`. Se a capacidade é multiplicada por um fator `g > 1`, a soma das cópias forma uma série geométrica e o custo total de `n` inserções permanece `O(n)`.

Um fator maior reduz a frequência de realocação, mas deixa mais memória ociosa. Um fator menor economiza capacidade excedente, mas pode copiar mais vezes. A escolha também depende do tamanho dos elementos, do custo de mover ou destruir objetos, do comportamento do alocador, da fragmentação, da localidade e da possibilidade de o novo bloco reutilizar o bloco antigo.

Não existe uma taxa de crescimento ótima independente da plataforma. A discussão sobre o fator áureo é útil para mostrar o conflito entre reutilizar um bloco existente e reduzir memória excedente, mas não é uma constante que deva ser aplicada automaticamente. Uma implementação pode copiar, mover, realocar no lugar ou usar uma política específica do alocador.

## Análise amortizada

Considere `n` inserções em um array que duplica a capacidade quando necessário. As realocações copiam aproximadamente `1 + 2 + 4 + ...`, que é menor que `2n`. O custo total das cópias é linear e, somado ao custo das inserções, resulta em `O(n)`. Dividido pelas `n` operações, o custo amortizado por inserção é `O(1)`.

Essa garantia não significa que toda chamada seja rápida. A operação que dispara uma realocação ainda pode parar o programa por tempo proporcional ao tamanho atual. Em uma aplicação com limites estritos de latência, pode ser necessário reservar capacidade antecipadamente, usar lotes ou escolher uma estrutura com outra política de alocação.

## O caso das listas do CPython

Listas do CPython são arrays dinâmicos, embora a palavra "lista" em Python não implique uma lista ligada. O código histórico do CPython 2.6 usa uma política de sobrealocação para reservar espaço além do tamanho lógico. A fórmula e os detalhes mudaram ao longo das versões, portanto o arquivo histórico é uma evidência de uma implementação específica, não uma especificação da linguagem Python.

O mesmo princípio aparece em outras bibliotecas: capacidade excedente troca memória por menos cópias. Ao analisar uma implementação, leia a versão exata, o alocador e a operação de crescimento. Não deduza o custo de toda linguagem a partir de uma única biblioteca.

## Escolha prática

Use um array fixo quando a capacidade for conhecida ou quando o limite fizer parte do contrato. Use um array dinâmico quando houver acesso indexado, crescimento variável e benefício de armazenamento contíguo. Use uma lista ligada somente quando suas operações e seu padrão de acesso justificarem o custo de referências, alocações individuais e pior localidade.

Se o tamanho final for conhecido, reserve capacidade antecipadamente. Se o array crescer e encolher, use limiares de redução com histerese para evitar alternância contínua entre dois tamanhos. Se mover elementos for caro, compare uma estrutura de indireção, um deque ou uma estrutura persistente.

## Fontes

- [Amortized analysis, Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis)
- [Discussão sobre a taxa ideal de crescimento](https://stackoverflow.com/questions/1100311/what-is-the-ideal-growth-rate-for-a-dynamically-allocated-array)
- [Optimal memory reallocation and the golden ratio, arquivo](https://web.archive.org/web/20170808090051/https://crntaylor.wordpress.com/2011/07/15/optimal-memory-reallocation-and-the-golden-ratio/)
- [CPython 2.6, `listobject.c`](https://github.com/python/cpython/blob/2.6/Objects/listobject.c#L41)
- [Algorithms + Data Structures = Programs, Niklaus Wirth](https://people.inf.ethz.ch/~wirth/AD.pdf)
