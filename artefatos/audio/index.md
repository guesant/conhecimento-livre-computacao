# Áudio

Áudio digital representa pressão sonora ou outro sinal como amostras. Um
arquivo pode armazenar amostras PCM diretamente ou um stream codificado por um
codec dentro de um container. Sample rate, profundidade de bits, canais,
layout, clock e codec determinam a experiência e o custo de armazenamento.

## Mapa

- [Formatos de áudio](formatos-de-audio.md) compara PCM, containers e codecs.
- [Formatos de compressão](../compressao/formatos.md) explica a diferença
  entre compressão geral e codec de áudio.
- [FFmpeg](../video/ffmpeg.md) processa áudio, vídeo, containers e streams.

## Captura e reprodução

O sample rate limita as frequências representáveis e a profundidade influencia
quantização e faixa dinâmica. Canais e layout precisam ser interpretados
corretamente para não trocar esquerda e direita ou somar canais de forma
incorreta.

Uma cadeia real inclui captura, conversão, buffer, codec, transporte,
decodificação e reprodução. Clock drift, latência, jitter, underrun e overrun
podem causar falhas mesmo quando o arquivo é válido.

## Metadados

Containers de áudio podem carregar artista, álbum, título, capa, número de
faixa, idioma, loudness e timestamps. Esses campos não alteram as amostras e
podem ser removidos ou reescritos em uma conversão. Trate nomes, letras e capas
como dados externos quando o arquivo vier de um usuário.
