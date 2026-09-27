# Laravel Gates

Laravel Gates são closures ou métodos nomeados para decisões de autorização
relativamente pequenas. Eles recebem o usuário autenticado e os dados
necessários para decidir uma ação.

## Uso

Gates são úteis para capacidades que não pertencem naturalmente a um único
modelo. Devem ser usados no endpoint e não somente na renderização da UI.

## Limites

Regras que crescem ou que dependem de um recurso específico normalmente ficam
mais claras em uma policy. Em qualquer caso, autorização não substitui
validação de entrada.

## Fonte

- [Laravel Gates](https://laravel.com/docs/authorization#gates)
