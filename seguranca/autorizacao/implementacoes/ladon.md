# Ladon

Ladon é uma biblioteca de autorização em Go associada ao ecossistema Ory. Ela
modela políticas com subjects, resources, actions e condições para decidir se
uma operação é permitida.

## Uso

Uma biblioteca local é adequada quando o serviço possui o contexto necessário
e a decisão precisa ter baixa latência. A política deve ser versionada junto
com o código ou distribuída por um mecanismo controlado.

## Limites

Ladon não é um diretório nem um provedor de login. A aplicação deve fornecer
identidade confiável, carregar políticas corretamente e registrar decisões
relevantes.

## Fonte

- [Ladon](https://github.com/ory/ladon)
