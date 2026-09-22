# Data-flow analysis

Data-flow analysis determina como valores ou propriedades associadas a valores podem se propagar por um programa.

Ela é uma técnica de análise, não um scanner de segurança por si só. Compiladores, IDEs e ferramentas de segurança podem usá-la para objetivos diferentes.

## Relação com SAST

SAST pode usar data-flow analysis para encontrar relações que uma regra puramente sintática não enxerga. [Taint analysis](taint-analysis.md) é uma aplicação especializada que acompanha dados considerados não confiáveis ou sensíveis.

## Fronteiras

Data flow não significa necessariamente executar o programa. Uma análise estática constrói uma aproximação dos fluxos possíveis. Essa aproximação precisa equilibrar precisão, custo e cobertura.

## Continue por aqui

[Taint analysis](taint-analysis.md) especializa o conceito para propagação de dados marcados. [SAST](index.md) situa a técnica dentro de segurança de aplicações.