# Sync, prune e self-heal

Sync aplica a revisão desejada ao ambiente. Prune remove recursos que não
estão mais no conjunto renderizado. Self-heal reaplica o desejado quando o
recurso diverge depois da sincronização.

## Trade-offs

Sync automático reduz atraso, mas aplica erros do repositório sem uma aprovação
no momento da entrega. Prune mantém o ambiente limpo, mas uma remoção
acidental pode ter efeito destrutivo. Self-heal corrige drift manual, mas pode
lutar com outro controller ou esconder uma alteração emergencial.

Use permissões, revisão, validação de manifests e janela de mudança para
reduzir o risco. A configuração precisa explicitar quais recursos pertencem ao
reconciler e quais são geridos por outra camada.

## Relações

- [Drift em GitOps](drift.md) classifica divergências.
- [Application](application.md) declara origem e destino.
- [Argo CD](../argocd.md) implementa essas opções.

## Fonte primária

- [Argo CD sync policy](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
