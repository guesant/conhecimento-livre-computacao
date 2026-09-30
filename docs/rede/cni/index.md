# CNI

Container Network Interface define uma especificação e um modelo de plugins para configurar conectividade de workloads. Em Kubernetes, a implementação de CNI participa da criação da rede dos Pods, mas produtos podem adicionar capacidades muito além do mínimo da especificação.

## Implementações

[Cilium](cilium.md) usa eBPF extensivamente e integra networking, policy e observabilidade. [Calico](calico.md) oferece networking e network policy com diferentes dataplanes e topologias.

## Boa prática

Compare implementações pelas necessidades reais: dataplane, policy, observabilidade, encapsulamento/roteamento, operação e compatibilidade. Não escolha apenas por benchmark isolado.

## Continue por aqui

[Cilium](cilium.md) e [Calico](calico.md) possuem páginas próprias; comparações devem apontar para elas em vez de repetir suas definições.
