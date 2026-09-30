# Casbin Rust

Casbin Rust é a implementação do modelo Casbin para aplicações Rust. Ela
permite reutilizar a separação entre model, policy, adapter e enforcer.

## Cuidados

O processo local precisa receber atributos confiáveis e usar uma policy
compatível com o modelo de dados do serviço. Em sistemas distribuídos, mudanças
de policy precisam ser propagadas e auditadas.

## Fonte

- [Casbin](https://casbin.org/docs/overview)
