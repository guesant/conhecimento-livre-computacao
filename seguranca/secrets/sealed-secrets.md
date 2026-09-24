# Sealed Secrets

Sealed Secrets cifra um Secret para a chave pública de um controller específico.
O recurso cifrado pode ser versionado, mas só o controller com a chave privada
correspondente pode materializar o Secret no cluster.

## Escopo

A chave liga o artefato ao cluster e às regras de namespace e nome escolhidas
pelo controller. Um arquivo produzido para um ambiente não é automaticamente
utilizável em outro.

A recuperação exige backup seguro da chave privada do controller. O repositório
com os SealedSecrets não basta para reconstruir a capacidade de decifrar.

## Trade-offs

A solução integra cifragem e materialização no cluster, mas aumenta
acoplamento a controller e cluster. SOPS e age são mais portáveis entre
ambientes; secret store externo evita manter o valor no Git.

## Relações

- [SOPS e age](sops-age.md) compara outra estratégia de Git.
- [Secret](secret.md) é o objeto materializado.
- [Bootstrap](bootstrap.md) continua necessário para operar o controller.

## Fonte primária

- [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets)
