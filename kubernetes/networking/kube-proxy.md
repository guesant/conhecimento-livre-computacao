# kube-proxy

kube-proxy é um componente de rede que observa Services e EndpointSlices e
programa regras no nó para encaminhar tráfego ao backend. Dependendo do modo,
usa iptables, IPVS ou outra implementação fornecida pelo ecossistema de rede.

## O que ele faz

O componente transforma a abstração de um ClusterIP e suas portas em regras
locais de encaminhamento. Ele não é o DNS do cluster, não cria Pods e não
implementa a aplicação. Os endpoints válidos ainda dependem de labels,
readiness e do controller que atualiza EndpointSlices.

## Substituição

Alguns CNIs e datapaths podem substituir kube-proxy. A substituição precisa
cobrir Service, NodePort, load balancing, session affinity e o comportamento
esperado para tráfego interno e externo. Desabilitar kube-proxy sem validar
essas capacidades deixa Services sem datapath funcional.

## Diagnóstico

Quando um Service não responde, compare DNS, ClusterIP, EndpointSlices, regras
do nó e conectividade direta com o Pod. Um Service sem endpoints não é corrigido
por kube-proxy; um endpoint correto sem regras locais indica outro problema no
datapath ou no agente do nó.

## Relações

- [Service](../core/service.md) define a abstração.
- [CNI](cni.md) pode fornecer datapath alternativo.
- [EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)
  representa backends observáveis.

## Fonte primária

- [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/)
