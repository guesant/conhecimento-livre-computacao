# Permit PDP

Permit PDP é o componente de decisão que avalia políticas para o ecossistema
Permit. A separação entre PDP e painel de administração permite que o serviço
consumidor consulte decisões sem conhecer a forma como as políticas são
editadas.

## Contrato

Uma chamada de decisão deve identificar principal, recurso, ação e contexto.
Respostas precisam ser tratadas como dados de segurança, com timeout, métricas,
logs sem segredos e associação à versão da política.

## Operação

O PDP deve ser dimensionado pelo volume de decisões e pela complexidade do
modelo. O comportamento durante indisponibilidade não pode ser implícito:
operações sensíveis normalmente devem negar por padrão.

## Fonte

- [Documentação do Permit](https://docs.permit.io/)
