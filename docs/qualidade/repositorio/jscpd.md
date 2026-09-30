# jscpd

jscpd é um detector de duplicação baseado em tokens. Ele compara blocos de arquivos e reporta clones que ultrapassam os limites de linhas e tokens configurados. O resultado é um sinal para revisão arquitetural, não uma prova de que toda repetição deve ser abstraída.

## Configuração de um projeto

O relatório pode ser gerado em um container por uma receita de automação. A configuração pode analisar YAML, ignorar templates, exigir um mínimo de linhas e tokens e produzir uma saída separada. O check é informativo quando parte da repetição entre wrappers e roles é estruturalmente intencional.

## Limitações

Tokens não entendem equivalência semântica. Duas funções que calculam o mesmo resultado com algoritmos diferentes podem ser Type-4 e não aparecer no relatório. Inversamente, duas estruturas parecidas podem ter responsabilidades diferentes. O relatório precisa ser lido junto da arquitetura e do contexto de manutenção.

## Fonte primária

- [Tipos de clone](clone-types.md)
- [Como o jscpd detecta duplicação](https://jscpd.dev/guides/how-detection-works)
