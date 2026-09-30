# Ciclo de vida de aplicações

O ciclo de vida de uma aplicação começa antes do primeiro commit e termina depois que o
último usuário, integração e operador deixam de depender dela. Ele inclui descoberta do
problema, planejamento, desenho, implementação, validação, entrega, operação,
manutenção, evolução e aposentadoria.

O ciclo não precisa ser uma sequência rígida de fases. Uma equipe pode voltar ao
planejamento depois de uma medição em produção, alterar o desenho depois de um teste de
capacidade ou interromper uma funcionalidade depois de validar que ela não resolve o
problema esperado. O que deve permanecer explícito é a intenção da etapa, a evidência
usada para decidir e o responsável pelo próximo estado.

Esta página apresenta um mapa amplo do ciclo. Ela não substitui páginas específicas sobre
[entrega progressiva](../entrega/progressiva/canary.md),
[observabilidade](../observabilidade/index.md),
[resiliência](../confiabilidade/resiliencia.md) ou
[segurança no ciclo de vida](../seguranca/appsec/seguranca-no-ciclo-de-vida.md).

## O ciclo completo

Uma visão útil é tratar a aplicação como um produto que passa continuamente por estes
estados:

1. descoberta do problema, usuários e contexto;
2. planejamento de escopo, riscos, custos e critérios de sucesso;
3. especificação de requisitos e contratos;
4. arquitetura, modelagem de dados e desenho operacional;
5. implementação e revisão;
6. validação funcional, de segurança, desempenho e operação;
7. empacotamento e promoção entre ambientes;
8. lançamento controlado e observação;
9. operação, suporte, manutenção e resposta a incidentes;
10. evolução, descontinuação e aposentadoria.

Esses estados podem se sobrepor. Uma migração de banco, por exemplo, tem planejamento,
implementação, validação e rollout próprios, mesmo quando faz parte de uma versão maior.
Uma aplicação madura também possui mais de uma versão em operação ao mesmo tempo, seja
por rollout gradual, compatibilidade de clientes ou processamento assíncrono pendente.

## Descoberta e planejamento

O planejamento deve começar pelo problema e pelas restrições, não pela escolha de uma
tecnologia. Antes de decidir entre monólito, microsserviço, fila, banco ou plataforma,
registre quem precisa do sistema, que decisão ele permite, qual processo ele modifica e
qual evidência demonstrará que a mudança foi útil.

### Problema e resultado esperado

Descreva o problema observável, o grupo afetado, a frequência, o custo atual e o risco de
não agir. Diferencie uma necessidade de uma solução já imaginada. "Reduzir o tempo de
atendimento" é uma necessidade; "criar uma API GraphQL" é uma possível solução.

Defina um resultado verificável. Ele pode combinar indicadores de negócio e indicadores
técnicos, como conclusão de uma tarefa, redução de erros, tempo de resposta, taxa de
abandono, disponibilidade ou custo por operação. Se o resultado não puder ser observado,
a equipe terá dificuldade para saber se a aplicação deve evoluir, ser corrigida ou ser
aposentada.

### Pessoas, ownership e operação

Identifique usuários, operadores, mantenedores, responsáveis por segurança, donos dos
dados e consumidores de cada contrato. Uma aplicação sem ownership explícito acumula
decisões sem dono, alertas sem resposta e dependências que ninguém pode alterar.

Defina antes do desenvolvimento:

- quem aprova mudanças de produto e mudanças de risco;
- quem responde a incidentes em horário normal e fora dele;
- quem pode publicar, reverter ou alterar configuração;
- quem é responsável por cada dado, integração e segredo;
- quais são os prazos de suporte e de correção;
- como usuários serão avisados sobre indisponibilidade e mudanças incompatíveis.

### Restrições e riscos

Registre orçamento, capacidade de equipe, prazo, requisitos legais, localização de dados,
dependências externas, contratos de licença, limites de plataforma e requisitos de
retenção. A classificação de dados deve ocorrer antes de escolher logs, backups,
telemetria e ambientes de teste.

Faça uma análise de risco que inclua pelo menos:

