# Encapsulamento em rede de cluster

Encapsulamento transporta pacotes de uma rede lógica dentro de outro protocolo de rede. VXLAN e Geneve são exemplos usados em redes overlay.

## Vantagem

A rede física não precisa conhecer diretamente cada prefixo de Pod; os nós transportam tráfego encapsulado entre endpoints do overlay.

## Custo

Headers adicionais reduzem MTU efetiva e adicionam processamento. Problemas de MTU podem aparecer como conexões parcialmente funcionais e são especialmente difíceis de diagnosticar.

## Continue por aqui

[CNI](index.md) situa encapsulamento entre decisões de dataplane. [Cilium](cilium.md) suporta modos encapsulados e de roteamento nativo.