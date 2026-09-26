# Filas de mensagens

Uma fila desacopla produtores e consumidores armazenando mensagens até que consumidores possam processá-las. O produtor não precisa manter o consumidor disponível durante a mesma requisição, e o consumidor pode processar o backlog conforme sua capacidade.

Dependendo do sistema, confirmações, retries, ordenação, visibilidade, retenção e semântica de entrega variam. Uma fila normalmente distribui cada mensagem para um consumidor de um grupo; um tópico ou event bus pode entregar o mesmo fato a vários consumidores.

[Fila de prioridade](fila-de-prioridade.md) trata a escolha por urgência em vez de FIFO.
Prioridade não resolve capacidade e pode causar starvation, por isso também precisa de
fairness, aging ou quotas.

## Casos de uso

Processamento assíncrono de jobs, absorção de picos e desacoplamento temporal são usos comuns.

## Boa prática

Projete consumidores idempotentes quando redelivery é possível, confirme a mensagem somente depois do efeito necessário, defina política de retry e dead letter e monitore idade, profundidade, taxa de consumo e tempo de processamento.

Limite a concorrência por worker e globalmente. O limite precisa caber no banco, nas APIs externas, na CPU, na memória e no orçamento de conexões. Aumentar consumidores sem controlar o recurso protegido apenas desloca o backlog para outro lugar.

## Má prática

Assumir "exactly once" sem compreender as garantias de broker, consumidor e efeitos externos cria duplicação difícil de detectar. Retry infinito também transforma mensagens impossíveis em bloqueio operacional. Mensagens que falham repetidamente devem ser encaminhadas para uma dead letter queue com motivo, tentativas, timestamps e possibilidade de investigação ou replay controlado.

## Implementações

- [BullMQ](bullmq.md) usa Redis para jobs e workers em aplicações Node.js.
- [ActiveMQ](activemq.md) oferece um broker Apache com protocolos e modelos de fila e tópico.
- [RabbitMQ](rabbitmq.md) usa exchanges, bindings, filas, confirmações e acknowledgements.
- [Amazon SQS](sqs.md) oferece filas gerenciadas com visibilidade, DLQ e modos Standard e FIFO.
- [MQTT](mqtt.md) é um protocolo leve de publish/subscribe para dispositivos e redes restritas.
- [Apache Kafka](kafka.md) mantém streams particionados com retenção e offsets.

## Continue por aqui

[Event streaming](event-streaming.md) preserva eventos de forma que múltiplos consumidores possam manter posições independentes.
