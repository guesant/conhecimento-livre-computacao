# Netdata

Netdata é uma ferramenta de observabilidade com agente voltada a métricas de alta resolução e feedback próximo do tempo real. O agente coleta sinais do host, containers, serviços e aplicações e os apresenta por meio de dashboards e consultas próprias.

## Fronteira

Netdata é forte na exploração imediata de saúde e capacidade, mas não deve ser confundido com um backend de retenção ilimitada ou com uma plataforma completa de tracing. Retenção, agregação, exportação e correlação com outros sinais precisam ser avaliadas separadamente.

## Quando usar

Ele é útil para diagnosticar hosts, workloads e mudanças recentes com baixa latência visual. Pode operar localmente ou enviar métricas para uma topologia centralizada, mas essa centralização introduz autenticação, rede, armazenamento e outro failure domain.

## Limitações

Dashboards não são uma política de alertas. Antes de criar alertas, defina a pergunta operacional, a janela, a severidade e a ação esperada. Também controle cardinalidade e retenção para que a telemetria não concorra com o workload por CPU, memória e disco.

## Relações

- [Observabilidade](index.md) explica sinais e responsabilidades.
- [Prometheus](prometheus.md) é uma alternativa orientada a métricas, regras e armazenamento de séries temporais.
- [OpenTelemetry](opentelemetry/index.md) trata instrumentação e transporte de sinais.

## Fonte primária

- [Netdata documentation](https://learn.netdata.cloud/docs/)
