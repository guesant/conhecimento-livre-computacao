# DNSSEC

DNSSEC adiciona autenticação criptográfica aos dados do DNS. Seu objetivo é permitir verificar autenticidade e integridade de respostas dentro de uma cadeia de confiança; ele não cifra as consultas nem oculta os nomes consultados.

## Casos de uso

DNSSEC é relevante quando um domínio precisa reduzir o risco de respostas forjadas entre a zona assinada e validadores que verificam a cadeia. É especialmente importante compreender DS, DNSKEY, RRSIG e a delegação entre zonas.

## Boa prática

Planeje rotação de chaves e delegação antes de ativar a assinatura. Confirme que o registrador e o provedor DNS suportam o fluxo necessário e monitore expiração e consistência.

## Má prática

Publicar um DS incorreto no parent pode tornar uma zona validada inacessível. Outra confusão comum é vender DNSSEC como "DNS criptografado"; privacidade de transporte é assunto de DoT/DoH e não a função do DNSSEC.

## Fontes

- RFC 4033, DNS Security Introduction and Requirements: https://www.rfc-editor.org/rfc/rfc4033
- ICANN DNSSEC: https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en

## Continue por aqui

[Registro de domínio](registro-de-dominio.md) explica a relação administrativa com a zona parent. [mDNS](mdns.md) resolve nomes num contexto local diferente do DNS global.