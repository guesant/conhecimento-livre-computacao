# Idempotência

Uma operação é idempotente quando executar a mesma operação novamente produz o mesmo
estado observável que executar uma vez. Em notação simples, para uma operação `f`, a
propriedade é `f(f(estado)) = f(estado)`.

Isso não significa que a segunda execução não faça nada internamente. Ela pode consultar
estado, registrar uma tentativa ou devolver o resultado já persistido. O requisito é que
ela não aplique um efeito incorreto adicional.

## Por que é necessária

Timeouts criam incerteza. O cliente pode não saber se o servidor falhou antes de executar,
executou e falhou antes de responder, ou executou e respondeu depois de o cliente desistir.
Filas com entrega pelo menos uma vez podem redeliver uma mensagem. Workers podem ser
reiniciados depois de aplicar parte do efeito.

Sem idempotência, retry e redelivery podem duplicar cobrança, envio de email, criação de
recurso, publicação de evento ou atualização de contador.

## Formas de obter

### Operação naturalmente idempotente

Definir o estado final pode ser repetível. Uma operação que garante que um recurso está
ativo tende a ser mais fácil de repetir do que uma operação que incrementa um valor.

### Chave de idempotência

O cliente envia uma chave única para a intenção. O servidor registra a chave, o resultado
e os parâmetros relevantes. Uma repetição com a mesma chave pode retornar o resultado
anterior. Reutilizar a chave com parâmetros diferentes deve ser rejeitado.

### Restrição e upsert

Uma constraint única pode impedir duplicatas. Upsert combina inserção e atualização sob uma
regra explícita. A constraint precisa estar no banco quando a concorrência puder criar a
mesma operação simultaneamente; um `SELECT` anterior sozinho tem condição de corrida.

### Deduplicação de mensagens

O consumidor registra message ID ou event ID antes de confirmar a entrega. O registro e o
efeito precisam possuir uma relação transacional ou uma estratégia de recuperação. Um
cache temporário não é suficiente se a mensagem puder ser redeliverada depois da expiração.

### Reconciliação

Um reconciler compara o estado observado com o estado desejado e aplica apenas a diferença.
Esse modelo é comum em IaC e controladores, mas continua sujeito a destruição, recriação,
drift e efeitos externos não idempotentes.

## HTTP

GET, HEAD, PUT e DELETE são definidos pelo HTTP como métodos idempotentes em sua semântica
de intenção, mas a implementação pode ter efeitos laterais como logs, métricas ou
auditoria. POST não é idempotente por padrão. Uma API pode tornar uma criação repetível
com uma chave de idempotência e um contrato explícito.

Ser idempotente não significa ser seguro. DELETE pode ser idempotente e ainda ser
destrutivo. Uma autorização válida continua necessária em todas as tentativas.

## Concorrência

Idempotência não elimina lost update, race condition ou ordenação. Duas requisições com
chaves diferentes podem tentar alterar o mesmo recurso ao mesmo tempo. Use constraints,
locks, versionamento, compare-and-set ou isolamento transacional conforme a invariável.

Uma mesma chave processada simultaneamente exige coordenação. O banco pode usar uma chave
única e tratar uma inserção concorrente, ou um lock apropriado pode serializar a decisão.

## Efeitos externos

Uma transação local não inclui automaticamente um provedor de email, pagamento, API ou
broker externo. Registre a intenção localmente e use uma operação que o provedor possa
deduplicar. Se isso não for possível, mantenha estado de tentativa, reconciliação e
compensação para lidar com a incerteza.

Outbox resolve a publicação confiável de uma mensagem a partir de uma transação local,
mas o consumidor ainda precisa ser idempotente. Saga e compensação tratam workflows que
não podem compartilhar uma transação ACID, mas não desfazem perfeitamente todo efeito
externo.

## Limites

Idempotência depende da janela de retenção da chave, do escopo do recurso e da identidade
da intenção. Uma chave válida por dez minutos não protege uma redelivery ocorrida depois
de um dia. Limpar o registro cedo demais pode reabrir a possibilidade de duplicação.

Também não existe garantia universal de exactly-once em uma cadeia formada por cliente,
rede, serviço, banco, fila e provedor externo. É possível obter processamento exatamente
uma vez em uma fronteira específica, mas a propriedade precisa ser descrita com precisão.

## Relações

- [Resiliência](resiliencia.md) usa idempotência para tornar retries seguros.
- [Transações e ACID](../dados/transacoes-acid.md) limita o que uma única transação pode
  garantir.
- [Comunicação assíncrona](../comunicacao/comunicacao-assincrona.md) explica redelivery e
  delivery semantics.
- [Idempotência em IaC](../iac/idempotence.md) trata estado desejado.
- [Idempotência em workloads Kubernetes](../kubernetes/workloads/idempotencia.md) trata
  jobs e reconciliação.

## Fontes

- [RFC 9110, métodos idempotentes](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods)
- [Microsoft, transient fault handling](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults)
- [Transactional outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html)
