# OpenBao

OpenBao é um secret store open source compatível com os conceitos centrais do
Vault. Ele centraliza valores, políticas, auditoria e operações de emissão ou
integração com identidades, sem transformar o cluster consumidor no local
obrigatório de armazenamento da credencial.

## Modelo de unseal

O armazenamento cifra os dados em repouso e precisa recuperar sua chave
interna antes de atender requisições. A inicialização cria material de unseal
e um token inicial; depois de um reinício, o processo precisa ser destravado
manualmente ou por auto-unseal.

Guardar as chaves de unseal dentro do mesmo cluster que o OpenBao protege cria
uma dependência circular. O material precisa ficar em outro domínio de falha,
ou a operação precisa usar um KMS externo com uma política de acesso mínima.

## Alta disponibilidade

O Integrated Storage usa Raft para replicar o estado e eleger um líder. Apenas
uma réplica recebe escritas; as demais funcionam como standbys e encaminham as
operações ao líder. Três réplicas toleram uma falha sem perder quorum. O
destravamento de cada réplica continua sendo necessário antes da participação
na eleição.

## Quando usar

OpenBao é uma opção quando a organização precisa de um backend centralizado e
quer manter uma implementação comunitária. Em ambientes de nó único ou
desenvolvimento, a complexidade pode ser maior que o benefício de centralizar
segredos.

## Relações

[External Secrets Operator](external-secrets.md) oferece a integração
declarativa com consumidores Kubernetes. [Auto-unseal e KMS](auto-unseal.md)
trata o destravamento automatizado.

## Fonte primária

- [Documentação oficial do OpenBao](https://openbao.org/docs/)
