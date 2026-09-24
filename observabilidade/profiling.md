# Profiling

Profiling mede onde um programa consome recursos ao longo da execução, como CPU, memória ou alocações.

## Relação com outros sinais

Métricas mostram que CPU aumentou; tracing pode mostrar qual caminho ficou lento; profiling pode revelar quais funções consumiram o tempo de CPU. Os sinais são complementares.

## Continuous profiling

Continuous profiling coleta profiles periodicamente em produção ou ambientes representativos, permitindo comparar comportamento ao longo do tempo.

## Custo e segurança

Frequência, retenção e tipo de profile afetam overhead e armazenamento. Profiles podem conter nomes de funções e outras informações internas, portanto também são dados operacionais a proteger.

## Continue por aqui

[Observabilidade](index.md) situa profiling ao lado de métricas, logs e tracing.
