# SPF

SPF, Sender Policy Framework, publica no DNS quais origens podem enviar mensagens
para um domínio ou para o domínio usado no envelope SMTP. O mecanismo é avaliado por
um receptor que compara a origem da conexão com a política do domínio.

SPF autentica principalmente a identidade do envelope, como MAIL FROM, e também pode
avaliar a identidade HELO ou EHLO. Essa identidade não é necessariamente o campo
visível From que o usuário vê. Por isso SPF sozinho não impede que uma mensagem use
um domínio visual diferente.

## Registro

SPF é publicado como um registro TXT no nome apropriado. Um domínio deve ter uma
política clara e evitar múltiplos registros SPF concorrentes. A política termina com
um mecanismo como -all, ~all, ?all ou +all, cada um com uma consequência diferente
para o resultado.

Inclua apenas fontes controladas e mantenha o número de consultas DNS dentro dos
limites do protocolo. Cadeias extensas de include, redirect, a, mx e exists podem
exceder o limite de avaliação e causar temperror ou permerror. Uma política gerada
deve ser revisada quando um provedor de envio é adicionado ou removido.

## Limitações

SPF valida o caminho de entrega observado pelo receptor, não a identidade humana do
remetente. Forwarders podem alterar a origem e quebrar SPF. Um relay que preserva
DKIM pode continuar autenticado por DKIM mesmo quando SPF falhar.

Não use SPF como substituto de DKIM ou DMARC. A política final precisa considerar
alinhamento, relatórios, subdomínios, encaminhamento e os provedores realmente usados.

## Relações

- [DKIM](dkim.md) usa assinatura criptográfica.
- [DMARC](dmarc.md) combina SPF, DKIM e alinhamento.
- [SMTP](smtp.md) explica as identidades de envelope.
- [Registros DNS](../dns/records.md) explica TXT.

## Fonte

- [RFC 7208, Sender Policy Framework](https://www.rfc-editor.org/rfc/rfc7208)
