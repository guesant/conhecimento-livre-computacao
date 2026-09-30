# POP3

POP3, Post Office Protocol version 3, é um protocolo simples para acessar mensagens
armazenadas em um servidor. Seu modelo tradicional baixa mensagens para o cliente e
pode removê-las do servidor, embora clientes também possam manter cópias e usar
operações limitadas de listagem e recuperação.

POP3 é útil quando um único cliente deve receber a caixa localmente ou quando a
sincronização exigida é pequena. Ele é menos adequado quando o usuário alterna entre
celular, navegador e computador e precisa preservar pastas, estado de leitura,
marcadores e operações sincronizadas.

## Sessão

Uma sessão passa por estados de autorização e transação. O cliente autentica, consulta
mensagens, recupera ou marca mensagens e encerra a sessão. O servidor mantém a caixa,
mas o protocolo não oferece o modelo rico de pastas e estado compartilhado do IMAP.

Use TLS direto ou STLS conforme a política do servidor. Credenciais não devem ser
enviadas em uma sessão sem proteção. Limites de tamanho, timeout e comportamento de
reconexão precisam ser definidos pelo cliente.

## Limitações

O download local não é um backup por si só. A máquina pode ser perdida, o cliente pode
remover mensagens antes de uma cópia independente e a retenção pode não atender a uma
necessidade legal ou operacional. Arquivamento e backup precisam de sua própria política.

POP3 também não é protocolo de envio. A submissão e a entrega usam SMTP.

## Relações

- [E-mail](index.md) explica a composição dos protocolos.
- [IMAP](imap.md) compara sincronização de caixa e acesso local.
- [SMTP](smtp.md) trata entrega e submissão.

## Fonte

- [RFC 1939, Post Office Protocol version 3](https://www.rfc-editor.org/rfc/rfc1939)
