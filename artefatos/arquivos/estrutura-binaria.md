# Estrutura binária

Uma estrutura binária descreve como campos e regiões ocupam bytes. Ela pode
usar inteiros de tamanho fixo, comprimentos variáveis, offsets relativos,
ponteiros lógicos, tabelas de índice, alinhamento e padding. A implementação
precisa diferenciar o endereço dentro do arquivo do endereço na memória.

## Regiões de um artefato

Uma divisão frequente é:

| Região | Função |
| --- | --- |
| Assinatura | Identificar o formato ou a família do parser |
| Cabeçalho | Declarar versão, tamanho, flags e parâmetros |
| Índices | Localizar registros ou streams |
| Payload | Carregar dados de aplicação, imagem, áudio ou código |
| Metadados | Descrever origem, parâmetros, tempo ou ferramentas |
| Integridade | Armazenar checksum, hash ou assinatura |
| Padding | Alinhar regiões ou reservar espaço |

Nem todo formato possui todas as regiões, e a ordem varia. Em ELF, por
exemplo, segmentos são relevantes para o loader e seções são relevantes para
linkers e ferramentas. Em um formato de mídia, índices podem apontar para
frames ou streams. Em um arquivo comprimido, o payload pode conter outra
estrutura depois da descompressão.

## Endianness e representação

Um inteiro de vários bytes pode ser armazenado em little-endian ou big-endian.
Strings podem usar ASCII, UTF-8, UTF-16 ou uma codificação específica. Números
de ponto flutuante, timestamps e identificadores também precisam de uma
representação definida.

Não leia um campo com um tipo nativo da linguagem sem confirmar tamanho,
alinhamento e endianness. Em C e C++, padding de uma struct pode variar entre
arquiteturas. Um parser portátil deve ler bytes explicitamente e validar cada
conversão.

## Offsets e limites

Offsets e tamanhos devem ser tratados como dados não confiáveis. Antes de
calcular `offset + length`, verifique overflow e compare os limites com o
tamanho do arquivo. Rejeite regiões que se sobrepõem de forma impossível,
ponteiros que apontam para o cabeçalho quando não deveriam e referências
recursivas sem limite.

Essas verificações protegem contra truncamento acidental e contra arquivos
construídos para provocar leitura fora dos limites, alocações enormes ou
recursão infinita.

## Diagnóstico

Comece por `file` e um dump pequeno. Depois use o parser oficial ou uma
ferramenta específica para interpretar campos. `xxd` responde quais bytes estão
presentes; `readelf`, `ffprobe`, ExifTool e ferramentas equivalentes respondem
como o formato atribui significado a eles.

Ao documentar um formato, registre a especificação, a versão suportada, a
ordem dos bytes, limites máximos, campos obrigatórios, comportamento diante de
campos desconhecidos e como a integridade é verificada.
