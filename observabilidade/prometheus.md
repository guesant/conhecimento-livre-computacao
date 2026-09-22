# Prometheus

Prometheus é um sistema de monitoramento e banco de séries temporais. Ele combina um modelo de dados baseado em métricas e labels, coleta normalmente orientada a pull, uma linguagem de consulta própria, PromQL, e avaliação de regras.

## O que ele é e o que não é

Prometheus é adequado para séries temporais numéricas e monitoramento operacional. Não é um banco genérico de eventos, um repositório de logs nem um sistema de tracing. Também não é sinônimo de "observabilidade": é uma implementação para parte do pipeline.

## Modelo de dados

Uma série é identificada pelo nome da métrica e por seu conjunto de labels. Alterar qualquer valor de label cria outra série. Essa propriedade torna labels poderosos para agregação e perigosos quando recebem valores praticamente únicos.

Counters crescem ao longo do tempo e representam ocorrências acumuladas. Gauges podem subir e descer. Histograms distribuem observações em buckets e permitem raciocinar sobre distribuições como latência.

## Coleta

No modelo comum, Prometheus descobre targets e executa scrape de endpoints HTTP. Service discovery pode vir de Kubernetes, arquivos ou outras integrações. Pushgateway existe para casos específicos, principalmente jobs efêmeros; não transforma push no modelo padrão para serviços long-running.

## PromQL e regras

PromQL consulta e agrega séries. Recording rules materializam expressões recorrentes em novas séries, reduzindo custo de consultas repetidas. Alerting rules avaliam condições e produzem alertas que podem ser encaminhados ao Alertmanager.

## Caso de uso: serviço HTTP

Um serviço pode expor contadores de requisições por status e histogramas de duração. A partir deles é possível calcular taxa de erro e distribuição de latência sem armazenar cada request como uma série separada.

Um request ID nunca deve ser label dessa métrica: cada requisição criaria uma série.

## Caso de uso: Kubernetes

Prometheus Operator adiciona recursos como ServiceMonitor, PodMonitor e PrometheusRule. Esses objetos descrevem descoberta e regras; o Operator traduz o estado declarativo para configuração dos componentes.

Isso é uma integração Kubernetes, não uma propriedade necessária do Prometheus fora do cluster.

## Single-node

Prometheus local é simples e pode ser suficiente para laboratório, homelab e ambientes em que perder métricas junto com o host é aceitável. Retenção precisa respeitar disco disponível.

Se as métricas precisam sobreviver à perda do host observado, o backend ou uma cópia precisa existir em outro failure domain.

## Escala e retenção

Prometheus isolado mantém armazenamento local. Arquiteturas maiores podem usar remote write e sistemas como Thanos, Mimir ou VictoriaMetrics para retenção longa, consulta global ou escala horizontal.

A adoção dessas peças deve nascer de requisito. Adicionar Thanos a um único Prometheus pequeno sem necessidade de retenção externa ou visão global cria custo operacional sem benefício proporcional.

## Boas práticas

Controle cardinalidade; use nomes e unidades consistentes; monitore scrape failures e o próprio Prometheus; defina retenção por necessidade; use recording rules para cálculos caros e recorrentes; trate alertas como interface operacional, não como coleção de thresholds arbitrários.

## Más práticas

IDs de usuário, URLs sem normalização e request IDs como labels. Alertar sobre toda métrica disponível. Usar `up == 1` como única definição de saúde. Armazenar eventos individuais como métricas. Assumir que mais retenção é sempre melhor sem calcular disco e valor histórico.

## Alternativas e complementos

VictoriaMetrics e Grafana Mimir cobrem armazenamento/consulta de métricas com arquiteturas diferentes. Thanos complementa Prometheus em cenários de armazenamento de objetos, alta disponibilidade e visão global. Serviços gerenciados transferem parte da operação ao provedor.

OpenTelemetry pode participar da instrumentação e transporte, mas não é simplesmente "um Prometheus alternativo": ocupa responsabilidades parcialmente diferentes.

## Fontes

- Prometheus documentation: <https://prometheus.io/docs/>
- Data model: <https://prometheus.io/docs/concepts/data_model/>
- Storage: <https://prometheus.io/docs/prometheus/latest/storage/>
- Prometheus Operator: <https://prometheus-operator.dev/>

## Continue por aqui

[Métricas](metricas.md) explica o sinal independentemente do produto. [Pipeline de observabilidade](../composicoes/observabilidade/pipeline.md) mostra como Prometheus se relaciona com coleta, visualização e alerta.
