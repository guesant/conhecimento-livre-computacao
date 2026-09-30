# RabbitMQ

RabbitMQ é um broker de mensagens que implementa AMQP e outros protocolos por meio de plugins. Seu modelo principal separa publicação, roteamento e consumo: produtores publicam em exchanges, bindings conectam exchanges a filas ou streams e consumidores retiram mensagens das filas.

## Exchanges e bindings

Exchanges aplicam regras de roteamento. Direct usa correspondência exata da routing key, topic usa padrões por segmentos, fanout distribui para todos os destinos ligados e headers usa metadados. A fila é o local onde o consumidor recebe o trabalho; a exchange não é uma fila.

Essa separação permite publicar um evento uma vez e encaminhá-lo para várias filas, cada uma com seu próprio ritmo, retenção e grupo de consumidores. Um binding mal configurado pode descartar ou duplicar roteamento, portanto topology, permissões e testes de publicação fazem parte do contrato.

## Confirmações e acknowledgements

Publisher confirms informam que o broker assumiu responsabilidade pela publicação. Consumer acknowledgements informam que o consumidor recebeu e processou a entrega. São mecanismos diferentes e ambos podem ser necessários para uma cadeia confiável.

O consumidor deve usar ack manual quando o efeito precisa ser concluído antes de remover a mensagem. Se o processo cair antes do ack, RabbitMQ pode redeliver. Prefetch limita quantas mensagens não confirmadas ficam em voo e deve ser ajustado junto com concorrência e memória.

## Quorum, dead letter e reply-to

Quorum queues usam replicação baseada em Raft e podem ser adequadas quando a segurança da mensagem e alta disponibilidade justificam latência e storage adicionais. Não são automaticamente melhores para filas temporárias, backlog enorme ou baixa latência sem necessidade de replicação.

Dead-letter exchanges encaminham mensagens rejeitadas, expiradas ou excedentes para investigação e reprocessamento. Configure limite de tentativas e não faça requeue infinito. RabbitMQ também possui Direct Reply-to para alguns padrões de requisição e resposta, mas a aplicação ainda precisa de correlation ID, timeout e tratamento de resposta perdida.

## Quando usar

RabbitMQ é forte para filas de trabalho, roteamento flexível, fan-out, integração com AMQP, RPC assíncrono e workloads que precisam de ack explícito e controle de prefetch. Kafka costuma ser melhor para retenção longa, replay e alto volume de event streaming; SQS é mais simples quando a organização quer uma fila gerenciada na AWS.

## Operação

Defina durabilidade de exchanges, filas e mensagens, política de quorum, TTL, DLX, limites de memória, conexões, canais, TLS, vhosts e permissões. Monitore backlog, idade da mensagem, consumidores, unacked, publish confirms, redelivery, memória e flow control.

## Fontes primárias

- [RabbitMQ exchanges](https://www.rabbitmq.com/docs/exchanges)
- [RabbitMQ acknowledgements and publisher confirms](https://www.rabbitmq.com/docs/confirms)
- [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues)
