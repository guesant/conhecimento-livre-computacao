# Revogação de certificados

Revogação invalida um certificado antes da data de expiração quando a chave
privada foi exposta, a identidade mudou, a emissão foi incorreta ou a política
exige retirada antecipada.

## CRL e OCSP

Uma CRL publica uma lista assinada de certificados revogados. O cliente precisa
obter e verificar a lista, que pode ser grande ou ficar desatualizada entre
publicações.

OCSP permite consultar o estado de um certificado individual. Isso reduz a
resposta, mas cria dependência de disponibilidade, privacidade e latência do
respondedor. Stapling permite que o servidor entregue uma prova recente junto
com a negociação TLS.

## Limitações

Nem todo cliente verifica revogação de forma obrigatória e nem todo ambiente
consegue alcançar o respondedor. Revogar não substitui rotação da chave
comprometida: uma nova chave e um novo certificado ainda precisam ser emitidos
e propagados.

## Relações

- [OCSP](ocsp.md) aprofunda a consulta de estado.
- [Cadeia de certificados](certificate-chain.md) valida a autoridade emissora.
- [Certificado X.509](certificate.md) explica o lifecycle completo.

## Fontes primárias

- [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280)
- [RFC 6960](https://www.rfc-editor.org/rfc/rfc6960)
