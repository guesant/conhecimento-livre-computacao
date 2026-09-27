# SpiceDB

SpiceDB é um serviço de autorização fina baseado em relações. Ele armazena
tuplas entre sujeitos, recursos e relações e deriva permissões a partir de um
schema. O modelo é inspirado em Zanzibar e foi projetado para responder
decisões de autorização fora do processo da aplicação.

## Modelo

Um schema declara tipos, relações e permissões. Uma tupla pode afirmar que um
usuário pertence a um grupo ou que um grupo pode visualizar um documento. A
permissão é uma expressão derivada, não necessariamente um registro explícito.

## Operação

O servidor oferece APIs para verificar permissões, escrever relações e
consultar expansão. Consistência, tokens de revisão, cache e topologia precisam
ser escolhidos de acordo com o risco de uma decisão observar estado antigo.

## Limites

SpiceDB não substitui autenticação, gerenciamento de identidade ou políticas de
negócio completas. O PEP ainda deve validar a identidade, normalizar o recurso
e aplicar a decisão no ponto protegido.

## Fontes

- [Documentação do SpiceDB](https://authzed.com/docs/spicedb/overview)
- [Schema do SpiceDB](https://authzed.com/docs/spicedb/concepts/schema)
