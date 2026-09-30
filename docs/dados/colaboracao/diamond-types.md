# Diamond Types

Diamond Types é um CRDT de alto desempenho para edição concorrente de texto. O projeto
usa Rust e possui bindings para JavaScript via WebAssembly. Seu foco principal é a lista
de caracteres e a representação eficiente do histórico de edições, não um banco JSON
genérico pronto para qualquer domínio.

## Identidade de caracteres e operações

Cada cliente possui um identificador e cada edição recebe uma sequência local. A combinação
de cliente e sequência identifica uma unidade da história. Isso permite nomear uma posição
de forma estável mesmo quando outro peer insere texto antes dela.

O documento precisa representar duas dimensões:

- espacial, o texto visível em um momento;
- temporal, a história de operações, dependências e autores.

Essa separação permite transformar uma operação recebida em uma posição atual sem depender
de um índice numérico que já ficou obsoleto.

## Eg-walker

O algoritmo Eg-walker percorre um grafo de eventos ou operações para aplicar mudanças
concorrentes e produzir a posição correspondente no texto. A ideia é manter informação de
causalidade suficiente para que edições sejam integradas sem um servidor central obrigatório.

Um CRDT de texto precisa resolver inserções na mesma posição, exclusões sobre conteúdo que
mudou e relações entre operações locais e remotas. O resultado deve ser determinístico e
convergente, mas ainda pode exigir uma política de intenção para casos em que o domínio
não é apenas texto.

## Positional updates e OT

Diamond Types trabalha internamente com identificadores estáveis, mas pode interagir com
updates posicionais. Isso é útil quando um peer simples ou um editor existente usa índices
de texto e não conhece a representação interna do CRDT.

Interoperabilidade não significa que qualquer operação posicional será segura. O adapter
precisa conhecer a versão sobre a qual a posição foi calculada, transformar ou rejeitar uma
operação obsoleta e preservar o contrato de undo e seleção.

## Escopo e estado do projeto

O projeto se concentra em texto simples e a própria documentação do repositório registra
que suporte mais amplo a tipos JSON ainda é trabalho em andamento. Não escolha Diamond
Types como se ele fosse automaticamente uma base para mapas, anexos, permissões ou
transações de negócio.

## Custo operacional

Avalie tamanho do histórico, custo de indexação, carga inicial, edição em documentos longos,
compactação e serialização WASM. O desempenho de uma operação de texto não prediz o custo
de uma aplicação com rich text, comentários, presença e armazenamento de documentos.

## Relações

[Yjs](yjs.md) oferece vários shared types e um ecossistema amplo de providers. [Loro](loro.md)
usa ideias relacionadas para combinar tipos de documento e texto. [ShareDB](sharedb.md)
usa OT com coordenação de servidor. [Algoritmos de diff](algoritmos-de-diff.md) compara
sequências, enquanto um CRDT precisa integrar operações concorrentes ao longo do tempo.

## Fontes primárias

- [Diamond Types repository](https://github.com/josephg/diamond-types)
- [Diamond Types internals](https://github.com/josephg/diamond-types/blob/master/INTERNALS.md)
- [Diamond Types package documentation](https://docs.rs/diamond-types)
