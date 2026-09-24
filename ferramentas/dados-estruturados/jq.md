# jq

jq é uma linguagem e ferramenta de linha de comando para consultar e transformar JSON.

## Casos de uso

Selecionar campos, filtrar arrays, construir novos objetos e transformar saída de APIs.

## Boa prática

Use jq quando a decisão depende da estrutura JSON. Prefira saída raw apenas quando o consumidor realmente espera texto.

## Má prática

Substituir validação de schema por filtros ad hoc ou usar grep/sed para interpretar JSON quando jq está disponível.
