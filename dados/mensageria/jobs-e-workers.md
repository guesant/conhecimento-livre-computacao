# Jobs persistentes e workers

Um job é uma unidade de trabalho que pode ser enfileirada, persistida, executada e
observada separadamente da requisição que a criou. Um worker é o processo ou thread que
retira jobs da fila e executa seus handlers. O storage mantém o estado necessário para
que o trabalho sobreviva ao ciclo de vida de um processo.

O modelo é diferente de criar uma task em memória. Uma task local pode desaparecer no
restart, no deploy ou na falha do host. Um job persistente precisa de uma fila, tabela,
stream ou outro storage com estado de pendência, lease, tentativa e resultado.

## Ciclo de vida

Um job normalmente passa por estados como criado, disponível, reservado, executando,
concluído, falho, atrasado ou enviado para dead letter. O estado exato varia, mas a
transição precisa ser recuperável quando um worker cai.

O worker obtém um lease ou reserva. Se ele morrer antes do ack, o lease expira e outro
worker pode tentar novamente. Se o ack ocorrer antes da persistência do efeito, o trabalho
pode ser perdido. Se ocorrer depois, o mesmo trabalho pode ser redeliverado. Essas
possibilidades exigem idempotência.

## Storage

O storage de jobs precisa suportar durabilidade, concorrência, visibilidade, expiração,
retry e observação de estado. Banco relacional, Redis, broker ou sistema especializado
podem cumprir funções diferentes. A escolha deve considerar volume, latência, retenção,
ordenação, backup, locks e comportamento em falhas.

O storage não deve guardar payloads enormes, secrets ou referências a objetos que não
existem mais. Prefira um identificador estável e faça o worker carregar os dados no
momento da execução. Versione o contrato do job para que workers antigos e novos possam
coexistir durante um deploy.

## Workers

Workers retiram jobs, limitam concorrência e executam o código. Aumentar workers pode
reduzir backlog, mas também pode esgotar conexões, CPU, memória, rate limit e capacidade
do sistema externo.

Use filas separadas ou prioridades quando jobs críticos não puderem esperar atrás de
trabalho pesado. Um worker deve aceitar cancelamento e encerramento gracioso, terminar ou
devolver leases e deixar métricas suficientes para explicar o estado do backlog.

## Jobs recorrentes

Um scheduler transforma uma agenda em ocorrências de jobs. A definição da agenda deve ser
idempotente e possuir um identificador estável. Em uma implantação com múltiplos schedulers,
use lock ou mecanismo de eleição para não criar ocorrências duplicadas.

O scheduler não é necessariamente o worker. Separar as responsabilidades permite que a
produção de trabalho continue mesmo quando o processamento estiver temporariamente
reduzido, mas adiciona um componente que precisa de health check, clock correto e
observabilidade.

Jobs recorrentes devem tolerar atraso. Se uma execução demora mais que o intervalo, defina
se pode haver concorrência, se a próxima ocorrência deve ser ignorada, acumulada ou
compactada.

## Retry

Retry pode ocorrer no cliente, na fila, no worker, no SDK ou na dependência externa. Some
as camadas antes de definir o limite. Um retry interno de uma chamada HTTP e um retry do
job inteiro podem multiplicar o número de efeitos.

Classifique erros permanentes e transitórios. Use backoff e jitter, limite o número de
tentativas e encaminhe poison messages para dead letter. Uma dead letter queue sem alerta,
retenção e procedimento de reprocessamento é apenas um lugar para esconder falhas.

## Idempotência

O handler deve possuir uma chave de operação ou uma ação naturalmente idempotente. A
deduplicação pode usar uma constraint única, registro de execução, upsert ou API externa
com idempotency key.

Verificar apenas se o recurso existe antes de escrever cria uma condição de corrida. A
proteção contra concorrência precisa estar no banco, no storage ou em um protocolo capaz
de serializar a decisão.

## Backpressure e capacidade

A fila absorve diferença temporária entre produção e consumo, mas não resolve uma taxa de
entrada permanentemente maior. Monitore idade do job mais antigo, profundidade por fila,
tempo de espera, taxa de sucesso, duração, retries e capacidade dos workers.

Defina limites de payload, concorrência, memória e tempo de execução. Quando o backlog
atingir o limite, rejeite, atrase ou degrade a produção de trabalho de forma explícita.

## Relação com HTTP e transações

Uma API pode persistir um job e responder aceito antes da conclusão. Essa resposta deve
descrever a semântica real e oferecer status ou um identificador quando o consumidor
precisar acompanhar o resultado.

Se uma transação local altera dados e precisa publicar um job, registre os dois efeitos
com outbox ou mecanismo equivalente. Publicar na fila antes do commit pode fazer o worker
observar dados que serão revertidos; publicar depois pode perder a mensagem se o processo
falhar sem um registro durável.

## Relações

- [Filas](filas.md) explica entrega, ack, retry e dead letter.
- [Comunicação assíncrona](../../comunicacao/comunicacao-assincrona.md) compara fila,
  pub/sub, streaming e webhook.
- [Idempotência](../../confiabilidade/idempotencia.md) trata repetição segura.
- [Hangfire](../../dotnet/hangfire.md) implementa jobs persistentes no ecossistema .NET.
- [Transações e ACID](../transacoes-acid.md) explica o limite local da transação.

## Fontes

- [Hangfire, documentação](https://docs.hangfire.io/en/latest/)
- [Kubernetes, Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [Kubernetes, CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