- perda, corrupção ou exposição de dados;
- indisponibilidade e degradação parcial;
- falha de dependências e de fornecedores;
- mudanças irreversíveis de esquema;
- abuso de permissões e comprometimento da cadeia de entrega;
- falta de capacidade, aumento de custo e saturação;
- impossibilidade de reverter uma versão;
- dependência de pessoas, chaves ou procedimentos não documentados.

Uma decisão importante deve registrar alternativas consideradas, motivo da escolha,
consequências aceitas e sinais que fariam a equipe reconsiderá-la. Isso é o papel de um
ADR ou de um registro equivalente, não de uma justificativa escondida em um comentário de
código.

## Requisitos e contratos

Requisitos funcionais descrevem comportamentos, regras e resultados. Requisitos não
funcionais descrevem propriedades do sistema e suas condições de operação. Os dois devem
ter critérios de aceitação testáveis.

Consulte a área de [engenharia de requisitos](requisitos/index.md) para aprofundar
elicitação, Use Cases, BDD, Gherkin, backlog, priorização e requisitos de qualidade.
[Descoberta, MVP e evolução](requisitos/descoberta-mvp-evolucao.md) detalha como testar
hipóteses, entregar incrementos e evoluir versões e releases.

### Requisitos funcionais

Descreva entradas, pré-condições, regras, saídas, estados intermediários, erros e efeitos
colaterais. Inclua casos de ausência, duplicidade, concorrência, cancelamento e retry.
Uma especificação que cobre somente o caminho feliz costuma transferir decisões críticas
para a implementação.

Para cada operação relevante, esclareça:

- quem pode executá-la e sobre qual recurso;
- se a operação é síncrona ou assíncrona;
- quando o resultado é considerado concluído;
- se pode ser repetida com segurança;
- qual resposta representa validação, ausência, conflito ou indisponibilidade;
- quais eventos, auditorias ou notificações são produzidos.

### Requisitos não funcionais

Requisitos não funcionais devem ser específicos o bastante para orientar arquitetura,
testes e operação. Exemplos importantes incluem:

| Dimensão | Pergunta que precisa de resposta |
| --- | --- |
| Disponibilidade | Qual proporção de tempo e quais funções precisam estar disponíveis? |
| Latência | Qual limite de p50, p95 e p99 para cada classe de operação? |
| Capacidade | Quantas requisições, usuários, eventos ou bytes devem ser processados? |
| Escalabilidade | O crescimento será vertical, horizontal, por partição ou por fila? |
| Resiliência | O que acontece quando uma dependência está lenta, indisponível ou inconsistente? |
| Recuperação | Qual perda de dados e tempo de recuperação são aceitáveis? |
| Segurança | Quais ameaças, identidades, controles e evidências devem ser tratados? |
| Privacidade | Quais dados são pessoais, sensíveis, retidos ou apagados? |
| Operabilidade | Como a equipe detecta, diagnostica, altera e reverte o sistema? |
| Manutenibilidade | Como dependências, esquema, contratos e componentes serão atualizados? |
| Compatibilidade | Quais clientes, versões e integrações precisam coexistir? |
| Custo | Qual limite de infraestrutura, transferência, armazenamento e suporte? |
| Acessibilidade | Quais usuários e tecnologias assistivas devem ser atendidos? |
| Localização | Quais idiomas, formatos, fusos, moedas e regras regionais existem? |

Um requisito como "a API deve ser rápida" não orienta uma decisão. Um requisito como
"99% das consultas de leitura devem completar em até 300 ms em uma janela de cinco
minutos, sob a carga definida" pode ser medido, embora ainda precise especificar a classe
de consulta, o ambiente e o comportamento quando o objetivo não for atingido.

### Contratos

Contratos incluem APIs HTTP, schemas, eventos, mensagens, formatos de arquivo, comandos,
interfaces internas e comportamento de componentes. Eles devem declarar tipos, campos
obrigatórios, valores permitidos, erros, limites, autenticação, versionamento e
compatibilidade.

