# Loki

Loki é um sistema de agregação de logs projetado em torno de labels. Diferente de mecanismos que indexam integralmente o conteúdo de cada documento, Loki mantém um índice dos labels dos streams e armazena o conteúdo em chunks.

## Casos de uso

Centralizar logs de workloads Kubernetes e correlacioná-los por namespace, aplicação, Pod ou outros labels de baixa cardinalidade é um caso comum.

## Boa prática

Use labels para dimensões estáveis e seletivas. Deixe valores de alta cardinalidade no conteúdo estruturado do log e filtre-os durante a consulta quando necessário.

## Má prática

Transformar request ID, timestamp ou identificador de usuário em label cria cardinalidade excessiva e contraria o modelo de custo do Loki.

## Fontes

- Grafana Loki documentation: <https://grafana.com/docs/loki/latest/>
- Loki labels: <https://grafana.com/docs/loki/latest/get-started/labels/>

## Continue por aqui

[Logs](logs.md) explica o sinal. [Grafana](grafana.md) fornece uma interface de consulta e visualização.
