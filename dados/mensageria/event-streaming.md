# Event streaming

Event streaming trata eventos como uma sequência durável e ordenada, frequentemente particionada. Consumidores mantêm uma posição e podem reler eventos conforme a retenção e as garantias da plataforma.

O evento é normalmente armazenado depois de publicado, em vez de ser removido assim que um consumidor o confirma. Isso permite que grupos independentes mantenham offsets diferentes, reconstruam projeções e processem o histórico novamente dentro da retenção configurada.

## Casos de uso

Integração orientada a eventos, pipelines de dados, reconstrução de projeções e múltiplos consumidores independentes são casos comuns.

## Boa prática

Defina chave de particionamento conscientemente, trate evolução de schema como contrato e planeje retenção e replay.

## Má prática

Escolher streaming para qualquer tarefa assíncrona aumenta complexidade quando uma fila simples bastaria. Outra má prática é assumir ordenação global quando o sistema só garante ordem dentro de uma partição.

## Kafka e filas

[Apache Kafka](kafka.md) é o exemplo clássico de event streaming. Um tópico possui partições, cada partição possui ordem própria e os consumidores avançam offsets. Um grupo de consumidores divide as partições entre suas instâncias; grupos diferentes podem ler o mesmo tópico de forma independente.

Uma fila tradicional é mais direta quando cada trabalho deve ser processado uma vez por um grupo e removido depois do ack. Kafka é mais adequado quando retenção, replay, múltiplos consumidores e processamento por partição são requisitos centrais.

## Continue por aqui

[Filas](filas.md) são frequentemente melhores quando o problema é distribuir trabalho, não preservar um log reproduzível.