Uma mudança compatível normalmente adiciona comportamento opcional sem quebrar consumidores.
Remover campo, mudar significado, restringir valor aceito ou alterar semântica de erro pode
ser uma quebra mesmo que a aplicação continue compilando. Use exemplos de contrato,
validação automática e testes de consumidor quando a integração for importante.

## Arquitetura e desenho

O desenho deve responder como o sistema alcançará os requisitos dentro das restrições
registradas. A menor arquitetura que atende ao problema costuma ser melhor que uma
arquitetura distribuída escolhida por prestígio. Distribuição adiciona rede, serialização,
autenticação, observabilidade, falhas parciais, compatibilidade e operação.

### Fronteiras

Defina módulos por responsabilidade e ownership. Um módulo deve possuir regras coerentes,
interfaces compreensíveis e dependências explícitas. Uma divisão por camadas técnicas pode
ser útil, mas não substitui a fronteira do domínio.

Considere separadamente:

- frontend, backend, workers e tarefas recorrentes;
- processos síncronos e consumidores assíncronos;
- dados de referência, dados transacionais e arquivos;
- componentes que precisam de escala ou disponibilidade diferentes;
- fronteiras de confiança, tenant, região e compliance;
- dependências internas e serviços de terceiros.

Um monólito modular pode oferecer fronteiras fortes, transações locais e deploy conjunto.
Microsserviços fazem sentido quando há ownership, escala, isolamento ou ciclo de mudança
que justifique o custo de rede e operação. Um frontend separado também precisa de contratos,
compatibilidade e observabilidade; separar repositórios não cria autonomia por si só.

### Dados e evolução de esquema

Defina quem é dono de cada dado, qual consistência é necessária, quais consultas são
críticas e como a informação será apagada, retida, replicada e restaurada. Escolha entre
transação local, evento, fila, cache, réplica ou leitura derivada com base na necessidade,
não apenas na ferramenta disponível.

Mudanças de banco devem considerar versões antigas e novas da aplicação. O padrão
expand-and-contract reduz o risco:

1. adicione estruturas compatíveis sem remover o contrato antigo;
2. publique código capaz de ler o formato antigo e o novo;
3. preencha ou migre dados de forma controlada;
4. comece a gravar no novo formato, preservando compatibilidade durante a transição;
5. valide cobertura e consistência;
6. remova o caminho antigo somente depois que nenhum consumidor depender dele.

Migração destrutiva durante canary ou blue-green pode tornar o rollback impossível. A
aplicação deve conseguir coexistir com a versão anterior enquanto o tráfego ainda está
dividido.

### Comunicação e efeitos colaterais

Use uma chamada síncrona quando o consumidor precisa do resultado dentro de um prazo
conhecido. Use job ou mensagem quando o trabalho puder terminar depois, precisar de retry,
ser reprocessado ou não precisar bloquear a resposta.

Toda operação remota precisa de timeout. Retries exigem backoff, jitter, limite e
idempotência. Um circuit breaker pode impedir chamadas repetidas para uma dependência
falha, mas não substitui uma resposta coerente, uma fila limitada ou uma estratégia de
degradação.

Caches precisam de política de invalidação, limite de tamanho, expiração e comportamento
em caso de dado ausente. Um cache não pode ser usado para esconder a ausência de uma
fonte de verdade nem para transformar uma consulta em uma gravação inesperada.

## Implementação

A implementação deve tornar as decisões verificáveis e manter baixo o custo de mudança.
Isso inclui estrutura do código, convenções, revisão, dependências e rastreabilidade.

### Controle de mudanças

Use controle de versão com commits pequenos, revisão por pull request, ownership claro e
histórico que explique a mudança. Uma revisão eficaz procura comportamento, segurança,
compatibilidade, migração, observabilidade e operação, não apenas estilo.

Evite branches longas quando elas acumulam divergência. Feature flags, branches por curta
duração e mudanças pequenas permitem integrar código incompleto sem ativar comportamento
inacabado. Uma flag não deve permanecer indefinidamente sem dono, prazo de remoção e
telemetria de uso.

### Qualidade e testes

Use uma combinação proporcional ao risco:

