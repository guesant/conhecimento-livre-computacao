# Estado desejado

Estado desejado é a descrição declarativa do resultado que uma ferramenta deve
convergir, não uma sequência de comandos que alguém precisa repetir. O
sistema compara essa descrição com o estado observado e decide se há mudança.

## Implicações

A descrição precisa ser completa o suficiente para que duas execuções
concordem sobre o resultado, mas não deve assumir controle sobre atributos
gerenciados por outro sistema. A fronteira de propriedade é parte do contrato.

Estado desejado não significa que o sistema real esteja sempre igual. Falhas,
drift, lock e reconciliação são situações esperadas que a ferramenta precisa
tornar visíveis.

## Relações

- [Idempotência](idempotence.md) permite repetir a convergência.
- [Drift](drift.md) descreve divergência entre desejado e observado.
- [Reconciliação](../entrega/reconciliation.md) aplica o mesmo modelo em
  GitOps.

## Fonte primária

- [OpenTofu language](https://opentofu.org/docs/language/)
