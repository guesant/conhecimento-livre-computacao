# grep

`grep` procura padrões em linhas de texto e imprime as linhas que correspondem. Seu modelo é deliberadamente simples: ele não entende a estrutura semântica de JSON, YAML, HTML ou uma linguagem de programação, apenas aplica um mecanismo de correspondência ao fluxo de entrada.

## Operações essenciais

```bash
grep -n "pattern" arquivo.txt
grep -R --include='*.conf' -n "listen" /etc
grep -E '^(warn|error):' application.log
grep -v '^#' config.txt
```

`-n` preserva o número da linha, `-R` percorre diretórios, `--include` limita os arquivos, `-E` habilita expressões regulares estendidas e `-v` inverte a seleção. Use `--` antes dos nomes quando um caminho puder começar com hífen.

## Limites

Uma correspondência textual não prova que o valor está ativo. Um comentário, uma string, uma variável ou uma linha de log podem conter o mesmo texto sem exercer a responsabilidade procurada. O mesmo problema aparece quando `grep` é usado para extrair campos de JSON ou YAML: quebras de linha, escapes e valores aninhados podem produzir resultados incorretos.

Use `grep` para localizar, filtrar e criar evidência inicial. Quando a decisão depende da estrutura, use o parser adequado. Em pipelines, trate o código de saída com cuidado, pois nenhum resultado e erro de leitura são situações diferentes.

## Portabilidade

A sintaxe básica é amplamente portátil, mas opções e extensões variam entre GNU grep, BSD grep e outras implementações. Se o script depende de `-P`, de uma semântica específica de locale ou de expressões avançadas, documente e valide a implementação exigida.

## Fontes primárias

- [GNU grep](https://www.gnu.org/software/grep/)
- [Manual do GNU grep](https://www.gnu.org/software/grep/manual/grep.html)
- [Padrão POSIX para grep](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/grep.html)
