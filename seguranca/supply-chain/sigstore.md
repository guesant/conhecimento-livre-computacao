# Sigstore

Sigstore é um ecossistema para assinar software com identidade verificável,
certificados temporários e transparência pública. Ele reduz a necessidade de
distribuir chaves privadas permanentes para cada workflow.

## Componentes

Fulcio emite certificados curtos ligados a uma identidade. Rekor registra
eventos em um log de transparência. Cosign assina e verifica artefatos e
atestados. A confiança depende de verificar cadeia, identidade, digest e
registro.

## Limites

Sigstore prova uma relação de assinatura e identidade, não a qualidade do
código, ausência de vulnerabilidade ou legitimidade do workflow que recebeu
permissão para publicar. Políticas de identidade e revisão do pipeline
continuam necessárias.

## Relações

- [Cosign](cosign.md) é a ferramenta de assinatura.
- [Fulcio](fulcio.md) emite identidade.
- [Rekor](rekor.md) oferece transparência.
- [SLSA](slsa.md) trata níveis de garantia da construção.

## Fonte primária

- [Sigstore](https://www.sigstore.dev/)
