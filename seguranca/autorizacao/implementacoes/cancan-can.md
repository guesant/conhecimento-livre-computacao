# CanCanCan

CanCanCan é uma biblioteca de autorização para Ruby e Rails. Ela centraliza
habilidades em uma classe de abilities e oferece helpers para verificar ações
contra recursos.

## Modelo

As regras normalmente combinam usuário, papel, recurso e ação. A aplicação
deve verificar a ability no controller e também proteger consultas para não
expor objetos que o usuário não pode ler.

## Limites

Esconder botões não é enforcement. A policy precisa ser aplicada no endpoint,
na consulta e, quando necessário, na camada de domínio.

## Fonte

- [CanCanCan](https://github.com/CanCanCommunity/cancancan)
