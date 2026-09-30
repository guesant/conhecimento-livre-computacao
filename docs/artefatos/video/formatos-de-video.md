# Formatos de vídeo

Um formato de vídeo pode designar um container, um codec ou o conjunto de
parâmetros usados na codificação. Separar essas camadas é essencial para
escolher uma ferramenta e diagnosticar incompatibilidade.

| Container | Codecs comuns | Uso típico |
| --- | --- | --- |
| MP4 | H.264, H.265, AAC, AV1 em combinações suportadas | Distribuição geral e dispositivos variados |
| Matroska | Muitos codecs de áudio, vídeo e legendas | Arquivo flexível e preservação de múltiplos streams |
| WebM | VP8, VP9, AV1 e Opus, conforme o perfil | Web e ecossistema aberto |
| MOV | Codecs do ecossistema QuickTime e outros | Produção e fluxos Apple |
| MPEG-TS | MPEG-2, H.264 e outros perfis | Broadcast e transporte segmentado |
| Ogg | Theora, Vorbis e outros | Ecossistema aberto e casos específicos |

## Codecs e frames

H.264, H.265, VP9 e AV1 usam frames intra e inter, previsão de movimento,
transformação, quantização e codificação estatística. Frames I, P e B têm custos
e dependências diferentes. Keyframes são pontos importantes para seek,
segmentação e recuperação.

O bitrate, o preset, o perfil, o nível, a resolução, o framerate e o conteúdo
alteram a qualidade e o custo. Um codec mais eficiente pode exigir mais CPU
para codificar ou decodificar e pode não estar disponível no hardware alvo.

## Compatibilidade

Escolha um conjunto de codecs que o navegador, sistema, dispositivo e
acelerador realmente suportem. Um container válido pode carregar um codec que o
cliente não sabe decodificar. Use `ffprobe` para inspecionar streams, perfis,
timestamps e metadata antes de diagnosticar um erro como se fosse apenas MIME.

## Preservação

Para preservação, mantenha a fonte original, o container, codecs, metadata,
checksums e informações sobre o software de criação. Uma cópia transcodificada
é um novo artefato e não substitui o original. Verifique também licenças e
patentes aplicáveis ao codec e ao território de distribuição.
