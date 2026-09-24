# Event streaming

Event streaming trata eventos como uma sequência durável e ordenada, frequentemente particionada. Consumidores mantêm uma posição e podem reler eventos conforme a retenção e as garantias da plataforma.

## Casos de uso

Integração orientada a eventos, pipelines de dados, reconstrução de projeções e múltiplos consumidores independentes são casos comuns.

## Boa prática

Defina chave de particionamento conscientemente, trate evolução de schema como contrato e planeje retenção e replay.

## Má prática

Escolher streaming para qualquer tarefa assíncrona aumenta complexidade quando uma fila simples bastaria. Outra má prática é assumir ordenação global quando o sistema só garante ordem dentro de uma partição.

## Continue por aqui

[Filas](filas.md) são frequentemente melhores quando o problema é distribuir trabalho, não preservar um log reproduzível.
