# Cosign

Cosign assina e verifica artefatos de container e outras declarações usando o
ecossistema Sigstore. A assinatura pode ser associada ao digest e armazenada
junto ao registry ou em uma transparência compatível.

## Modelo

A verificação precisa conhecer a identidade esperada do signer, o issuer e o
digest do artefato. Verificar apenas que existe uma assinatura não confirma
que ela veio do workflow correto.

Chaves podem ser gerenciadas diretamente ou por um fluxo keyless. O modelo
keyless usa identidade temporária e registro de transparência, reduzindo
chaves privadas de longa duração, mas adicionando dependências de identidade e
serviços.

## Relações

- [Sigstore](sigstore.md) apresenta o ecossistema.
- [Fulcio](fulcio.md) emite certificados de identidade.
- [Rekor](rekor.md) registra eventos de transparência.
- [Pinagem por digest](../../pinagem-por-digest-e-hash.md) identifica o artefato.

## Fonte primária

- [Cosign](https://docs.sigstore.dev/cosign/signing/signing_with_containers/)
