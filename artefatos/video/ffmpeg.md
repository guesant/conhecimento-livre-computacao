# FFmpeg

FFmpeg é um projeto e uma suíte de bibliotecas e ferramentas para processar
áudio, vídeo, containers e streams. Os comandos mais conhecidos são `ffmpeg`,
`ffprobe` e `ffplay`. O projeto também fornece bibliotecas como libavcodec,
libavformat, libavfilter, libswscale e libswresample.

## Ferramentas

`ffprobe` inspeciona streams, containers, codecs, timestamps e metadata sem
precisar gerar uma saída. `ffmpeg` demuxa, decodifica, filtra, converte,
codifica e muxa. `ffplay` ajuda a reproduzir e diagnosticar fluxos localmente.

```bash
ffprobe -hide_banner arquivo.mp4
ffmpeg -i entrada.mov -c:v libx264 -c:a aac saida.mp4
ffmpeg -i entrada.mp4 -vf scale=1280:-2 -c:v libx264 -c:a copy derivado.mp4
```

Copiar um stream com `-c:a copy` evita re-encode daquela parte. Alterar filtros,
resolução ou codec exige decodificação e nova codificação. Uma opção como
`-c copy` pode preservar bytes do stream, mas não garante que o container final
seja adequado para o cliente.

## Containers, codecs e filtros

FFmpeg separa demuxers e muxers de decoders e encoders. Filtros transformam
frames, amostras ou timestamps. Protocolos e dispositivos de entrada e saída
formam outra camada. Ao diagnosticar, identifique em qual camada a operação
falhou.

Uma conversão correta precisa decidir container, codec, pixel format, sample
rate, canais, bitrate, framerate, keyframes, metadata, legendas e timestamps.
Escolher apenas a extensão do arquivo não configura esse contrato.

## Desempenho

Use threads, aceleração de hardware e filtros com cuidado. A aceleração pode
alterar qualidade, compatibilidade, latência, consumo e caminho de metadata.
Meça decode, filtro, encode, I/O e tamanho do buffer separadamente.

Para jobs assíncronos, limite concorrência por worker, duração, resolução,
frames e tamanho de saída. Não permita que um único arquivo comprimido ou
malformado monopolize CPU e memória.

## Segurança

FFmpeg processa formatos complexos e pode habilitar protocolos, demuxers,
decoders e delegates que não são necessários em todos os serviços. Aceite
somente formatos previstos, desabilite recursos não utilizados quando possível,
execute a conversão em sandbox e mantenha a versão atualizada.

Não passe argumentos construídos a partir de entrada do usuário de forma que
sejam interpretados como opções. Use APIs ou separação segura de argumentos,
normalize nomes e escreva em um diretório temporário controlado.

## Relações

- [Formatos de vídeo](formatos-de-video.md) explica a diferença entre
  containers e codecs.
- [Formatos de áudio](../audio/formatos-de-audio.md) explica PCM, codecs e
  transporte.
- [Compressão](../compressao/index.md) explica fundamentos e algoritmos.

## Fontes primárias

- [FFmpeg documentation](https://ffmpeg.org/documentation.html)
- [FFmpeg formats documentation](https://ffmpeg.org/ffmpeg-formats.html)
- [FFmpeg codecs documentation](https://ffmpeg.org/ffmpeg-codecs.html)
- [FFmpeg source repository](https://git.ffmpeg.org/ffmpeg.git)
