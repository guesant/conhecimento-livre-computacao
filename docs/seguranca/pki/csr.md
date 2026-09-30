# Certificate Signing Request

Uma CSR é uma solicitação de assinatura que contém uma chave pública, atributos
da identidade pretendida e uma assinatura feita com a chave privada
correspondente. A CA verifica a posse da chave antes de emitir o certificado.

A CSR não contém a chave privada. Ela pode ser criada no mesmo host que usará
a identidade e enviada à autoridade sem expor o material secreto.

## Conteúdo

O pedido pode carregar subject, SAN, usos de chave e extensões que a política
da CA aceita. A autoridade não precisa assinar tudo o que foi pedido: ela
aplica sua própria política e pode reduzir nomes, usos ou duração.

## Failure modes

Uma CSR assinada não é um certificado confiável. O consumidor ainda precisa
receber a cadeia correta e confiar na CA. Nomes fora do SAN, key usages
incompatíveis e uma chave pública diferente da chave usada no endpoint causam
falhas apesar da CSR ser formalmente válida.

## Relações

- [Certificado X.509](certificate.md) é o resultado emitido.
- [SAN](san.md) define a identidade de hostname.
- [ACME](acme.md) automatiza solicitação e renovação.

## Fonte primária

- [RFC 2986](https://www.rfc-editor.org/rfc/rfc2986)