- testes unitários para regras locais e invariantes;
- testes de integração para banco, filas e dependências reais;
- testes de contrato para consumidores e produtores;
- testes end-to-end para fluxos críticos;
- testes de segurança e análise estática;
- testes de carga, stress, spike e soak para capacidade e degradação;
- testes de backup, restauração e falhas operacionais;
- testes de migração e coexistência entre versões.

Teste também condições que normalmente aparecem em produção: timeout, resposta parcial,
repetição, ordem diferente de eventos, dados antigos, clock incorreto, falta de espaço,
limite de conexão e reinício durante uma operação.

### Dependências e cadeia de fornecimento

Registre dependências diretas e transitivas, mantenha lockfiles revisados, produza SBOM
quando apropriado e acompanhe vulnerabilidades, licenças e suporte. Builds devem ser
reprodutíveis tanto quanto possível, gerar artefatos imutáveis e permitir identificar o
código, dependências, ferramenta e configuração usados.

Não confunda uma imagem construída com um artefato pronto para produção. Valide origem,
checksums, assinatura, permissões, conteúdo, vulnerabilidades e proveniência antes de
promover. A [segurança no ciclo de vida](../seguranca/appsec/seguranca-no-ciclo-de-vida.md)
e a [software supply chain](../seguranca/supply-chain/index.md) detalham essas práticas.

## Ambientes e promoção

Ambientes separados ajudam a testar mudanças, mas não resolvem sozinhos a diferença entre
teste e produção. Registre o que varia entre ambientes e por quê.

- desenvolvimento deve favorecer feedback rápido e dados seguros;
- integração deve testar contratos e composição;
- homologação deve representar fluxos e dependências relevantes;
- produção deve ter configurações, limites, observabilidade e acesso controlados.

Configuração não deve ser recompilada sem necessidade. Separe código, configuração não
secreta e segredos. Segredos devem ser injetados pelo ambiente, rotacionáveis e auditáveis.
Não copie dados pessoais de produção para teste sem minimização, autorização e controles.

O pipeline deve construir uma vez e promover o mesmo artefato. Recompilar em cada ambiente
pode produzir binários diferentes e torna a origem do que foi executado menos clara. O
pipeline deve executar validação, testes, análise de segurança, migração compatível,
aprovação necessária e registro de evidências.

## Estratégias de implantação e lançamento

Implantação é colocar uma versão no ambiente. Lançamento é permitir que usuários ou
tráfego utilizem seu comportamento. Separar os dois conceitos permite publicar código
desligado por uma flag, validar uma revisão antes de liberar a funcionalidade ou reverter
o tráfego sem reconstruir a imagem.

### Comparação

| Estratégia | Como expõe a versão | Principal benefício | Principal risco ou custo |
| --- | --- | --- | --- |
| Recreate | Encerra a versão antiga antes de iniciar a nova | Simplicidade | Indisponibilidade durante a troca |
| Rolling | Substitui réplicas gradualmente | Usa capacidade existente | Versões coexistem e precisam ser compatíveis |
| Canary | Envia uma fração controlada do tráfego | Limita blast radius com dados reais | Exige roteamento, métricas e abortamento confiáveis |
| Blue-green | Mantém duas revisões e troca o tráfego | Switch rápido e rollback simples de tráfego | Duplica capacidade e não desfaz migração destrutiva |
| A/B | Divide usuários ou grupos para comparar comportamentos | Mede efeito de produto ou experiência | Exige desenho experimental e pode misturar efeitos |
| Feature flag | Código é implantado, comportamento é ativado separadamente | Desacopla deploy de exposição | Flags esquecidas e estados combinatórios |

As estratégias podem ser compostas. Um canary pode usar uma feature flag; um blue-green
pode receber uma validação antes da troca; um rolling update pode ser controlado por um
orquestrador. O nome da estratégia não substitui o plano de medição e rollback.

### Canary

Canary libera uma revisão para um subconjunto de tráfego, usuários, regiões ou filas. A
fração pode começar pequena e aumentar em etapas, mas o percentual não é a segurança por
si só. Um canary de 1% ainda pode atingir uma operação crítica, e um canary de 20% pode
ser insuficiente para revelar um problema raro.

