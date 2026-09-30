# Resolução de conflitos

Conflito é uma diferença concorrente que a política escolhida não consegue combinar de
modo suficiente para o domínio. Não é simplesmente qualquer divergência entre réplicas.
Uma divergência pode ser normal durante a sincronização e convergir sem intervenção.

Resolução de conflitos tem pelo menos três objetivos que podem entrar em tensão:

- convergência, todas as réplicas chegam ao mesmo resultado;
- preservação, nenhuma alteração válida é descartada silenciosamente;
- intenção, o resultado representa o que o usuário tentou fazer.

Nenhuma técnica garante os três para qualquer estrutura e regra de negócio.

## LWW

Last-write-wins escolhe um valor por uma ordem determinística, usando timestamp, contador,
relógio lógico ou combinação de metadados. É barato de consultar e simples de explicar
para dados em que a atualização mais recente realmente deve vencer.

Ele pode perder uma alteração válida e o relógio físico não é uma boa autoridade isolada.
Use uma ordenação lógica e registre versões quando a decisão precisar ser investigada.
LWW por campo preserva mais alterações que LWW por documento, mas pode formar uma combinação
sem sentido entre campos relacionados.

## Merge por campo e por domínio

Merge por campo combina alterações em propriedades diferentes. Merge por domínio aplica
regras como soma de incrementos, união de conjuntos, ordenação por posição ou aprovação
explícita.

Uma operação de reserva não deve ser resolvida como string mais recente. Ela precisa validar
capacidade e concorrência. Uma lista de participantes pode usar conjunto; uma ordem de
itens precisa de identidade, posição e política para inserções simultâneas.

Quanto mais significado uma operação possui, menos seguro é usar uma regra genérica de
valor. Modele operações com intenção quando a aplicação precisa saber que alguém aprovou,
moveu, cancelou ou publicou algo.

## Three-way merge

Three-way merge compara base comum, mudança A e mudança B. Uma alteração de A em uma região
que B não mudou pode ser preservada. Se ambos mudaram a mesma região, o resultado pode ser
um conflito explícito.

É adequado para arquivos, branches e documentos que possuem uma base identificável. Ele
não resolve automaticamente edição offline por muitos peers se a base escolhida não cobre
a causalidade real das mudanças.

## OT

Operational Transformation transforma uma operação em relação às operações concorrentes
que chegaram antes. O objetivo é permitir que uma intenção posicional continue válida
quando o documento mudou.

OT costuma usar um servidor coordenador para ordenar versões, mas variantes podem distribuir
mais responsabilidades. A implementação de transformação precisa satisfazer propriedades
de convergência e lidar com texto, mapas, listas e undo conforme o tipo.

ShareDB é um exemplo de plataforma baseada em OT. O tipo de documento define a semântica
das operações; usar um tipo de texto para um objeto JSON não produz um merge correto.

## CRDT

CRDTs associam operações ou elementos a identidade e causalidade para que peers possam
aplicar mudanças em ordens diferentes e convergir. Há CRDTs de estado e de operação, com
tipos diferentes para mapas, conjuntos, listas, contadores e texto.

Convergência não significa ausência de decisões de produto. Dois usuários podem remover e
editar o mesmo item e o CRDT pode escolher um estado consistente, mas o domínio pode exigir
revisão humana. Tombstones, metadados e histórico também geram custo de memória, transporte
e garbage collection.

Yjs, Loro, JSON Joy e Diamond Types representam pontos diferentes desse espaço. Não compare
somente a sigla CRDT; compare tipos suportados, edição de texto, encoding, compactação,
providers, histórico, performance e controles de autorização.

## CouchDB e revision trees

CouchDB mantém revisões concorrentes e escolhe um vencedor determinístico. As revisões
perdedoras continuam disponíveis para que a aplicação possa inspecionar e resolver o
conflito. Isso evita divergência entre peers, mas não combina automaticamente campos nem
conhece a intenção do usuário.

## Estado versus operações

Resolver o estado final pode ser suficiente para uma preferência de usuário ou cache. Para
auditoria, colaboração de texto, contabilidade ou workflow, preserve operações, autores,
versões e transições. O histórico permite explicar como o estado surgiu e criar uma
operação compensatória.

Não confunda snapshot com resolução. Um snapshot reduz o custo de carregar o estado, mas
não decide quais operações concorrentes eram válidas. A compactação só pode remover
informação quando todos os peers relevantes tiverem uma base compatível.

## Resolução manual

Quando o algoritmo não consegue conhecer a regra, mostre alternativas ao usuário. A tela
deve preservar o valor local, o valor remoto, a base ou o histórico relevante, permitir
escolher ou editar o resultado e registrar quem resolveu.

Evite exibir um diff de duas vias quando o usuário precisa entender mudanças relativas à
base. Use three-way diff ou uma visualização por campo. Para texto rico, preserve marcas,
comentários e posições ao apresentar o conflito.

## Checklist de escolha

- Qual é a unidade que pode entrar em conflito, campo, documento, linha ou operação?
- O resultado precisa ser determinístico entre peers?
- A aplicação pode perder uma alteração ou precisa preservar todas?
- O domínio possui operações semânticas, como mover, aprovar ou reservar?
- Existe uma base comum e um servidor coordenador?
- Os clientes ficam offline por quanto tempo?
- Como serão identificadas operações duplicadas e fora de ordem?
- Qual histórico e auditoria precisam ser preservados?
- Como ocorrerão snapshots, compactação e garbage collection?
- Como autorização e revogação funcionam quando o peer está offline?
- O usuário consegue revisar e corrigir uma situação que o algoritmo não entende?

## Relações

- [Local-first e offline-first](local-first-e-offline-first.md)
- [ShareDB](sharedb.md)
- [PouchDB e CouchDB](pouchdb-couchdb.md)
- [Yjs](yjs.md)
- [Loro](loro.md)
- [Diamond Types](diamond-types.md)
- [Algoritmos de diff](algoritmos-de-diff.md)

## Fontes primárias

- [PouchDB conflicts](https://pouchdb.apache.org/guides/conflicts.html)
- [CouchDB replication conflicts](https://docs.couchdb.org/en/stable/replication/conflicts.html)
- [ShareDB types and OT](https://share.github.io/sharedb/types/)
- [Yjs introduction](https://docs.yjs.dev/)
- [A conflict-free replicated JSON datatype](https://arxiv.org/abs/1608.03960)
