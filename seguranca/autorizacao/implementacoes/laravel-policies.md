# Laravel Policies

Laravel Policies agrupam regras de autorização para um modelo ou recurso. Elas
podem proteger operações como visualizar, criar, atualizar, remover e restaurar.

## Operação

Controllers, requests e policies devem ter responsabilidades distintas. A
policy decide; a consulta precisa filtrar o conjunto; o serviço de aplicação
coordena a operação.

## Limites

Uma policy não deve ser tratada como filtro automático de toda consulta. A
aplicação precisa impedir que um usuário leia ou altere um objeto fora de seu
tenant.

## Fonte

- [Laravel Authorization](https://laravel.com/docs/authorization#creating-policies)
