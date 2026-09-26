# Event bus

Um event bus distribui fatos que já aconteceram para consumidores interessados. O publicador comunica algo como `OrderPlaced`; ele não escolhe necessariamente todos os consumidores nem espera um resultado de cada um. O bus pode existir dentro de um processo ou ser implementado por um broker entre processos.

## Evento e comando

Evento descreve uma mudança concluída. Comando solicita uma ação a um destinatário responsável. `OrderPlaced` é diferente de `PlaceOrder`. A primeira mensagem pode ter vários consumidores independentes; a segunda precisa de ownership, autorização, resultado e política de erro mais explícitos.

## Modelo de entrega

Um event bus em memória não oferece por si só durabilidade, replay, isolamento de processo ou recuperação depois de uma reinicialização. Ele é útil para desacoplar módulos dentro de um monólito, mas não deve ser apresentado como garantia de entrega distribuída.

Um bus baseado em broker pode persistir mensagens, distribuir para consumidores, controlar confirmação, reter eventos e permitir que grupos diferentes leiam o mesmo fato. Essas propriedades dependem do broker e da configuração, não apenas do nome `event bus`.

## Publicação confiável

Se o evento representa uma alteração de banco, publicar fora da transação cria uma janela entre o commit e a entrega. Publicar antes do commit permite que o consumidor observe um fato que pode ser revertido. A [outbox](../dados/mensageria/outbox.md) registra o evento na mesma transação e um worker faz a publicação posterior.

O publicador deve incluir identificador do evento, tipo, versão, timestamp, correlation ID e uma referência suficiente para o consumidor. O consumidor deve ser idempotente, tolerar duplicação, validar schema e tratar eventos fora de ordem quando a topologia não garante ordenação.

## Event bus e resposta

Um event bus não é uma API de retorno. Se o solicitante precisa de uma resposta para continuar a mesma interação, use RPC ou um padrão explícito de reply-to com correlation ID e timeout. Se a resposta for opcional e puder chegar depois, um evento de resultado pode ser suficiente.

## Relação com o barramento interno

O [barramento interno](../arquitetura-aplicacoes/bus-interno.md) explica a versão dentro de um processo, incluindo command bus, query bus e event bus. Esta página trata o contrato conceitual que continua válido quando a entrega passa a ser feita por um broker.

## Fontes primárias

- [CloudEvents specification](https://cloudevents.io/)
- [RabbitMQ, exchanges](https://www.rabbitmq.com/docs/exchanges)
- [Apache Kafka, introduction](https://kafka.apache.org/intro/)
