# Permit.io

Permit.io é uma plataforma de autorização como serviço que oferece componentes
para RBAC, ABAC e autorização fina. Ela separa a modelagem de permissões da
implementação dos pontos de enforcement.

## Arquitetura

O sistema administra políticas e pode fornecer um PDP remoto ou um componente
de decisão próximo da aplicação. A integração precisa registrar o modelo de
tenant, os recursos, as ações e a origem dos atributos.

## Trade-offs

Uma plataforma reduz código repetido e melhora governança, mas adiciona
dependência operacional. Defina cache, timeout, fail-closed e processo de
rollback antes de depender da decisão remota em caminhos críticos.

## Fonte

- [Documentação do Permit.io](https://docs.permit.io/)
