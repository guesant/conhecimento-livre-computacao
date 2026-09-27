# Cyberduck

Cyberduck é um cliente gráfico para macOS e Windows voltado a servidores,
serviços de armazenamento e compartilhamento de arquivos. Ele oferece
conexões por FTP, FTPS, SFTP, WebDAV, S3, Google Cloud Storage, Azure,
Backblaze B2 e outros backends, conforme o protocolo e o perfil configurado.

## Modelo de uso

O programa apresenta um navegador de objetos ou diretórios remotos. O usuário
pode abrir uma conexão, transferir arquivos, editar um arquivo por meio de um
editor local e sincronizar pastas. Essas ações são conveniências de cliente;
elas não mudam a semântica de durabilidade, versionamento ou permissões do
serviço remoto.

O modelo é particularmente útil quando a equipe precisa operar destinos de
naturezas diferentes por uma interface semelhante. SFTP representa uma árvore
de arquivos sobre SSH, enquanto S3 e serviços compatíveis representam objetos,
chaves e buckets. Uma pasta exibida pelo cliente não significa que todos os
backends possuem as mesmas operações de rename, lock ou atomicidade.

## SFTP e armazenamento de objetos

Para SFTP, valide a chave do host e as permissões da conta como faria no
cliente `sftp`. Para object storage, proteja as chaves de acesso e limite o
escopo da policy ao bucket e prefixos necessários. A capacidade de listar um
bucket não deve ser concedida apenas porque o usuário precisa enviar um
arquivo.

Operações de sincronização devem ser avaliadas com cuidado. Alguns backends
não oferecem as mesmas garantias de metadados, timestamp, rename atômico ou
remoção. Antes de usar o modo de espelhamento, teste a direção, a política de
exclusão e o comportamento diante de interrupções.

## Criptografia no cliente

O suporte a cofres do Cryptomator permite cifrar o conteúdo antes de enviá-lo
ao armazenamento remoto. Isso protege o conteúdo contra leitura pelo backend,
mas não necessariamente esconde todos os metadados, como tamanho, frequência
de acesso ou nomes dependendo da configuração do cofre. A senha do cofre
continua sendo uma responsabilidade operacional separada das credenciais do
serviço de armazenamento.

## Quando escolher

Cyberduck é adequado para exploração manual de vários protocolos e serviços
de storage. Para uma rotina de CI, migração ou backup, prefira [rclone](rclone.md)
ou uma ferramenta declarativa que possa ser executada sem interface gráfica.
Para sincronização eficiente de duas árvores Unix, [rsync](rsync.md) é mais
específico.

## Relações

- [SFTP](sftp.md) explica o transporte sobre SSH.
- [rclone](rclone.md) oferece automação para múltiplos backends.
- [FTP](ftp.md) e [FTPS](ftps.md) explicam os protocolos de transferência.
- [Cryptomator](../../cifrar-um-cofre-de-segredos-em-repouso.md) trata cofres
  cifrados no lado do cliente.

## Fontes primárias

- [Documentação do Cyberduck](https://docs.cyberduck.io/cyberduck/)
- [Protocolos suportados](https://docs.cyberduck.io/protocols/)
- [Interface de linha de comando](https://docs.cyberduck.io/cli/)
