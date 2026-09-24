# Sinais de observabilidade

Observabilidade não é uma ferramenta, é a capacidade de responder perguntas sobre o estado interno de um sistema a partir de sinais externos. Três sinais cobrem perguntas diferentes, e nenhum substitui os outros. **Métricas** são amostras numéricas organizadas como séries temporais, contadores, gauges, histogramas; respondem "quanto" e "com que frequência", são baratas de armazenar e ótimas para alertas e agregações, mas não guardam o contexto de uma execução específica. **Logs** são registros discretos de eventos; respondem "o que aconteceu exatamente nesta execução", custam mais para armazenar e consultar em volume, e frequentemente contêm dados sensíveis que exigem tratamento. **Traces** capturam o caminho e a duração de uma operação através de múltiplos serviços, dividida em spans; respondem "onde o tempo foi gasto" numa requisição distribuída. Os três se correlacionam por tempo, cluster, namespace e, quando adotado, um `trace_id` comum, mas um identificador de requisição nunca deve virar label de métrica, porque criaria uma série nova por requisição. Métricas vêm sempre primeiro, o sinal mais barato, cobrindo a maioria dos alertas de disponibilidade e capacidade; logs entram quando métricas não explicam a causa de um erro específico; traces entram quando a aplicação já é distribuída entre múltiplos serviços e a origem de uma latência não é óbvia a partir de métricas isoladas por serviço.

## Saúde de aplicação

Disponibilidade percebida, probes e monitoramento de caixa-branca e caixa-preta
estão em [saúde de aplicação](observabilidade/application-health.md).

## Continue por aqui

[Stack Prometheus, Loki e Grafana](stack-prometheus-loki-grafana.md) cobre a implementação concreta de métricas e logs; [alertas acionáveis](observabilidade/alertas-acionaveis.md) cobre como transformar sinais em uma notificação útil.
