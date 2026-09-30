# Plataformas de execução

Esta área organiza plataformas de execução em três níveis relacionados, mas
distintos: containers, virtualização e orquestração. Cada categoria resolve um
problema próprio e pode ser usada sem assumir uma implementação específica.

## Categorias

- [Containers](../containers/index.md) trata empacotamento, isolamento,
  runtimes, engines, imagens OCI e distribuição.
- [Virtualização](virtualizacao/index.md) trata máquinas virtuais, hypervisors,
  microVMs e containers de sistema.
- [Kubernetes](../kubernetes/index.md) trata orquestração, control plane,
  workloads, rede, armazenamento e extensibilidade.

## Containers

Namespaces, cgroups, capabilities, seccomp, filesystem e OCI são mecanismos e especificações diferentes que se combinam num runtime de container. A área [Sistemas e Linux](../sistemas/index.md) aprofunda os mecanismos do kernel; especificações OCI e runtimes explicam o empacotamento e execução.

## Orquestração

Orquestradores administram ciclo de vida de workloads em múltiplos recursos. Kubernetes é uma plataforma concreta; K3s é uma distribuição Kubernetes.

## Kubernetes

As categorias principais são workloads, rede, armazenamento, identidade/autorização, políticas, extensibilidade por operators e operação do cluster. Cada uma deve ser aprendida independentemente das ferramentas escolhidas pelo repositório.

## Continue por aqui

[Distribuições Kubernetes](../comparacoes/plataforma/distribuicoes-kubernetes.md) compara formas de empacotar a plataforma. [K3s](../k3s.md) aprofunda a distribuição usada neste projeto.

## Nuvem e hospedagem

[Nuvem e hospedagem](cloud/index.md) organiza provedores de infraestrutura, plataformas de aplicação, redes de borda e hospedagem gerenciada. A categoria separa o modelo de responsabilidade do fornecedor específico, para que uma decisão sobre AWS, Vercel, um VPS brasileiro ou hospedagem compartilhada não seja tomada com critérios incompatíveis.
