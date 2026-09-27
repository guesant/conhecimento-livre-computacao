# Sharp

Sharp é um módulo para processamento de imagens em runtimes JavaScript que
implementam Node-API. Ele usa libvips e é voltado a operações como resize,
crop, rotate, composite, conversão de formato e geração de dados brutos de
pixels.

## Modelo de processamento

Uma aplicação cria uma pipeline a partir de Buffer, stream ou arquivo e encadeia
operações antes de produzir uma saída. A implementação usa libuv e processamento
eficiente por regiões, evitando manter toda a imagem descomprimida quando isso
não é necessário.

```javascript
import sharp from "sharp";

await sharp(input)
  .rotate()
  .resize({ width: 1200, withoutEnlargement: true })
  .webp({ quality: 82 })
  .toFile(output);
```

O código precisa definir limites e tratar rejeições. `rotate()` pode usar
orientação EXIF, e `metadata()` retorna propriedades sem necessariamente
produzir a imagem final. Não confunda inspeção com validação de segurança do
arquivo.

## Formatos e qualidade

Sharp lê JPEG, PNG, WebP, GIF, AVIF, TIFF e SVG em cenários suportados e pode
produzir vários desses formatos, além de pixels raw. O codec escolhido, a
qualidade, o subsampling, o espaço de cor, o perfil ICC e o alpha influenciam
qualidade e tamanho.

Para uma imagem publicada, escolha o formato com base no conteúdo e na matriz
de navegadores, não apenas no menor arquivo de um benchmark. Teste fotografias,
texto, transparência, animação e perfis de cor.

## Concorrência e limites

Sharp pode usar múltiplos núcleos, filas internas e recursos nativos. Em um
servidor, limite concorrência por usuário e por worker, observe heap do
JavaScript, memória nativa, fila do libuv, tempo de decode e tamanho do output.

Um Buffer recebido por upload pode consumir muito mais memória depois de
decodificado. Valide tipo, dimensões, frames e tamanho antes de transformar, e
execute a operação em um processo com limites quando o conteúdo não for
confiável.

## Segurança e metadata

SVG e delegates podem carregar uma superfície diferente de um JPEG simples.
Defina quais formatos são aceitos, remova ou preserve metadata de forma
explícita e não escreva em caminhos fornecidos pelo cliente. O arquivo original
deve ser preservado separadamente se houver necessidade de auditoria.

## Relações

- [ImageMagick](imagemagick.md) oferece uma suíte mais ampla, com outra
  arquitetura e política de delegates.
- [Formatos de imagem](formatos-de-imagem.md) explica raster, cor, alpha e
  compressão.
- [EXIF](exif.md) explica orientação e metadata de captura.

## Fontes primárias

- [Sharp](https://sharp.pixelplumbing.com/)
- [Sharp API](https://sharp.pixelplumbing.com/api-constructor)
- [libvips](https://www.libvips.org/)
