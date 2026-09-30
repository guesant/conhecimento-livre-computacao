# CPU no Kubernetes

Kubernetes representa CPU como uma quantidade absoluta de tempo de processador.
Uma unidade de CPU corresponde a um core físico ou a um vCPU, conforme o tipo
de nó. A API não promete que o Pod receberá um core físico dedicado apenas
porque o manifesto contém uma quantidade de CPU.

## Millicpu

O sufixo `m` significa millicpu. `1000m` equivale a uma unidade de CPU, `500m`
equivale a 0,5 CPU e `100m` equivale a 0,1 CPU. A precisão mínima aceita é
`1m`.

Essa é uma unidade absoluta. `500m` representa aproximadamente metade do
tempo de uma CPU tanto em um nó com dois processadores lógicos quanto em um nó
com 48. Não significa metade de todos os cores do nó e não é uma porcentagem
relativa ao tamanho da máquina.

## Request

O request é a demanda usada pelo scheduler para decidir se o Pod cabe no nó.
O scheduler soma os requests dos containers e compara o resultado com a
capacidade alocável do nó. Ele não usa apenas o consumo instantâneo, porque a
decisão precisa continuar válida quando a carga aumentar.

Um request de `500m` não impede o container de usar mais CPU se houver margem e
um limite permitir. Ele representa uma reserva lógica para scheduling e um peso
de disputa no host.

## Limit

O limit é um teto de tempo de CPU aplicado pelo runtime através de cgroups. Se
o container tentar usar mais que a cota durante o período de controle, o kernel
o estrangula até a próxima janela. CPU excedente costuma produzir throttling,
não encerramento imediato do processo como ocorre com um limite de memória.

Quando request e limit são iguais e positivos, o Pod pode receber a classe de
QoS `Guaranteed` se a configuração de memória também satisfizer as regras. Isso
não equivale automaticamente a pinning de core.

## CPU Manager

O kubelet pode usar a política `static` para entregar CPUs exclusivas a
containers de Pods `Guaranteed` que peçam um número inteiro positivo de CPUs.
Essa é uma exceção importante à regra geral de compartilhamento por cgroup.
Ela exige que o nó seja configurado para isso e que o workload realmente
precise de afinidade e previsibilidade.

Requests fracionários, como `500m`, normalmente continuam no pool compartilhado.
O CPU Manager não cria capacidade e não corrige um request mal dimensionado.

## Relação com cores e sockets

O kubelet normalmente anuncia uma capacidade de CPU baseada nos processadores
que o sistema operacional do nó apresenta. A informação pode incluir
processadores lógicos derivados de SMT, e um nó virtualizado pode anunciar os
vCPUs apresentados pelo hypervisor.

Por isso, `1 CPU` no Kubernetes não deve ser interpretado como uma afirmação
universal sobre um core físico. Para entender a capacidade real, observe a
topologia do host, a VM e a configuração do kubelet. Em máquinas NUMA, também
avalie CPU Manager e Topology Manager quando a latência for relevante.

## Exemplo

```yaml
resources:
  requests:
    cpu: 250m
  limits:
    cpu: 1000m
```

Esse container participa do scheduling com uma demanda de um quarto de CPU e
pode consumir até uma CPU de tempo durante a execução. Se o nó estiver
contendido, seu peso será menor que o de um container com request maior. Se a
carga tentar ultrapassar o limite, haverá throttling.

## Diagnóstico

Compare request, limit, throttling e uso observado. Um Pod lento pode estar
limitado por CPU, por espera de I/O, por locks, por conexões ou por uma VM
subdimensionada. Aumentar o limit sem medir pode apenas transferir a contenção
para o nó.

Use `kubectl describe node` para verificar capacidade alocável e requests
agregados. Relacione métricas de throttling do cgroup com latência da aplicação
e não trate a porcentagem de uso instantânea como única evidência.

## Relações

- [Requests](requests.md) detalha a demanda usada pelo scheduler.
- [Limits](limits.md) detalha o teto aplicado pelo cgroup.
- [QoS de Pods](qos.md) explica as classes derivadas.
- [Cores](../../sistemas/cpu/cores.md) e [sockets](../../sistemas/cpu/sockets.md)
  explicam a topologia física.
- [CPU virtual no Proxmox](../../sistemas/virtualizacao/proxmox-cpu.md) explica
  a camada anterior quando o nó é uma VM.

## Fontes primárias

- [Kubernetes, resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Kubernetes, assign CPU resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/)
- [Kubernetes, CPU management policies](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/)
- [Kubernetes, topology management](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/)
