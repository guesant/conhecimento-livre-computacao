# DNSKEY

DNSKEY é o registro DNS que publica uma chave pública usada pelo DNSSEC. A
chave não cifra consultas nem autentica o transporte do DNS. Ela permite que um
validador verifique assinaturas RRSIG associadas a conjuntos de registros.

## KSK e ZSK

Uma zona pode usar uma Zone Signing Key, ZSK, para assinar dados da zona e uma
Key Signing Key, KSK, para assinar o DNSKEY RRset. Essa separação facilita
rotacionar a chave que assina os registros com mais frequência e publicar uma
âncora de confiança menor para a chave que autentica o conjunto DNSKEY.

Os nomes KSK e ZSK descrevem papéis operacionais, não formatos diferentes do
registro. Cada DNSKEY possui flags, protocolo, algoritmo e material de chave.
O algoritmo precisa ser suportado pelo validador e aceito pela política vigente.

## Cadeia de confiança

O parent publica um DS que referencia uma DNSKEY da child. O validador começa
em uma trust anchor, verifica o DS, encontra a DNSKEY e valida as RRSIGs. Uma
chave publicada sem DS não cria uma cadeia validada; uma chave com DS incorreto
faz a zona falhar como bogus.

## Rotação

A rotação precisa respeitar TTL, caches, sobreposição e ordem de publicação.
Primeiro a nova chave precisa estar disponível e referenciada no conjunto
assinado; depois o DS ou o conjunto de chaves do parent é alterado segundo o
procedimento da zona. Remover uma chave antes de expirar respostas antigas pode
quebrar validação em resolvers que ainda possuem dados em cache.

## Relações

- [DNSSEC](dnssec.md) explica a cadeia completa.
- [RRSIG](rrsig.md) explica a assinatura dos RRsets.
- [Registros DNS](records.md) apresenta o modelo de dados da zona.

## Fontes primárias

- [RFC 4034, DNSSEC resource records](https://www.rfc-editor.org/rfc/rfc4034)
- [RFC 6781, DNSSEC operational practices](https://www.rfc-editor.org/rfc/rfc6781)
