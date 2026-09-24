# Provider GKE

O provider Google Cloud administra recursos do Google Cloud, incluindo clusters Google Kubernetes Engine. O cluster GKE é apenas um recurso dentro de uma superfície maior que também inclui rede, IAM, projeto, registros e armazenamento.

## Cuidados

Separe o state do cluster do state de workloads que o GitOps administra. Não faça o OpenTofu e o Argo CD disputarem os mesmos objetos Kubernetes. Use contas de serviço e permissões por projeto com escopo mínimo.

## Relações

O provider Google administra o cluster e os serviços de suporte; os objetos executados nele pertencem ao ciclo de vida de [Kubernetes](../../distribuicoes-kubernetes.md) e do GitOps, conforme a arquitetura escolhida.

## Fonte primária

- [Google provider](https://registry.opentofu.org/providers/hashicorp/google/latest)
