# WinSCP

WinSCP é um cliente gráfico e automatizável para Windows. Ele reúne uma
interface de gerenciamento de arquivos com suporte a SFTP, SCP, FTP, FTPS,
WebDAV e S3. Seu foco é facilitar transferências autenticadas, sincronizações
dirigidas e operações administrativas sem transformar o cliente em um servidor
de arquivos.

## Modelo de uso

O uso mais seguro normalmente começa por uma sessão SFTP sobre SSH. O usuário
confirma a chave do host, escolhe uma chave privada ou outro método de
autenticação e opera somente dentro das permissões concedidas pela conta
remota. A interface pode apresentar os diretórios local e remoto lado a lado,
ou abrir o destino como um navegador de arquivos.

SCP aparece como uma alternativa de compatibilidade para servidores Unix que
oferecem esse protocolo. Ele é mais limitado para operações de filesystem e
depende de comandos remotos em várias funcionalidades da interface. Quando o
servidor oferece SFTP, essa costuma ser a opção preferível.

## Transferência e sincronização

O cliente mantém fila de transferências, pode retomar operações interrompidas
e possui modos de sincronização entre árvores locais e remotas. Sincronizar
não é o mesmo que copiar: a direção, os critérios de comparação e a política
para arquivos removidos precisam ser definidos antes de confirmar a operação.

Para uma rotina repetível, prefira script, log e parâmetros explícitos. A
interface é útil para validar o primeiro fluxo, mas uma rotina de publicação
ou backup precisa ser revisável e reproduzível. O modo de sincronização não
substitui um sistema de versionamento nem uma política de backup.

## Segurança

Confirme a impressão digital da chave do host por um canal independente antes
da primeira conexão. Não aceite uma troca de chave inesperada apenas para
restabelecer acesso. A senha da sessão não deve ser embutida em URLs, scripts
ou atalhos compartilhados.

Use contas com menor privilégio, diretórios restritos e chaves separadas por
finalidade. O armazenamento local de sessões e credenciais deve ser protegido
por senha mestra ou pelo cofre do sistema operacional. Em automações, prefira
um agente de chaves ou um mecanismo de segredo adequado ao ambiente.

## Quando escolher

WinSCP é uma boa escolha para equipes que operam Windows e precisam de uma
interface gráfica para SFTP, com possibilidade de evoluir para scripts e
automação. Não é a escolha principal para sincronização entre múltiplos
backends de object storage; nesse caso, [rclone](rclone.md) representa melhor
o problema. Para transferências recorrentes em árvores Unix, [rsync](rsync.md)
tem uma semântica mais específica.

## Relações

- [SFTP](sftp.md) define o protocolo usado na maioria das conexões seguras.
- [rsync](rsync.md) é orientado a sincronização diferencial de árvores.
- [SSHFS](sshfs.md) monta um caminho remoto usando SSH e FUSE.
- [Transferência de arquivos](transferencia/index.md) compara os fluxos
  atendidos por cada ferramenta.

## Fontes primárias

- [Documentação do WinSCP](https://winscp.net/eng/docs/start)
- [Protocolos suportados pelo WinSCP](https://winscp.net/eng/docs/protocols)
- [Automação de transferências](https://winscp.net/eng/docs/guide_automation)
