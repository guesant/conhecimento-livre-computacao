# Formato de arquivo

Um formato de arquivo é um contrato que define como uma sequência de bytes
representa dados. O contrato pode definir assinatura, cabeçalhos, campos,
ordem dos bytes, offsets, alinhamento, checksum, compressão, codificação,
extensões e regras de evolução.

## Estrutura comum

Muitos formatos possuem uma assinatura ou magic number, uma versão, parâmetros
de tamanho e um payload. Alguns adicionam uma tabela de offsets ou índices para
encontrar partes do arquivo sem percorrer tudo. Outros usam framing, em que
cada registro informa o seu tamanho ou termina com um marcador.

Um parser robusto não deve confiar apenas em um tamanho declarado. Ele deve
verificar overflow, limites, offsets sobrepostos, recursão, campos obrigatórios,
versão suportada e coerência entre o cabeçalho e os dados disponíveis.

## Texto, binário e containers

Formato textual costuma favorecer inspeção humana e interoperabilidade, mas não
é automaticamente mais seguro ou mais simples. JSON, YAML, CSV e XML possuem
regras próprias e precisam de parsers adequados. Formato binário pode ser mais
compacto e rápido, mas exige uma especificação precisa e tratamento de
endianness, alinhamento e compatibilidade.

Um container reúne partes internas. MP4 possui streams de mídia, ZIP possui
entradas e ELF possui segmentos e seções. O container pode carregar dados
comprimidos, não comprimidos ou codificados por outra especificação. O nome do
container não identifica necessariamente o codec ou a representação final.

## Versionamento

Um formato evolui adicionando campos opcionais, extensões, novos tipos ou uma
versão incompatível. O leitor deve decidir se ignora, rejeita ou preserva
campos desconhecidos. O escritor precisa declarar qual versão gera e não
produzir combinações que leitores antigos interpretam incorretamente.

Compatibilidade de leitura, compatibilidade de escrita e compatibilidade de
round trip são propriedades diferentes. Um leitor novo pode aceitar arquivos
antigos sem que um escritor novo produza arquivos que leitores antigos
entendam.

## Integridade e confiança

Checksum detecta parte das alterações acidentais. Hash e assinatura podem
estabelecer integridade e origem quando a chave ou o valor esperado vêm de uma
fonte confiável. Nenhuma dessas propriedades garante que o parser seja seguro
ou que o conteúdo seja benigno.

Ao receber um arquivo, preserve o original, registre o tipo detectado, valide a
estrutura antes de processar e execute a transformação em uma fronteira com
limites de CPU e memória. Não derive confiança da extensão, do MIME declarado
ou do nome enviado pelo cliente.

## Materiais relacionados

- [What is a File Format?](https://youtu.be/VVdmmN0su6E)
- [Funky File Formats, Ange Albertini](https://youtu.be/hdCs6bPM4is)
- [Magic numbers](https://en.wikipedia.org/wiki/List_of_file_signatures)
