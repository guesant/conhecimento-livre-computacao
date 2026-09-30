# Sentry

Sentry é uma plataforma de observabilidade de aplicações focada em erros, exceções, performance e contexto de execução. Ela agrupa eventos semelhantes, preserva stack traces e pode correlacionar transações, releases, usuários e outros metadados conforme a instrumentação e a política de retenção.

Um evento individual possui um event ID. Um issue é um agrupamento de eventos que o Sentry
considera semelhantes. Uma transação ou trace descreve execução e performance. Esses
identificadores têm funções diferentes de um Correlation ID da aplicação.

## O que ele observa

Sentry responde perguntas como quais erros cresceram depois de uma release, qual transação está lenta e qual stack trace representa a falha. Traces, profiles, breadcrumbs e contexto de ambiente ajudam a reproduzir o problema, mas o valor depende de instrumentar os caminhos relevantes e de não enviar segredos ou dados pessoais indevidos.

Sentry não é SAST, DAST, antivírus ou EDR. Ele pode registrar uma exceção causada por um ataque, mas não substitui análise preventiva nem resposta de endpoint. Também não deve receber payloads completos quando eles contêm credenciais, tokens ou dados regulados.

## Correlation ID, trace ID e event ID

O Correlation ID é definido pela aplicação e pode atravessar vários requests, mensagens,
retries e jobs. O trace ID pertence a uma execução distribuída específica. O event ID
identifica o evento recebido pelo Sentry. Não substitua um pelo outro.

Uma prática útil é registrar o Correlation ID como contexto ou tag sanitizada quando a
busca individual for realmente necessária, mantendo também trace ID e span ID nativos do
tracing. Tags precisam de uma política de cardinalidade e retenção; adicionar um valor
único para cada request a todo evento pode aumentar custo e ruído. Em muitos casos, logs
estruturados são o lugar mais eficiente para procurar a correlação, e o trace é o caminho
para navegar até o erro.

Ao capturar uma exceção, associe apenas dados que não contenham segredo ou informação
pessoal desnecessária. O Sentry deve receber o contexto mínimo necessário para responder
qual release, operação e dependência falharam.

## Investigação com OpenTelemetry

OpenTelemetry pode fornecer trace context e correlação de logs, enquanto o Sentry agrupa
exceções, apresenta stack traces, releases, breadcrumbs e dados de performance. Uma
integração pode permitir sair de um evento de erro para a transação ou trace relacionado,
desde que a instrumentação, sampling e propagação sejam compatíveis.

Não presuma que todo trace está disponível no Sentry. Sampling, falha de exportação,
retenção e diferenças entre SDKs podem deixar apenas o evento de erro ou apenas os logs.
Registre os identificadores nos logs e defina qual sistema é a fonte de cada sinal.

## SaaS e self-hosted

Sentry Cloud é o modelo SaaS, com operação e retenção delegadas ao fornecedor conforme o plano contratado. Sentry self-hosted permite manter eventos na própria infraestrutura, mas exige operar banco, filas, armazenamento, upgrades, retenção, capacidade e segurança do próprio Sentry.

A escolha deve considerar residência dos dados, volume de eventos, retenção, custo de ingestão, integração com o ciclo de release e capacidade de manter a plataforma. Self-hosted não significa custo zero: o sistema de observabilidade também precisa de backup, monitoramento e controle de acesso.

## Boas práticas

Defina níveis de amostragem e retenção, remova dados sensíveis antes do envio, associe eventos a releases, preserve Correlation ID somente quando houver justificativa e mantenha alertas acionáveis. Use o evento para investigar e corrigir a causa; não transforme cada exceção esperada em incidente. Teste o comportamento quando o endpoint de telemetria estiver indisponível para que a aplicação continue funcional.

## Modelo de ingestão

O SDK coleta o evento no processo da aplicação e o envia para um endpoint de ingestão. O envio pode ocorrer de forma síncrona ou assíncrona, conforme o SDK, mas nunca deve bloquear o caminho principal indefinidamente. A aplicação precisa de timeout, fila local limitada e descarte controlado quando o serviço de telemetria estiver indisponível. Falha no Sentry não pode transformar uma falha de negócio em indisponibilidade adicional.

O evento precisa carregar ambiente e release de forma consistente. Um mesmo serviço pode ter desenvolvimento, homologação, staging e produção com comportamentos diferentes. Misturar esses ambientes em uma issue torna a prioridade e a investigação ambíguas. A release deve apontar para o commit ou artefato realmente implantado, e não para uma versão calculada somente no momento do build local.

## Issues e agrupamento

O Sentry agrupa ocorrências semelhantes em issues. A qualidade desse agrupamento influencia diretamente a operação. Uma URL dinâmica, um ID de usuário ou uma mensagem que contém dados variáveis não deve criar uma issue diferente para cada valor. Por outro lado, uma regra excessivamente ampla pode juntar falhas com causas diferentes e esconder uma regressão.

Revise fingerprint, normalização de mensagens e stack traces quando o volume de issues parecer incompatível com o número de causas. Erros esperados, como validação de entrada ou autenticação anônima, devem ser tratados com métricas e logs apropriados quando não exigirem uma issue. A captura indiscriminada aumenta custo, ruído e tempo de triagem.

## Breadcrumbs e contexto

