# eBPF

eBPF é uma tecnologia do kernel Linux que permite carregar programas verificados para execução em hooks controlados do kernel.

Networking é um de seus usos, mas eBPF não é uma tecnologia exclusiva de CNI ou Kubernetes. Também aparece em observabilidade, segurança e tracing.

## Modelo

Programas eBPF são verificados antes de serem aceitos. Maps permitem compartilhar estado entre programas e espaço de usuário. Tipos de programa e hooks determinam onde a lógica pode executar.

## Relação com Cilium

[Cilium](cilium.md) usa eBPF extensivamente para networking, policy, load balancing e observabilidade. Isso não torna "eBPF" e "Cilium" sinônimos.

## Continue por aqui

[Cilium](cilium.md) é uma implementação que aplica eBPF ao domínio de rede de cluster.
