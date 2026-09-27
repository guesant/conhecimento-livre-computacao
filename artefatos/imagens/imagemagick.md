# ImageMagick

ImageMagick é uma suíte open source para criar, converter, identificar,
compor, redimensionar e manipular imagens. Ela oferece ferramentas de linha de
comando, APIs e suporte a muitos formatos. A suíte é escrita em C e depende de
delegates e bibliotecas que ampliam o conjunto de formatos e operações.

## Ferramentas

Em instalações atuais, `magick` é a entrada principal para várias operações.
`identify` inspeciona propriedades, `mogrify` transforma arquivos em lote e
`convert` aparece em documentação legada. Verifique a versão instalada antes
de copiar comandos, pois a interface e os nomes mudam entre ImageMagick 6 e 7.

```bash
magick identify foto.jpg
magick foto.jpg -resize 1200x1200\> -strip foto-web.jpg
magick entrada.png -format webp saida.webp
```

Redimensionar, recortar, compor, converter espaço de cor, aplicar filtros e
gerar animações são operações diferentes. A qualidade depende do filtro, do
perfil de cor, da profundidade, da transparência e das opções do encoder.

## Delegates e formatos

ImageMagick pode chamar bibliotecas ou programas externos para alguns formatos.
Isso amplia a capacidade, mas também aumenta a superfície de ataque e a
complexidade de instalação. Uma política de segurança deve permitir somente os
coders, delegates, paths e recursos necessários ao serviço.

Arquivos recebidos de usuários precisam de limites de largura, altura, pixels,
frames, memória, tempo, threads e tamanho de saída. Não habilite delegates
desnecessários para aceitar uma extensão nova sem revisar o risco.

## Metadados

Operações podem preservar, alterar ou remover EXIF, XMP, perfis ICC, comentários
e outros campos. `-strip` remove metadata que a ferramenta considere removível,
mas não deve ser assumido como anonimização completa. Confira o arquivo gerado
com uma ferramenta de inspeção e mantenha o original conforme a política de
retenção.

## Uso em produção

Prefira executar ImageMagick em um worker ou processo isolado, com filesystem
temporário, usuário sem privilégios e quotas. Normalize o formato antes de
servir previews e não permita que nomes de arquivos ou caminhos enviados pelo
cliente definam o destino de escrita.

Para pipelines grandes, avalie custo de CPU, memória, I/O e paralelismo. A
conversão de uma imagem pequena e a decodificação de uma imagem comprimida com
dimensões enormes são cargas muito diferentes.

## Relações

- [Formatos de imagem](formatos-de-imagem.md) explica as propriedades que a
  ferramenta precisa preservar.
- [EXIF](exif.md) trata de metadata de câmeras.
- [Sharp](sharp.md) é uma alternativa integrada a aplicações JavaScript.

## Fontes primárias

- [ImageMagick](https://imagemagick.org/)
- [ImageMagick security policy](https://imagemagick.org/script/security-policy.php)
- [ImageMagick usage](https://imagemagick.org/Usage/)
