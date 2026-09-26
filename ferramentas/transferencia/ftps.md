# FTPS

FTPS é FTP protegido por TLS. Ele mantém o modelo de FTP com canal de
controle, canal de dados, modo ativo ou passivo, diretórios e comandos, mas
adiciona negociação e proteção criptográfica TLS.

## Modos de proteção

No modo explícito, o cliente começa uma sessão FTP e solicita que o servidor
ative TLS, normalmente com `AUTH TLS`. No modo implícito, a sessão espera TLS
desde o início em uma porta dedicada. Os nomes e portas exatos dependem do
servidor, cliente e compatibilidade exigida.

O canal de dados também precisa ser protegido quando o conteúdo ou os nomes de
arquivos forem sensíveis. Configurar TLS apenas no canal de controle pode
deixar a transferência exposta. O modo passivo continua exigindo a publicação
correta do intervalo de portas do servidor.

## Certificados e operação

Valide o certificado do servidor, a cadeia de confiança, o nome esperado e as
versões e cifras TLS permitidas. Não desabilite a validação apenas porque um
cliente legado não consegue negociar corretamente. Registre falhas de
autenticação, negociação, abertura do canal de dados e transferência.

FTPS pode ser necessário para integrar um parceiro que já usa FTP e exige
compatibilidade com comandos ou ferramentas existentes. Quando não houver
essa restrição, SFTP ou HTTPS podem resultar em um caminho operacional mais
simples, porque não precisam administrar um segundo canal de dados com portas
dinâmicas.

## Relações

- [FTP](ftp.md) explica os canais e modos herdados pelo FTPS.
- [SFTP](sftp.md) é um protocolo diferente baseado em SSH.
- [TLS 1.3](../../seguranca/tls/tls13.md) explica certificados e negociação.

## Fonte primária

- [RFC 4217, Securing FTP with TLS](https://www.rfc-editor.org/rfc/rfc4217)
- [RFC 959, File Transfer Protocol](https://www.rfc-editor.org/rfc/rfc959)
