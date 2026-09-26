# Transferência de arquivos

Transferir arquivos significa mover ou sincronizar dados entre sistemas sem
necessariamente expor o filesystem remoto como parte do sistema local. O
protocolo precisa definir autenticação, confidencialidade, integridade,
retomada, atomicidade aparente e o comportamento diante de uma interrupção.

## Ferramentas

- [FTP](../ftp.md) e [FTPS](../ftps.md) mantêm o modelo de canais do FTP, com
  FTPS adicionando TLS.
- [SFTP](../sftp.md) oferece uma sessão de transferência sobre SSH.
- [rsync](../rsync.md) sincroniza árvores de arquivos e transmite somente o
  que precisa ser atualizado.
- [rclone](../rclone.md) abstrai múltiplos backends de storage.

## Escolha

Para uma cópia autenticada sobre SSH, SFTP costuma ser suficiente. Para
sincronização repetida de árvores, rsync expõe semântica mais adequada. FTP e
FTPS permanecem relevantes para sistemas legados e integrações que já dependem
do modelo de transferência, mas exigem análise cuidadosa de autenticação,
separação de canais e exposição de portas.
