# Algoritmos de compressão

Algoritmos de compressão normalmente combinam uma etapa que encontra padrões
com uma etapa que representa símbolos com menos bits. A escolha depende do tipo
de dado, do custo aceitável e da necessidade de reconstrução exata.

## Codificação estatística

Huffman atribui códigos menores aos símbolos mais frequentes. Ele é simples,
rápido e aparece em formatos como DEFLATE, mas sua eficiência depende da
distribuição e da granularidade dos símbolos.

Arithmetic coding e range coding representam uma sequência como um intervalo
de probabilidade. Eles podem se aproximar melhor do modelo estatístico, mas
exigem mais cuidado com precisão, desempenho e implementação.

Codificações como RLE representam repetições explicitamente. São eficazes em
imagens simples, máscaras e dados com longas sequências iguais, mas podem
aumentar o tamanho de dados sem repetição.

## Famílias LZ

LZ77 mantém uma janela de dados anteriores e substitui repetições por pares de
distância e comprimento. LZ78 e LZW constroem dicionários de frases vistas no
fluxo. Essas famílias são rápidas e servem de base para formatos como
DEFLATE, gzip, ZIP, LZMA e vários codecs.

O tamanho da janela, o dicionário, a busca de matches e o nível de esforço
alteram taxa de compressão, memória e CPU. Um nível máximo pode ser inadequado
para uma API síncrona ou para um worker com concorrência alta.

## Transformadas e compressão perceptual

JPEG usa transformação por blocos, quantização e codificação estatística para
reduzir imagens com perdas. Codecs de áudio e vídeo também usam transformadas,
modelos perceptuais e previsão temporal. Essas técnicas não são equivalentes a
gzip, porque alteram o domínio e podem descartar informação.

A qualidade deve ser avaliada junto com resolução, framerate, sample rate,
perfil de cor, bitrate e conteúdo. Um algoritmo mais eficiente pode custar
mais CPU ou ter suporte menor em hardware e navegadores.

## Escolha do algoritmo

Use compressão sem perdas para bytes que precisam voltar exatamente. Escolha
codec com perdas quando o domínio tolerar aproximação e o ganho de tamanho for
mais importante que a preservação integral. Para dados de rede, considere
latência, ganho real, bomb-out, compatibilidade e possibilidade de atacar o
decodificador.

Benchmarks devem usar amostras representativas, medir warmup e separar encode
de decode. Não compare apenas o tamanho de um arquivo pequeno, pois cabeçalhos,
dicionários e metadados podem dominar o resultado.
