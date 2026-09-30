# Registros DNS

Um registro DNS associa nome, tipo, classe, TTL e conteúdo. O tipo determina como um
resolver interpreta o valor e quais consultas podem depender dele. O nome do registro
pode ser o apex da zona, um subdomínio, um nome de serviço ou um nome especial com
underscore, como `_dmarc.example.com`.

A lista abaixo cobre os tipos padronizados e operacionais mais importantes. A
[IANA mantém o registro oficial de RRTYPEs](https://www.iana.org/assignments/dns-parameters),
que também inclui tipos históricos, experimentais, privados e tipos usados por
extensões específicas. "Todos os tipos" não é uma lista imutável: o registro oficial
é a autoridade quando uma implementação suportar um tipo que não apareça nesta página.

## Endereçamento e aliases

| Tipo | Uso |
| --- | --- |
| `A` | associa um nome a um endereço IPv4. |
| `AAAA` | associa um nome a um endereço IPv6. |
| `CNAME` | cria um alias para outro nome canônico. |
| `DNAME` | redireciona uma árvore de nomes para outra árvore. |
| `ALIAS`, `ANAME` e CNAME flattening | extensões ou comportamentos de provedores para responder no apex; não são equivalentes universais ao `CNAME` padronizado. |

`CNAME` não deve coexistir com outros dados no mesmo nome conforme as regras do DNS.
Um apex normalmente precisa publicar `SOA` e `NS`, por isso não pode simplesmente ser
um `CNAME` em servidores autoritativos tradicionais. Recursos de provedor que simulam
um alias no apex precisam ser avaliados pela documentação do próprio provedor.

## Autoridade e delegação

| Tipo | Uso |
| --- | --- |
| `SOA` | identifica a autoridade da zona, o serial e temporizadores de atualização, retry, expire e TTL mínimo conforme a semântica atual. |
| `NS` | informa servidores autoritativos para uma zona ou delegação. |
| `DS` | publica, na zona pai, a âncora que liga a delegação ao DNSSEC da zona filha. |
| `CDS` | sinaliza alteração ou remoção de `DS` pelo mecanismo automatizado de publicação suportado pela cadeia de confiança. |
| `CDNSKEY` | sinaliza a chave DNSSEC que pode ser usada para atualizar o `DS` na zona pai. |

`NS` e `SOA` descrevem autoridade. Eles não são registros de endereço para clientes.
Os nomes apontados por `NS` normalmente também precisam de `A` ou `AAAA`, e o registro
de endereço publicado na zona pai pode ser um glue record quando o servidor de nomes
está dentro da própria zona delegada.

## E-mail e localização de serviços

| Tipo | Uso |
| --- | --- |
| `MX` | informa os servidores que recebem e-mail para o domínio, com prioridade numérica. |
| `SRV` | publica serviço, protocolo, prioridade, peso, porta e alvo, normalmente em um nome como `_service._proto.example.com`. |
| `NAPTR` | descreve regras de transformação ou descoberta de serviços, usado por sistemas como ENUM e algumas arquiteturas de descoberta. |
| `TLSA` | associa material de autenticação TLS a um nome e porta quando DANE é usado. |
| `URI` | publica um URI para um serviço ou recurso. |
| `SVCB` | publica parâmetros de conexão e alternativas de serviço. |
| `HTTPS` | variante de `SVCB` destinada à descoberta de serviços HTTPS. |

`MX` aponta para nomes de servidores, não para endereços IP. O cliente resolve o alvo
do `MX` usando `A` e `AAAA`. Um `MX` ausente não significa necessariamente que o
domínio não possa enviar e-mail, mas impede a entrega normal como domínio receptor.

## Texto, verificação e políticas

| Tipo | Uso |
| --- | --- |
| `TXT` | carrega texto estruturado ou arbitrário, usado por SPF, DKIM, DMARC, ACME DNS-01 e verificações de propriedade. |
| `CAA` | limita as autoridades certificadoras autorizadas a emitir certificados para o domínio. |
| `OPENPGPKEY` | publica uma chave OpenPGP associada a um endereço, conforme a especificação adotada pelo cliente. |
| `SMIMEA` | publica associação de certificado ou chave S/MIME, conforme DANE para S/MIME. |

O conteúdo de `TXT` não tem uma semântica única. SPF, DKIM e DMARC usam formatos
diferentes e nomes diferentes: SPF costuma usar o apex do domínio, DKIM usa um seletor
como `selector._domainkey`, e DMARC usa `_dmarc`. O texto sozinho não prova que uma
política está correta; é necessário testar a avaliação feita pelo receptor.

## DNSSEC e integridade

| Tipo | Uso |
| --- | --- |
| `DNSKEY` | publica chaves usadas para assinar ou validar a zona DNSSEC. |
| `RRSIG` | contém a assinatura de um conjunto de registros. |
| `NSEC` | prova a inexistência de nomes ou tipos em uma zona assinada. |
| `NSEC3` | oferece prova de inexistência com hashing dos nomes, conforme a política escolhida. |
| `NSEC3PARAM` | publica parâmetros usados por `NSEC3`. |
| `DS` | liga a chave da zona filha à cadeia de confiança da zona pai. |

Esses registros não são configurados de forma independente. A zona precisa publicar
uma cadeia coerente, com chaves, assinaturas, relação pai e filho e períodos de
validade compatíveis. Um `DNSKEY` sem `DS` no pai não cria, sozinho, uma cadeia de
confiança pública.

## Resolução reversa e inventário

| Tipo | Uso |
| --- | --- |
| `PTR` | associa um endereço IP a um nome em uma zona reversa, como `in-addr.arpa` ou `ip6.arpa`. |
| `A6` | tipo histórico de endereçamento IPv6, substituído por `AAAA`. |
| `HINFO` | informação histórica sobre hardware e sistema operacional de um host. |
| `LOC` | posição geográfica de um recurso, quando publicada e suportada. |
| `EUI48` e `EUI64` | associa identificadores de interface a nomes, conforme os usos padronizados. |

Um `PTR` não é publicado na zona direta do domínio. A autoridade da zona reversa
normalmente pertence ao provedor que delega o bloco IP ou à organização que recebeu a
delegação reversa.

## Registros de infraestrutura do protocolo

| Tipo | Uso |
| --- | --- |
| `OPT` | pseudo-registro do EDNS, usado para transportar opções da consulta; não é persistido em uma zona como um registro comum. |
| `TSIG` | autentica mensagens DNS entre participantes que compartilham uma chave, usado em transferências e atualizações. |
| `TKEY` | negocia ou distribui chaves para autenticação de mensagens DNS em cenários específicos. |
| `SIG(0)` | assina mensagens DNS individuais, diferente da assinatura de dados de zona feita por DNSSEC. |
| `IXFR` e `AXFR` | não são RRTYPEs de dados; são mecanismos de transferência de zona consultados por operações de servidor. |

Alguns tipos históricos, como `MD`, `MF`, `MB`, `MG`, `MR`, `NULL`,
`WKS` e `MINFO`, aparecem no registro da IANA, mas não devem ser escolhidos para uma configuração nova
sem uma exigência explícita da aplicação. A existência de um RRTYPE no registro não
significa que ele seja interoperável ou recomendado para uso geral.

## Diagnóstico

Use `dig nome tipo` e observe resposta, authority section, TTL e flags. Para consultar
tipos que exigem escaping ou nomes especiais, use o nome completo quando necessário, por
exemplo `dig TXT _dmarc.example.com`.

Compare o autoritativo com o resolver recursivo para separar erro de publicação de
cache. Um registro pode estar correto e ainda não aparecer em todos os clientes durante
sua validade de cache. Para e-mail, valide também a cadeia de `MX`, o reverse DNS, os
registros de autenticação e o comportamento de um receptor real.

## Relações

- [Zona DNS](zone.md) define onde o registro é administrado.
- [Servidor autoritativo](authoritative.md) publica os dados.
- [Resolver](resolver.md) responde a clientes e mantém cache.
- [Reverse DNS](reverse-dns.md) explica zonas reversas e registros PTR.
- [DNSSEC](dnssec.md) explica chaves, assinaturas e prova de inexistência.
- [SMTP](../email/smtp.md), [POP3](../email/pop3.md) e [IMAP](../email/imap.md)
  explicam o transporte e o acesso às caixas de correio.
- [DKIM](../email/dkim.md), [SPF](../email/spf.md) e [DMARC](../email/dmarc.md)
  explicam autenticação e política de e-mail.

## Fontes primárias

- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)
- [RFC 2181](https://www.rfc-editor.org/rfc/rfc2181)
- [IANA, DNS parameters](https://www.iana.org/assignments/dns-parameters)
- [RFC 6895, DNS IANA considerations](https://www.rfc-editor.org/rfc/rfc6895)
