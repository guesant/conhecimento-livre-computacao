# Amazon SQS

Amazon Simple Queue Service é uma fila gerenciada para desacoplar componentes distribuídos sem operar um broker próprio. A API trabalha com envio, recebimento, visibilidade e remoção da mensagem. A mensagem permanece armazenada enquanto está invisível para outros consumidores durante o visibility timeout e é removida depois que o consumidor confirma o processamento com uma exclusão.

## Standard e FIFO

Standard oferece alta escala e entrega pelo menos uma vez, portanto duplicação é possível. FIFO acrescenta ordenação por `MessageGroupId` e deduplicação em uma janela limitada, mas não elimina a necessidade de consumidores idempotentes quando efeitos externos estão envolvidos.

Ordenação FIFO é por grupo de mensagens, não necessariamente global. Um grupo com uma mensagem em processamento pode bloquear as seguintes do mesmo grupo até exclusão ou expiração da visibilidade.

## Visibility timeout

O timeout deve ser maior que o tempo esperado de processamento e exclusão. Se for curto, outro consumidor pode receber a mesma mensagem enquanto o primeiro ainda trabalha. Se for longo demais, uma falha demora para permitir nova tentativa. Para jobs longos, o consumidor pode estender a visibilidade enquanto continua ativo.

## Dead letter e retries

Uma redrive policy pode encaminhar mensagens que excederam o número permitido de recebimentos para uma dead-letter queue. A DLQ precisa de alarmes, retenção e procedimento de investigação. Reprocessar diretamente sem corrigir a causa pode gerar um loop de falha.

SQS não oferece uma transação automática com o banco da aplicação. Use outbox quando a mensagem precisar ser criada no mesmo commit do dado de negócio, ou aceite explicitamente a possibilidade de publicação perdida e reconciliação posterior.

## Fire-and-forget e escala

SQS é apropriado para aceitar um trabalho e processá-lo depois, mas a resposta do produtor só deve indicar que o envio foi confirmado pela API. O efeito final pode estar pendente. Escale consumidores observando backlog, idade da mensagem, tempo de processamento, taxa de erro, visibilidade e limites de API.

## Segurança e payload

Use IAM, políticas de fila, criptografia gerenciada ou KMS e TLS. A mensagem possui limite de tamanho; para dados maiores, armazene o conteúdo em S3 e coloque na fila um ponteiro validado. Não coloque PII ou segredos no nome da fila nem em payload sem classificação e retenção.

## Relações

- [Outbox](outbox.md) trata a publicação local antes do envio para SQS.
- [Filas](filas.md) explica ack, retry e dead letter.
- [Apache Kafka](kafka.md) representa event streaming com retenção e replay diferentes.

## Fontes primárias

- [O que é Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)
- [Outage recovery scenarios](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/designing-for-outage-recovery-scenarios.html)
