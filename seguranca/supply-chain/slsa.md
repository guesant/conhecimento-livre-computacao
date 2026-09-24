# SLSA

SLSA é um framework de níveis e requisitos para aumentar a confiança na
proveniência e integridade de artefatos de software. Ele organiza práticas de
origem, construção e distribuição em vez de ser um scanner único.

## Proveniência

A proveniência descreve fonte, builder, parâmetros e artefato produzido. Uma
verificação útil precisa ligar a declaração ao digest do resultado e verificar
a identidade do produtor.

SLSA não prova que o código é seguro ou que a dependência não possui
vulnerabilidade. Ele ajuda a responder de onde o artefato veio e como foi
produzido.

## Relações

- [Proveniência](provenance.md) registra origem e processo.
- [Attestation](attestation.md) transporta uma afirmação verificável.
- [Assinatura de artefatos](artifact-signing.md) protege integridade e origem.
- [SBOM](sbom.md) lista componentes.

## Fonte primária

- [SLSA](https://slsa.dev/spec/v1.0/)
