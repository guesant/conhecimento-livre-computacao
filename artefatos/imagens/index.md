# Imagens

Uma imagem digital representa uma cena, desenho ou composição por pixels,
vetores, camadas ou uma combinação dessas estruturas. O formato define como
essas informações são armazenadas, comprimidas, coloridas e acompanhadas de
metadados.

## Mapa

- [Formatos de imagem](formatos-de-imagem.md) compara raster, vetor, perdas,
  transparência, animação e HDR.
- [EXIF](exif.md) explica metadados de câmeras e imagens.
- [ImageMagick](imagemagick.md) explica a suíte de conversão e processamento.
- [Sharp](sharp.md) explica processamento em JavaScript com libvips.

## Raster e vetor

Imagem raster armazena amostras de uma grade de pixels. Resolução, profundidade
de cor, canais, alpha, espaço de cor e perfil ICC influenciam o resultado. Ao
ampliar uma raster, o algoritmo de resampling precisa criar amostras que não
existiam no arquivo.

Imagem vetorial armazena formas, caminhos, textos, filtros e transformações.
Ela pode ser renderizada em diferentes resoluções, mas depende de fontes,
engines e recursos suportados. SVG é texto estruturado e pode carregar links,
scripts ou entidades, portanto não deve ser tratado como um bitmap inofensivo.

## Pipeline

Um pipeline de imagem normalmente identifica o formato, verifica dimensões e
metadados, decodifica, transforma, aplica cor e re-encode em um formato de
saída. Cada etapa pode aumentar memória e tempo. Limite pixels totais,
dimensões, número de frames, profundidade e tamanho descomprimido antes de
alocar.

A saída deve ser canônica para o caso de uso. Re-encode ajuda a eliminar bytes
adicionais e estruturas ambíguas, mas pode remover qualidade, animação, perfis,
camadas e metadados desejados.
