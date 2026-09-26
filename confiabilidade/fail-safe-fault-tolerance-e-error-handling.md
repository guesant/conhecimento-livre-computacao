# Fail-safe, fault tolerance e error handling

Falhas são inevitáveis em sistemas de software e hardware. O objetivo de um projeto confiável não é prometer que nenhum componente falhará, mas definir o que deve acontecer quando uma falha, um erro, uma entrada inválida ou uma condição desconhecida aparecer. Essa decisão precisa considerar segurança, integridade dos dados, disponibilidade, custo e possibilidade de recuperação.

## Falha, erro, defeito e incidente

Um defeito é uma condição incorreta no projeto ou na implementação. Um erro é um estado interno incorreto produzido por um defeito, uma entrada inesperada ou uma falha externa. Uma falha é o comportamento observável que não atende ao contrato do sistema. Um incidente é o evento operacional que exige investigação ou intervenção.

Uma requisição que recebe `404` por um recurso inexistente não é necessariamente um incidente. Uma API que responde `200` com dados de outro usuário é uma falha de segurança mesmo que nenhum processo tenha travado. Uma exceção capturada e registrada pode ser um tratamento correto; engolir a exceção e continuar com estado inválido não é.

## Fail-safe, fail-secure e fail-soft

Fail-safe é uma estratégia em que a terminação ou a mudança para um estado limitado evita dano a recursos, dados, propriedades ou pessoas quando a falha é detectada. O estado seguro depende do domínio. Para uma porta física, bloquear pode ser seguro; para uma saída de emergência, bloquear pode ser perigoso.

Fail-secure prioriza não conceder acesso ou privilégio quando a decisão de segurança não pode ser tomada. Se o autorizador está indisponível, uma operação administrativa deve falhar fechada. Isso pode ser diferente de uma leitura pública não crítica, que pode mostrar cache stale sem conceder qualquer permissão.

Fail-soft encerra ou degrada apenas partes não essenciais, mantendo o núcleo do serviço. A página pode continuar exibindo o conteúdo crítico enquanto um widget de recomendações falha. A aplicação precisa declarar o que é essencial e tornar visível quando a resposta está degradada.

Fail-operational mantém a função por algum tempo depois de uma falha, normalmente usando redundância. Aviônicos, sistemas de controle e serviços críticos podem combinar fail-operational e fail-safe: uma primeira falha não interrompe a missão, mas falhas adicionais levam o sistema a um estado seguro.

