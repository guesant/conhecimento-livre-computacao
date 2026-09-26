# SFTP

SSH File Transfer Protocol, SFTP, fornece operações de arquivos sobre um
subsystem de SSH. Normalmente usa a autenticação, a proteção criptográfica e o
controle de acesso do servidor SSH, frequentemente na porta TCP 22, embora a
porta possa ser alterada.

## Operação

Clientes podem oferecer sessão interativa ou automação. SFTP permite listar,
criar, remover, renomear, ler e escrever arquivos sem montar o filesystem
remoto. O cliente fala um protocolo de arquivos com o servidor, que aplica as
permissões da conta e pode restringir o usuário a um diretório.

SFTP é adequado para cópia administrativa, integração entre sistemas,
intercâmbio de arquivos e jobs que precisam de autenticação forte. Para
sincronização eficiente de árvores, `rsync` sobre SSH pode transmitir apenas
diferenças. Para montar um diretório, SSHFS acrescenta uma camada FUSE sobre
SSH e SFTP.

## Segurança e limites

Valide a chave do host, proteja chaves privadas, use contas com menor
privilégio e restrinja o subsystem quando a conta só deve transferir arquivos.
Registre autenticação, origem, destino e operações quando houver requisito de
auditoria. SFTP não concede acesso além das permissões do servidor, mas uma
conta de escrita ainda pode alterar ou substituir arquivos importantes.

SFTP não é FTP sobre TLS. São protocolos diferentes, com negociação,
permissões, clientes, logs e modos de operação próprios.

## Fonte primária

- [OpenSSH sftp manual](https://man.openbsd.org/sftp)
- [RFC 4253, SSH Transport Layer Protocol](https://www.rfc-editor.org/rfc/rfc4253)
- [RFC 4254, SSH Connection Protocol](https://www.rfc-editor.org/rfc/rfc4254)
