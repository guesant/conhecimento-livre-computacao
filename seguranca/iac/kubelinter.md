# KubeLinter

KubeLinter analisa manifestos Kubernetes e Helm charts procurando configurações problemáticas e ausência de práticas recomendadas.

## Casos de uso

É adequado para checks específicos de workloads Kubernetes, como securityContext, probes, resources e outras propriedades do domínio.

## Boa prática

Execute sobre o material que representa o deployment efetivo e customize checks quando a política do ambiente divergir conscientemente do padrão.

## Má prática

Desabilitar uma categoria inteira porque um workload excepcional não atende à regra perde cobertura dos demais. Prefira exceções estreitas e justificadas.

## Fontes

- KubeLinter: https://docs.kubelinter.io/

## Continue por aqui

[Checkov](checkov.md) cobre um conjunto mais amplo de formatos de IaC.