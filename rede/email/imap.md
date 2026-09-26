# IMAP

IMAP, Internet Message Access Protocol, permite que clientes manipulem uma caixa que
permanece no servidor. O cliente consulta pastas, mensagens e estados, baixa partes
quando necessário e sincroniza alterações entre vários dispositivos.

O servidor continua sendo o local autoritativo da caixa. Isso permite que um usuário
veja a mesma mensagem, pasta, flag de leitura e movimentação em clientes diferentes,
desde que todos respeitem a semântica do servidor.

## Operações

O protocolo organiza a caixa em mailboxes. Um cliente pode selecionar uma mailbox,
pesquisar mensagens, obter envelopes ou partes, marcar flags, copiar, mover e apagar
mensagens. A sessão pode permanecer ativa para receber notificações de novas mensagens
e alterações.

Baixar somente cabeçalhos ou partes reduz tráfego, mas torna a experiência dependente
da conexão. O cliente deve tratar mudanças concorrentes, expiração de sessão, limites
de comandos, falhas parciais e mensagens que foram alteradas ou removidas por outro
cliente.

## Segurança e capacidade

Use TLS e autenticação compatíveis com a política da conta. Revise o armazenamento de
tokens, o cache local, o acesso offline e a retenção de anexos. A caixa pode conter
informação pessoal e empresarial, então logs não devem registrar conteúdo ou senhas.

IMAP precisa de limites de conexões, tamanho de resposta, número de buscas simultâneas
e duração de sessão. Uma sincronização agressiva pode consumir CPU, I/O e largura de
banda tanto no servidor como no cliente.

## Relações

- [E-mail](index.md) diferencia acesso à caixa de transporte.
- [POP3](pop3.md) trata o modelo de download.
- [SMTP](smtp.md) trata entrega e submissão.

## Fonte

- [RFC 9051, Internet Message Access Protocol version 4rev2](https://www.rfc-editor.org/rfc/rfc9051)
