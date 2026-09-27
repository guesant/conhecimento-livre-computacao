# Formatos de áudio

Formato de áudio pode significar o container, o codec ou a representação das
amostras. Um arquivo WAV normalmente contém PCM, mas o container pode carregar
outras codificações. MP4 pode carregar streams de áudio junto com vídeo. O
nome do arquivo não é suficiente para decidir como decodificar.

| Formato ou codec | Categoria | Uso e trade-off |
| --- | --- | --- |
| WAV | Container | Simples, frequentemente PCM, arquivos grandes |
| AIFF | Container | PCM e metadata, comum em fluxos Apple e produção |
| FLAC | Codec sem perdas | Reduz tamanho preservando amostras originais |
| MP3 | Codec com perdas | Compatibilidade ampla, eficiência histórica |
| AAC | Codec com perdas | Boa eficiência em distribuição e streaming |
| Opus | Codec com perdas | Voz e música, baixa latência e uso em tempo real |
| Vorbis | Codec com perdas | Ecossistema aberto e uso em containers como Ogg |
| Ogg | Container | Pode carregar Vorbis, Opus e outros streams |

## Sem perdas e com perdas

Codec sem perdas permite reconstruir as amostras originais. Ele explora
redundância estatística sem descartar informação, mas o tamanho depende da
carga. Codec com perdas usa um modelo perceptual para descartar detalhes que
podem ser menos audíveis, reduzindo tamanho ao custo de fidelidade.

Transcodificar repetidamente com perdas acumula artefatos. Preserve uma fonte
sem perdas quando houver necessidade de edição, masterização, evidência ou
reprocessamento futuro. Para distribuição, escolha o codec e o bitrate de
acordo com latência, qualidade, rede e compatibilidade do cliente.

## Streaming

Streaming precisa tratar duração, timestamps, sincronização, buffers, bitrate,
mudança de qualidade e perda de pacotes. Um arquivo para download pode tolerar
um índice no final; um fluxo ao vivo precisa de metadata e segmentação que
permitam iniciar e recuperar a reprodução.

Não confunda codec com transporte. RTP, WebRTC, HLS, DASH, HTTP e containers
resolvem partes diferentes do problema. O mesmo codec pode aparecer em
transporte e containers distintos.

## Segurança

Decodificadores processam bytes complexos e podem consumir CPU e memória de
forma desproporcional. Limite duração, canais, sample rate, tamanho
descomprimido e número de streams. Mantenha bibliotecas atualizadas e use
processos isolados para conteúdo não confiável.
