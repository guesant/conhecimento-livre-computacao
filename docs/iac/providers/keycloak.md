# Provider Keycloak

O provider Keycloak declara realms, clients, roles, grupos, identity providers e outras configurações administrativas pela API do Keycloak. Ele permite tratar identidade como código, mas torna o state parte da superfície de segurança.

## Cuidados

Separe o realm de bootstrap dos realms administrados, use credenciais de serviço com escopo mínimo e examine o plano quanto a secrets e mudanças de acesso. Rotacionar um client secret exige coordenar consumidores, state e rollout.

## Relações

O provider administra o serviço de identidade por API; a documentação de [identidade e diretórios](../../seguranca/identidade/index.md) situa o conceito no restante da plataforma.

## Fonte primária

- [Keycloak provider](https://registry.opentofu.org/providers/keycloak/keycloak/latest)