Breadcrumbs devem registrar etapas úteis que precederam o erro, como navegação, chamadas externas, mudanças de estado, eventos de fila e operações importantes. Eles não devem armazenar tokens, corpos completos de requisições, senhas ou dados pessoais desnecessários. Um breadcrumb deve ajudar a reconstruir a sequência sem se tornar um espelho do payload do usuário.

Tags são úteis para filtrar por serviço, ambiente, região, release e tipo de operação. Elas precisam de controle de cardinalidade. Colocar um identificador único em todas as ocorrências pode tornar a consulta cara e criar uma combinação diferente para cada evento. Valores com alta cardinalidade pertencem ao contexto do evento ou aos logs quando a busca individual for necessária.

## Performance e amostragem

Transactions, spans e profiles ajudam a localizar tempo gasto em frontend, backend, banco e dependências. Eles podem mostrar que o problema está na fila antes do controller, em uma query, em uma chamada externa ou na hidratação da interface. Sampling deve representar erros, transações lentas e rotas críticas, mesmo quando o tráfego normal for amostrado em uma taxa menor.

Avalie sampling por ambiente, rota, duração, erro e release. Uma taxa alta em tráfego comum pode consumir orçamento sem melhorar o diagnóstico. Uma taxa baixa pode perder uma transação rara que explica o incidente. O volume, a retenção e a latência de ingestão da própria plataforma devem ser observados.

## Releases e source maps

No frontend, source maps permitem transformar uma stack trace minificada no arquivo e na linha de origem. Eles devem ser enviados por um canal protegido, associado à release correta e impedidos de ficar publicados como arquivos acessíveis a qualquer pessoa. A publicação de source maps exige avaliar se o código-fonte embutido contém segredos, endpoints internos ou informações que não devem ser públicas.

Use releases para comparar antes e depois de uma implantação. Uma regressão pode aparecer como aumento de uma issue, criação de um novo grupo, piora de p95 ou concentração em uma região. O registro de deploy deve incluir versão, commit, ambiente, início do rollout e resultado da promoção ou reversão.

## Privacidade e acesso

Filtre dados sensíveis antes do envio. Isso inclui tokens, cookies, headers de autenticação, payloads de login, conteúdo de formulários, e-mails, endereços, identificadores regulados e dados de pagamento. A filtragem no painel não é a única barreira, porque o dado já teria deixado o ambiente. Use hooks do SDK, normalizadores e políticas de retenção para limitar a coleta na origem.

Defina se IP, user context, replay, anexos e breadcrumbs podem ser coletados. A decisão deve considerar LGPD, contratos, residência dos dados e necessidade operacional. Restrinja acesso por equipe, ambiente e função. A chave pública usada por SDK de navegador não deve ser confundida com uma credencial administrativa.

## Alertas e ownership

Alertas do Sentry devem representar uma decisão operacional. Bons sinais são uma nova issue em produção, aumento sustentado de uma issue, regressão após release, crescimento de usuários afetados, falha em uma rota crítica ou aumento de transações lentas. Alertar cada ocorrência individual cria fadiga e incentiva silenciamento.

Cada regra precisa de severidade, owner, canal, janela, condição de resolução e runbook. A integração com uma ferramenta de tarefas deve preservar a issue original, evitar duplicação e indicar a release ou componente responsável. O alerta precisa ter uma ação possível; se ninguém pode agir sobre ele, provavelmente deve ser uma métrica ou uma consulta, não uma página.

## Incidente e aprendizado

Durante um incidente, o Sentry ajuda a identificar início, release, rota, usuários afetados e efeito de uma mitigação. Combine seus dados com métricas de tráfego, logs estruturados, traces, eventos de deploy e estado da infraestrutura. Não presuma que todo trace estará disponível: sampling, retenção, falha de exportação e diferenças entre SDKs podem deixar apenas o evento ou os logs.

Depois do incidente, use o evento para criar um teste de regressão, melhorar agrupamento, ajustar contexto, corrigir alerta ou revisar o runbook. Sentry não deve ser um depósito passivo de erros. O valor está no ciclo entre sinal, investigação, mitigação, correção, prevenção e manutenção.

## Self-hosted

Sentry Cloud delega ingestão, armazenamento e retenção ao fornecedor conforme o plano contratado. Sentry self-hosted mantém eventos na própria infraestrutura, mas transforma a plataforma de observabilidade em mais um sistema a operar. Banco, filas, storage, upgrades, backup, retenção, capacidade, autenticação e segurança passam a ser responsabilidade da equipe.

Self-hosted não significa custo zero nem elimina requisitos de disponibilidade. Se o Sentry for usado para investigar o mesmo incidente que derrubou a plataforma observada, ele precisa de um domínio de falha considerado no desenho. Retenção, amostragem e acesso devem ser configurados antes de o volume crescer sem controle.

## Relações

- [Observabilidade](index.md) separa sinais, coleta, armazenamento e ação.
- [Distributed tracing](tracing.md) explica correlação entre serviços.
- [Correlation ID](correlation-id.md) explica o identificador definido pela aplicação.
- [OpenTelemetry](opentelemetry/index.md) cobre instrumentação e transporte interoperáveis.
- [Segurança no ciclo de vida](../seguranca/appsec/seguranca-no-ciclo-de-vida.md) posiciona Sentry em relação aos scanners de segurança.

## Fonte primária

- [Sentry documentation](https://docs.sentry.io/)
