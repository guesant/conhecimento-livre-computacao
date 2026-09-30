# Vídeo

Vídeo digital é uma sequência temporal de imagens, normalmente acompanhada por
áudio, legendas, dados auxiliares e metadata. Um arquivo de vídeo combina um
container com um ou mais codecs, e a reprodução depende do decoder, do
timestamp, do dispositivo e do pipeline gráfico.

## Mapa

- [Formatos de vídeo](formatos-de-video.md) explica containers, codecs, frames
  e streaming.
- [FFmpeg](ffmpeg.md) explica a principal suíte de processamento multimídia.
- [Compressão](../compressao/index.md) explica os princípios gerais que também
  aparecem nos codecs de vídeo.

## Pipeline

O pipeline pode demuxar o container, decodificar frames, converter espaço de
cor, aplicar filtros, sincronizar áudio e vídeo, compor legendas e renderizar.
Na codificação, o processo ocorre no sentido inverso e pode incluir análise de
movimento, previsão, quantização, entropy coding e geração de índices.

Cada etapa pode exigir CPU, memória, I/O ou acelerador de hardware. Um vídeo
pequeno no filesystem pode expandir para muitos frames e exigir grande memória
quando decodificado.

## Streaming e publicação

Vídeo ao vivo e sob demanda precisam de timestamps consistentes, segmentação,
bitrate, keyframes, cache e uma política de compatibilidade. HLS e DASH
distribuem segmentos e manifestos; WebRTC privilegia comunicação em tempo real.
O container usado no arquivo original não determina sozinho o protocolo de
entrega.

Ao gerar derivados, defina resolução, framerate, codec, bitrate, áudio, legendas,
thumbnail, metadata e retenção. Registre qual fonte produziu cada variante e
evite re-encodes sucessivos que degradam qualidade.
