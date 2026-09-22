# Calico

Calico é uma solução de networking e segurança para containers e Kubernetes. Ela suporta network policy e diferentes opções de dataplane e roteamento.

## Casos de uso

Clusters que precisam de CNI e políticas de rede, inclusive ambientes que valorizam integração com roteamento e políticas expressivas.

## Boa prática

Entenda qual dataplane e modo de rede estão sendo usados antes de comparar comportamento ou performance. Teste políticas de deny e caminhos de recuperação.

## Má prática

Tratar "Calico" como uma configuração única ignora que escolhas de dataplane e topologia mudam substancialmente o comportamento operacional.

## Fontes

- Calico documentation: <https://docs.tigera.io/calico/latest/about/>

## Continue por aqui

[CNI](index.md) explica a categoria. [Cilium](cilium.md) é outra implementação relevante.
