# Infisical

Infisical é uma plataforma de gerenciamento de segredos com backend
centralizado, interface de equipes, versionamento e operadores para
sincronização com workloads. Pode ser usada como serviço hospedado ou
auto-hospedada.

## Integração com Kubernetes

O Infisical Secrets Operator usa recursos próprios para representar a conexão,
a autenticação e o segredo estático a sincronizar. A conexão aponta para a
instância; a autenticação usa uma Machine Identity; o recurso de segredo
referencia projeto, ambiente e caminho.

Esse modelo é mais integrado à plataforma que o `ExternalSecret` genérico,
mas também cria acoplamento com a API e com o modelo de identidade do
Infisical. A troca de backend exige adaptar os recursos específicos do
operator.

## Quando usar

Infisical é adequado quando a equipe valoriza uma experiência integrada de
administração, convites, ambientes e histórico. Um operator genérico com
Vault, OpenBao ou outro backend é preferível quando portabilidade entre
provedores é requisito central.

## Relações

[External Secrets Operator](external-secrets.md) oferece uma API comum para
múltiplos backends. [Secret stores externos](../../secret-store-externo.md)
compara as arquiteturas.
