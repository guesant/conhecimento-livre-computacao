# Compressão

Compressão reduz a representação de dados explorando redundância, padrões,
probabilidade e percepção. Ela pode ser sem perdas, quando o dado original é
reconstruído exatamente, ou com perdas, quando parte da informação é removida
para reduzir tamanho e custo.

## Mapa

- [Compressão de dados](compressao-de-dados.md) explica o problema, métricas e
  trade-offs.
- [Algoritmos de compressão](algoritmos.md) explica famílias como LZ,
  Huffman, arithmetic coding e transformadas.
- [Formatos de compressão](formatos.md) explica gzip, ZIP, Brotli, Zstandard,
  xz e a diferença entre archive e compressor.

Compressão não é criptografia. Um compressor tenta representar o mesmo dado de
forma menor; ele não deve ser usado para esconder conteúdo. Compressão também
não garante integridade, autenticidade ou proteção contra conteúdo malformado.
