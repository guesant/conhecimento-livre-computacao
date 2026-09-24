# Pod

Pod é a menor unidade que o Kubernetes agenda e executa. Ele agrupa um ou
mais containers que compartilham namespace de rede, volumes montados e parte
do contexto de execução. O Pod existe para representar uma unidade de
co-localização e não para ser um substituto genérico de uma máquina virtual.

## Modelo de lifecycle

O scheduler vincula o Pod a um nó. O kubelet desse nó cria os containers,
monta volumes, executa probes e reporta o estado para o API server. Um Pod
normalmente é substituível: se o nó falha ou a identidade do workload muda,
outro Pod pode ser criado com um nome e um endereço diferentes.

Um container principal e sidecars podem compartilhar filesystem por volumes e
podem conversar por `localhost`, mas isso cria acoplamento de lifecycle e de
recursos. Colocar processos no mesmo Pod só faz sentido quando eles precisam
de co-localização ou de uma interface de execução compartilhada.

## O que não é

Pod não é um controller, não mantém réplicas sozinho e não fornece endereço
estável para clientes. [Deployment](deployment.md), [StatefulSet](statefulset.md)
e [DaemonSet](daemonset.md) criam Pods por meio de controllers. [Service](service.md)
fornece descoberta estável para um conjunto de Pods.

## Recursos e segurança

Requests influenciam scheduling e limits influenciam o comportamento de
runtime. Probes, SecurityContext, ServiceAccount e volumes fazem parte do
contrato do Pod, mas representam preocupações distintas. Um Pod `Running` não
prova que a aplicação está pronta para receber tráfego.

## Relações

- [ReplicaSet](replicaset.md) mantém uma quantidade de Pods.
- [Namespace](namespace.md) fornece isolamento lógico de objetos.
- [Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
  define estados e transições observáveis.

## Fonte primária

- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
