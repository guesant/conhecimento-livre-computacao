# Azure RBAC

Azure RBAC concede acesso a recursos Azure por meio de definições de papel,
atribuições, escopo e principal. O escopo pode ser gerenciamento, subscription,
resource group ou recurso individual.

## Operação

O papel deve ser escolhido pelo conjunto mínimo de ações necessárias. Herança
de escopo facilita administração, mas pode produzir acesso amplo sem revisão
das atribuições superiores.

## Relações

Azure RBAC controla o plano de gerenciamento e outros recursos integrados. Ele
não substitui as permissões internas de um banco, aplicação ou sistema
operacional.

## Fonte

- [Azure RBAC](https://learn.microsoft.com/azure/role-based-access-control/overview)
