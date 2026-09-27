# Auth0 FGA

Auth0 FGA é um serviço de autorização fina baseado em relações. Ele modela
relações entre usuários, grupos, recursos e permissões derivadas, seguindo a
família de sistemas inspirada em Zanzibar.

## Modelo

O modelo separa o armazenamento de tuples da consulta de autorização. A
aplicação pergunta se um usuário pode executar uma ação sobre um recurso, sem
precisar carregar todas as relações para seu próprio banco.

## Cuidados

O schema é parte do contrato de segurança. Mudanças devem ser compatíveis,
testadas e associadas a uma estratégia para revogar acesso rapidamente.

## Fonte

- [Auth0 Fine-Grained Authorization](https://auth0.com/fine-grained-authorization)
