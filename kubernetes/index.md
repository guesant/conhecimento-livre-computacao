# Kubernetes

Kubernetes é uma plataforma de orquestração baseada em estado desejado,
controladores e uma API. A categoria é ampla: aprender um objeto de workload
não substitui compreender o control plane, a rede, o armazenamento ou o modelo
de segurança.

## Categorias

- [Distribuições e arquitetura](../comparacoes/plataforma/distribuicoes-kubernetes.md)
  compara formas de empacotar e operar um cluster.
- [Objetos fundamentais](core/pod.md) apresenta os objetos que descrevem
  workloads, serviços, configuração e identidade.
- [Control plane](control-plane/api-server.md) explica API server, controllers,
  scheduler, kubelet, datastore e quorum.
- [Rede](networking/cni.md) explica CNI, Service, kube-proxy, Ingress,
  HTTPRoute e NetworkPolicy.
- [Scheduling](scheduling/affinity.md) explica como o scheduler escolhe nós e
  como restrições de colocação alteram essa decisão.
- [Workloads batch](recursos/index.md) reúne jobs, CronJobs e condições de
  prontidão e desligamento.
- [Segurança de workload](core/serviceaccount.md) reúne identidade, RBAC,
  SecurityContext, Secrets e políticas de acesso.
- [Extensibilidade](extensibility/crd.md) trata CRDs, operators, admission
  control e controllers.
- [Lifecycle](lifecycle/finalizers.md) trata finalizers e owner references.
- [Armazenamento](storage/persistent-volume.md) trata volumes persistentes,
  classes, CSI, modos de acesso e políticas de reclaim.
- [Empacotamento](../containers/packaging/helm.md) trata Helm e a geração de
  manifests.

## Modelo mental

O usuário publica objetos na API. Controladores observam esses objetos e
recursos dependentes, comparam o estado observado ao estado desejado e fazem
alterações graduais. Por isso, um manifesto não é um script executado uma vez:
é uma declaração que continuará sendo reconciliada.

## Fronteiras

Kubernetes não é uma implementação de container, um banco de dados ou uma
política de segurança completa. Ele coordena essas integrações por APIs e
controladores, mas a confiabilidade depende também do runtime, da rede, do
datastore, do storage, da identidade e do processo operacional.
