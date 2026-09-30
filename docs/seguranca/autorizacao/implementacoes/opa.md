# Open Policy Agent

Open Policy Agent, OPA, é um policy decision engine de propósito geral. Ele
separa a decisão de políticas da aplicação e pode ser usado em APIs, pipelines,
proxies, Kubernetes e infraestrutura como código.

## Rego

As políticas são escritas em Rego e avaliadas contra um documento de entrada.
O resultado pode ser uma decisão booleana, um conjunto de violações ou dados
derivados. A aplicação define o contrato de entrada e a forma de aplicar o
resultado.

## Limites

OPA não é um sistema de identidade nem um mecanismo automático de enforcement.
Políticas precisam de testes, versionamento, revisão e controle de distribuição.
Um OPA indisponível exige uma decisão explícita sobre fail-open ou fail-closed.

## Fontes

- [Documentação do OPA](https://www.openpolicyagent.org/docs/latest/)
- [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/)
