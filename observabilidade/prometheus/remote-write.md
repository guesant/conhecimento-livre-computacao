# Prometheus remote write

Remote write envia amostras do Prometheus para um backend remoto. Ele separa
coleta local da retenção, consulta ou agregação de longo prazo.

## Uso

Remote write é útil quando métricas precisam sobreviver à perda do host, ser
consultadas por múltiplos Prometheus ou chegar a um armazenamento escalável.
A fila local precisa de limites e comportamento definido durante indisponibilidade
do destino.

## Trade-offs

O envio acrescenta rede, CPU, armazenamento temporário e uma nova falha. Um
backend remoto indisponível pode criar backlog e consumir disco. Filtrar
métricas antes do envio reduz custo, mas pode remover evidência necessária.

## Relações

- [Prometheus](../prometheus.md) coleta e avalia métricas.
- [Métricas](../metricas.md) define cardinalidade.
- [Pipeline de observabilidade](../../composicoes/observabilidade/pipeline.md)
  posiciona armazenamento e consulta.

## Fonte primária

- [Prometheus remote write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write)
