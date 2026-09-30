# Allow-overrides

Allow-overrides é um algoritmo de combinação em que uma permissão explícita
pode prevalecer sobre decisões contrárias menos específicas.

## Risco

Essa estratégia pode transformar uma exceção em bypass de uma negação necessária.
Use-a apenas quando a hierarquia de políticas for explícita e o allow puder ser
provado como mais específico e confiável.

## Relações

O algoritmo precisa ser documentado junto com default deny, precedência e
escopo. Misturar políticas de engines diferentes pode produzir semânticas
incompatíveis.
