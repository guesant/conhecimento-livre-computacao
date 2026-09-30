# Artefatos digitais

Um artefato digital é uma sequência de bytes interpretada por um formato,
programa ou protocolo. A extensão do nome é apenas uma pista. O significado
real depende de cabeçalhos, magic numbers, tabelas, offsets, codificação,
metadados, compressão e, em muitos casos, de uma versão do formato.

Esta categoria separa arquivos, imagens, áudio, vídeo e compressão. A separação
é importante porque um container de vídeo não é um codec, um arquivo de imagem
não é necessariamente uma imagem sem perdas, e um executável não é apenas um
arquivo com permissão de execução.

## Como navegar

- [Arquivos](arquivos/index.md) explica formatos, regiões binárias,
  executáveis, metadados e arquivos poliglotas.
- [Imagens](imagens/index.md) explica pixels, formatos raster e vetoriais,
  EXIF e processamento de imagens.
- [Áudio](audio/index.md) explica amostragem, codecs, containers e formatos de
  distribuição.
- [Vídeo](video/index.md) explica codecs, containers, frames, streaming e
  FFmpeg.
- [Compressão](compressao/index.md) explica redundância, perda, formatos e
  algoritmos.

## Formato não é extensão

Um nome como `foto.jpg` pode conter dados incompatíveis com JPEG, estar
truncado ou carregar bytes adicionais. Da mesma forma, um arquivo chamado
`programa` pode ser ELF, script com shebang, bytecode ou apenas dados. Para
identificar um artefato, examine seu conteúdo, valide a estrutura e compare
com a especificação ou com uma biblioteca apropriada.

Uma cadeia de processamento também pode conter várias camadas. Um arquivo
`video.mp4` combina um container com streams codificados por codecs, e cada
stream pode ter seus próprios parâmetros e metadados. Um arquivo `tar.gz`
combina um formato de arquivo com uma camada de compressão. Confundir essas
camadas causa escolhas erradas de ferramenta, incompatibilidade e perda de
qualidade.

## Segurança

Parsers de formatos processam dados controlados pelo usuário e podem conter
vulnerabilidades. Valide tamanho, dimensões, profundidade, número de streams,
recursão, decompression ratio, tempo de CPU e uso de memória. Execute
conversões em processos com permissões mínimas e mantenha bibliotecas
atualizadas.

Metadados podem conter GPS, nomes, horários, software, identificadores e
miniaturas. Antes de publicar ou compartilhar um arquivo, decida quais
metadados são necessários. Remover metadados não prova que o conteúdo visual ou
o histórico do arquivo foi removido.
