# Policy Decision Point

Policy Decision Point, PDP, é o componente que avalia uma requisição contra as
policies e retorna uma decisão. Ele não precisa executar a operação protegida.

## Localização

O PDP pode viver na aplicação, em um sidecar, em um gateway ou em um serviço
compartilhado. A posição altera latência, disponibilidade, consistência e
governança.

## Contrato

A entrada deve conter subject, resource, action e contexto confiável. A saída
deve ser determinística, observável e associada à versão da policy.
