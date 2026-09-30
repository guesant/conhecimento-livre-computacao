# Comparação entre RPC e comunicação assíncrona

RPC e comunicação assíncrona resolvem necessidades diferentes, embora possam aparecer na mesma arquitetura. RPC representa uma operação que o consumidor solicita e normalmente espera concluir dentro de um deadline. Comunicação assíncrona representa trabalho ou um fato que pode ser processado depois, sem manter o produtor bloqueado até a conclusão.

## Comparação

| Dimensão | RPC síncrono | Comunicação assíncrona |
| --- | --- | --- |
| Resposta | Na mesma interação ou stream | Depois, por status, evento ou callback |
| Acoplamento temporal | Consumidor e provedor precisam estar disponíveis | Pode existir buffer entre eles |
| Falha | Timeout e resultado desconhecido | Retry, ack, backlog e dead letter |
| Consistência | Resultado imediato ou erro | Estado intermediário e eventual |
| Escala | Limitada por chamadas concorrentes | Limitada por fila, partição e workers |
| Uso comum | Consulta e comando curto | Job, evento e integração |
| Principal risco | Cascata de latência e indisponibilidade | Duplicação, atraso e reprocessamento |

## Escolha por interação

Use RPC quando a interface precisa saber imediatamente se uma operação foi aceita, quando o resultado é pequeno e quando o cliente pode aguardar dentro de um timeout. Uma consulta de perfil, validação de permissão ou criação simples de recurso pode ser síncrona.

Use uma fila quando o trabalho é demorado, precisa sobreviver à indisponibilidade do consumidor ou pode ser processado por workers em ritmo controlado. Geração de relatório, envio de email, importação e atualização de índice são candidatos comuns.

Use um evento quando outros componentes precisam reagir a um fato sem o produtor conhecer todos os consumidores. O produtor não deve depender da implementação de cada consumidor para concluir seu próprio comando.

## Composição

Uma requisição pode usar RPC para aceitar um comando e publicar um evento depois que a transação local for confirmada. O padrão outbox registra o evento no mesmo limite transacional do dado e um publicador o entrega ao broker.

Outra composição usa RPC para consulta síncrona e eventos para invalidar caches. Um serviço pode consultar uma fonte autoritativa e ainda reagir assincronamente a mudanças de outros domínios.

Não publique um evento antes de confirmar o estado que ele descreve. Não use um broker como substituto de uma resposta quando o usuário precisa saber se a operação foi validada. O contrato deve dizer se a resposta significa aceito, processado ou concluído.

## Retries e idempotência

RPC precisa de deadline e retry somente quando a operação for repetível ou quando existir uma chave de idempotência. O cliente pode não saber se o servidor executou a escrita antes do timeout.

Mensagens normalmente usam at-least-once. O consumidor deve aceitar duplicação, persistir uma chave de processamento e confirmar depois do efeito. Uma operação assíncrona também precisa de estado observável para que o cliente consulte erro, progresso e conclusão.

## Backpressure

RPC transmite pressão por conexões, filas internas e latência. Comunicação assíncrona torna o backlog explícito, mas não o elimina. Limite publicadores, workers, tamanho de mensagem e retenção. Um sistema que aceita eventos mais rápido do que consegue processar precisa rejeitar, atrasar ou amostrar de forma declarada.

## Segurança

Em ambos os modelos, autentique o chamador, autorize a ação, valide o payload e proteja dados. RPC deve validar metadados e mensagens; brokers devem proteger tópicos, grupos, offsets e operações administrativas. Não trate a posse de um correlation ID como autorização.

## Critério prático

Pergunte: o consumidor precisa do resultado para continuar? Se sim, comece com RPC. O trabalho pode continuar sem o consumidor ou precisa sobreviver a um restart? Se sim, considere uma fila. Outros componentes precisam reagir sem acoplamento direto? Considere eventos. Se a resposta é apenas "a solicitação foi recebida", retorne um identificador de operação e mova a execução para background.

## Fontes

- [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
- [Martin Fowler, Microservices](https://martinfowler.com/articles/microservices.html)
- [Transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html)
