# API gateway consumer

Consumer representa a identidade de um cliente de API no catálogo do gateway.
Ele pode ser associado a credenciais, grupos, quotas e políticas.

## Identidade

O mecanismo de autenticação precisa mapear a credencial apresentada para um
consumer sem expor segredo em logs ou headers encaminhados indevidamente.
Consumer não é necessariamente um usuário final; pode representar uma
aplicação, integração ou plano de uso.

Uma quota por consumer exige uma chave estável e política para credenciais
rotacionadas. Se a chave muda, a contagem pode separar o mesmo cliente em duas
identidades.

## Relações

- [Plugin](plugin.md) autentica e aplica políticas.
- [Route](route.md) define a API acessada.
- [Upstream](upstream.md) recebe o tráfego depois da decisão.

## Fonte primária

- [Kong consumers](https://docs.konghq.com/gateway/latest/entities/consumer/)
