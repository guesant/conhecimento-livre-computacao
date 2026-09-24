# jscpd e tipos de clone

jscpd é um detector de duplicação baseado em tokens. Ele compara blocos de arquivos e reporta clones que ultrapassam os limites de linhas e tokens configurados. O resultado é um sinal para revisão arquitetural, não uma prova de que toda repetição deve ser abstraída.

## Tipos de clone

| Tipo | Diferença entre cópias | Tratamento no jscpd |
| --- | --- | --- |
| Type-1 | Espaçamento, layout e comentários | Detecção padrão de clones exatos |
| Type-2 | Nomes de identificadores, literais e anotações | Opções como `--ignore-identifiers`, `--ignore-literals` e `--ignore-annotations` |
| Type-3 | Linhas adicionadas, removidas ou alteradas | `--max-gap-lines` e comparação sintática com `--similarity` |
| Type-4 | Mesmo comportamento com implementação diferente | Fora do alcance de um detector baseado em tokens |

Type-1 é o melhor candidato a um gate determinístico, porque o resultado é estável e a repetição costuma ser inequívoca. Type-2 é útil para localizar cópias parametrizadas durante uma refatoração, mas pode capturar padrões legítimos. Type-3 deve ser tratado como investigação e não como prova automática de duplicação arquitetural.

## Configuração deste repositório

O relatório é gerado em container por `just quality-jscpd`. A configuração em `.config/jscpd.json` analisa YAML das roles do Ansible, ignora templates, exige pelo menos 8 linhas e 70 tokens e produz saída em `.build/jscpd-report/`. O check é informativo porque parte da repetição entre charts wrapper e roles é estruturalmente intencional.

## Limitações

Tokens não entendem equivalência semântica. Duas funções que calculam o mesmo resultado com algoritmos diferentes podem ser Type-4 e não aparecer no relatório. Inversamente, duas estruturas parecidas podem ter responsabilidades diferentes. O relatório precisa ser lido junto da arquitetura e do contexto de manutenção.

## Fonte primária

- [Tipos de clone no jscpd](https://jscpd.dev/guides/clone-types)
- [Como o jscpd detecta duplicação](https://jscpd.dev/guides/how-detection-works)
