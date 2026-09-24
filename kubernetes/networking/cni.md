# CNI no Kubernetes

Container Network Interface, CNI, é uma especificação e um ecossistema de
plugins para configurar interfaces e conectividade de containers. No
Kubernetes, o kubelet ou runtime invoca o plugin para conectar Pods à rede e
remover essa configuração quando o Pod termina.

## Responsabilidade

Um CNI pode criar interfaces, atribuir endereços, configurar rotas,
encapsulamento, bridges, eBPF e políticas. A forma como ele realiza essas
funções varia entre implementações. CNI não é sinônimo de service discovery,
Ingress ou NetworkPolicy, embora um mesmo projeto possa implementar várias
dessas capacidades.

## Failure domains

Falhas de IPAM, plugin binário, daemon do CNI, rota, MTU e policy têm sintomas
parecidos, como Pod sem conectividade. Diagnóstico precisa separar criação da
interface, endereço, rota, DNS, acesso ao Service e tráfego externo.

O CNI também define dependências no lifecycle do nó. Se o agente não estiver
pronto, Pods podem ficar em `ContainerCreating` mesmo com imagem e volume
corretos.

## Relações

- [NetworkPolicy](network-policy.md) aplica isolamento quando suportado.
- [Service](../core/service.md) fornece descoberta e balanceamento lógico.
- [Cilium](../../rede/cni/cilium.md) e [Calico](../../rede/cni/calico.md) são
  implementações com modelos diferentes.

## Fontes primárias

- [CNI specification](https://github.com/containernetworking/cni)
- [Kubernetes cluster networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
