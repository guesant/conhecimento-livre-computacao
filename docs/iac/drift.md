# Drift de infraestrutura

Drift é a divergência entre o estado declarado, o state conhecido e o recurso
real. Ele pode ser causado por alteração manual, automação concorrente,
mudança externa ou provider que não representa todos os atributos.

## Classificação

Compare configuração com state para encontrar diferença declarativa. Compare
state com a API real para encontrar diferença observada. Nem toda diferença
deve ser corrigida automaticamente: alguns atributos são calculados, mutáveis
por outro controlador ou deliberadamente ignorados.

## Resposta

Primeiro preserve evidência e descubra quem possui a propriedade do atributo.
Depois escolha importar, atualizar a declaração, reconciliar o recurso ou
reverter a mudança manual. Aplicar um plano destrutivo apenas para eliminar a
diferença transforma um diagnóstico em incidente.

## Relações

- [State](state.md) registra identidade e observações.
- [Estado desejado](desired-state.md) define a intenção.
- [Reconciliação](../entrega/reconciliation.md) trata convergência contínua em
  GitOps.

## Fonte primária

- [OpenTofu plan](https://opentofu.org/docs/cli/commands/plan/)
