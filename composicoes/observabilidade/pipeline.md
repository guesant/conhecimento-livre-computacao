# Pipeline de observabilidade

Uma stack de observabilidade possui responsabilidades independentes: instrumentar, coletar, transportar, armazenar, consultar, visualizar e alertar.

## Instrumentação

A aplicação ou infraestrutura produz sinais. OpenTelemetry fornece APIs, SDKs e protocolos para telemetria; exporters e endpoints específicos também podem produzir métricas ou logs.

## Coleta e transporte

Prometheus pode fazer scrape de métricas. Agentes como Grafana Alloy ou OpenTelemetry Collector podem receber, transformar e encaminhar sinais. Essa camada não precisa ser o armazenamento definitivo.

## Armazenamento

Prometheus armazena séries temporais; Loki armazena logs; backends de tracing armazenam spans. Retenção e cardinalidade pertencem a esta decisão.

## Consulta e visualização

Grafana consulta data sources. Ele não transforma automaticamente qualquer fonte em observabilidade útil; dashboards dependem da semântica dos sinais.

## Alerta

Alertas devem nascer de condições que exigem ação. A regra pode ser avaliada no backend de métricas ou em componentes dedicados, e a entrega precisa de roteamento, agrupamento e silenciamento.

## Cenário single-node

Uma stack local é simples e barata, mas compartilha o failure domain do sistema observado. Se o host morre, a telemetria local pode desaparecer junto. Isso pode ser aceitável em laboratório e insuficiente para produção com requisitos de post-mortem.

## Cenário com requisito de sobrevivência

Enviar sinais para outro failure domain ou serviço gerenciado preserva evidência quando o cluster falha. O custo é rede, armazenamento externo, credenciais e possivelmente custo financeiro.

## Anti-patterns

Não instale um componente para cada sinal antes de definir perguntas operacionais. Não duplique collectors sem responsabilidade clara. Não use dashboards como substituto de alertas acionáveis.

## Continue por aqui

[Observabilidade](../../observabilidade/index.md) e suas páginas de métricas, logs e tracing aprofundam os sinais.