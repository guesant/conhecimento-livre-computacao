# Processamento de texto no Unix

`grep`, `sed` e `awk` formam uma família de ferramentas de linha de comando para selecionar texto, transformar fluxos e produzir relatórios. Elas trabalham bem com pipes e arquivos pequenos ou médios, mas não devem ser usadas como substitutas automáticas de um parser quando a entrada possui uma gramática estruturada, como JSON, YAML ou código-fonte.

## Divisão de responsabilidades

[grep](grep.md) procura linhas que correspondem a padrões. [sed](sed.md) aplica transformações programáveis a um fluxo de texto. [awk](awk.md) interpreta uma linguagem própria para filtrar registros, extrair campos e produzir relatórios.

Uma composição típica seleciona com `grep`, transforma com `sed` e agrega com `awk`, mas a divisão não é uma regra obrigatória. A escolha deve considerar se a entrada é realmente textual, se há necessidade de preservar sintaxe e se o resultado será consumido por outra ferramenta.

## Portabilidade

Linux frequentemente usa as implementações GNU, enquanto BSD e macOS podem fornecer implementações com opções diferentes. Evite depender de extensões GNU quando o script precisa rodar em vários sistemas, declare a dependência quando ela for necessária e teste o script sob o ambiente que realmente o executará.

Para JSON e YAML, prefira [jq](../../../ferramentas/dados-estruturados/jq.md) e [yq](../../../ferramentas/dados-estruturados/yq.md). Para código, prefira ferramentas que conheçam a linguagem, como compiladores, formatadores e analisadores sintáticos.

## Fontes primárias

- [GNU grep](https://www.gnu.org/software/grep/)
- [GNU sed](https://www.gnu.org/software/sed/)
- [GNU awk](https://www.gnu.org/software/gawk/)
- [Padrão POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/)
