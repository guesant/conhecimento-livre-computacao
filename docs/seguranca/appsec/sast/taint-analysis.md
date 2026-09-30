# Taint analysis

Taint analysis acompanha dados marcados com uma propriedade relevante ao longo de um programa. Em segurança, o caso clássico marca entrada não confiável e procura caminhos até operações sensíveis.

## Modelo

Uma [source](source.md) introduz o dado marcado. Um [sink](sink.md) representa uma operação sensível. Um [sanitizer](sanitizer.md) transforma ou valida o dado de forma que, para uma classe específica de risco, o fluxo possa deixar de ser considerado perigoso.

## Exemplo

Entrada HTTP pode ser source e execução de SQL pode ser sink. A análise procura um caminho entre ambos que não passe por tratamento reconhecido.

## Limite

O resultado depende do modelo. Uma abstração interna que encapsula validação pode ser desconhecida pela ferramenta e gerar falso positivo; uma função perigosa não modelada pode gerar falso negativo.

## Continue por aqui

[Data-flow analysis](data-flow-analysis.md) é o conceito mais geral. [SAST](index.md) explica onde a técnica é usada.
