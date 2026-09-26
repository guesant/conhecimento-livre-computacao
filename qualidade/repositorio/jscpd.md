# jscpd

jscpd é um detector de duplicação baseado em tokens. Ele compara blocos de arquivos e reporta clones que ultrapassam os limites de linhas e tokens configurados. O resultado é um sinal para revisão arquitetural, não uma prova de que toda repetição deve ser abstraída.

## Configuração deste repositório

O relatório é gerado em container por `just quality-jscpd`. A configuração em `.config/jscpd.json` analisa YAML das roles do Ansible, ignora templates, exige pelo menos 8 linhas e 70 tokens e produz saída em `.build/jscpd-report/`. O check é informativo porque parte da repetição entre charts wrapper e roles é estruturalmente intencional.

## Limitações

Tokens não entendem equivalência semântica. Duas funções que calculam o mesmo resultado com algoritmos diferentes podem ser Type-4 e não aparecer no relatório. Inversamente, duas estruturas parecidas podem ter responsabilidades diferentes. O relatório precisa ser lido junto da arquitetura e do contexto de manutenção.

## Fonte primária

- [Tipos de clone](clone-types.md)
- [Como o jscpd detecta duplicação](https://jscpd.dev/guides/how-detection-works)
