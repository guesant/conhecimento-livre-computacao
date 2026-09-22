# SSHFS

SSHFS monta um filesystem remoto sobre SSH/SFTP usando FUSE.

É útil para navegação e edição pontual como se o caminho remoto fosse local. Latência e perda de conexão afetam diretamente operações de filesystem.

Não é a escolha natural para transferir grandes lotes repetidamente; [rsync](rsync.md) resolve outro problema.