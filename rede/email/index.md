# Correio eletrônico na Internet

O correio eletrônico separa transporte, submissão, acesso à caixa e autenticação de
domínio. SMTP transporta mensagens entre agentes e também pode ser usado para
submissão autenticada. POP3 e IMAP permitem que um cliente acesse mensagens armazenadas.
DKIM, SPF e DMARC publicam e avaliam sinais de autenticidade e política, principalmente
com registros DNS.

Uma mensagem costuma atravessar mais de um componente:

1. o cliente submete a mensagem a um servidor de saída;
2. o servidor consulta o MX do domínio destinatário;
3. agentes SMTP estabelecem conexões e relays;
4. o receptor aplica SPF, DKIM, DMARC, reputação, antispam e política local;
5. o usuário acessa a caixa por IMAP ou POP3.

Essas etapas têm identidades diferentes. A autenticação do usuário na submissão não
prova que o domínio do remetente autorizou o servidor, e SPF não assina o conteúdo da
mensagem. DKIM assina conteúdo e domínio, mas não decide sozinho se a mensagem deve
ser entregue. DMARC combina resultados e publica uma política para o domínio.

## Escolha do protocolo

| Necessidade | Protocolo ou mecanismo |
| --- | --- |
| Entrega entre servidores | SMTP |
| Submissão do cliente ao servidor de saída | SMTP Submission, normalmente com autenticação e TLS |
| Caixa sincronizada em vários dispositivos | IMAP |
| Download simples para um cliente | POP3 |
| Autorização do servidor de envio por domínio | SPF |
| Assinatura criptográfica por domínio | DKIM |
| Política, alinhamento e relatórios | DMARC |

## Relações

- [SMTP](smtp.md) explica transporte e submissão.
- [POP3](pop3.md) explica download de mensagens.
- [IMAP](imap.md) explica acesso sincronizado a uma caixa.
- [DKIM](dkim.md) explica assinatura criptográfica.
- [SPF](spf.md) explica autorização por endereço de envio.
- [DMARC](dmarc.md) explica política e alinhamento.
- [Registros DNS](../dns/records.md) explica MX, TXT, TLSA, SRV e outros registros
  usados em e-mail.

## Fontes

- [RFC 5321, SMTP](https://www.rfc-editor.org/rfc/rfc5321)
- [RFC 9051, IMAP4rev2](https://www.rfc-editor.org/rfc/rfc9051)
- [RFC 1939, POP3](https://www.rfc-editor.org/rfc/rfc1939)
- [RFC 6376, DKIM](https://www.rfc-editor.org/rfc/rfc6376)
- [RFC 7208, SPF](https://www.rfc-editor.org/rfc/rfc7208)
- [RFC 7489, DMARC](https://www.rfc-editor.org/rfc/rfc7489)
