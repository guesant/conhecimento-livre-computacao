# inodes

Um inode é a estrutura de metadados que representa um objeto de filesystem
Unix. Ele guarda identidade numérica, modo, proprietário, timestamps, tamanho,
contagem de links e referências aos blocos ou extensões de dados. O nome do
arquivo não vive no inode: diretórios relacionam nomes a números de inode.

## Nome e conteúdo

Dois nomes no mesmo diretório ou em diretórios diferentes podem apontar para o
mesmo inode por meio de hard links. Remover um nome reduz a contagem de links;
o conteúdo só é liberado quando não há nomes nem processos mantendo o arquivo
aberto. Isso explica por que espaço pode continuar ocupado depois de um arquivo
ser removido.

Symlink é diferente: ele possui seu próprio inode e contém um caminho para
outro objeto. Permissões, resolução, ciclos e travessia de diretórios precisam
ser analisados de forma diferente.

## Limite de inodes

Um filesystem pode ficar sem inodes antes de ficar sem blocos. Diretórios com
milhões de arquivos pequenos, cache, filas e artefatos temporários são causas
comuns. `df -i` mostra ocupação de inodes; `stat` e `find` ajudam a localizar
árvores densas. Expandir o disco não cria necessariamente mais inodes se o
filesystem não puder ser aumentado ou se o problema estiver em sua proporção
original.

## Consistência e concorrência

Alterações de inode e diretório passam pelo modelo de journaling ou copy-on-write
do filesystem. Um timestamp pode ter resolução e semântica diferentes de outro
filesystem. Aplicações que usam inode, tamanho ou mtime como identidade devem
considerar rename atômico, hard links, caches e concorrência.

## Relações

- [Filesystems](index.md) compara estruturas e garantias.
- [Syscalls](../../kernel/system-calls.md) trata a fronteira entre filesystem e kernel.
- [Hard link e symlink](https://man7.org/linux/man-pages/man7/symlink.7.html) detalha referências de nomes.

## Fontes primárias

- [inode(7)](https://man7.org/linux/man-pages/man7/inode.7.html)
- [stat(2)](https://man7.org/linux/man-pages/man2/stat.2.html)
- [The Linux VFS](https://www.kernel.org/doc/html/latest/filesystems/vfs.html)
