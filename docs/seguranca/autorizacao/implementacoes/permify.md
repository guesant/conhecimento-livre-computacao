# Permify

Permify é uma plataforma de autorização fina baseada em relações e políticas.
Ela permite modelar tenants, tipos de recurso, relações e permissões, expondo
um serviço para decisões de autorização.

## Modelo

O modelo separa a relação armazenada, como membro de uma organização, da
permissão derivada, como editar um projeto. Essa separação evita copiar uma
lista de permissões para cada objeto.

## Uso

Permify é adequado quando várias aplicações precisam consultar a mesma política
de acesso e quando a autorização por objeto cresce além de verificações locais
simples. O schema deve ser versionado e testado junto com os consumidores.

## Limites

O serviço não resolve autenticação nem garante sozinho isolamento entre tenants.
Identificadores, cache, consistência e comportamento durante falhas continuam
sendo decisões da arquitetura.

## Fonte

- [Documentação do Permify](https://docs.permify.co/)
