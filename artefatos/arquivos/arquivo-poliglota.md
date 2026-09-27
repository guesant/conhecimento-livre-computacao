# Arquivo poliglota

Um arquivo poliglota é uma sequência de bytes que pode ser aceita por dois ou
mais parsers como formatos diferentes. Isso pode acontecer por coincidência,
por uma região de bytes ignorada por um parser, por sobreposição de estruturas
ou por uma técnica deliberada de exploração.

## Como a ambiguidade surge

Parsers podem examinar apenas o início do arquivo, procurar estruturas em
offsets diferentes ou ignorar dados adicionais depois do fim lógico. Um prefixo
válido para uma imagem pode coexistir com um sufixo interpretado por outro
formato. Um documento pode carregar uma estrutura de script, archive ou payload
que outra ferramenta extrai.

Ser aceito por dois leitores não significa necessariamente que o arquivo seja
malicioso. O risco aparece quando componentes diferentes validam e executam
camadas diferentes do mesmo byte stream, produzindo uma confusão de tipos ou
uma divergência entre o que foi inspecionado e o que será executado.

## Riscos

Arquivos poliglotas podem contornar validação de upload baseada em extensão,
MIME ou magic bytes. Também podem explorar diferenças entre antivírus, proxy,
CDN, parser de thumbnail, navegador, extractor de archive e serviço final.

O problema é agravado quando uma aplicação salva o arquivo com um nome
executável, descomprime conteúdo sem limites, gera preview com uma biblioteca
vulnerável ou envia o mesmo byte stream para vários consumidores com políticas
distintas.

## Defesa

Valide o formato pelo parser que será usado no próximo estágio, não apenas por
um detector genérico. Se o sistema aceita uma imagem, decodifique e re-encode
para um formato permitido, remova metadados desnecessários e descarte bytes
que não pertencem à saída canônica.

Mantenha uploads fora de diretórios executáveis, use nomes gerados pelo sistema,
limite tamanho e tempo de parsing, desabilite delegates não necessários e
execute conversores em sandbox. Rejeite estruturas ambíguas quando a política
de segurança exigir uma representação única.

Em gateways e pipelines, defina quem é a autoridade sobre o tipo do arquivo.
O proxy, o scanner, o gerador de preview e o serviço final devem concordar
sobre o formato e sobre o que é considerado conteúdo. Registre os hashes do
original e do derivado para investigar divergências.

## Pesquisa

O estudo de formatos incomuns é útil para compreender parsers, fronteiras de
validação e exploração de ambiguidade. O material [Funky File Formats, de Ange
Albertini](https://youtu.be/hdCs6bPM4is) apresenta exemplos didáticos, mas um
ambiente de teste isolado continua sendo necessário para experimentar arquivos
malformados.
