# Ory Hydra

Ory Hydra é um servidor OAuth 2.0 e OpenID Connect. Ele emite tokens e delega
autenticação do usuário a um login provider, mas não é um motor geral de
autorização por recurso.

## Fronteira

Hydra responde se um cliente pode obter um token conforme o fluxo configurado.
O serviço protegido ainda deve validar o token e decidir se o subject pode
executar a ação solicitada.

## Fonte

- [Documentação do Ory Hydra](https://www.ory.sh/hydra/docs/)