Antes de começar, defina:

- qual tráfego pertence ao grupo de controle e ao grupo canary;
- quais indicadores devem permanecer dentro do objetivo;
- quanto tempo ou quantas requisições são necessárias para observar o efeito;
- quais erros interrompem a promoção imediatamente;
- quem ou qual controlador pode pausar e reverter;
- como lidar com sessões, jobs, cache, conexões persistentes e eventos;
- como confirmar que o grupo canary é comparável ao controle.

Observe erro, latência, saturação, tráfego, conversão e sinais de negócio. Compare a mesma
rota, região, tamanho de payload e classe de usuário. Uma média global pode esconder um
problema que afeta somente o canary.

Canary é especialmente útil quando o custo de atingir todos os usuários é alto e existe
telemetria suficientemente rápida para interromper a promoção. Ele não elimina a
necessidade de testes, compatibilidade de dados ou rollback.

### Blue-green

Blue-green mantém duas revisões operacionais, uma recebendo tráfego e outra preparada para
recebê-lo. A troca pode ocorrer por service selector, balanceador, gateway, DNS ou outro
controle de tráfego. O mecanismo deve considerar conexões persistentes, sessões, cache,
jobs e drenagem de conexões.

O benefício principal é separar a preparação da troca. O custo é manter capacidade dupla,
sincronizar dados e garantir que a revisão inativa esteja realmente pronta. Se a versão
nova alterou o esquema de maneira incompatível ou publicou eventos com formato diferente,
voltar o tráfego não reverte o estado já produzido.

Use smoke tests, health checks, verificação de dependências e uma janela de observação
antes da troca. Depois da troca, mantenha a revisão anterior disponível pelo tempo definido
pela política de rollback, sem permitir que ela receba tráfego acidentalmente.

### A/B

A/B é uma técnica de comparação de produto ou comportamento. Dois grupos recebem variantes
definidas e uma métrica de resultado é comparada. A atribuição precisa ser estável o bastante
para que o mesmo usuário não alterne de grupo sem intenção. O experimento deve declarar
hipótese, população, métrica primária, duração, tamanho de amostra, critérios de parada e
efeitos negativos aceitáveis.

A/B não é sinônimo de canary. Canary pergunta se uma versão pode ser operada com segurança;
A/B pergunta se variantes produzem resultados diferentes para uma métrica. Um A/B pode ser
feito entre duas versões estáveis, e um canary pode ser feito sem experimento de produto.
Misturar as duas perguntas dificulta a interpretação dos resultados.

### Rollback, rollforward e flags

Rollback de aplicação substitui a versão por uma anterior. Rollback de tráfego muda a rota
para uma revisão já preparada. Rollback de banco pode ser impossível ou mais perigoso que
corrigir a versão nova. Rollforward significa corrigir o problema com uma nova versão
compatível, muitas vezes a opção mais segura depois de uma migração de dados.

Uma feature flag controla exposição e pode desligar comportamento sem remover o código.
Ela precisa de dono, estado padrão seguro, auditoria, métrica, prazo de remoção e testes
para cada combinação relevante. Uma flag não deve proteger uma mudança de esquema que a
versão anterior não consegue interpretar.

Veja [entrega progressiva](../entrega/index.md), [canary](../entrega/progressiva/canary.md),
[blue-green](../entrega/progressiva/blue-green.md),
[Argo Rollouts](../entrega/progressiva/argo-rollouts.md) e
[feature flags](../feature-flags.md).

## Observabilidade e critérios de decisão

Observabilidade deve ser desenhada junto com a aplicação. Instrumentar depois do primeiro
incidente costuma produzir dados sem contexto, dimensões inconsistentes e alertas que não
indicam uma ação.

Uma aplicação operável deve permitir responder:

- está recebendo tráfego;
- está concluindo operações com sucesso;
- está respondendo dentro do objetivo;
- qual dependência ou recurso está limitando o resultado;
- qual versão, configuração, região e grupo de rollout está envolvido;
- quais usuários e operações foram afetados;
- qual ação reduz o impacto agora.

