# Subject Alternative Name

Subject Alternative Name, SAN, declara os nomes e endereços para os quais um
certificado é válido. Clientes TLS modernos verificam o hostname no SAN em vez
de depender do Common Name.

## Tipos

Uma extensão SAN pode carregar DNS names, endereços IP, identificadores URI e
outros formatos conforme a política. O tipo precisa corresponder ao valor
consultado: um hostname não deve ser validado como se fosse um endereço IP.

Wildcards possuem escopo limitado. Um wildcard para `*.example.com` cobre um
nível sob o domínio e não deve ser tratado como autorização para
`a.b.example.com` sem regra específica.

## Diagnóstico

Confira o SAN apresentado pelo endpoint com uma ferramenta TLS e compare com o
nome usado pelo cliente. Erros comuns são nome ausente, wildcard fora do
escopo, cadeia correta para outra autoridade ou certificado antigo após
renovação.

## Relações

- [Certificado X.509](certificate.md) usa SAN no processo de validação.
- [SNI](../tls/sni.md) informa o nome desejado ao endpoint TLS.
- [ACME](acme.md) automatiza provas de controle do nome.

## Fonte primária

- [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280)
