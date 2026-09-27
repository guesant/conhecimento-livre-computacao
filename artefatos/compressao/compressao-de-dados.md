# Compressão de dados

Compressão de dados transforma uma representação em outra menor ou mais
adequada ao transporte. O ganho vem de redundância estatística, repetição,
estrutura, previsibilidade ou características perceptuais do conteúdo.

## Sem perdas

Na compressão sem perdas, descomprimir produz exatamente os mesmos bytes. Ela é
necessária para código, bancos de dados, documentos, arquivos de configuração,
imagens técnicas e qualquer dado em que uma alteração seja inaceitável.

O ganho depende do conteúdo. Texto repetitivo comprime bem; dados já
comprimidos, criptografados ou aleatórios normalmente não. Tentar comprimir
novamente pode aumentar tamanho por causa dos cabeçalhos e do custo de
processamento.

## Com perdas

Na compressão com perdas, o encoder descarta informação de acordo com um
modelo. Codecs de imagem, áudio e vídeo podem explorar limites perceptuais,
frequência espacial, mascaramento e redundância temporal. A qualidade depende
do conteúdo e não pode ser resumida apenas por um número de bitrate.

Transcodificação repetida pode acumular artefatos. Preserve uma fonte sem
perdas quando o arquivo ainda será editado, analisado ou convertido para outras
variantes.

## Métricas

Avalie taxa de compressão, tamanho final, tempo de encode, tempo de decode,
latência, uso de CPU, memória, paralelismo, compatibilidade e recuperação de
erros. Em serviços, o custo total inclui I/O, bandwidth, armazenamento, cache e
energia, não apenas o tamanho do arquivo.

Para mídia, compare qualidade perceptual, SSIM, PSNR ou métricas específicas com
inspeção humana. Uma métrica isolada pode favorecer artefatos que são visíveis
ou audíveis no produto real.

## Segurança

Descomprimir pode expandir poucos bytes para uma saída enorme. Isso é relevante
para archives, imagens, documentos e protocolos comprimidos. Defina limite de
razão de expansão, tamanho total, número de entradas, profundidade, tempo de
CPU e espaço temporário.

Não use compressão como mecanismo de confidencialidade. Em protocolos que
combinam compressão e segredo, avalie vazamentos por tamanho e ataques de
compressão antes de habilitar o recurso.
