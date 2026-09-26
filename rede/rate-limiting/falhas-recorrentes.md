# Limitação adaptativa por falhas recorrentes

Rate limiting normalmente controla volume. Uma política adaptativa também pode reagir
a falhas repetidas recentes, reduzindo a velocidade de uma identidade, origem,
operação ou combinação de sinais. O objetivo é conter brute force, retry storm,
abuso automatizado e consumo inútil de recursos sem transformar qualquer erro legítimo
em bloqueio permanente.

A limitação deve ser aplicada depois de definir o que é falha. Uma senha incorreta,
um token inválido, uma entrada rejeitada, um timeout da dependência e um erro interno
não representam a mesma intenção. Contar todos os status 4xx e 5xx em uma única
penalidade pode punir usuários por problemas causados pelo próprio serviço.

## Modelo de pontuação

Uma implementação pode manter um score com decaimento temporal:

1. classifique o resultado da operação;
2. atribua um peso para falhas que realmente indicam abuso ou retry;
3. aumente o score com TTL;
4. reduza ou expire o score quando não houver novas falhas;
5. aplique uma janela de cooldown quando o score ultrapassar o limite;
6. permita recuperação gradual em vez de bloqueio indefinido.

O score não precisa ser exibido ao usuário. O cliente deve receber uma resposta
consistente, normalmente HTTP 429 quando a operação foi limitada, com Retry-After
quando o prazo puder ser informado. Não revele se um usuário, e-mail ou conta existe
apenas porque a resposta de uma tentativa falhou.

## Chaves de limitação

Use a chave mais próxima da ameaça e mais confiável para a fase da operação:

| Fase | Chave possível | Risco |
| --- | --- | --- |
| Antes da autenticação | IP, prefixo de rede, fingerprint limitada ou combinação de sinais | NAT pode agrupar usuários legítimos; fingerprint pode ser instável. |
| Depois da autenticação | ID interno do usuário, tenant, token ou client ID | A identidade pode ser roubada ou usada para provocar bloqueio. |
| Por operação | Identidade e nome normalizado da operação | A chave fica mais específica e exige mais estado. |
| Por recurso caro | Identidade, recurso e janela | Evita que uma operação cara consuma todo o serviço. |

Não use apenas IP para proteger usuários atrás de NAT e não use apenas usuário para
proteger contra ataque distribuído. Uma política robusta combina limites por origem,
identidade e operação, com valores diferentes e duração limitada.

## O risco de bloqueio provocado pelo atacante

Um atacante pode enviar tentativas inválidas para a conta de outra pessoa e provocar
um bloqueio. Esse ataque transforma o mecanismo de proteção em negação de serviço.
Para reduzir o risco:

- use limitação combinada, não apenas uma chave de usuário;
- prefira atraso, step-up ou desafio antes de bloqueio longo;
- limite a duração máxima da penalidade;
- permita recuperação por uma autenticação forte;
- diferencie falhas do cliente de falhas da dependência;
- audite mudanças de score sem registrar segredos;
- ofereça suporte operacional para desbloqueio seguro.

Em fluxos de recuperação de conta, não faça o tempo de resposta revelar se o endereço
existe. Em fluxos críticos, considere autenticação multifator, CAPTCHA ou aprovação
adicional em vez de simplesmente aumentar a duração do bloqueio.

## Estado distribuído

Em uma única réplica, estado local pode ser suficiente. Em múltiplas réplicas, o
limite local pode ser facilmente contornado alternando instâncias. Um estado
compartilhado representa melhor o total, mas introduz latência, custo, expiração,
particionamento e uma nova dependência.

Use TTL e limites de memória para scores, buckets e contadores. O sistema precisa
definir o que acontece quando o armazenador de estado está indisponível. Fail-open
favorece disponibilidade, mas pode liberar abuso. Fail-closed protege capacidade, mas
pode bloquear clientes legítimos durante uma falha interna. A escolha deve ser feita
por operação e risco, não globalmente.

## Observabilidade sem cardinalidade explosiva

Registre eventos de limitação em logs estruturados ou eventos de segurança, com
identificadores protegidos e retenção adequada. Não transforme cada user ID, IP ou
token em label de Prometheus. Métricas devem agregar por rota, classe de resultado,
serviço, região ou motivo controlado.

Monitore:

- quantidade de respostas 429;
- score e penalidades por classe, sem expor a identidade em métricas;
- falhas antes e depois da limitação;
- tempo de resposta;
- uso do armazenador compartilhado;
- expiração e tamanho dos buckets;
- clientes legítimos afetados;
- tentativas distribuídas pelo mesmo alvo.

Alertas devem distinguir aumento de abuso, falha do rate limiter e aumento de erros
do serviço. Se o próprio mecanismo estiver falhando, ele não pode ser interpretado
como evidência de que o tráfego está saudável.

## Integração com retry

Clientes que repetem imediatamente uma falha podem transformar uma degradação em
sobrecarga. Respostas transitórias devem incentivar backoff com jitter, respeitar
Retry-After e limitar a quantidade de tentativas. O servidor não deve aplicar uma
penalidade a uma operação simplesmente porque a dependência interna falhou, a menos
que exista uma razão clara para conter o retry do cliente.

Circuit breaker, fila, timeout e rate limiting resolvem problemas diferentes. Rate
limiting controla admissão; timeout limita espera; circuit breaker evita insistir em
uma dependência; fila absorve trabalho; retry tenta recuperar uma falha transitória.

## Relações

- [Rate limiting](index.md) apresenta dimensões, estado e algoritmos.
- [Token bucket](token-bucket.md) controla taxa média e burst.
- [Rate limiting local e compartilhado](../../rate-limiting-politica-local-e-compartilhada.md)
  compara estado por réplica e estado agregado.
- [Crescimento de erros e alertas](../../observabilidade/crescimento-de-erros-e-alertas.md)
  explica como medir aumento de falhas.
- [Resiliência](../../confiabilidade/resiliencia.md) relaciona timeout, retry e circuit
  breaker.

## Fontes

- [RFC 6585, HTTP 429](https://www.rfc-editor.org/rfc/rfc6585)
- [RFC 9110, HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP, credential stuffing prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html)
