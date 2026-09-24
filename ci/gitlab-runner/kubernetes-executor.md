# GitLab Runner com Kubernetes executor

O Kubernetes executor chama a API do cluster e cria um Pod para cada job. O
Pod pode conter o container do job e containers de services, com requests,
limits, volumes, service account, tolerations e políticas definidos pela
configuração do runner.

O diretório `/cache` pode ser um volume temporário, um PVC ou outro volume
suportado pelo executor. Para compartilhar o cache entre Pods e runners, o
backend distribuído é geralmente mais simples do que exigir um volume
`ReadWriteMany` em todos os nós.

## Isolamento e capacidade

O runner deve usar um namespace próprio, service account com permissões mínimas
e limites para os Pods de job. `privileged` e Docker-in-Docker só devem ser
habilitados para projetos que realmente precisam construir imagens. A
concorrência do runner precisa ser compatível com CPU, memória, storage e
limites de API do cluster.

Um cache miss não pode bloquear indefinidamente o job. O Pod precisa continuar
funcionando sem o cache e o cluster precisa ter capacidade para a explosão de
downloads causada por uma limpeza ou expiração.

## Relações

- [Docker executor](docker-executor.md) descreve o modelo baseado em Docker
  Engine.
- [Cache de GitLab Runner](cache.md) descreve o backend compartilhado.
- [Taints](../../kubernetes/scheduling/taints.md) e [tolerations](../../kubernetes/scheduling/tolerations.md)
  ajudam a reservar nós para workloads de CI.

## Fonte primária

- [GitLab Runner Kubernetes executor](https://docs.gitlab.com/runner/executors/kubernetes/)
- [GitLab Runner Helm chart](https://docs.gitlab.com/runner/install/kubernetes_helm_chart_configuration/)
