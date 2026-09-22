# Observabilidade

Observabilidade é a capacidade de inferir o estado interno de um sistema a partir das saídas que ele produz. Na prática de engenharia, isso exige mais do que instalar uma "stack": sinais precisam ser instrumentados, coletados, armazenados, consultados e transformados em diagnóstico ou ação.

## Sinais não são ferramentas

[Métricas](metricas.md) representam medições agregáveis e séries temporais. [Logs](logs.md) preservam eventos e contexto discreto. [Distributed tracing](tracing.md) relaciona operações ao longo de uma requisição. Profiles descrevem onde recursos de execução são consumidos ao longo do tempo.

Prometheus, Loki, Grafana e OpenTelemetry ocupam responsabilidades dentro dessa cadeia; eles não definem os sinais.

## Escolha o sinal pela pergunta

"Qual a taxa de erro nos últimos 30 minutos?" favorece métricas. "O que aconteceu com a requisição 8f...?" favorece logs e traces. "Qual serviço adicionou 400 ms?" favorece tracing. "Qual função consome CPU?" favorece profiling.

Forçar toda pergunta para o mesmo backend produz custo e baixa qualidade de diagnóstico.

## RED e USE

RED organiza sinais de serviços em Rate, Errors e Duration. USE organiza recursos em Utilization, Saturation e Errors. São heurísticas para começar uma cobertura, não substitutos de entender o sistema.

Um dashboard pode usar RED para API e USE para CPU/disco sem que um framework precise vencer o outro.

## Golden signals

Latência, tráfego, erros e saturação são uma heurística popularizada por SRE. O valor está em cobrir experiência e capacidade, não em criar quatro gráficos obrigatórios para qualquer componente.

## Observabilidade versus monitoramento

Monitoramento normalmente parte de condições conhecidas que queremos acompanhar. Observabilidade também precisa permitir investigar estados que não foram antecipados exatamente.

Isso não significa que "observabilidade" elimina monitoramento ou alertas. Uma operação madura combina sinais exploráveis com condições acionáveis conhecidas.

## Cenário single-node

Uma stack Prometheus + Loki + Grafana local pode ser adequada para laboratório e operação sem requisito de sobrevivência da telemetria. É simples, mas compartilha disco, CPU e failure domain com o sistema observado.

## Cenário distribuído

Coletores locais podem enviar sinais a backends externos ou centralizados. Isso melhora retenção e correlação entre clusters, ao custo de rede, autenticação, armazenamento e uma plataforma de observabilidade que também precisa ser operada.

## Implementações

[Prometheus](prometheus.md) cobre métricas e regras. [Loki](loki.md) cobre logs. [Grafana](grafana.md) consulta e visualiza data sources. OpenTelemetry padroniza instrumentação e transporte de múltiplos sinais. Alertmanager cuida de roteamento de alertas no ecossistema Prometheus.

## Boas práticas

Comece por perguntas e SLOs; instrumente caminhos críticos; controle cardinalidade e retenção; preserve correlação entre sinais; mantenha telemetria sensível sob política; teste se alertas levam a uma ação concreta.

## Más práticas

Instalar a stack antes de definir perguntas. Criar dashboards para cada métrica. Guardar tudo indefinidamente. Alertar em thresholds sem impacto. Depender apenas de logs. Usar tracing em 100% do tráfego sem avaliar volume e custo.

## Composição e evolução

[Pipelines de observabilidade](../composicoes/observabilidade/pipeline.md) mostra instrumentação → coleta → armazenamento → consulta → alerta e como a topologia muda entre single-node e ambientes em que a telemetria precisa sobreviver à plataforma observada.

## Continue por aqui

Aprofunde [métricas](metricas.md), [logs](logs.md), [tracing](tracing.md) ou as implementações [Prometheus](prometheus.md), [Loki](loki.md) e [Grafana](grafana.md).