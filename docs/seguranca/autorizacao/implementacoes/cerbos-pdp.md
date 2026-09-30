# Cerbos PDP

Cerbos PDP é a forma de implantação do Cerbos como serviço independente de
decisão. Ele recebe uma entrada estruturada, avalia políticas e retorna o
resultado sem executar a operação protegida.

## Separação

O PEP permanece no gateway, controller ou serviço de negócio. O PDP não deve
ser confundido com o componente que busca dados privados, altera o banco ou
realiza a ação autorizada.

## Operação

Distribua o PDP perto dos consumidores, mantenha políticas versionadas e
registre a versão avaliada. Cache de decisões exige limites curtos quando
revogações precisam ter efeito rápido.

## Fonte

- [Cerbos PDP](https://www.cerbos.dev/docs/)
