# Certificado X.509

Um certificado X.509 liga uma identidade a uma chave pública por meio da
assinatura de uma autoridade certificadora. Ele contém sujeito, emissor,
período de validade, usos permitidos e extensões como SAN e Key Usage.

## Verificação

O consumidor valida assinatura, cadeia até uma âncora confiável, período de
validade, hostname no SAN e uso permitido. Possuir uma assinatura válida não
prova que o certificado serve para o protocolo ou nome consultado.

A chave privada não pertence ao certificado. Ela precisa ser protegida
separadamente e nunca deve ser distribuída como parte da cadeia pública.

## Lifecycle

Emissão, distribuição, renovação, expiração e revogação são etapas distintas.
Uma aplicação pode receber o novo certificado antes da expiração do antigo para
evitar uma janela sem identidade válida.

## Relações

- [CSR](csr.md) solicita uma assinatura sem entregar a chave privada.
- [SAN](san.md) define nomes e endereços autenticados.
- [Cadeia de certificados](certificate-chain.md) liga emissor e âncora.
- [Revogação](revocation.md) trata invalidação antes da expiração.
- [TLS](../tls/index.md) usa o certificado para autenticar endpoints.

## Fontes primárias

- [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280)
- [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446)
