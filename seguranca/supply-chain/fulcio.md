# Fulcio

Fulcio é uma autoridade certificadora do ecossistema Sigstore que emite
certificados de curta duração ligados à identidade de um workflow ou usuário.

## Uso

O signer autentica numa identidade suportada, recebe um certificado temporário
e usa a chave correspondente para assinar. O consumidor verifica o certificado
e aplica uma policy sobre identidade e issuer, não apenas sobre a validade
criptográfica.

Certificados curtos reduzem o valor de uma chave vazada depois da expiração,
mas não eliminam a necessidade de revogar ou investigar um workflow
comprometido.

## Relações

- [Sigstore](sigstore.md) compõe o ecossistema.
- [Cosign](cosign.md) usa a assinatura.
- [Rekor](rekor.md) registra a evidência.

## Fonte primária

- [Fulcio](https://docs.sigstore.dev/certificate_authority/overview/)
