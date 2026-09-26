# Conflict-free Replicated Data Types

Um Conflict-free Replicated Data Type, ou CRDT, é uma estrutura de dados replicada cujo modelo de estado ou de operações permite que réplicas aceitem atualizações concorrentes e cheguem a um resultado comum quando receberem informação suficiente. A aplicação pode editar uma réplica sem coordenar cada operação com as demais, e o algoritmo do tipo define como as mudanças serão combinadas.

O nome "conflict-free" não significa que a intenção de todos os usuários será preservada nem que qualquer regra de negócio pode ser combinada automaticamente. Significa que o tipo foi construído para que certas operações concorrentes sejam compatíveis com uma propriedade de convergência. O domínio ainda precisa definir autorização, validação, invariantes, limites e tratamento de situações semanticamente incompatíveis.

## Propriedades

Uma implementação de CRDT normalmente precisa tornar explícitos:

- identidade da réplica, do ator, da operação ou do elemento;
- causalidade e conhecimento de quais atualizações já foram observadas;
- representação do estado ou das operações;
- regra de merge e sua determinismo;
- transporte, sincronização, retransmissão e deduplicação;
- retenção de metadados, tombstones e histórico;
- compactação e garbage collection;
- autorização e validação de alterações.

As réplicas podem apresentar estados diferentes durante uma partição ou enquanto mensagens estão em trânsito. A garantia é que, sob as hipóteses do protocolo, estados compatíveis convergirão quando as atualizações necessárias forem entregues. Essa convergência é eventual e não equivale a leitura forte, consenso ou transação distribuída.

## CRDTs de estado e de operação

CRDTs baseados em estado disseminam estados completos ou deltas de um estado. O merge precisa ser associativo, comutativo e idempotente para que a ordem, a agrupação e a repetição da entrega não alterem o resultado. Sem essas propriedades, a sincronização pode divergir.

CRDTs baseados em operação disseminam operações. A operação precisa ser aplicável em ordens compatíveis ou transformada por metadados de causalidade. Essa abordagem pode reduzir o tamanho da mensagem, mas exige identificar, ordenar ou deduplicar operações e manter informação suficiente para que uma operação atrasada ainda possa ser interpretada.

Delta-state CRDTs enviam deltas que representam mudanças de estado em vez de retransmitir o estado completo. Eles podem reduzir tráfego, mas a definição do delta, a composição, a retenção e a recuperação de uma réplica que ficou muito atrasada continuam sendo parte do protocolo.

## Tipos comuns

Um contador somente de incremento pode somar contribuições por réplica. Um contador positivo-negativo separa incrementos e decrementos para evitar ambiguidades de concorrência. Um conjunto somente de adição é simples, mas não representa remoção. Conjuntos observados-removidos e conjuntos de duas fases registram identidade e causalidade para distinguir uma remoção de uma adição posterior.

Registros podem usar last-write-wins, ordem lógica ou resolução por campo. Essa escolha pode ser aceitável para preferências, mas é perigosa para campos que formam uma unidade de negócio. Mapas CRDT combinam registros e conjuntos, porém a composição não cria automaticamente invariantes entre campos.

Listas e sequências são mais difíceis. Inserções concorrentes precisam de identificadores estáveis e uma regra de ordenação que não dependa apenas da posição numérica atual. Exclusões normalmente deixam tombstones ou referências equivalentes até que seja seguro compactá-las. CRDTs de texto acrescentam problemas de posição, seleção, undo, formatação e custo de metadados.

## Como o merge funciona

Imagine duas réplicas que conhecem o mesmo estado inicial. Cada uma registra uma alteração local com identidade e causalidade. Quando uma recebe a mudança da outra, o merge compara o que já foi observado e aplica uma combinação determinística. Se a mensagem for repetida, ela deve ser ignorada ou produzir o mesmo estado. Se as mensagens chegarem em ordem diferente, as propriedades do tipo devem produzir o mesmo resultado final.

Essa propriedade resolve divergência de representação, não o significado do domínio. Dois usuários que reservam a última vaga podem produzir um conjunto convergente de operações e ainda violar a regra "a capacidade não pode ser negativa". Nesse caso, a autoridade precisa validar a reserva, usar uma operação especializada, limitar a edição offline ou aceitar uma reconciliação explícita.

## CRDT e outras técnicas

Operational Transformation, ou OT, transforma operações em relação ao histórico coordenado para preservar sua aplicabilidade. CRDT codifica identidade, causalidade e regras de merge na estrutura. As duas técnicas podem suportar edição colaborativa, mas possuem modelos de implementação, memória, transporte, undo e operação diferentes.

Three-way merge compara uma base comum com duas mudanças e pode apresentar conflito quando ambas alteraram a mesma região. Um CRDT geralmente tenta produzir uma combinação determinística sem pedir intervenção para cada divergência. Um log de eventos preserva uma sequência de fatos, mas não é um CRDT só por ser replicado. Um banco com replicação também não converge automaticamente de acordo com as propriedades de um CRDT.

## Custo e limites

O preço da edição sem coordenação costuma aparecer em metadados, tombstones, histórico, mensagens, compactação e complexidade de autorização. Peers offline por muito tempo podem gerar muitos estados concorrentes. Um peer que nunca reconecta pode impedir garbage collection segura se o sistema precisar preservar alterações para ele.

O servidor ainda pode ser a autoridade para identidade, schema, permissões, limites, publicação e invariantes. Um cliente CRDT não deve poder alterar campos administrativos, conceder acesso ou confirmar uma operação financeira apenas porque o tipo aceita a mutação local.

## Quando usar

CRDT é adequado quando edição local e concorrente tem valor, a convergência pode ser definida para a estrutura, a aplicação tolera estados intermediários e o custo de metadados é aceitável. Exemplos incluem editores colaborativos, notas offline, presença, listas compartilhadas e alguns modelos de configuração.

Ele é inadequado como solução genérica para qualquer banco distribuído. Para contabilidade, estoque, reservas, autorização, workflow ou regras com capacidade limitada, a aplicação precisa de uma autoridade ou de um tipo de operação que represente o invariante. Às vezes uma fila, uma transação central, um log ou um merge manual é a escolha mais segura.

## Relações

- [Colaboração distribuída e local-first](index.md)
- [Resolução de conflitos](resolucao-de-conflitos.md)
- [Operational Transformation com ShareDB](sharedb.md)
- [JSON Joy](json-joy.md)
- [Yjs](yjs.md)
- [Loro](loro.md)
- [Diamond Types](diamond-types.md)

## Fontes

- [Conflict-free Replicated Data Types, Shapiro, Preguiça, Baquero e Zawirski](https://pages.lip6.fr/Marc.Shapiro/papers/CRDTs-beatcs-2011-06.pdf)
- [Bibliografia de trabalhos sobre CRDT](https://crdt.tech/papers.html)
- [CRDT, Wikipedia](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type)
