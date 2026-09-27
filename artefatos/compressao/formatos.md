# Formatos de compressão

Um compressor codifica dados; um archive organiza vários arquivos; um container
de mídia organiza streams. Alguns formatos fazem somente uma dessas funções e
outros combinam duas delas.

| Formato | Papel | Características |
| --- | --- | --- |
| gzip | Compressão de um fluxo | DEFLATE, simples, comum em HTTP e Unix |
| ZIP | Archive e compressão por entrada | Pode armazenar várias entradas e métodos diferentes |
| tar | Archive sem compressão própria | Frequentemente combinado com gzip, xz ou zstd |
| Brotli | Compressão de fluxo | Muito usado para conteúdo web, com níveis e janela próprios |
| Zstandard | Compressão de fluxo e frames | Decode rápido, níveis amplos e dicionários |
| bzip2 | Compressão de fluxo | Boa taxa em alguns dados, custo maior e uso mais específico |
| xz | Compressão baseada em LZMA2 | Alta taxa, decode e memória mais exigentes |
| 7z | Archive com métodos variados | Recursos de archive e compressão, compatibilidade deve ser verificada |

## Archive não é compressor

`tar` preserva uma coleção de entradas, nomes, permissões e outros atributos,
mas tradicionalmente não comprime. `tar.gz` significa um archive tar passado
por gzip. ZIP combina archive e compressão em um formato de entradas. Essa
diferença afeta extração seletiva, streaming, permissões, corrupção parcial e
ferramentas disponíveis.

## HTTP e distribuição

Brotli e gzip podem reduzir HTML, CSS, JavaScript, JSON e texto, mas a escolha
precisa considerar CPU do servidor, cache, negociação do cliente e compressão
já aplicada ao conteúdo. Não comprima novamente JPEG, AVIF, MP4, ZIP ou outros
artefatos já compactados sem medir.

Use `Content-Encoding` para indicar uma codificação de transporte e preserve o
tipo do recurso. Armazene e sirva arquivos com headers coerentes, checksums e
cache control apropriados.

## Integridade e ataques

A compressão não autentica o fluxo. Archives podem conter caminhos absolutos,
`..`, links simbólicos, milhares de entradas ou dados que expandem muito. Ao
extrair, normalize caminhos, rejeite saída fora do diretório alvo, limite
entradas e bytes descomprimidos e valide permissões.

Para artefatos de distribuição, combine checksum ou assinatura com uma política
de proveniência. Verificar que o archive foi descomprimido sem erro não prova que
ele veio da fonte esperada.

## Fontes primárias

- [DEFLATE, RFC 1951](https://www.rfc-editor.org/rfc/rfc1951)
- [GZIP, RFC 1952](https://www.rfc-editor.org/rfc/rfc1952)
- [Brotli, RFC 7932](https://www.rfc-editor.org/rfc/rfc7932)
- [Zstandard format](https://github.com/facebook/zstd/blob/dev/doc/zstd_compression_format.md)
- [XZ file format](https://github.com/tukaani-project/xz/blob/master/doc/file-format.txt)
- [ZIP application note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
