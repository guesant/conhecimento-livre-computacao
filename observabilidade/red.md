# RED

RED organiza observação de serviços em três dimensões: Rate, Errors e Duration.

Rate mede volume de operações por unidade de tempo. Errors mede operações que falham segundo a semântica definida. Duration mede quanto tempo as operações levam.

RED é uma heurística de instrumentação e dashboards, não uma ferramenta nem um conjunto obrigatório de métricas.

## Caso de uso

APIs e serviços orientados a requisições são um encaixe natural porque possuem operações contáveis, resultado e duração.

## Limite

Recursos como disco e CPU não se encaixam tão naturalmente. [USE](use.md) oferece outra lente para recursos.

## Continue por aqui

[Golden signals](golden-signals.md) possui sobreposição conceitual, mas origem e formulação diferentes.