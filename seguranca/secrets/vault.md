# HashiCorp Vault

Vault é um secret store centralizado para valores sensíveis, políticas de
acesso, auditoria e credenciais dinâmicas. Ele cifra os dados em repouso e
exige um processo de unseal antes de servir segredos.

## Modelo operacional

Uma inicialização gera material de unseal e um token inicial. Depois de um
reinício, operadores ou um mecanismo de auto-unseal precisam fornecer o
material necessário para recuperar a chave interna. O token root inicial deve
ser tratado como credencial de bootstrap, não como identidade de uso diário.

O acesso normal deve usar políticas com menor privilégio e uma identidade
específica do workload. A autenticação Kubernetes pode validar o token
projetado de uma ServiceAccount, evitando distribuir uma senha permanente ao
operator ou à aplicação.

## Armazenamento e disponibilidade

O Integrated Storage usa Raft para manter cópias replicadas e eleger um
líder. Três réplicas toleram a perda de uma sem perder quorum; cinco toleram a
perda de duas. Cada réplica ainda precisa estar destravada antes de participar
do cluster.

Auto-unseal pode usar um KMS externo, mas desloca a responsabilidade para a
política que autoriza o Vault a usar aquela chave. Não elimina a necessidade
de proteger a identidade do Vault nem de manter backups verificáveis.

## Quando usar

Vault é adequado quando múltiplos consumidores precisam de políticas
centralizadas, auditoria, rotação ou credenciais dinâmicas. Em ambientes
pequenos, SOPS com age ou um secret store mais simples pode reduzir o custo
operacional.

## Relações

[External Secrets Operator](external-secrets.md) pode materializar valores do
Vault como Secrets Kubernetes. [Auto-unseal e KMS](auto-unseal.md) detalha a
dependência externa usada durante a inicialização.

## Fonte primária

- [Documentação oficial do Vault](https://developer.hashicorp.com/vault/docs)
