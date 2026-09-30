# awk

`awk` interpreta uma linguagem orientada a registros e campos. O programa define padrões e ações; para cada registro de entrada, as regras correspondentes executam e podem selecionar, transformar, agregar ou formatar dados.

## Modelo de execução

```bash
awk '{ print $1, $3 }' access.log
awk -F: '{ print $1 }' /etc/passwd
awk '$3 > 100 { total += $3 } END { print total }' data.tsv
```

Por padrão, `$0` representa o registro inteiro, `$1`, `$2` e os demais campos representam as partes separadas pelo espaço, e `NF` informa a quantidade de campos. `-F` escolhe o separador. A regra `END` executa depois do último registro, o que a torna útil para totais e relatórios.

## Casos apropriados

`awk` é adequado para relatórios pequenos, sumarização de logs, transformação de tabelas e extração de colunas. Ele também pode manter arrays associativos e funções, mas um programa que cresce muito deve ser reavaliado como um candidato a uma linguagem de uso geral, especialmente quando precisa de testes, bibliotecas ou tratamento complexo de erros.

## Portabilidade

O `awk` POSIX fornece uma base comum. `gawk`, a implementação GNU, adiciona extensões como `gensub` e recursos de rede. Se um script deve rodar em macOS, BSD e Linux, mantenha-se no subconjunto portátil ou declare `gawk` como dependência.

## Limites

Como `awk` opera sobre registros, ele não deve ser usado para interpretar estruturas aninhadas sem uma gramática apropriada. Para JSON, use `jq`; para YAML, use `yq`. Também não confunda uma soma produzida por `awk` com uma validação: entrada malformada precisa ser detectada explicitamente.

## Fontes primárias

- [GNU awk](https://www.gnu.org/software/gawk/)
- [Guia do usuário do GNU awk](https://www.gnu.org/software/gawk/manual/gawk.html)
- [Padrão POSIX para awk](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html)
