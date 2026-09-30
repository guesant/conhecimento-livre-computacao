# Resiliência

Resiliência é a capacidade de continuar prestando um serviço aceitável durante
falhas, degradação ou recuperação. Ela não é sinônimo de capacidade: aumentar
recursos pode evitar saturação, mas não resolve uma falha de dependência, perda
de estado ou comportamento incorreto.

## Categorias

- [Resiliência](../resiliencia.md) apresenta princípios de continuidade,
  degradação e recuperação.
- [Fail-safe, fault tolerance e error handling](../fail-safe-fault-tolerance-e-error-handling.md)
  separa respostas seguras, tolerância a falhas e tratamento de erros.
- [Heartbeat](../heartbeat.md) detecta atividade ou ausência de progresso.
- [Idempotência](../idempotencia.md) permite repetir operações sem multiplicar
  efeitos indesejados.
- [Testes de capacidade](../testes/index.md) mede o comportamento sob demanda e
  sob falha controlada.

## Relação com capacidade

Capacidade pergunta quanto trabalho o sistema suporta dentro de um objetivo de
latência e erro. Resiliência pergunta como ele reage quando um componente
falha, a demanda muda ou a recuperação demora. Os dois domínios se encontram
em timeouts, filas, rate limiting, circuit breakers, retries e backpressure,
mas não devem ser tratados como uma única métrica.
