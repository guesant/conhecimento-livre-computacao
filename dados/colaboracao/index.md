# Colaboração distribuída e local-first

Aplicações colaborativas precisam resolver problemas diferentes que muitas vezes recebem
o mesmo nome: disponibilidade offline, sincronização, edição concorrente, persistência
local, transmissão de eventos e resolução de conflitos.

Uma aplicação pode ser offline-first sem permitir edição simultânea. Pode usar um CRDT sem
ser um banco de dados. Pode usar WebSocket sem convergir alterações. Pode replicar documentos
com CouchDB sem preservar automaticamente a intenção do usuário. A arquitetura precisa
descrever cada propriedade separadamente.

## Vocabulário

| Conceito | Pergunta que responde |
| --- | --- |
| Local-first | A operação deve funcionar primeiro sobre dados locais? |
| Offline-first | O produto continua útil quando a rede está ausente? |
| Sincronização | Como alterações e estado trafegam entre réplicas? |
| Colaboração | Vários atores podem alterar o mesmo estado ou documento? |
| OT | Como transformar operações concorrentes para preservar a edição? |
| CRDT | Como representar mudanças para que réplicas possam convergir? |
| Diff | Como encontrar diferenças entre duas sequências ou árvores? |
| Merge | Como produzir um estado a partir de bases ou operações diferentes? |
| Conflito | Qual mudança não pode ser combinada sem uma política adicional? |
| Presença | Como representar usuários conectados, cursores e seleção? |

Uma implementação concreta deve declarar fonte de verdade, durabilidade, identidade de
operação, causalidade, ordenação, autenticação, autorização, reconexão, retenção,
compactação, garbage collection e como o usuário pode corrigir um conflito sem perder dados.

## Páginas

- [Local-first e offline-first](local-first-e-offline-first.md) explica o modelo de
  execução local, sincronização posterior, durabilidade e trade-offs.
- [CRDT](crdt.md) explica estruturas replicadas que aceitam alterações concorrentes e
  convergem sob as hipóteses do tipo.
- [ShareDB](sharedb.md) explica colaboração de documentos JSON baseada em Operational
  Transformation.
- [JSON Joy](json-joy.md) explica JSON CRDT, patches, codificação e operações estruturais.
- [PouchDB e CouchDB](pouchdb-couchdb.md) explica replicação de documentos, revision trees
  e conflitos entre réplicas.
- [Yjs](yjs.md) explica shared types, CRDT, providers, presença e persistência offline.
- [Loro](loro.md) explica os tipos CRDT e o foco em colaboração local-first.
- [Diamond Types](diamond-types.md) explica o CRDT de texto e o algoritmo Eg-walker.
- [Jazz](jazz.md) explica banco relacional local-first, sincronização e permissões.
- [Algoritmos de diff](algoritmos-de-diff.md) compara Myers, patience, histogram e diffs
  estruturais.
- [Resolução de conflitos](resolucao-de-conflitos.md) compara LWW, 3-way merge, OT, CRDT
  e resolução orientada ao domínio.

## Escolha inicial

Comece perguntando se o dado é estado compartilhado, documento editável, evento, cache ou
registro transacional. Depois determine se uma perda de atualização é aceitável, se o
usuário precisa trabalhar offline, se a edição simultânea existe e se o histórico precisa
ser auditável.

Use uma solução mais simples quando apenas uma leitura local com invalidação for necessária.
Use uma fila ou log quando o requisito for replay de eventos. Use OT ou CRDT quando vários
atores editarem a mesma estrutura e o merge automático tiver valor real. Para invariantes
financeiras, autorização crítica e operações que precisam de autoridade única, preserve um
servidor que valide a transação, mesmo que a interface seja otimista.
