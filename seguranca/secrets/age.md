# age

age é um formato, ferramenta e biblioteca para criptografia de arquivos. Seu
modelo principal usa recipients públicos para cifrar e identities privadas
para decifrar. A chave privada não precisa ser entregue a quem somente produz
arquivos cifrados.

## Modelo híbrido

age gera ou usa uma chave simétrica para cifrar o conteúdo e protege essa chave
para cada recipient. O arquivo carrega os metadados necessários para encontrar
o recipient e recuperar a chave de conteúdo, mas não revela a identity privada.
Assim, vários destinatários podem decifrar o mesmo arquivo sem compartilhar uma
senha entre si.

Uma chave age nativa é pequena e pode ser publicada como recipient no arquivo
de configuração do SOPS. A publicação da chave pública não concede capacidade
de decifrar. Essa capacidade fica na identity privada correspondente.

## Chaves e recuperação

A identity privada é um segredo administrativo. Ela precisa de proteção,
backup, rotação e procedimento de recuperação. Adicionar um recipient exige
recifrar o arquivo para que a nova chave de conteúdo seja protegida também
para ele. Remover acesso exige recifrar sem o recipient antigo.

Se a identity for perdida, os arquivos continuam cifrados, mas podem se tornar
irrecuperáveis. Se for exposta, todos os arquivos que ela consegue abrir
devem ser considerados comprometidos e recifrados com um conjunto novo de
recipients.

age não é um password hash, não é uma CA e não substitui assinatura de release.
Ele protege confidencialidade. Autenticidade e integridade dependem do formato
e da verificação usada no fluxo que transporta o arquivo.

## Plugins e hardware

O formato pode ser integrado a plugins para dispositivos ou serviços que
mantêm a chave fora de um arquivo comum. Isso permite usar tokens, módulos
seguros ou outros agentes, mas cria dependências de disponibilidade,
compatibilidade e recuperação. O segredo continua sendo a capacidade de
decifrar, mesmo quando a chave não pode ser exportada.

## Relações

- [SOPS](sops.md) cifra valores estruturados e usa age como backend.
- [SOPS keyservice](sops-keyservice.md) delega operações de chave.
- [Backup da chave age](age-key-backup.md) trata recuperação.
- [Criptografia simétrica](../criptografia/criptografia-simetrica.md)
  explica a proteção do conteúdo.

## Fontes primárias

- [age, projeto oficial](https://github.com/FiloSottile/age)
- [Especificação age](https://age-encryption.org/v1)
