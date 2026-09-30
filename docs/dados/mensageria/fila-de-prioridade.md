# Fila de prioridade

Fila de prioridade, frequentemente abreviada como priority queue ou PQ, retorna o item
mais urgente segundo uma ordenação definida em vez de respeitar somente a ordem de chegada.
O item de maior prioridade pode ser o menor ou maior valor de uma chave, conforme o
contrato.

Uma fila comum implementa FIFO. Uma fila de prioridade implementa uma política de escolha.
Ela é adequada quando jobs urgentes não devem esperar atrás de trabalho normal, quando um
scheduler escolhe o próximo vencimento ou quando um algoritmo precisa retirar repetidamente
o menor custo conhecido.

## Estruturas de implementação

Um heap binário oferece inserção e remoção do item prioritário em `O(log n)` e consulta ao
item no topo em `O(1)`. Um array ordenado torna consulta barata, mas pode tornar inserção
cara. Um array não ordenado simplifica inserção e torna a remoção do prioritário mais cara.

Heaps d-ários, árvores balanceadas, filas de prioridade concorrentes e estruturas de
calendário mudam o custo conforme o número de prioridades, a frequência de atualização e a
necessidade de estabilidade.

Se dois itens têm a mesma prioridade, defina se a ordem de chegada será preservada. Uma
fila pode usar `(prioridade, sequência)` para obter uma ordenação determinística.

## Prioridade não é urgência absoluta

Prioridade absoluta pode causar starvation: itens de baixa prioridade nunca são retirados
quando novos itens urgentes chegam continuamente. Soluções incluem aging, quota por classe,
filas separadas, fairness ponderada e limite de tempo de espera.

Uma prioridade configurável pelo usuário também é uma superfície de abuso. Não permita que
qualquer consumidor transforme todo trabalho em urgente. Autorize classes, limite taxa e
monitore a distribuição.

## Fila de jobs

Em um sistema distribuído, a fila de prioridade precisa definir ack, visibilidade, retry,
TTL, dead letter, concorrência e persistência. Reordenar mensagens depois da publicação
pode ser difícil ou impossível em brokers particionados.

Prioridade pode reduzir a latência de jobs importantes, mas não aumenta capacidade. Se os
workers estão saturados, mais prioridade apenas reorganiza a espera. Separe pool ou fila
quando jobs urgentes e pesados competirem pelo mesmo recurso.

## Algoritmos

Dijkstra usa uma fila de prioridade para selecionar o vértice com menor estimativa em
implementações eficientes. A fila é uma parte da implementação; a correção vem da
propriedade de pesos não negativos e do relaxamento das arestas.

Schedulers, sistemas de interrupção, simulações de eventos discretos, gerenciamento de
memória e busca heurística também usam filas de prioridade. Em cada caso, a prioridade
precisa representar uma propriedade válida do problema, não apenas uma preferência visual.

## Relações

- [Filas de mensagens](filas.md) trata FIFO, ack, retry e dead letter.
- [Event streaming](event-streaming.md) trata ordem por partição e offsets.
- [Jobs e workers](jobs-e-workers.md) trata concorrência e leases.
- [Dijkstra](../../engenharia-software/dijkstra.md) relaciona a estrutura ao algoritmo de
  caminhos mínimos.

## Fontes

- [Python, heapq](https://docs.python.org/3/library/heapq.html)
- [C++ standard library, priority_queue](https://en.cppreference.com/w/cpp/container/priority_queue)
