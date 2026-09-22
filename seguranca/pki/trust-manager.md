# trust-manager

trust-manager é um controller Kubernetes para distribuir bundles de certificados confiáveis a namespaces e workloads. Seu problema é trust distribution, não emissão de certificados.

## Casos de uso

Quando múltiplas aplicações precisam confiar na mesma CA privada, um Bundle pode manter material de confiança sincronizado sem cópias manuais independentes.

## Boa prática

Mantenha a fonte de confiança explícita, limite destinos ao necessário e planeje sobreposição durante rotação de CA para evitar quebrar consumidores.

## Má prática

Copiar manualmente a mesma CA para dezenas de namespaces cria drift. No outro extremo, distribuir toda CA interna para todo workload sem necessidade amplia confiança além do necessário.

## Fontes

- trust-manager documentation: https://cert-manager.io/docs/trust/trust-manager/

## Continue por aqui

[step-ca](step-ca.md) pode emitir certificados; trust-manager distribui âncoras de confiança.