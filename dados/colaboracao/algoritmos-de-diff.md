# Algoritmos de diff

Diff é o processo de encontrar diferenças entre duas sequências, árvores ou estados. O
resultado pode ser usado para exibir uma revisão, gerar patch, migrar dados, comparar
arquivos, preparar um merge ou sincronizar réplicas. Um diff não é automaticamente uma
resolução de conflito.

## Sequências e LCS

Para sequências de linhas ou tokens, muitos algoritmos procuram uma subsequência comum mais
longa, LCS, e descrevem inserções, remoções e elementos preservados. A escolha da sequência
comum influencia a leitura do diff: duas respostas podem transformar o mesmo texto, mas
uma delas pode parecer muito mais natural.

## Myers

O algoritmo de Myers procura um caminho mínimo no grafo de edições, normalmente minimizando
o número de inserções e remoções. É uma base comum para diffs de texto porque encontra
patches compactos em muitos casos.

O custo depende do tamanho das sequências e da distância de edição. Em arquivos muito
grandes ou entradas adversariais, limite memória e tempo. Um diff mínimo em quantidade de
linhas não necessariamente preserva blocos semânticos ou a intenção de quem editou.

## Patience diff

Patience diff usa elementos únicos para encontrar âncoras estáveis e depois aplica uma
estratégia de subsequência nas regiões entre elas. Ele pode produzir diffs mais legíveis em
código reorganizado, porque tende a preservar blocos que possuem linhas identificáveis.

Ele pode ser pior quando há pouca unicidade, arquivos gerados ou conteúdo repetitivo. Por
isso, muitas ferramentas usam fallback para outra estratégia.

## Histogram diff

Histogram diff escolhe frequências de linhas para encontrar âncoras sem depender somente de
linhas únicas. Ele tenta equilibrar qualidade visual e custo em arquivos de código e dados
com repetição moderada.

O nome do algoritmo não garante uma política universal. Consulte a implementação, os
limites e o tratamento de whitespace, renomeações, binários e arquivos grandes.

## Diff de texto, tokens e árvores

Diff por caracteres é sensível a pequenas mudanças e pode gerar ruído. Diff por linhas é
mais legível para código e documentos. Diff por tokens entende palavras, identificadores e
pontuação. Diff estrutural usa AST ou um modelo de documento e pode reconhecer que uma
função mudou de posição sem tratá-la como remoção e reinserção.

Para JSON, ordenar chaves e comparar strings é insuficiente quando listas possuem identidade
ou ordem significativa. Um diff semântico pode tratar lista por ID, mapa por chave e texto
por operações. O contrato deve explicar se reordenar uma lista é mudança de conteúdo ou
somente de apresentação.

## Diff e merge de três vias

Um three-way merge recebe base comum, versão A e versão B. Mudanças feitas somente em A ou
somente em B podem ser combinadas. Quando ambas alteram a mesma região de forma
incompatível, o algoritmo marca conflito.

Comparar somente A e B não informa quais partes cada lado mudou. Por isso, diff de duas vias
é útil para visualização, mas three-way merge é geralmente mais apropriado para integrar
branches ou réplicas.

## Diff em colaboração

Em um editor colaborativo, um diff posterior entre snapshots pode não preservar a intenção
das operações. Uma inserção e uma remoção podem parecer iguais ao resultado final apesar de
terem vindo de usuários diferentes. OT e CRDT mantêm operações, identidade e causalidade
para integrar mudanças durante o tempo.

Use diff para inspeção e apresentação. Use OT, CRDT, MVCC ou uma política de domínio para
decidir como as mudanças serão aplicadas.

## Performance e segurança

Defina limite de tamanho, tempo, memória, recursão e número de operações. Não aceite um
payload de diff arbitrariamente grande em uma API pública. Normalize encoding apenas quando
isso fizer parte do contrato; alterar newline, Unicode ou whitespace pode produzir mudanças
falsas.

Para documentos sensíveis, evite gravar diffs em logs, porque um patch pode revelar o valor
antigo e o novo. Trate patches como entrada não confiável e valide caminho, operação, tipo,
tamanho e autorização.

## Fontes e implementações

- [Myers, An O(ND) Difference Algorithm](http://www.xmailserver.org/diff2.pdf)
- [Git diff algorithms](https://git-scm.com/docs/git-diff)
- [diff-match-patch](https://github.com/google/diff-match-patch)
- [JSON Joy JSON CRDT](https://jsonjoy.com/specs/json-crdt/)
- [Diamond Types internals](https://github.com/josephg/diamond-types/blob/master/INTERNALS.md)