Use métricas, logs, traces e eventos com correlação consistente. Dashboards mostram estado;
alertas devem apontar para uma condição acionável. Cada alerta importante deve ter dono,
severidade, runbook, limite, janela e caminho de escalonamento.

### p50, p95 e p99

Um percentil descreve a posição de uma observação em uma distribuição. Se a latência p95
é 400 ms, aproximadamente 95% das observações da janela estão em até 400 ms e a cauda
restante está acima disso. Isso não significa que exatamente 95 requisições tiveram esse
valor nem que todas as pessoas tiveram a mesma experiência.

- p50 é a mediana e ajuda a representar a experiência típica;
- p95 mostra uma cauda que já afeta uma parcela relevante dos usuários;
- p99 mostra uma cauda mais extrema e ajuda a encontrar lentidão rara, mas operacionalmente
  importante.

A média pode parecer saudável enquanto uma parcela dos usuários espera muito. Por isso,
latência deve ser analisada por rota, método, status, região, tamanho de resposta, cliente,
versão e dependência quando essas dimensões forem necessárias para uma decisão. Não faça
uma média simples dos percentis de cada instância para representar o serviço inteiro.

Percentis precisam de amostras suficientes e de uma janela definida. Com poucas requisições,
p99 pode ser instável. Com uma janela muito longa, uma regressão recente pode desaparecer
na agregação. Com cardinalidade excessiva, a coleta pode prejudicar o próprio sistema.

