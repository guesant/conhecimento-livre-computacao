# Service

Service fornece um endpoint lógico para um conjunto de Pods. Ele desacopla o
cliente dos IPs efêmeros dos Pods e permite que o Kubernetes mantenha a
associação entre selector, Endpoints ou EndpointSlices e o modo de exposição
escolhido.

## Seleção e descoberta

Um Service com selector observa labels e cria objetos de endpoints para os
Pods correspondentes. Readiness influencia quais endpoints recebem tráfego.
Um Service sem selector pode representar um destino externo ou uma associação
gerenciada de outra forma, mas perde a descoberta automática por labels.

DNS interno resolve o nome do Service para um endereço estável. O DNS não
prova que há Pods prontos e não substitui timeout, retry ou circuit breaking
no cliente.

## Tipos de exposição

`ClusterIP` expõe dentro do cluster. `NodePort` abre uma porta em cada nó
elegível. `LoadBalancer` pede integração com um provedor de balanceamento.
`ExternalName` publica um alias DNS e não cria proxy ou healthcheck local.
Gateway API e Ingress tratam HTTP e outros protocolos na borda, acima do
endpoint lógico do Service.

## Relações

- [Pod](pod.md) fornece os endpoints potenciais.
- [Ingress](../networking/ingress.md) e [Gateway API](../../gateway-api.md)
  publicam rotas para Services.
- [NetworkPolicy](../networking/network-policy.md) controla conectividade,
  não seleção de endpoints.

## Fonte primária

- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
