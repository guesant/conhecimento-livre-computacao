# Kubescape

Kubescape é uma ferramenta de avaliação de segurança para Kubernetes. Ela
analisa manifests e recursos do cluster contra frameworks e controles de
segurança, produzindo achados que ajudam a priorizar correções.

O resultado de uma avaliação não altera automaticamente o comportamento da
API. Para bloquear uma admissão, o ambiente precisa de uma política aplicada
por um mecanismo próprio, como Pod Security Admission, Kyverno ou Gatekeeper.
Essa distinção evita tratar um relatório de postura como se fosse um controle
preventivo.

Kubescape pode ser usado no repositório, no pipeline e contra um cluster em
execução. Cada contexto responde uma pergunta diferente: o scan de manifests
detecta problemas antes da aplicação; o scan do cluster encontra o estado que
realmente foi aplicado e pode incluir drift ou recursos criados fora do Git.

## Relações

- [Policy enforcement](policy-enforcement.md) cobre bloqueio e mutação na
  admissão.
- [Drift em GitOps](../../entrega/drift.md) explica por que o estado aplicado
  pode divergir do repositório.
- [SAST](../appsec/sast/index.md) trata da análise do código da aplicação.

## Fonte primária

- [Kubescape documentation](https://kubescape.io/docs/)
