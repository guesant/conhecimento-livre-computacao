# Sentry

Sentry é uma plataforma de observabilidade de aplicações focada em erros, exceções, performance e contexto de execução. Ela agrupa eventos semelhantes, preserva stack traces e pode correlacionar transações, releases, usuários e outros metadados conforme a instrumentação e a política de retenção.

## O que ele observa

Sentry responde perguntas como quais erros cresceram depois de uma release, qual transação está lenta e qual stack trace representa a falha. Traces, profiles, breadcrumbs e contexto de ambiente ajudam a reproduzir o problema, mas o valor depende de instrumentar os caminhos relevantes e de não enviar segredos ou dados pessoais indevidos.

Sentry não é SAST, DAST, antivírus ou EDR. Ele pode registrar uma exceção causada por um ataque, mas não substitui análise preventiva nem resposta de endpoint. Também não deve receber payloads completos quando eles contêm credenciais, tokens ou dados regulados.

## SaaS e self-hosted

Sentry Cloud é o modelo SaaS, com operação e retenção delegadas ao fornecedor conforme o plano contratado. Sentry self-hosted permite manter eventos na própria infraestrutura, mas exige operar banco, filas, armazenamento, upgrades, retenção, capacidade e segurança do próprio Sentry.

A escolha deve considerar residência dos dados, volume de eventos, retenção, custo de ingestão, integração com o ciclo de release e capacidade de manter a plataforma. Self-hosted não significa custo zero: o sistema de observabilidade também precisa de backup, monitoramento e controle de acesso.

## Boas práticas

Defina níveis de amostragem e retenção, remova dados sensíveis antes do envio, associe eventos a releases e mantenha alertas acionáveis. Use o evento para investigar e corrigir a causa; não transforme cada exceção esperada em incidente. Teste o comportamento quando o endpoint de telemetria estiver indisponível para que a aplicação continue funcional.

## Relações

- [Observabilidade](index.md) separa sinais, coleta, armazenamento e ação.
- [Distributed tracing](tracing.md) explica correlação entre serviços.
- [OpenTelemetry](opentelemetry/index.md) cobre instrumentação e transporte interoperáveis.
- [Segurança no ciclo de vida](../seguranca/appsec/seguranca-no-ciclo-de-vida.md) posiciona Sentry em relação aos scanners de segurança.

## Fonte primária

- [Sentry documentation](https://docs.sentry.io/)
