# Apache ActiveMQ

Apache ActiveMQ é uma família de brokers de mensagens da Apache. O nome inclui o ActiveMQ Classic e o ActiveMQ Artemis, que possuem arquiteturas, APIs, protocolos e trajetórias de operação diferentes. Uma decisão precisa registrar qual produto foi escolhido, em vez de tratar ActiveMQ como uma implementação única.

## Modelo de mensagens

ActiveMQ pode oferecer filas, tópicos, acknowledgements, redelivery, persistência, transações e integração com APIs como JMS ou Jakarta Messaging. Artemis também trabalha com um modelo de endereços e filas, além de protocolos como AMQP, MQTT, STOMP, OpenWire e o protocolo próprio.

Fila distribui trabalho para consumidores. Tópico publica para múltiplos assinantes. A escolha deve refletir a semântica de entrega, o número de consumidores, o replay necessário e a forma de reconhecer processamento.

## Persistência e falhas

Configure armazenamento, redelivery delay, máximo de tentativas e dead letter address ou queue. Uma mensagem não deve voltar indefinidamente para a mesma fila sem uma classificação de falha. Falhas de conexão, confirmação tardia e reinício do broker precisam ser testadas com consumidores idempotentes.

Artemis oferece recursos de alta disponibilidade, replicação, cluster, bridges, federation, métricas e controle de utilização. Eles aumentam a capacidade, mas também aumentam o número de failure domains e decisões de operação.

## Quando usar

ActiveMQ é uma opção natural quando a organização precisa de um broker Apache com compatibilidade JMS, múltiplos protocolos, integração com aplicações Java ou migração de uma topologia tradicional de mensagens. Artemis costuma ser considerado quando throughput, recursos modernos de broker e operação distribuída são requisitos relevantes.

## Cuidados

Não confunda compatibilidade de protocolo com equivalência de semântica. Confirme como cada cliente trata ack, transação, redelivery, ordering, TTL, DLQ e confirmação de publicação. Defina autenticação, autorização por destino, TLS, limites de payload, retenção, storage e backups.

## Relações

- [Filas](filas.md) explica a semântica comum.
- [MQTT](mqtt.md) trata o protocolo publish/subscribe para dispositivos.
- [RabbitMQ](rabbitmq.md) usa um modelo diferente baseado em exchanges e bindings.
- [Apache Kafka](kafka.md) é um event streaming com partições e offsets.

## Fontes primárias

- [Apache ActiveMQ Classic documentation](https://activemq.apache.org/components/classic/documentation/)
- [Apache ActiveMQ Artemis documentation](https://artemis.apache.org/components/artemis/documentation/latest/)
