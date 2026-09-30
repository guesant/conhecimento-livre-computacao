# Reconciliação

Reconciliação é o loop que observa estado desejado e estado atual, calcula a
diferença e tenta aplicar uma mudança até que a condição esperada seja
alcançada. O loop repete porque APIs, rede e outros controllers podem falhar.

## Modelo

O reconciler precisa ser idempotente, tolerar eventos repetidos e atualizar
status sem confundir intenção com observação. Ele deve tratar recursos que
desaparecem, mudanças concorrentes e dependências ainda não prontas.

Reconciliação não é um único apply. Ela é uma atividade contínua que pode
reverter drift e reagir à alteração de uma dependência.

## Failure modes

Um loop pode falhar por credencial, conflito, schema inválido, dependência não
pronta ou erro transitório. Backoff evita sobrecarregar a API, enquanto status
e eventos preservam o motivo da não convergência.

## Relações

- [GitOps](gitops.md) usa reconciliação como mecanismo.
- [Drift](../iac/drift.md) descreve a diferença observada.
- [Controller](../kubernetes/control-plane/controller.md) implementa loops no
  Kubernetes.

## Fonte primária

- [Kubernetes controllers](https://kubernetes.io/docs/concepts/architecture/controller/)
