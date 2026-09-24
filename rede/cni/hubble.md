# Hubble

Hubble é a camada de observabilidade de rede associada ao Cilium. Ele usa os dados produzidos pelo dataplane para apresentar fluxos e decisões de policy.

## Caso de uso

Hubble ajuda a responder quais endpoints se comunicaram, se um fluxo foi permitido ou negado e qual identidade/policy participou da decisão.

## Limite

Ele observa a rede e metadados disponíveis nesse nível. Não substitui instrumentação de negócio, logs de aplicação ou distributed tracing.

## Continue por aqui

[Cilium](cilium.md) situa Hubble dentro do produto e [observabilidade](../../observabilidade/index.md) cobre o domínio mais amplo.
