# Registros DNS

Um registro DNS associa nome, tipo, classe, TTL e conteúdo. O tipo determina
como um resolver interpreta o valor e quais consultas podem depender dele.

## Tipos frequentes

| Tipo | Uso |
| --- | --- |
| A | endereço IPv4 |
| AAAA | endereço IPv6 |
| CNAME | alias para outro nome |
| MX | entrega de e-mail |
| NS | servidor autoritativo |
| SOA | metadados da zona |
| TXT | texto para SPF, DKIM, ACME e verificações |
| SRV | serviço, protocolo, prioridade, peso, porta e alvo |
| CAA | autoridades certificadoras permitidas |
| PTR | resolução reversa de endereço para nome |

CNAME não deve coexistir com outros dados no mesmo nome conforme as regras do
DNS. Um PTR vive numa zona reversa, não na zona direta do nome original.

## Diagnóstico

Use `dig nome tipo` e observe resposta, authority section, TTL e flags.
Compare o autoritativo com o resolver recursivo para separar erro de publicação
de cache. Um registro pode estar correto e ainda não aparecer em todos os
clientes durante sua validade de cache.

## Relações

- [Zona DNS](zone.md) define onde o registro é administrado.
- [Servidor autoritativo](authoritative.md) publica os dados.
- [Resolver](resolver.md) responde a clientes e mantém cache.

## Fontes primárias

- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)
- [RFC 2181](https://www.rfc-editor.org/rfc/rfc2181)
