# Transferência e acesso a arquivos remotos

Ferramentas diferentes atendem cópia, sincronização, sessão e montagem.

[rsync](rsync.md) sincroniza em uma direção. [SSHFS](sshfs.md) monta filesystem remoto. [SFTP](sftp.md) oferece sessão de transferência sobre SSH. [FTP](ftp.md) e [FTPS](ftps.md) mantêm o modelo de canais do FTP, com FTPS adicionando TLS. [rclone](rclone.md) integra múltiplos backends de storage.

A escolha deve começar pelo comportamento desejado, não pelo protocolo disponível.
