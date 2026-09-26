# Loro

Loro é uma biblioteca CRDT voltada a dados colaborativos e aplicações local-first. Ela
oferece tipos para mapas, listas, texto rico, árvores móveis e outros contêineres, com
bindings para Rust, JavaScript via WebAssembly e Swift.

## Modelo

O aplicativo modela seu estado em um documento Loro. Alterações locais produzem operações
que podem ser exportadas, transmitidas, aplicadas a outra réplica e compactadas. O estado
visível é uma projeção dos contêineres e da história que o documento mantém.

O transporte não é a mesma coisa que o CRDT. A aplicação ainda precisa escolher WebSocket,
WebRTC, HTTP, fila ou armazenamento de updates, além de autenticação, autorização,
reconexão e retenção.

## Tipos e algoritmos

O tipo correto depende da semântica do dado:

- mapa para chaves e valores estruturados;
- lista para itens ordenados;
- texto para edição de caracteres;
- texto rico para marcas e atributos;
- árvore móvel para hierarquias que podem ser reorganizadas;
- contador ou registro com política específica quando a operação exigir.

O texto colaborativo não deve ser representado apenas como uma string substituível. O
algoritmo precisa preservar inserções, exclusões e marcas concorrentes. Loro documenta o
uso de Fugue para texto e Eg-walker como inspiração ou base para eficiência de histórico.

## Estado, histórico e versões

Uma vantagem de manter operações é permitir histórico, snapshots, undo e inspeção da
causalidade. O custo é memória, armazenamento e complexidade de compactação. A aplicação
precisa decidir quando pode eliminar operações antigas, quais clientes podem ainda estar
offline e como um snapshot será validado.

Não trate exportar o JSON final como exportar a colaboração. Para reabrir o documento em
outra réplica, preserve o formato de atualização ou um snapshot com metadados compatíveis.

## Local-first e sincronização

Loro pode servir como camada local imediata, enquanto updates são enviados em segundo plano.
O servidor pode armazenar operações, snapshots ou ambos. Um peer precisa recuperar as
alterações que perdeu, confirmar quais updates já foram observados e responder a operações
duplicadas ou fora de ordem.

A aplicação deve distinguir estado local de confirmação remota. Um merge automático garante
convergência do modelo, mas não garante que o resultado faça sentido para a regra de negócio.

## Desempenho

Meça o tamanho do log, tempo de carga, tempo de merge, custo de serialização, memória dos
contêineres, edição de listas grandes e compactação. Benchmarks de texto curto podem não
representar um editor com histórico longo, marcas, movimentação de árvores e peers offline.

Limite frequência de updates quando o editor produzir muitas operações pequenas. Agrupar
operações pode reduzir transporte, mas deve preservar undo, causalidade e recuperação.

## Segurança e limites

O CRDT não valida autorização. A camada de sync deve controlar quais documentos e campos um
peer pode ler ou escrever. Para invariantes que exigem autoridade, use transação no
servidor, operação assinada, validação ou um modelo híbrido.

Tombstones e histórico podem conservar dados apagados. A política de privacidade precisa
considerar compactação, snapshots, backups, dispositivos offline e peers que não se
conectam há muito tempo.

## Quando usar

Loro é interessante para editores, estruturas hierárquicas, quadros, listas móveis,
documentos ricos e aplicações local-first que precisam de mais tipos que um texto simples.
Compare-o com [Yjs](yjs.md), [JSON Joy](json-joy.md) e
[Diamond Types](diamond-types.md) por modelo de dados, linguagem, bindings, encoding,
performance e maturidade dos providers.

## Fontes primárias

- [Loro documentation](https://loro.dev/docs)
- [Loro CRDT type selection](https://www.loro.dev/docs/concepts/choose_crdt_type)
- [Loro rich text](https://www.loro.dev/blog/loro-richtext)
- [Loro repository](https://github.com/loro-dev/loro)
