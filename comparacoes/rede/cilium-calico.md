# Cilium e Calico

Cilium e Calico podem fornecer networking e policy em Kubernetes. A comparação útil começa pelo dataplane e pelas capacidades necessárias, não por uma classificação absoluta.

## Cilium

Cilium usa eBPF extensivamente e integra recursos de networking, policy e observabilidade. Pode assumir responsabilidades adicionais como kube-proxy replacement e recursos de service mesh.

## Calico

Calico oferece networking e policy com diferentes opções de dataplane e forte histórico de integração com roteamento e políticas Kubernetes.

## Critérios

Considere kernel e plataforma suportados, modo de roteamento/encapsulamento, política necessária, observabilidade, experiência da equipe, integração com cloud, upgrades e quais responsabilidades adicionais deseja concentrar na CNI.

## Concentração versus separação

Usar Cilium para CNI, observabilidade de rede e partes de service mesh reduz número de produtos, mas concentra responsabilidades. Usar componentes separados pode aumentar peças móveis e também tornar fronteiras mais explícitas.

Nenhum modelo é universalmente superior.

## Anti-pattern

Trocar CNI por um benchmark sintético sem reproduzir MTU, encapsulamento, policies e tráfego real é uma decisão frágil. Migração de CNI afeta uma camada fundamental do cluster e merece plano próprio.

## Continue por aqui

[CNI](../../rede/cni/index.md), [Cilium](../../rede/cni/cilium.md) e [Calico](../../rede/cni/calico.md) aprofundam cada nível.