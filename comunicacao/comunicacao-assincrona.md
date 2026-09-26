# Comunicação assíncrona

Comunicação assíncrona separa o envio de uma mensagem da disponibilidade imediata e da execução do consumidor. O produtor publica trabalho ou um evento e pode continuar sem esperar a conclusão final. O resultado pode ser entregue depois, consultado por status ou usado para disparar outros consumidores.

Assíncrono não significa necessariamente paralelo, durável ou sem resposta. Uma função pode ser assíncrona no código e ainda usar uma chamada HTTP síncrona. O conceito importante é a separação temporal entre produtor e consumidor.

## Fire-and-forget

Fire-and-forget significa aceitar o trabalho e encerrar a operação do produtor sem esperar o resultado final. A resposta deve indicar apenas que a intenção foi aceita, enfileirada ou persistida, conforme o contrato. Ela não deve afirmar que o efeito externo já ocorreu.

Fire-and-forget só é seguro quando a durabilidade, o retry, a observabilidade e o destino da falha estão definidos. Colocar uma função em uma thread, promise ou callback sem storage persistente não cria uma fila: a execução pode desaparecer quando o processo reiniciar.

## Formas

### Fila de trabalho

Uma mensagem representa trabalho para um consumidor. Em geral, cada mensagem é processada por um worker ou por um grupo, com ack, retry e dead letter. Fila é apropriada para distribuir tarefas e limitar concorrência.

### Pub/sub

O produtor publica em um tópico e múltiplos consumidores recebem uma cópia lógica. Cada consumidor possui seu offset ou ack. Pub/sub é adequado quando vários domínios precisam reagir ao mesmo fato.

### Event streaming

Um log persistente mantém eventos ordenados dentro de partições para que consumidores leiam e retomem a partir de offsets. O histórico pode ser reprocessado, mas retenção, compactação, ordem e schema precisam ser definidos.

### Callback e webhook

O resultado é enviado para um endpoint depois. O receptor deve autenticar a origem, validar assinatura, suportar duplicação e responder rapidamente. O produtor precisa de retry com backoff e uma política para falhas permanentes.

### Reply-to

Reply-to é um metadado que indica para onde uma resposta de uma mensagem deve ser publicada. Ele permite um padrão de requisição e resposta sobre um transporte assíncrono, normalmente acompanhado por um correlation ID para relacionar a resposta à solicitação.

Reply-to não transforma a chamada em RPC confiável. O solicitante ainda precisa de timeout, tratamento de resposta perdida, autorização da fila ou tópico de resposta e uma política para respostas atrasadas. Em RabbitMQ, Direct Reply-to pode evitar a criação de uma fila de resposta em alguns cenários, mas deve ser usado somente quando suas garantias e limitações forem compatíveis com o caso.

## Contrato da mensagem

Uma mensagem deve ter tipo, versão, identificador, timestamp, correlation ID e payload suficiente para o consumidor. Eventos descrevem fatos que ocorreram; comandos pedem que um destinatário execute uma ação. Misturar os dois dificulta ownership e reprocessamento.

Schemas precisam evoluir de forma compatível. Consumidores devem tolerar campos adicionais, produtores não devem reutilizar identificadores com outra semântica e mudanças incompatíveis precisam de migração ou nova versão.

## Entrega

At-most-once pode perder mensagens, mas evita duplicação. At-least-once pode entregar mais de uma vez e exige idempotência. Exactly-once costuma ser uma propriedade limitada a uma fronteira específica, não uma garantia mágica de toda a cadeia.

O consumidor deve confirmar somente depois de persistir o efeito necessário. Se confirmar antes, uma falha pode perder trabalho. Se processar e cair antes do ack, a mensagem pode voltar. Isso é esperado e deve ser tratado com chave idempotente, deduplicação ou operação naturalmente repetível.

## Backpressure e ordenação

Limite concorrência, tamanho da fila, taxa de publicação e tempo máximo de processamento. Sem backpressure, um consumidor lento acumula memória, backlog e custo.

Ordenação normalmente existe por partição, chave ou fila, não globalmente. Se dois eventos para o mesmo recurso precisam de ordem, escolha uma chave de particionamento adequada e trate eventos atrasados.

## Falhas

Defina retry transitório, dead letter, expiração, poison messages e replay. Um retry infinito pode bloquear a fila. Um dead letter sem monitoramento apenas esconde perda de negócio. Reprocessamento deve ser seguro e observável.

Quando o broker estiver indisponível, uma outbox transacional pode registrar a mensagem junto com a alteração local. Um worker publica depois, confirma a entrega e marca o registro como publicado. Isso preserva a intenção durante a indisponibilidade, mas não torna o broker síncrono nem elimina a necessidade de idempotência.

## Quando usar

Use comunicação assíncrona para jobs lentos, integração com sistemas indisponíveis, notificações, ingestão, processamento em lote e reação de múltiplos consumidores. Use RPC quando o cliente precisa da decisão ou do resultado para continuar a mesma interação.

## Segurança

Autentique produtores e consumidores, autorize tópicos e operações, proteja dados em trânsito e em repouso e defina retenção. Mensagens podem permanecer armazenadas muito depois da resposta HTTP e devem receber classificação e controle de acesso compatíveis.

## Fontes

- [CloudEvents specification](https://cloudevents.io/)
- [Apache Kafka documentation](https://kafka.apache.org/documentation/)
- [RabbitMQ, queues and messages](https://www.rabbitmq.com/docs/queues)
