# AWS Verified Permissions

AWS Verified Permissions é um serviço de autorização gerenciado que usa Cedar
para avaliar políticas. A aplicação envia principal, ação, recurso e contexto,
recebendo uma decisão allow ou deny.

## Modelo

O schema define tipos, ações e relações. Policies podem ser estáticas ou
associadas a entidades e grupos. A aplicação continua sendo o PEP e deve
proteger a integridade dos dados usados na decisão.

## Trade-offs

O serviço reduz a operação do PDP, mas adiciona latência, dependência de rede
e acoplamento à nuvem. Cache e fail-closed precisam ser definidos para cada
operação sensível.

## Fonte

- [AWS Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html)
