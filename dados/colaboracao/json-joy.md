# JSON Joy

JSON Joy é um conjunto de bibliotecas e especificações para dados colaborativos em JSON,
incluindo JSON CRDT, patches, codificação e protocolos relacionados. A proposta é
representar objetos, mapas, listas e valores estruturados de maneira que atualizações
concorrentes possam ser aplicadas e as réplicas possam convergir.

## JSON CRDT

Um JSON CRDT é uma estrutura de dados replicada que associa operações a identidade e
causalidade, permitindo que cópias recebam mudanças em ordens diferentes e cheguem ao
mesmo estado sob as condições definidas pelo algoritmo.

O documento JSON visível é apenas uma projeção do estado interno. O algoritmo também
precisa manter metadados para identificar nós, inserções, remoções, relações de causalidade
e operações que já foram observadas.

## Modelo e encoding

As especificações do projeto separam modelo, semântica de operações e encoding. Isso é
importante porque uma representação binária compacta não define sozinha o comportamento de
merge.

Uma implementação pode ter:

- formato estrutural legível para inspeção;
- encoding compacto para transporte;
- encoding binário para menor espaço e custo de parsing;
- índices para localizar nós e operações;
- sidecar com metadados ou referências externas.

Escolha o encoding pela necessidade de persistência, rede, debugging e compatibilidade.
Não descarte metadados de causalidade apenas para guardar o JSON final; o estado final não
é suficiente para sincronizar dois editores que se separaram.

## Operações e merge

Mapas, listas e objetos têm problemas diferentes. Atribuir uma chave pode usar uma política
de registro; inserir em uma lista exige uma identidade estável para a posição; excluir um
item exige distinguir uma ausência inicial de uma remoção observada; mover um item exige
preservar identidade e intenção.

Um merge determinístico não significa que o resultado seja semanticamente correto para o
domínio. Dois usuários podem editar um campo de preço, remover uma autorização ou alterar
uma data de maneiras que o algoritmo consegue ordenar, mas que exigem aprovação humana.

## JSON CRDT e JSON comum

Serializar um CRDT para JSON e carregá-lo de volta como JSON comum perde a história e os
metadados necessários para continuar colaborando. JSON é uma forma de intercâmbio; o
estado colaborativo precisa manter sua representação nativa ou um snapshot acompanhado de
metadados suficientes.

Isso também afeta APIs. Uma API que aceita o documento final não representa
necessariamente operações concorrentes. Se o transporte for baseado em patches, defina
identidade, versão, deduplicação, autenticação e tamanho máximo.

## Quando usar

JSON Joy é interessante quando a aplicação precisa de documentos JSON estruturados,
patches, serialização eficiente ou interoperabilidade com uma especificação de CRDT. Ele
precisa ser comparado por workload com Yjs, Loro, Automerge, ShareDB e uma solução de
merge própria.

Meça tamanho de metadados, custo de aplicação, tempo de merge, compactação, garbage
collection, carregamento inicial, edição de listas e comportamento com histórico longo.

## Limitações

CRDT não remove a necessidade de schema, autorização, limites, garbage collection ou
validação de domínio. Operações inválidas podem convergir perfeitamente para um estado
inválido se a aplicação não verificar invariantes.

Também é necessário definir como apagar dados de modo compatível com privacidade. Tombstones
e histórico ajudam a sincronizar remoções, mas podem manter conteúdo sensível por mais tempo
que o permitido. Compactação e expurgo precisam preservar os peers que ainda podem enviar
operações antigas.

## Relações

[Yjs](yjs.md) fornece shared types para colaboração. [Loro](loro.md) combina vários tipos
CRDT e suporte a texto. [Diamond Types](diamond-types.md) concentra-se em edição de texto.
[Algoritmos de diff](algoritmos-de-diff.md) compara diferenças sintáticas, enquanto um
JSON CRDT representa operações e causalidade.

## Fontes primárias

- [JSON Joy](https://jsonjoy.com/)
- [JSON CRDT specification](https://jsonjoy.com/specs/json-crdt/)
- [JSON CRDT patch specification](https://jsonjoy.com/specs/json-crdt-patch/)
- [JSON Joy repository](https://github.com/streamich/json-joy)