Histograms preservam contagens por faixas e podem ser agregados de várias instâncias,
desde que os buckets e a consulta sejam compatíveis. Summaries calculam quantis no cliente
e não podem ser combinados como se fossem observações brutas. A documentação do
[Prometheus sobre histograms e summaries](https://prometheus.io/docs/practices/histograms/)
explica essa diferença e seus efeitos.

Um objetivo útil combina percentil, classe de operação, janela e condição de carga, por
exemplo: "99% das leituras públicas, excluindo respostas de validação, devem completar em
até 300 ms durante cada janela de cinco minutos sob a carga prevista". O objetivo precisa
ser relacionado a um SLO e a uma ação, não apenas exibido em um dashboard.

Não use p99 isoladamente. Relacione latência com taxa de erro, throughput, saturação,
profundidade de fila, conexões, CPU, memória, disco, dependências e tamanho de payload.
Uma regressão de p99 com erro estável pode apontar para contenção; p99 e erro subindo junto
podem indicar saturação ou dependência indisponível.

### SLI, SLO e SLA

Um SLI é a medição de uma propriedade observável, como proporção de requisições válidas
concluídas dentro de um limite. Um SLO é o objetivo interno para esse indicador. Um SLA é
um compromisso externo que pode conter consequências contratuais.

Defina o evento válido, a população, a janela e o tratamento de manutenção, dependências e
erros de cliente. Um SLO de latência sem especificar a rota ou o tamanho da resposta não
é comparável. A diferença entre SLO e SLA deve ser explícita; operar sempre no limite do
SLA deixa pouco espaço para incidentes.

### Métricas de entrega

Métricas de entrega ajudam a encontrar gargalos no fluxo de mudanças, mas não devem virar
metas isoladas que incentivem comportamento artificial. As métricas DORA atuais cobrem
throughput e instabilidade: change lead time, deployment frequency, failed deployment
recovery time, change fail rate e deployment rework rate. Use-as por aplicação ou serviço,
com contexto, e relacione-as a qualidade, segurança e bem-estar da equipe.

## Operação e confiabilidade

O sistema deve ser operável por alguém que não o escreveu. Isso exige documentação de
procedimentos, logs úteis, configuração visível, limites conhecidos e capacidade de agir
sem editar arquivos manualmente em produção.

### Saúde e capacidade

Defina readiness, liveness e startup de modo diferente quando necessário. Readiness
indica se a instância deve receber tráfego; liveness indica se ela precisa ser reiniciada;
startup dá tempo para inicialização. Uma probe que consulta uma dependência crítica pode
derrubar todas as réplicas durante uma falha externa.

Estime capacidade para tráfego normal, pico, crescimento e recuperação. Inclua CPU, memória,
conexões, threads, filas, disco, IOPS, rede, limites de terceiros e capacidade de banco.
Teste o comportamento quando o limite é atingido. Degradação explícita é melhor que uma
fila infinita ou um timeout em cascata.

### Resiliência

Timeout, retry limitado, backoff, jitter, circuit breaker, bulkhead, rate limiting,
backpressure e fallback devem ter semântica definida. Repetir uma operação não idempotente
pode duplicar cobrança, registro ou evento. Um fallback que mostra dado velho precisa
indicar a política de validade e não ocultar uma condição que exige intervenção.

Use [idempotência](../confiabilidade/idempotencia.md) e
[resiliência](../confiabilidade/resiliencia.md) como propriedades de contrato, não como
detalhes de uma biblioteca.

### Backup e recuperação

Defina RPO, RTO, retenção, criptografia, acesso, restauração parcial e teste periódico.
Backup não provado não é uma estratégia de recuperação. Teste restauração, consistência,
tempo, dependências, chaves e procedimento de troca. Documente o que acontece quando o
backup mais recente está corrompido ou quando a chave de recuperação não está disponível.

### Incidentes e suporte

Um plano de incidente deve cobrir detecção, triagem, contenção, comunicação, mitigação,
recuperação, validação e revisão posterior. Durante o incidente, prefira reduzir impacto e
preservar evidência a tentar uma refatoração ampla. Depois, investigue causa contribuinte,
detecção tardia, comunicação, decisão e ações preventivas, sem transformar o postmortem em
culpa individual.

Runbooks devem dizer quando usar o procedimento, quais pré-condições verificar, quais
comandos ou mudanças executar, como validar o resultado e quando escalar. Procedimentos de
alto risco precisam de rollback e de registro da mudança.

## Manutenção e novas versões

Manutenção não é somente corrigir bugs. Ela inclui atualização de dependências, correções
de segurança, mudança de requisitos, redução de dívida, adaptação de plataforma,
otimização, migração de dados e remoção de código obsoleto.

### Patching e dependências

Mantenha uma matriz de versões suportadas, datas de fim de vida, compatibilidade de runtime,
drivers, banco, navegador, SDK e integrações. Classifique atualização por risco e urgência.
Correção de segurança não deve esperar uma janela arbitrária quando existe exploração ativa,
mas ainda precisa de teste, aprovação proporcional e plano de recuperação.

Automação de atualização deve abrir mudanças pequenas, validar checksums e lockfiles,
executar testes e indicar incompatibilidades. Atualizar tudo sem entender a mudança pode
acelerar a entrada de uma falha; nunca atualizar também acumula risco.

### Compatibilidade e depreciação

Defina política para versões de API, clientes, schemas, eventos e formatos exportados.
Comunique depreciação antes da remoção, registre consumidores, ofereça migração e meça o
uso do caminho antigo. O período de compatibilidade deve refletir o tempo real de atualização
dos consumidores, não somente o ciclo ideal da equipe.

Uma nova versão deve ser capaz de conviver com a anterior quando o rollout for gradual.
Isso envolve campos opcionais, tolerância a campos desconhecidos, ordenação de eventos,
migrações expand-and-contract e cuidado com cache. Contratos de fila são especialmente
importantes porque mensagens antigas podem permanecer armazenadas por muito tempo.

### Revisão pós-lançamento

Depois da promoção, confirme saúde técnica, comportamento de negócio, impacto de custo,
uso de flags, suporte e feedback. Compare a versão com uma linha de base. Uma mudança que
passa nos testes pode aumentar p99, consumo, retrabalho ou chamados de suporte.

Registre o que foi aprendido e transforme sinais repetidos em melhoria do produto, do
pipeline, da arquitetura ou do runbook. Métrica deve orientar aprendizado, não criar uma
competição entre equipes.

## Segurança, governança e evidência

Segurança deve estar presente em descoberta, desenho, código, build, entrega e operação.
Faça threat modeling proporcional ao risco, valide entradas, limite privilégios, proteja
segredos, audite ações sensíveis, mantenha dependências e considere abuso, não apenas erro.

O [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) organiza práticas de
desenvolvimento seguro que podem ser incorporadas ao ciclo existente. Ele não exige um
modelo único de desenvolvimento; fornece uma linguagem para planejar, produzir, proteger
e responder a software.

Governança deve manter evidência suficiente para explicar quem mudou o quê, quando, por
qual motivo, com qual validação e qual resultado. Isso inclui revisões, artefatos,
aprovações, scans, migrações, alterações de configuração, incidentes e exceções aceitas.
Não transforme a evidência em burocracia desconectada do risco: registre o que permite
reconstruir a decisão e demonstrar controle.

## Aposentadoria

Uma aplicação ou funcionalidade deve ter um caminho de saída. Quando o uso, suporte ou
valor não justifica o custo, planeje descontinuação em vez de manter uma superfície sem
dono.

O plano deve incluir:

- identificação de usuários, integrações e dados dependentes;
- anúncio, prazo, alternativa e suporte de migração;
- exportação, retenção ou eliminação conforme obrigação aplicável;
- desativação gradual de tráfego, jobs, filas, webhooks e flags;
- revogação de credenciais, certificados, tokens e acessos;
- remoção de DNS, rotas, alertas, dashboards e infraestrutura;
- preservação de evidências e documentação necessária;
- validação de que nenhum consumidor restante foi quebrado.

Desligar um deployment não é necessariamente aposentar uma aplicação. Dados, backups,
segredos, registros, domínios e consumidores podem continuar ativos. O encerramento deve
ser verificado por dependência, não somente por processo.

## Checklist de prontidão

Antes de uma mudança relevante, confirme que:

- o problema, o resultado e o dono estão claros;
- requisitos funcionais e não funcionais têm critérios mensuráveis;
- contratos e compatibilidade foram revisados;
- riscos, dados, privacidade e ameaças foram avaliados;
- testes cobrem comportamento, integração, contrato, segurança e operação;
- o artefato é identificável, imutável e promovido sem recompilação;
- migrações são compatíveis e existe plano de recuperação;
- timeouts, retries, limites, filas e idempotência foram definidos;
- logs, métricas, traces, dashboards e alertas permitem diagnosticar;
- p95 e p99 têm janela, população e objetivo definidos;
- existe estratégia de rollout, critério de abortamento e rollback ou rollforward;
- suporte, comunicação e runbooks estão preparados;
- custo e capacidade foram medidos em condições representativas;
- dependências, segredos, permissões e vulnerabilidades foram revisados.

Depois do lançamento, confirme saúde, impacto e recuperação. Se a evidência não for
suficiente para decidir, a aplicação ainda não está pronta para uma promoção irreversível.

## Relações

- [Engenharia de software](index.md)
- [Entrega e GitOps](../entrega/index.md)
- [Canary](../entrega/progressiva/canary.md)
- [Blue-green](../entrega/progressiva/blue-green.md)
- [Argo Rollouts](../entrega/progressiva/argo-rollouts.md)
- [Feature flags](../feature-flags.md)
- [Observabilidade](../observabilidade/index.md)
- [Métricas](../observabilidade/metricas.md)
- [Golden signals](../observabilidade/golden-signals.md)
- [Resiliência](../confiabilidade/resiliencia.md)
- [Idempotência](../confiabilidade/idempotencia.md)
- [Transações ACID](../dados/transacoes-acid.md)
- [Revisões, exclusão e WAL](../dados/revisoes-exclusao-e-wal.md)
- [Segurança no ciclo de vida](../seguranca/appsec/seguranca-no-ciclo-de-vida.md)
- [Software supply chain](../seguranca/supply-chain/index.md)

## Fontes primárias

- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)
- [ISO/IEC/IEEE 12207, life cycle processes](https://www.iso.org/standard/63712.html)
- [DORA, software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [Google SRE books](https://sre.google/books/)
- [Prometheus, histograms and summaries](https://prometheus.io/docs/practices/histograms/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [Argo Rollouts documentation](https://argo-rollouts.readthedocs.io/)
