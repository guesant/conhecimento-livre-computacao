# Sistemas distribuídos

Um sistema distribuído é composto por processos, máquinas ou serviços que cooperam por comunicação e não compartilham necessariamente memória ou relógio. Cada participante conhece apenas parte do estado e pode falhar enquanto os demais continuam executando.

## O que muda em relação ao local

Uma chamada remota pode atrasar, duplicar, perder-se ou produzir resultado desconhecido. O processo remoto pode concluir a operação e cair antes de devolver a resposta. Relógios podem divergir. Uma partição de rede pode impedir que dois participantes saibam qual estado é atual.

Por isso, abstrair a rede como uma função local é perigoso. Timeouts, cancelamento, idempotência, retries, circuit breakers, observabilidade e compatibilidade fazem parte do contrato da operação.

## Propriedades

Um sistema distribuído pode ter:

- múltiplos processos e failure domains;
- comunicação por rede ou mensagens;
- estado replicado ou particionado;
- concorrência e ordem parcial de eventos;
- falhas parciais;
- consistência configurável;
- descoberta e autenticação entre participantes.

Nem todo sistema distribuído é microsserviço. Um cluster de banco, um sistema de arquivos distribuído, um scheduler e uma fila também são sistemas distribuídos.

## Coordenação

Coordenação pode usar liderança, quorum, consenso, locks distribuídos, leases, relógios lógicos, versionamento ou eventos. Cada mecanismo tem hipóteses sobre falhas, latência e durabilidade.

Um lock distribuído não torna uma operação automaticamente idempotente. Um quorum não impede bugs de aplicação. Um evento ordenado em uma partição não produz ordem global sem custo adicional.

## Consistência

Consistência forte facilita raciocínio, mas custa latência, disponibilidade ou capacidade de particionar. Consistência eventual permite disponibilidade e escala maiores, mas exige reconciliação, idempotência, compensação e uma UX que tolere estados intermediários.

Escolha a consistência por operação. Uma leitura de catálogo pode aceitar atraso curto; uma transferência financeira pode exigir confirmação forte e uma sequência transacional. Não trate o sistema inteiro com uma única promessa vaga de consistência.

## Comunicação

RPC é apropriado quando o consumidor precisa de uma resposta dentro de um prazo. Mensagens e eventos são adequados quando o trabalho pode continuar depois, quando o consumidor pode estar indisponível ou quando vários consumidores devem reagir.

Uma arquitetura pode combinar RPC síncrono, filas duráveis e streams. O protocolo não elimina as decisões sobre retry, ordenação, duplicação, backpressure e dead letters.

## Observabilidade

Logs isolados por processo são insuficientes. Use correlation IDs, tracing distribuído, métricas de chamadas, filas, retries, timeouts e dependências. Registre a versão do contrato e a identidade do consumidor quando isso for necessário para diagnóstico.

Não capture payloads sensíveis por padrão. Observabilidade também precisa de autorização, retenção e limites de cardinalidade.

## Segurança

Cada chamada entre processos precisa de autenticação e autorização compatíveis com sua responsabilidade. TLS protege o canal, mas não decide se um serviço pode executar uma operação. Secrets, identidades de workload, rotação, replay e confiança em headers precisam ser tratados como parte da arquitetura.

## Quando usar

Distribuição é justificável quando capacidade, disponibilidade, localização, isolamento ou autonomia exigem mais de um failure domain. Ela também pode ser imposta pelo ambiente, como dispositivos edge e regiões distintas.

Não distribua somente para imitar uma tendência. O custo de rede, operação, consistência e diagnóstico precisa produzir um benefício observável.

## Fontes

- [Martin Fowler, distributed objects and microservices](https://martinfowler.com/articles/distributed-objects-microservices.html)
- [Martin Kleppmann, Designing Data-Intensive Applications](https://dataintensive.net/)
- [Google SRE book, distributed systems](https://sre.google/sre-book/)
