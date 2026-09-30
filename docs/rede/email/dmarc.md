# DMARC

DMARC, Domain-based Message Authentication, Reporting, and Conformance, permite que
o dono de um domínio publique uma política para mensagens que alegam usar esse domínio.
O receptor compara o domínio visível no campo From com os resultados de SPF e DKIM,
avalia alinhamento e pode enviar relatórios ao domínio.

DMARC não é um terceiro mecanismo independente de assinatura. Ele usa resultados de
SPF e DKIM para estabelecer uma identidade de domínio confiável e aplicar a política
publicada.

## Registro e política

O registro DMARC fica em:

_dmarc.example.com

A política define o tratamento de mensagens sem autenticação alinhada:

| Política | Intenção |
| --- | --- |
| p=none | observar e receber relatórios sem pedir rejeição ou quarentena. |
| p=quarantine | tratar falhas como suspeitas, normalmente enviando para quarentena. |
| p=reject | rejeitar a mensagem conforme a política do receptor. |

Parâmetros podem indicar política para subdomínios, porcentagem de aplicação,
alinhamento estrito ou relaxado e destinos de relatórios agregados ou forenses. Os
destinos de relatório precisam ser tratados como informação sensível e, em alguns
casos, exigem autorização explícita entre domínios.

## Alinhamento

Uma mensagem passa DMARC quando SPF ou DKIM passa e o domínio autenticado está alinhado
com o domínio do From. Alinhamento relaxado costuma aceitar domínios organizacionais
relacionados; alinhamento estrito exige correspondência mais específica. O modo deve
ser escolhido considerando subdomínios, provedores de envio, encaminhamento e serviços
de terceiros.

## Implantação

Comece observando relatórios com p=none, catalogue todos os remetentes legítimos e
corrija SPF e DKIM. Depois teste quarentena em uma parcela controlada e só adote reject
quando os fluxos esperados estiverem cobertos. Mudanças devem considerar newsletters,
CRM, suporte, alertas, encaminhamento e sistemas que enviam em nome do domínio.

DMARC reduz spoofing do domínio, mas não substitui antispam, análise de conteúdo,
proteção de contas, TLS, política de senha ou resposta a incidentes. Uma mensagem de
um domínio legítimo pode continuar sendo maliciosa se a conta ou o serviço que assina
estiver comprometido.

## Relações

- [SPF](spf.md) autoriza origens para a identidade do envelope.
- [DKIM](dkim.md) autentica a assinatura do domínio.
- [SMTP](smtp.md) explica transporte e envelope.
- [Registros DNS](../dns/records.md) explica TXT e o nome _dmarc.

## Fontes

- [RFC 7489, DMARC](https://www.rfc-editor.org/rfc/rfc7489)
- [RFC 8616, DMARC interoperability](https://www.rfc-editor.org/rfc/rfc8616)
