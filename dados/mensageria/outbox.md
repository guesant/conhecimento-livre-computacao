# Outbox transacional

A outbox transacional é uma tabela ou registro local que armazena uma mensagem junto com a alteração de negócio que a originou. A aplicação confirma a transação local e um publicador separado tenta entregar os registros pendentes ao broker ou a outro sistema.

## Problema que resolve

Uma operação pode confirmar o banco e falhar antes de publicar o evento, ou publicar e falhar antes de confirmar o banco. Não existe uma transação local comum que inclua automaticamente PostgreSQL, RabbitMQ, Kafka, SQS e o serviço externo.

A outbox reduz essa janela colocando alteração e intenção de publicação no mesmo limite transacional. Se a transação confirmar, o worker poderá reenviar a mensagem mesmo que o broker esteja temporariamente indisponível.

## Fluxo

1. A aplicação valida o comando e abre uma transação.
2. Persiste a alteração de negócio.
3. Persiste na outbox o tipo, versão, payload, identificador e destino lógico do evento.
4. Confirma a transação.
5. Um worker busca registros pendentes com concorrência controlada.
6. Publica com confirmação do broker.
7. Marca o registro como publicado ou agenda nova tentativa.

O passo de publicação pode ocorrer mais de uma vez. Se o worker publicar e cair antes de marcar o registro, a próxima execução reenviará a mesma mensagem. Por isso o evento precisa de um identificador estável e os consumidores precisam ser idempotentes.

## Outbox como fallback local

Uma outbox é uma fila interna persistente para o período em que o broker não está disponível, mas não é um substituto permanente para o broker. Ela não deve ser usada para armazenar payload sem limite, nem para esconder indisponibilidade indefinidamente.

Defina retenção, tamanho máximo, política de compactação, prioridade, backoff, tentativas, dead letter e alerta. Se o backlog cresce mais rápido do que o worker publica, o sistema precisa aplicar backpressure ou degradar funcionalidades explicitamente.

## Concorrência

Vários workers podem processar a outbox se houver leasing, locking ou uma operação equivalente que impeça a mesma linha de ser trabalhada simultaneamente. O lock precisa ter expiração para que uma execução abandonada possa ser recuperada.

Uma estratégia comum é selecionar um lote pendente, marcá-lo como em processamento com um token de tentativa e publicar fora da transação do banco. O registro só deve ser considerado publicado depois da confirmação do destino. Não mantenha uma transação aberta durante uma chamada de rede lenta.

## Payload e schema

Prefira payload pequeno e versionado. Um evento pode carregar o identificador do recurso e dados mínimos para o consumidor buscar uma projeção atual, ou carregar um snapshot suficiente para replay independente. A escolha afeta acoplamento, custo de consultas e comportamento quando o recurso original muda ou é removido.

Não coloque segredos, credenciais ou objetos ORM inteiros na outbox. Classifique dados, aplique retenção e autorize acesso ao registro como faria com qualquer outra forma de armazenamento de mensagens.

## Outbox e inbox

Outbox protege a saída do produtor. Uma inbox ou tabela de consumo registra mensagens já aceitas pelo consumidor. Usar as duas pode permitir que a deduplicação e o efeito de negócio sejam confirmados no mesmo limite transacional local, embora a integração completa ainda precise tratar retry e falhas externas.

## Quando não usar

Não use outbox para uma notificação descartável que pode ser recriada, para uma métrica que pode ser perdida ou para substituir um broker com requisitos de retenção, fan-out, replay ou throughput que o banco não suporta. Nesses casos, o registro local pode apenas transferir o problema para a tabela de negócio.

## Relações

- [Idempotência](../../confiabilidade/idempotencia.md) trata a duplicação criada por publicação e redelivery.
- [Filas](filas.md) explica ack, retry e dead letter.
- [Event streaming](event-streaming.md) explica retenção, partições e offsets.
- [Event bus](../../comunicacao/event-bus.md) trata o contrato de publicação de fatos.
- [Jobs e workers](jobs-e-workers.md) trata o processamento persistente da outbox.

## Fonte

- [Transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html)
