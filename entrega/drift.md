# Drift em GitOps

Drift é a diferença entre o estado declarado no repositório e o estado
observado no ambiente. Ele pode ser uma alteração manual, uma mutação de
admission, um controller legítimo ou uma ferramenta que possui parte do
recurso.

## Resposta

Antes de reverter, identifique o proprietário do campo. Um reconciler que
aplica self-heal em todo campo pode lutar com outro controller ou desfazer uma
alteração legítima calculada pelo ambiente.

Prune remove recursos que deixaram de ser declarados. É útil para evitar
resíduos, mas aumenta o impacto de uma remoção acidental no repositório. A
política deve ser validada em revisão e em ambiente de teste.

## Relações

- [Reconciliação](reconciliation.md) executa a convergência.
- [Sync, prune e self-heal](sync-prune-self-heal.md) descreve as ações.
- [State drift de IaC](../iac/drift.md) usa um modelo parecido com outro
  lifecycle.

## Fonte primária

- [Argo CD automated sync](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
