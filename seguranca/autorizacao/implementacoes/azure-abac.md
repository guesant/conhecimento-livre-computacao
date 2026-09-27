# Azure ABAC

Azure ABAC usa condições baseadas em atributos para refinar atribuições de
papéis. A condição é avaliada junto com o papel e o escopo da solicitação.

## Uso

ABAC pode limitar acesso por tags, caminhos, classificações ou atributos do
recurso. A taxonomia de atributos precisa ser governada para não depender de
valores que usuários possam alterar sem autorização.

## Limites

Condições de atributo não são automaticamente portáveis para outros serviços.
Documente o recurso, as chaves aceitas e o comportamento quando o atributo
estiver ausente.

## Fonte

- [Condições do Azure ABAC](https://learn.microsoft.com/azure/role-based-access-control/conditions-overview)
