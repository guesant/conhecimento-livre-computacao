# State locking

State locking impede execuções concorrentes de ler e alterar o mesmo state
simultaneamente. Sem lock, dois planos podem partir da mesma versão e aplicar
mudanças intercaladas.

## Comportamento

Um backend com lock adquire exclusão antes de ler ou gravar o state. A segunda
execução espera ou falha conforme a configuração. O lock precisa ter timeout e
ser liberado por uma execução que termine normalmente.

Forçar unlock sem confirmar que não há execução ativa pode permitir exatamente a
corrida que o lock deveria impedir. Em caso de lock órfão, confirme processo,
pipeline, backend e versão antes de removê-lo.

## Relações

- [State](state.md) é o objeto protegido.
- [Desired state](desired-state.md) define o conteúdo a convergir.
- [Drift](drift.md) pode ser criado por mudanças externas durante uma corrida.

## Fonte primária

- [OpenTofu state locking](https://opentofu.org/docs/language/state/locking/)
