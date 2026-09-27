# Ory Keto

Ory Keto é um servidor de permissões da Ory para autorização baseada em
relações. Ele separa a decisão de autorização do serviço de identidade e pode
ser usado por aplicações que precisam de permissões por objeto.

## Modelo

O modelo descreve relações entre sujeitos e recursos. Uma consulta verifica se
uma relação ou permissão está presente para um sujeito, uma ação e um recurso.
O schema deve ser tratado como contrato versionado, pois mudanças alteram o
significado das decisões existentes.

## O que não é

Keto não é um provedor geral de login. Ory Kratos trata identidade e Ory Hydra
trata OAuth 2.0 e OpenID Connect. Keto trata permissões.

## Fonte

- [Documentação do Ory Keto](https://www.ory.sh/keto/docs/)
