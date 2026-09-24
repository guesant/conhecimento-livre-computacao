# OCSP

Online Certificate Status Protocol, OCSP, permite consultar se um certificado
está good, revoked ou unknown conforme a resposta assinada do serviço
responsável pela autoridade emissora.

## Fluxo

O cliente envia ao respondedor a identificação do certificado e da CA. O
respondedor retorna uma resposta assinada com o estado e o período de validade
da informação. OCSP stapling permite que o servidor apresente essa resposta no
handshake sem exigir que cada cliente consulte o respondedor diretamente.

## Trade-offs

Consulta direta acrescenta latência, dependência de rede e possibilidade de
vazar quais certificados o cliente está verificando. Stapling reduz esses
custos, mas exige que o servidor renove a prova e trate a ausência de uma
resposta recente conforme a política do cliente.

OCSP não remove a necessidade de emitir novo certificado quando a chave foi
comprometida.

## Relações

- [Revogação](revocation.md) compara CRL e OCSP.
- [TLS](../tls/index.md) transporta a identidade e pode usar stapling.
- [Certificado X.509](certificate.md) define a identidade consultada.

## Fonte primária

- [RFC 6960](https://www.rfc-editor.org/rfc/rfc6960)