Não existe um significado universal de “seguro”. O requisito deve dizer seguro para quem, contra qual dano, por quanto tempo e sob quais falhas. O [glossário do NIST](https://csrc.nist.gov/glossary/term/fail_safe) diferencia fail-safe de fail-secure e fail-soft; a escolha final pertence à análise de risco do sistema.

## Fault tolerance

Fault tolerance é a capacidade de continuar executando corretamente, em uma capacidade definida, quando componentes falham. A definição não promete que toda função continuará disponível. O contrato deve dizer quais falhas são toleradas, qual degradação é aceita, qual integridade é obrigatória e quando a recuperação passa a ser necessária.

Tolerância depende de redundância, detecção, isolamento, decisão e recuperação. Ter duas instâncias não basta se ambas usam a mesma fonte de energia, o mesmo switch, o mesmo Secret incorreto ou o mesmo defeito de software. A análise precisa considerar falhas de causa comum, operadores, configuração, dados e dependências externas.

## Formas de redundância

Replicação mantém várias instâncias de um componente ou estado. As instâncias podem responder em paralelo e um mecanismo de quorum pode escolher um resultado. Esse modelo aumenta disponibilidade ou permite votação, mas exige lidar com divergência, particionamento, duplicação e atualização.

Redundância com failover mantém uma instância reserva e transfere o trabalho quando a primária falha. Active-passive simplifica alguns conflitos, mas pode deixar a reserva desatualizada ou não testada. Active-active usa várias instâncias ao mesmo tempo, aumentando capacidade, mas exige consistência, roteamento e coordenação.

Diversidade usa implementações diferentes da mesma especificação. Ela reduz o risco de um defeito comum derrubar todas as réplicas, mas aumenta custo de teste, integração e diagnóstico. Diversidade não elimina falhas de especificação, entrada, operador ou infraestrutura compartilhada.

Quorum e votação comparam resultados de várias réplicas. Dual modular redundancy consegue detectar divergência, mas não identifica sozinha qual réplica está correta. Triple modular redundancy pode escolher o resultado majoritário quando uma réplica falha, mas ainda precisa reparar, isolar e validar o estado suspeito. Se duas réplicas compartilham o mesmo defeito, a maioria pode estar errada.

Lockstep executa réplicas em sincronismo e compara seus resultados. O modelo é útil para detectar divergência em sistemas críticos, mas exige controlar estado, tempo, entradas, efeitos colaterais e recuperação. Replicar uma função que chama um serviço externo não torna automaticamente seus efeitos idempotentes.

## Error handling

Tratamento de erro começa no contrato. Para cada operação, classifique falhas como validação, autenticação, autorização, ausência, conflito, limitação, falha transitória, dependência indisponível, corrupção ou erro inesperado. A classificação deve determinar a resposta, o retry, o código de retorno, a métrica, o log e a necessidade de intervenção.

Erros esperados devem ser representados de forma explícita e tipada quando a linguagem permitir. Exceções são adequadas para interromper um fluxo quando o chamador não pode continuar localmente, mas não devem ser usadas para esconder estados normais como “não encontrado”. O caminho de erro deve preservar contexto suficiente para diagnóstico sem expor segredos ou dados pessoais.

Uma API deve retornar um contrato consistente, com status apropriado, código estável, mensagem segura, detalhes úteis e correlation ID. O cliente precisa distinguir retry seguro de erro permanente. O servidor não deve retornar uma mensagem de stack trace ao usuário nem transformar toda falha em `500` quando a causa é entrada inválida ou falta de autorização.

## Retry e recuperação

Retry só é adequado quando a falha pode ser transitória e a operação puder ser repetida com segurança. Use deadline, número finito de tentativas, backoff e jitter. Não repita autenticação negada, validação, conflito ou uma escrita sem idempotência.

Circuit breaker impede chamadas contínuas a uma dependência que está falhando. Bulkhead separa pools, filas ou limites para conter o blast radius. Fallback pode usar cache stale, réplica, resposta parcial ou fila, mas deve declarar se o resultado é antigo, incompleto ou apenas aceitou o trabalho para processamento posterior.

Uma operação que excedeu o timeout pode ter sido concluída no servidor. O cliente não deve repetir cegamente uma transferência, criação ou cobrança. Use idempotency key, consulta de status, outbox, deduplicação ou compensação de acordo com o domínio.

## Isolamento e degradação

Separe o caminho crítico dos recursos opcionais. Uma falha de analytics não deve impedir login; uma falha de recomendações não deve substituir o conteúdo principal por uma tela de erro; uma dependência lenta não deve ocupar todas as conexões disponíveis.

Degradação precisa ser projetada, medida e testada. Defina o valor mínimo que continua correto, o que deve ser removido, o que pode ser stale, qual mensagem o usuário verá e como o sistema volta ao modo normal. Não exiba dados antigos como se fossem confirmação de uma escrita recente.

## Integridade e segurança

Fail-safe não autoriza ignorar validação. Continuar executando com valores fabricados pode mascarar corrupção e produzir decisões perigosas. Failure-oblivious computing, recuperação instrumental e técnicas semelhantes podem ser úteis para limitar um crash em um contexto específico, mas o valor substituído precisa ser semanticamente seguro.

Em sistemas críticos, prefira detectar e conter a falha a continuar silenciosamente. Checksums, invariantes, validação de schema, limites, watchdogs, circuit breakers, monotonicidade e logs de auditoria tornam a recuperação verificável. O default de autorização deve ser fail closed; o default de uma leitura não crítica pode ser uma degradação limitada, desde que não eleve privilégio nem produza uma falsa confirmação.

## Teste e operação

Teste componentes isolados, integração, failover, recuperação, perda de uma réplica, partição de rede, dados inválidos, timeout, erro de configuração e falhas de causa comum. Exercite a reserva, porque um componente redundante que nunca foi ativado pode falhar justamente durante o incidente.

Monitore taxa e classe de erros, latência, retries, timeouts, breaker, failover, divergência de réplicas, fila de recuperação, uso de fallback e tempo de estabilização. Registre a versão, o correlation ID, o componente e a dependência, mas redija credenciais, tokens e dados sensíveis.

Faça postmortem sem limitar a análise ao primeiro processo que apresentou erro. O objetivo é entender como o defeito atravessou as barreiras, por que a detecção não impediu o impacto, por que a recuperação funcionou ou falhou e qual teste ou sinal reduzirá a recorrência.

## Relações

- [Resiliência](resiliencia.md)
- [Idempotência](idempotencia.md)
- [Sistemas distribuídos](../arquitetura-aplicacoes/sistemas-distribuidos.md)
- [Self-stabilization e autoestabilização](../arquitetura-aplicacoes/self-stabilization.md)
- [Circuit breaker em .NET](../dotnet/polly.md)
- [Correlation ID](../observabilidade/correlation-id.md)

## Fontes

- [NIST, fault tolerance](https://csrc.nist.gov/glossary/term/fault_tolerance)
- [NIST, fault tolerant](https://csrc.nist.gov/glossary/term/fault_tolerant)
- [NIST, fail-safe](https://csrc.nist.gov/glossary/term/fail_safe)
- [NASA, failure tolerance e redundância](https://nodis3.gsfc.nasa.gov/displayCA.cfm?Internal_ID=N_PR_8715_0003_&page_name=Chapter1)
- [Microsoft, fault tolerance e continuidade](https://learn.microsoft.com/en-us/azure/reliability/concept-business-continuity-high-availability-disaster-recovery)
- [Microsoft, error handling em aplicações críticas](https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-application-design)
- [Microsoft, padrões de confiabilidade](https://learn.microsoft.com/en-ie/azure/well-architected/reliability/design-patterns)
