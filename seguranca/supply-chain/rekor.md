# Rekor

Rekor é um transparency log para registrar assinaturas, atestações e
proveniência. O log permite verificar que uma entrada foi publicada e detectar
alterações posteriores na história observada.

## Verificação

Uma entrada de transparência não substitui a verificação da assinatura. O
consumidor ainda precisa validar o artefato, o digest, a identidade e a policy.
O valor do log está em tornar a publicação observável e auditável.

## Relações

- [Sigstore](sigstore.md) usa transparência.
- [Cosign](cosign.md) publica e consulta assinaturas.
- [Proveniência](provenance.md) descreve o processo de build.

## Fonte primária

- [Rekor](https://docs.sigstore.dev/logging/overview/)
