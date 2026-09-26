# Apache Kafka

Apache Kafka é uma plataforma distribuída de event streaming. Eventos são publicados em tópicos e armazenados em partições ordenadas por offset. Consumidores leem pela posição que controlam, e a retenção permite que o mesmo histórico seja processado por grupos independentes ou novamente depois de uma falha.

## Tópicos, partições e chaves

Um tópico pode ter vários produtores e consumidores. Partições distribuem armazenamento e paralelismo entre brokers. Eventos com a mesma chave são direcionados para a mesma partição, permitindo ordenar eventos relacionados ao mesmo recurso. Kafka não oferece ordem total entre partições diferentes.

O número de partições limita o paralelismo de um consumer group na forma tradicional: em um instante, uma partição é atribuída a um consumidor do grupo. Adicionar consumidores além das partições não aumenta o processamento desse tópico, embora possa ser útil quando o grupo assina vários tópicos.

## Consumer groups e offsets

Um consumer group representa um assinante lógico. Instâncias do grupo dividem partições e reequilibram a atribuição quando entram ou saem. Grupos diferentes leem o mesmo tópico independentemente, o que oferece semântica de fan-out sem duplicar o armazenamento do evento.

O offset é a posição do consumidor. Commitar o offset antes de persistir o efeito pode perder trabalho; commitá-lo depois pode causar redelivery. O consumidor deve combinar a posição com idempotência, transações ou uma estratégia de processamento que tolere duplicação.

## Retenção e replay

Eventos não são removidos simplesmente porque um consumidor os leu. Retenção por tempo, tamanho ou compactação define quanto histórico permanece. Replay é útil para reconstruir projeções, corrigir consumidores e alimentar novos grupos, mas exige schema compatível, controle de carga e cuidado com efeitos externos não repetíveis.

## Produtores, confirmação e schema

O produtor deve definir chave, confirmação, compressão, batching e tratamento de erro de acordo com a semântica desejada. Eventos precisam de envelope versionado, identificador, timestamp, correlation ID e contrato de evolução. Um schema registry pode ajudar a governar compatibilidade, mas não substitui a decisão sobre significado do evento.

## Quando usar

Kafka é apropriado para integração por eventos, ingestão contínua, alto volume, múltiplos consumidores, replay, processamento por janelas e reconstrução de projeções. Para um job simples que precisa ser processado por uma única instância e removido após o ack, uma fila como RabbitMQ ou SQS tende a ser mais simples.

## Operação e segurança

Planeje fator de replicação, brokers, armazenamento, retenção, partições, rebalanceamento, quotas, autenticação, autorização, TLS, monitoramento de lag e evolução de schema. Replicação do tópico não substitui backup, e retenção não deve ser confundida com uma estratégia de recuperação completa.

## Relações

- [Event streaming](event-streaming.md) explica o conceito de log particionado.
- [Event bus](../../comunicacao/event-bus.md) explica publicação de fatos.
- [Outbox](outbox.md) trata a transação entre banco local e publicação.
- [RabbitMQ](rabbitmq.md) e [Amazon SQS](sqs.md) representam modelos de fila diferentes.

## Fontes primárias

- [Apache Kafka introduction](https://kafka.apache.org/intro/)
- [Apache Kafka documentation](https://kafka.apache.org/documentation/)
