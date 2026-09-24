# Cardinalidade em observabilidade

Cardinalidade é a quantidade de combinações distintas de valores que uma dimensão pode assumir. Em sistemas de métricas baseados em labels, cada combinação pode criar uma série diferente.

## Exemplo

Um label `method` com cinco valores possui cardinalidade baixa. Um label `request_id` pode ter um valor novo para cada requisição e criar milhões de séries.

## Impacto

Alta cardinalidade aumenta memória, índice, armazenamento e custo de consulta. O efeito exato depende do backend.

## Boa prática

Use dimensões com conjuntos limitados e operacionalmente úteis. Preserve identificadores únicos em logs ou traces quando a pergunta exige individualidade.

## Continue por aqui

[Métricas](metricas.md) explica o modelo do sinal e [Prometheus](prometheus.md) mostra como labels identificam séries.
