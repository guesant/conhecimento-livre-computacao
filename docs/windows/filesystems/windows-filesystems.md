# Filesystems Windows

## NTFS

NTFS é o filesystem padrão de instalações Windows modernas. Ele suporta ACLs, security descriptors, journaling, compressão, quotas, reparse points, hard links, streams nomeados e criptografia conforme o recurso e a versão. É a escolha geral para volumes de sistema e dados Windows.

## ReFS

ReFS foi projetado para disponibilidade, grandes conjuntos de dados e integridade em cenários específicos. Ele não é um substituto universal de NTFS: não é normalmente bootável, não é adequado para todas as mídias removíveis e não oferece todas as funções de NTFS.

## FAT32 e exFAT

FAT32 tem ampla interoperabilidade, mas limites pequenos para arquivos e volumes. exFAT remove parte desses limites e é comum em mídia removível, mas não fornece o mesmo modelo de ACL, journaling e recuperação de NTFS. A escolha deve considerar o dispositivo consumidor e o risco de remoção abrupta.

## UDF e outros

UDF é usado em mídias ópticas e alguns cenários de troca. O Windows também pode acessar outros filesystems por drivers ou ferramentas externas, mas isso não transforma o suporte adicional em uma propriedade nativa ou em uma garantia de recuperação.

## Organização

Windows apresenta volumes por letras como `C:` e `D:`, pontos de montagem e caminhos UNC como `\\servidor\\compartilhamento`. Cada volume tem sua própria raiz. Junctions, symbolic links, reparse points e shares podem fazer um caminho visível apontar para outro volume ou serviço.

## Fontes primárias

- [NTFS overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)
- [ReFS overview](https://learn.microsoft.com/en-us/windows-server/storage/refs/refs-overview)
- [Windows local file systems](https://learn.microsoft.com/en-us/windows/win32/fileio/file-systems)
- [Windows path naming](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file)
