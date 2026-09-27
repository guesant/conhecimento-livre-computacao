# Formatos de imagem

Formatos de imagem fazem escolhas diferentes sobre representação, compressão,
transparência, animação, camadas e reprodução de cor. A extensão identifica
uma convenção, mas o conteúdo deve ser validado pelo parser.

| Formato | Modelo | Compressão e uso típico |
| --- | --- | --- |
| JPEG | Raster, normalmente sem alpha | Com perdas, fotografias e compatibilidade ampla |
| PNG | Raster | Sem perdas, transparência, diagramas e interfaces |
| GIF | Raster indexado | Limitado em cores, animação simples e legado web |
| WebP | Raster | Com ou sem perdas, transparência e animação |
| AVIF | Raster baseado em AV1 | Boa eficiência, mas custo de encode e suporte devem ser avaliados |
| TIFF | Raster e páginas ou camadas | Flexível, impressão, scanner e preservação |
| HEIF/HEIC | Container de imagens | Boa compressão e dependência de suporte por plataforma |
| SVG | Vetorial em XML | Formas, texto e filtros, com superfície de parsing própria |
| RAW | Dados do sensor | Preserva informação para revelação posterior, varia por fabricante |

## Qualidade e tamanho

JPEG, WebP, AVIF e outros formatos podem usar compressão com perdas. Uma taxa
menor pode reduzir bytes, mas introduzir blocos, ringing, banding e perda de
detalhes. PNG e formatos sem perdas preservam os valores decodificados, mas não
garantem arquivos pequenos para fotografias.

Escolha por conteúdo. Texto e line art normalmente exigem preservação de bordas
e alpha; fotografias toleram escolhas perceptuais diferentes; imagens de
ciência e captura podem exigir profundidade e perfil de cor maiores.

## Cor e alpha

RGB, grayscale, CMYK, YCbCr e espaços HDR representam informações diferentes.
Um perfil ICC pode ser necessário para interpretar os valores corretamente.
Remover o perfil sem converter as amostras pode alterar a aparência.

Alpha pode ser straight ou premultiplied, conforme o formato e a biblioteca.
Compor imagens sem respeitar esse contrato produz halos e bordas escuras. Teste
transparência em fundos claros e escuros.

## Web e distribuição

Para publicar imagens, gere dimensões adequadas, defina cache, preserve a
orientação visual, escolha quality e envie o MIME correto. `srcset`, negociação
de formato e lazy loading podem reduzir transferência, mas não substituem uma
imagem de saída bem codificada.

Valide dimensões e número de pixels no servidor. Um arquivo pequeno comprimido
pode expandir para uma imagem enorme e causar consumo de memória ou negação de
serviço durante o decode.

## Relações

- [EXIF](exif.md) aborda metadados que podem acompanhar imagens.
- [ImageMagick](imagemagick.md) oferece conversão e manipulação geral.
- [Sharp](sharp.md) oferece processamento eficiente para aplicações Node.js.
- [Formatos de compressão](../compressao/formatos.md) separa compressão geral
  de codecs de imagem.
