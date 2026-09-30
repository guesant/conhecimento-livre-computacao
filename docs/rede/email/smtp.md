# SMTP

SMTP, Simple Mail Transfer Protocol, é o protocolo de transporte de mensagens
eletrônicas. Ele descreve uma conversa orientada a comandos e respostas entre um
cliente SMTP e um servidor, ou entre dois agentes que encaminham a mensagem.

## Transporte e submissão

Entrega entre servidores usa o MX do domínio destinatário. O servidor de origem
consulta DNS, tenta os destinos conforme a prioridade dos registros e estabelece uma
sessão SMTP. A mensagem pode atravessar relays até chegar ao servidor responsável pela
caixa.

Submissão é o caminho entre o cliente do usuário e o servidor de saída. Ela normalmente
exige autenticação, políticas de tamanho, limites por conta e TLS. Não deve ser
confundida com a entrega entre servidores: permitir relay aberto em uma porta de
transporte cria uma fonte de abuso e prejudica a reputação do domínio.

## Conversa básica

Uma transação SMTP identifica remetente de envelope, destinatários e conteúdo. Os
campos do envelope controlam a entrega; os cabeçalhos From, To e Date fazem parte da
mensagem e podem não coincidir com a identidade usada no envelope.

O servidor responde com códigos de três dígitos. Respostas da classe 2xx indicam
sucesso, 4xx indicam falha temporária que pode ser tentada novamente e 5xx indicam
falha permanente para aquela tentativa. A fila do remetente deve usar retry com
backoff e preservar mensagens que ainda podem ser entregues.

## TLS e portas

SMTP pode começar em uma conexão simples e negociar TLS com STARTTLS, ou usar uma
porta dedicada com TLS desde a abertura. A política deve validar certificado, nome,
versão, cifra e comportamento quando TLS não está disponível. TLS protege o transporte
entre os pontos que o negociam, mas não torna automaticamente toda a cadeia ponta a
ponta.

## Autenticação do domínio

SMTP usa MX para localizar a entrega, SPF para verificar autorização da origem do
envelope, DKIM para validar uma assinatura e DMARC para comparar esses sinais com o
domínio visível no From. Nenhum mecanismo elimina sozinho spam, phishing ou
comprometimento de uma conta legítima.

## Operação

Monitore filas, códigos de rejeição, retries, timeouts, reputação, listas de bloqueio,
falhas de DNS, expiração de certificados, uso de disco e tamanho das mensagens.
Registre o identificador da mensagem e a sequência de relays sem armazenar conteúdo
desnecessário ou credenciais.

## Relações

- [E-mail](index.md) diferencia transporte, submissão e acesso à caixa.
- [SPF](spf.md), [DKIM](dkim.md) e [DMARC](dmarc.md) tratam autenticação de domínio.
- [MX](../dns/records.md) trata a localização dos servidores receptores.

## Fonte

- [RFC 5321, Simple Mail Transfer Protocol](https://www.rfc-editor.org/rfc/rfc5321)
