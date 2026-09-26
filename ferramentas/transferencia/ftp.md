# FTP

File Transfer Protocol, FTP, é um protocolo de transferência que separa o
canal de controle do canal de dados. O cliente abre uma sessão de controle,
autentica e solicita operações. A transferência de arquivos ou listagens usa
uma conexão de dados adicional.

## Canais e modos

No modo ativo, o servidor abre a conexão de dados de volta para o cliente. No
modo passivo, o servidor anuncia uma porta e o cliente abre a conexão de
dados. O modo passivo costuma atravessar NAT e firewalls com menos dificuldade,
mas exige que o intervalo de portas anunciado pelo servidor esteja publicado
corretamente.

O canal de controle tradicional usa TCP 21. A porta do canal de dados muda
conforme o modo e a operação. Um firewall que libera apenas TCP 21 pode
permitir login e ainda quebrar listagens ou transferências.

## Segurança

FTP tradicional não cifra credenciais nem conteúdo. Captura de tráfego pode
expor usuário, senha e arquivos. Se uma aplicação ainda precisa do modelo FTP,
use FTPS com TLS, restrinja o alcance e valide certificados. Em novas
integrações, compare com [SFTP](sftp.md), HTTPS ou um armazenamento de objetos,
conforme o requisito.

## Operação

Defina diretórios de entrada e saída separados, limites de tamanho, retenção,
permissões, nomes temporários e confirmação de integridade. Não considere um
arquivo presente no diretório como uma transferência concluída: o produtor
pode ainda estar escrevendo. Um padrão comum é enviar com nome temporário e
renomear somente após fechar e validar o arquivo.

## Relações

- [FTPS](ftps.md) protege FTP com TLS.
- [SFTP](sftp.md) usa o protocolo SSH e não o protocolo FTP.
- [rclone](rclone.md) pode integrar backends que não usam FTP.

## Fonte primária

- [RFC 959, File Transfer Protocol](https://www.rfc-editor.org/rfc/rfc959)
