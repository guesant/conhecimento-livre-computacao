# Metadados binários

Metadados binários são informações que descrevem um artefato sem serem o
payload principal que o usuário deseja consumir. Eles podem estar no cabeçalho,
em uma tabela interna, em uma seção, em um trailer, em um sidecar ou no sistema
que armazena o arquivo.

## Exemplos

Metadados podem registrar:

- versão do formato e do software;
- dimensões, duração, codec, resolução e perfil de cor;
- timezone, data, localização, autor e dispositivo;
- arquitetura, ABI, build ID, dependências e símbolos;
- checksum, assinatura, licença, origem e proveniência;
- permissões, ownership, timestamps e extended attributes do filesystem.

O mesmo campo pode ter significado diferente em camadas diferentes. A data do
filesystem não é necessariamente a data capturada por uma câmera, e um build
ID não é uma assinatura de origem. Documente a fonte, a semântica e a
confiabilidade de cada metadado.

## Interno, externo e derivado

Metadados internos viajam com o arquivo, mas podem ser removidos por uma
conversão. Metadados externos, como um sidecar ou uma linha de banco, podem
preservar informação sem alterar o payload, mas correm o risco de se separar.
Metadados derivados, como duração calculada, checksum ou thumbnail, precisam
ser invalidados quando o arquivo muda.

Não misture metadados de controle com dados fornecidos pelo usuário sem uma
política de confiança. Um campo `content-type` informado pelo cliente é uma
afirmação, não o resultado de identificar o arquivo.

## Privacidade

EXIF, XMP, ID3 e propriedades de documentos podem revelar GPS, nome de usuário,
software, número de série, horário e histórico de edição. Antes de publicar,
defina quais campos são necessários, remova os demais e valide o resultado.

A remoção de metadados não anonimiza automaticamente a imagem, o áudio, o
vídeo ou o documento. Conteúdo visual, voz, nomes de arquivo e padrões de uso
podem continuar identificáveis.

## Integridade e provenance

Um checksum é útil para detectar mudança acidental. Uma assinatura ou atestação
relaciona o artefato a uma chave e a um processo de produção. Um campo de
metadados escrito dentro do arquivo não oferece essa garantia sozinho, porque
um atacante pode alterá-lo junto com o payload.

Para artefatos de build, mantenha o build ID, commit, dependências, imagem base,
SBOM e proveniência em um sistema de release. Para mídia, preserve o original
e trate derivados como novos artefatos com sua própria identificação.
