# FileZilla

FileZilla é uma família de clientes e servidores para transferência de
arquivos. O FileZilla Client oferece uma interface gráfica multiplataforma
para FTP, FTPS e SFTP, com gerenciador de sites, fila de transferências e
visualização de diretórios local e remoto.

## Protocolos

FTP não cifra credenciais nem conteúdo por padrão. FTPS adiciona TLS ao modelo
do FTP e mantém suas características de canais e negociação. SFTP é outro
protocolo: ele funciona dentro de uma sessão SSH e não deve ser confundido com
FTP protegido por TLS.

A escolha do protocolo precisa considerar o servidor existente, o firewall, o
modelo de autenticação e a necessidade de retomada. Se o servidor oferece SSH,
SFTP costuma evitar a complexidade operacional de múltiplos canais do FTP.

## Operação

O gerenciador de sites permite salvar parâmetros de conexão, diretório inicial
e método de autenticação. A fila separa a navegação da execução das
transferências e facilita acompanhar erros, pausas e retomadas.

Para publicar conteúdo manualmente, a interface pode ser suficiente. Para
deploy, backup ou integração de sistemas, prefira um processo declarativo e
auditável com [rsync](rsync.md), [rclone](rclone.md), SFTP automatizado ou uma
ferramenta própria do pipeline.

## Segurança

Confirme a chave do host em conexões SFTP e valide o certificado quando usar
FTPS. Evite FTP sem criptografia fora de uma rede controlada e nunca trate a
presença de uma interface gráfica como evidência de segurança.

As configurações salvas pelo cliente podem conter nomes de host, usuários e,
dependendo do modo escolhido, material sensível. Restrinja o acesso ao perfil
do usuário, evite salvar senhas em máquinas compartilhadas e use chaves ou
integrações com o armazenamento seguro do sistema quando disponíveis.

## Limites

FileZilla Client é um cliente de transferência, não um mecanismo de
sincronização bidirecional com resolução de conflitos. Também não substitui
um servidor SFTP, uma política de backup ou um sistema de publicação. A fila
organiza operações do usuário, mas não fornece por si só idempotência,
versionamento ou retenção.

## Relações

- [FTP](ftp.md) explica o protocolo sem criptografia.
- [FTPS](ftps.md) explica FTP protegido por TLS.
- [SFTP](sftp.md) explica o protocolo baseado em SSH.
- [WinSCP](winscp.md) oferece uma alternativa gráfica especialmente comum em
  Windows.
- [Cyberduck](cyberduck.md) cobre SFTP, WebDAV e serviços de armazenamento.

## Fontes primárias

- [Site oficial do FileZilla](https://filezilla-project.org/)
- [Documentação do FileZilla](https://wiki.filezilla-project.org/Documentation)
- [Código-fonte do FileZilla](https://filezilla-project.org/sourcecode.php)
