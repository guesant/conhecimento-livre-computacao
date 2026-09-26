# Containers e Kubernetes

Esta área organiza o caminho de abstração desde isolamento de processos e imagens OCI até orquestração, Kubernetes e implementações concretas.

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
