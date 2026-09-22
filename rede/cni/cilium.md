# Cilium

Cilium é uma implementação de networking, segurança e observabilidade para ambientes como Kubernetes, construída em torno de eBPF no dataplane.

## Casos de uso

CNI para clusters Kubernetes, network policy, observabilidade de fluxos e substituição de componentes tradicionais do dataplane são usos possíveis conforme a configuração.

## Boa prática

Adote apenas os recursos que consegue operar e observar. Entenda modo de roteamento, encapsulamento, kube-proxy replacement e políticas antes de alterar defaults de dataplane.

## Má prática

Habilitar simultaneamente todos os recursos avançados porque existem aumenta superfície operacional. Mudanças de dataplane devem ser tratadas como mudanças de rede, com rollback e observabilidade.

## Fontes

- Cilium documentation: https://docs.cilium.io/

## Continue por aqui

[CNI](index.md) explica a categoria. [Calico](calico.md) é outra implementação relevante.