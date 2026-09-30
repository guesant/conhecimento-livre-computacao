# Arquivos

Arquivos são containers de bytes persistidos em um filesystem, transportados
por uma rede ou incorporados em outro artefato. O formato descreve como esses
bytes devem ser interpretados. O filesystem fornece nome, permissões, tamanho,
timestamps e blocos; o formato interno fornece cabeçalhos, registros,
índices, streams e metadados.

## Mapa

- [Formato de arquivo](formato-de-arquivo.md) explica assinatura, cabeçalho,
  payload, offsets, framing e versionamento.
- [Estrutura binária](estrutura-binaria.md) explica regiões, endianness,
  alinhamento e referências internas.
- [Arquivo executável](executavel.md) compara ELF, PE, Mach-O, scripts e
  bytecode.
- [Metadados binários](metadados-binarios.md) explica informações descritivas
  internas e externas ao payload.
- [Arquivo poliglota](arquivo-poliglota.md) explica arquivos válidos em mais de
  um parser e seus riscos.

Um arquivo não precisa ter uma estrutura única. Containers como ZIP, PDF e
formatos de mídia podem conter entradas, streams ou objetos internos. A análise
deve começar identificando o formato externo e depois verificar cada camada
aninhada.

## Identificação e validação

Use a extensão para orientar a escolha inicial, não para aceitar entrada. Uma
identificação mais confiável combina magic bytes, tamanho mínimo, versão,
estrutura interna, checksum e um parser que rejeite inconsistências.

```bash
file artefato
xxd -l 32 artefato
```

Para formatos conhecidos, prefira uma ferramenta específica. Um hexdump ajuda a
investigar, mas não substitui validação estrutural. Em upload de usuário,
registre o tipo detectado, normalize o nome, limite o tamanho e mantenha o
arquivo fora de diretórios executáveis.

## Referências relacionadas

- [Inspeção de binários](../../sistemas/linux/binarios/index.md) cobre `file`,
  `readelf`, `ldd`, `strip` e `xxd`.
- [Proveniência](../../seguranca/supply-chain/provenance.md) liga um artefato a
  suas entradas e ao build.
- [Builds reproduzíveis](../../seguranca/supply-chain/reproducible-builds.md)
  explica como obter artefatos equivalentes.
