# Clerk Organizations Roles

Clerk Organizations and Roles oferece membership, organizações e papéis para
aplicações que usam Clerk como camada de identidade. É uma forma de organizar
autorização administrativa e isolamento inicial entre organizações.

## Limites

Um role de organização não substitui autorização por objeto, por campo ou por
linha. O backend deve validar a organização ativa e aplicar suas próprias
policies antes de executar a operação.

## Fonte

- [Clerk Organizations](https://clerk.com/docs/organizations/overview)
