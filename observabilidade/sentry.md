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

## Relações

- [Observabilidade](index.md) separa sinais, coleta, armazenamento e ação.
- [Distributed tracing](tracing.md) explica correlação entre serviços.
- [Correlation ID](correlation-id.md) explica o identificador definido pela aplicação.
- [OpenTelemetry](opentelemetry/index.md) cobre instrumentação e transporte interoperáveis.
- [Segurança no ciclo de vida](../seguranca/appsec/seguranca-no-ciclo-de-vida.md) posiciona Sentry em relação aos scanners de segurança.

## Fonte primária

- [Sentry documentation](https://docs.sentry.io/)
