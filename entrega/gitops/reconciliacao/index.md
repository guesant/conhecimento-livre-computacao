# Reconciliação

Reconciliação compara um estado observado com um estado desejado e executa
ações para reduzir a diferença. O controlador precisa lidar com repetição,
falhas parciais, ordem, ownership, prune e alterações feitas fora da fonte de
verdade.

[GitOps](../index.md) aplica esse modelo quando o estado desejado é versionado
em Git. [Drift](../../drift.md), [sync, prune e self-heal](../../sync-prune-self-heal.md)
e as estratégias pull-based e push-based tratam decisões distintas do ciclo.
