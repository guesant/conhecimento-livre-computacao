# Métricas

Métricas representam valores numéricos observados ao longo do tempo. Em sistemas de séries temporais, uma série é normalmente identificada pelo nome da métrica e por um conjunto de labels.

## Casos de uso

Taxa de requisições, latência agregada, erros, saturação de recursos e tamanho de filas são bons candidatos. Métricas funcionam bem quando a pergunta pode ser agregada e comparada ao longo do tempo.

## Boa prática

Escolha labels com cardinalidade controlada. Modele dimensões úteis para agregação e alerta. Use histogramas quando precisa compreender distribuições como latência.

## Má prática

IDs de usuário, request IDs e valores praticamente únicos como labels criam séries demais e aumentam custo de memória, armazenamento e consulta. Eventos individuais pertencem melhor a logs ou traces.

## Continue por aqui

[Prometheus](prometheus.md) implementa um modelo de séries temporais e PromQL. [Logs](logs.md) cobrem eventos discretos.
