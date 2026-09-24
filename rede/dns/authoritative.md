# Servidor DNS autoritativo

Um servidor autoritativo responde por uma ou mais zonas e retorna os dados
publicados para os nomes sob sua responsabilidade. Ele não precisa consultar
a raiz ou um TLD para responder por uma zona que possui.

## Dados e delegação

A zona possui um SOA, servidores NS e registros de dados. A zona pai delega
autoridade por NS e pode publicar glue quando o nameserver está dentro do
próprio domínio delegado.

Um autoritativo deve responder de forma previsível, manter serial e
replicação coerentes e estar disponível nos servidores publicados pela
delegação. Um resolver pode cachear a resposta conforme TTL, mas a autoridade
continua sendo a fonte do dado.

## Escolha

BIND, PowerDNS e outros servidores podem cumprir o papel autoritativo. A
decisão considera backend de zona, automação, DNSSEC, operação, separação de
recursão e integração com provedores.

Não misture recursão pública com autoridade sem compreender o raio de abuso e
as políticas de acesso.

## Relações

- [Resolver](resolver.md) consulta a autoridade.
- [Zona DNS](zone.md) descreve o conjunto administrado.
- [Registros DNS](records.md) define os dados publicados.

## Fontes primárias

- [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035)
