# Object-level authorization

Object-level authorization decide acesso a uma instância específica, não
apenas ao tipo de recurso. Por exemplo, permitir editar um projeto não implica
permitir editar todos os projetos.

## Risco

Falhas de object-level authorization produzem IDOR e exposição horizontal de
dados. A policy deve ser aplicada depois de identificar o objeto e antes de
retornar ou alterar seu conteúdo.

## Relações

Ownership, RBAC por objeto, ABAC e ReBAC podem implementar essa decisão.
