# AccessControl

AccessControl é uma biblioteca de autorização para Node.js que modela papéis,
ações, recursos e grants. Ela se encaixa no processo da aplicação e produz
decisões locais.

## Uso

É adequada para RBAC e permissões de recursos em aplicações que conseguem
carregar todos os grants necessários localmente. A política deve permanecer
separada do controller e coberta por testes.

## Limites

Não é um PDP distribuído nem um sistema de identidade. Para decisões
compartilhadas por vários serviços, a replicação dos grants precisa ser
tratada explicitamente.

## Fonte

- [AccessControl](https://onury.io/accesscontrol/)
