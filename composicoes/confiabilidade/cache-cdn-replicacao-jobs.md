# Cache, CDN, replicação e jobs

Cache, CDN, replicação e jobs podem formar uma cadeia de leitura, escrita e processamento
assíncrono. Cada componente reduz um tipo de custo ou falha, mas também cria estado,
atraso e uma nova política de consistência.

Uma composição típica é:

1. o cliente consulta a CDN;
2. a CDN serve uma resposta fresca ou consulta a origem;
3. a aplicação consulta um cache interno;
4. em um miss, a leitura vai ao primary ou a uma réplica elegível;
5. alterações são confirmadas no primary;
6. invalidação, replicação e eventos atualizam cópias e projeções;
7. workers executam jobs persistentes e atualizam sistemas derivados.

Essa cadeia não precisa conter todas as camadas. Adicionar uma cópia ou um worker só é
melhoria quando o custo que ele reduz for maior que a complexidade que introduz.

## Caminho de leitura

Conteúdo público e imutável pode ser servido pela CDN com TTL longo e assets versionados.
Conteúdo público mutável pode usar TTL curto, revalidação ou stale-while-revalidate. Dados
privados exigem chave que inclua identidade e autorização ou devem permanecer fora de uma
cache pública.

Depois da CDN, um cache de aplicação pode evitar consultas repetidas ao banco. O cache
deve ter chave, versão, TTL, invalidação e política de miss. Se a origem estiver lenta,
stale pode manter a leitura, mas o sistema deve mostrar a idade ou respeitar o limite de
staleness definido pelo domínio.

Uma réplica de leitura pode reduzir carga do primary, mas pode estar atrasada. Depois de
uma escrita, a aplicação pode precisar ler do primary ou esperar uma posição de replicação
para cumprir read-after-write.

## Caminho de escrita

Escritas devem ir para a autoridade definida, normalmente o primary. O banco confirma a
transação local; depois disso, o sistema pode invalidar cache, publicar evento e permitir
que replicas ou projeções recebam a alteração.

Não confirme a escrita apenas porque o cache foi atualizado. O cache é derivado. Se a
origem falhar, o sistema deve deixar clara a diferença entre alteração confirmada, job
aceito e atualização de cópia pendente.

Outbox registra o evento na mesma transação da alteração e um worker o publica depois.
Esse padrão reduz a janela entre banco e fila, mas o publicador e o consumidor ainda
precisam de retry, idempotência e observabilidade.

## Workers e jobs

O worker deve receber trabalho persistido, possuir lease ou ack, aceitar encerramento
gracioso e controlar concorrência. Jobs recorrentes precisam de identificador estável,
clock confiável e proteção contra duas ocorrências para o mesmo intervalo.

Um job que recalcula cache, replica uma projeção ou invalida uma CDN pode ser repetido.
Use chave de operação, geração de conteúdo e estado de conclusão para evitar que retries
produzam efeitos inconsistentes.

## Resiliência da cadeia

Toda chamada entre componentes precisa de timeout. Retry deve ser finito, usar backoff e
ser aplicado apenas quando a operação puder ser repetida. Circuit breaker evita continuar
chamando uma origem ou provedor em falha. Fallback pode servir stale, uma réplica ou uma
resposta parcial, desde que isso seja semanticamente permitido.

Rate limiting protege a origem contra usuários e contra os próprios retries. Hedging pode
reduzir latência de leitura ao consultar uma réplica alternativa, mas aumenta carga e não
deve ser aplicado a escritas ou operações sem idempotência.

Bulkheads, filas separadas e pools distintos impedem que refresh de cache, jobs pesados ou
uma CDN em miss consumam todas as conexões do sistema.

## Replicação e cache não são backup

Uma alteração destrutiva confirmada pode ser replicada e aquecer o cache com o valor
errado. CDN, cache interno e réplica melhoram latência ou continuidade; backup preserva
histórico e permite recuperar um estado anterior.

O procedimento de recuperação precisa dizer qual fonte será restaurada, como invalidar
cópias antigas, como pausar workers e como reconstruir jobs pendentes. Reativar workers
antes de restaurar invariantes pode produzir novos efeitos sobre dados incompletos.

## Observabilidade

Correlacione request, trace, cache key versionada, operação de escrita, primary/replica,
job, tentativa e efeito externo. Monitore:

- hit, miss, stale, eviction e idade do cache;
- status da CDN, POP, origem e purge;
- lag, elegibilidade e troca de primary;
- profundidade e idade das filas;
- duração e retries dos workers;
- timeouts, circuit breakers, fallbacks e rate limiting;
- operações hedgeadas e seu custo adicional.

Sem essas dimensões, um aumento de latência pode parecer problema da API quando foi uma
avalanche de cache miss, uma réplica atrasada ou um backlog de jobs.

## Relações

- [Cache](../../dados/cache.md) define cópias derivadas e invalidação.
- [CDN](../../rede/cdn.md) define cache HTTP na borda.
- [Replicação](../../dados/replicacao.md) define primary, replicas, lag e failover.
- [Jobs e workers](../../dados/mensageria/jobs-e-workers.md) define processamento persistente.
- [Resiliência](../../confiabilidade/resiliencia.md) define timeout, retry, breaker e fallback.
- [Rate limiting](../../rede/rate-limiting/index.md) controla capacidade compartilhada.
- [Polly](../../dotnet/polly.md) implementa pipelines de resiliência em .NET.

## Fontes

- [RFC 9111, HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [PostgreSQL, alta disponibilidade](https://www.postgresql.org/docs/current/high-availability.html)
- [Microsoft, transient fault handling](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults)
