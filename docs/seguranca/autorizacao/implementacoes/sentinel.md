# Sentinel

Sentinel é a linguagem e o framework de policy as code da HashiCorp. Ele pode
ser usado para controlar operações em produtos que integram o runtime de
políticas, incluindo fluxos de infraestrutura como código.

## Modelo

A política recebe dados da operação e retorna uma decisão conforme regras
configuradas. O ambiente define imports, funções, mocks e o modo de execução.

## Governança

Políticas Sentinel devem ter revisão, testes e uma estratégia para diferenciar
advertência de bloqueio. O modo aplicado em produção deve ser explícito e
observável.

## Fonte

- [Documentação do Sentinel](https://developer.hashicorp.com/sentinel/docs)
