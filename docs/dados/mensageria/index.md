# Mensageria

Mensageria transporta comandos, eventos e unidades de trabalho entre produtores e consumidores. A categoria inclui filas, jobs, workers, event streaming e brokers, mas cada modelo possui garantias diferentes de retenção, ordenação, replay, entrega e concorrência.

## Páginas

- [Filas](filas.md) apresenta produtores, consumidores, ack, retry e dead letter.
- [Fila de prioridade](fila-de-prioridade.md) trata ordenação por urgência.
- [Jobs e workers](jobs-e-workers.md) separa o trabalho persistido do processo que o executa.
- [Event streaming](event-streaming.md) trata logs particionados e posições de consumidores.
- [Outbox](outbox.md) coordena a persistência da intenção de publicar com a transação de negócio.
- [BullMQ](bullmq.md), [ActiveMQ](activemq.md), [MQTT](mqtt.md), [RabbitMQ](rabbitmq.md), [Amazon SQS](sqs.md) e [Apache Kafka](kafka.md) apresentam implementações distintas.

## Decisão

Defina se a mensagem é comando ou evento, o que significa sucesso, por quanto tempo ela fica retida, se pode ser reprocessada e como falhas são observadas. Concorrência, idempotência e limites de consumo precisam estar no contrato. Um broker não corrige uma operação que não pode ser repetida com segurança.
