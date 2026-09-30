# RRSIG

RRSIG é o registro DNSSEC que carrega uma assinatura sobre um RRset. Ele
identifica o tipo de registro assinado, a zona, a chave DNSKEY, o algoritmo e
os tempos de validade. Um validador usa a DNSKEY correspondente para confirmar
que o RRset não foi alterado e que veio da cadeia de confiança esperada.

## RRset e assinatura

DNSSEC assina o conjunto de registros com o mesmo nome e tipo, não uma resposta
isolada como aparece no wire format. A ordem canônica dos registros é necessária
para que assinante e validador obtenham os mesmos bytes. Um RRset que muda
precisa de uma nova assinatura antes de ser publicado de forma coerente.

Uma RRSIG possui inception e expiration. O resolver valida o horário, o nome,
o tipo, o algoritmo, a chave indicada e o conteúdo canônico. Clock drift e
assinaturas expiradas podem produzir `SERVFAIL` mesmo quando o DNS autoritativo
continua respondendo.

## Ausência autenticada

RRSIG também pode autenticar uma resposta negativa quando combinada com NSEC ou
NSEC3. A ausência de um nome ou tipo não é provada por uma lista vazia: o
validador precisa verificar o intervalo assinado que demonstra a inexistência.

## Operação

A zona deve publicar RRSIG durante a janela em que os dados podem estar em
cache. Configure refresh e validade de modo que uma falha de assinatura não
torne toda a zona inválida antes que o operador consiga recuperar o signer.
Monitore expiração iminente, diferença de relógio, algoritmo e cobertura dos
RRsets.

## Relações

- [DNSKEY](dnskey.md) fornece a chave pública.
- [DNSSEC](dnssec.md) define a cadeia de validação.
- [NSEC](https://www.rfc-editor.org/rfc/rfc4034) permite ausência autenticada.

## Fontes primárias

- [RFC 4034, DNSSEC resource records](https://www.rfc-editor.org/rfc/rfc4034)
- [RFC 4035, DNSSEC protocol modifications](https://www.rfc-editor.org/rfc/rfc4035)
- [RFC 6781, DNSSEC operational practices](https://www.rfc-editor.org/rfc/rfc6781)
