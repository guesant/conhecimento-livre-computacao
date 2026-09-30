# EXIF

EXIF é um conjunto de tags de metadados usado principalmente em imagens de
câmeras e arquivos relacionados ao formato TIFF. JPEG, HEIF e outros containers
podem transportar tags EXIF. Elas descrevem captura, dispositivo, orientação,
exposição, lente, software, horário e, em alguns casos, coordenadas GPS.

EXIF não é a imagem e não define sozinho a qualidade ou a autenticidade da
captura. Um editor pode alterar, remover ou recriar tags. O valor de uma tag
deve ser tratado como metadata fornecida pelo arquivo, não como prova externa.

## Tags importantes

Orientação pode informar que os pixels devem ser girados ou espelhados na
exibição. Data e hora podem usar convenções e timezone diferentes. GPS pode
revelar o local da captura. Make, model, serial, software e histórico podem
ajudar a identificar o equipamento ou o fluxo de edição.

Um serviço precisa decidir se normaliza a orientação fisicamente, mantendo os
pixels na posição final, ou se conserva a tag. A escolha deve ser consistente
entre thumbnail, CDN, download e visualização original.

## Privacidade

Antes de publicar uma foto, examine GPS, identificadores, nomes, horários e
miniaturas. Remover EXIF reduz exposição, mas não remove informação visível,
voz, documentos fotografados ou padrões que identificam uma pessoa.

Não remova metadados de forma indiscriminada em fluxos que dependem de cor,
direitos autorais, preservação científica ou auditoria. Separe o original
protegido do derivado público e documente a transformação.

## Processamento

Use uma ferramenta que conheça o container e valide o resultado depois da
operação. Ao fazer re-encode, confirme dimensões, perfil ICC, orientação,
transparência, qualidade, checksum e ausência dos campos que a política manda
remover.

Em upload de usuário, não confie em `Content-Type`, extensão ou texto de uma
tag para decidir o parser. Identifique o formato real, limite o custo do
decode e execute a manipulação em um processo com permissões mínimas.

## Relações

- [Formatos de imagem](formatos-de-imagem.md) explica raster, vetor, cor e
  compressão.
- [Metadados binários](../arquivos/metadados-binarios.md) compara metadata
  interna, externa e derivada.
- [ImageMagick](imagemagick.md) e [Sharp](sharp.md) podem ler ou preservar
  partes de metadata conforme a operação.

## Fonte

- [ExifTool](https://exiftool.org/)
- [EXIF specification and resources](https://www.cipa.jp/e/std/std-sec.html)
