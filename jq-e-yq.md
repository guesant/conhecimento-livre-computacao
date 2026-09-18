# jq e yq: consulta estruturada de JSON e YAML

`grep` e `sed`, cobertos em [Coreutils e documentação](coreutils-e-documentacao.md), tratam qualquer arquivo como texto plano, uma sequência de linhas sem estrutura conhecida; isso funciona bem para log e texto solto, mas se torna frágil contra um documento estruturado como JSON ou YAML, onde o mesmo valor lógico pode aparecer formatado em mais de uma linha, ou onde um campo aninhado dentro de outro não tem uma forma confiável de ser isolado só com correspondência de padrão de texto. `jq` resolve isso para JSON, e `yq` estende a mesma abordagem para YAML: os dois entendem a estrutura real do documento (objetos, arrays, tipos) e permitem navegar, filtrar e transformar essa estrutura através de uma linguagem de consulta própria, em vez de tratar o arquivo como texto solto.

## Navegar e filtrar

A operação mais básica de `jq` é navegar um caminho dentro do documento: `jq '.metadata.name'` extrai o campo `name` de dentro de `metadata`, de forma confiável independentemente de como o JSON foi formatado (numa linha só ou espalhado por várias, com indentação diferente). Filtros mais ricos selecionam elementos de um array que satisfazem uma condição (`jq '.items[] | select(.status == "Running")'`, por exemplo, filtrando só os itens com um campo específico), o tipo de consulta que exigiria um script inteiro para replicar de forma confiável usando só correspondência de texto. `yq` replica a mesma sintaxe de consulta para documentos YAML, o que faz sentido dado que YAML é, na prática, um superconjunto de JSON na maioria dos casos de uso comuns; quem já sabe escrever uma consulta `jq` transporta esse conhecimento quase diretamente para `yq`.

## Transformar, não só ler

Além de extrair um valor, as duas ferramentas conseguem modificar o documento e emitir um novo, o que as torna adequadas para automação que precisa editar um arquivo de configuração estruturado sem reescrever o arquivo inteiro à mão: atualizar um único campo de versão dentro de um `values.yaml` grande, por exemplo, preservando o restante do arquivo intacto. Isso é mais seguro do que uma substituição de texto ingênua (via `sed`, por exemplo), que não tem como garantir que só o campo pretendido foi alterado, especialmente quando o mesmo valor aparece em mais de um lugar do documento por coincidência.

## O limite: um scanner de segurança, uma ferramenta de consulta não é

Vale notar o que `jq`/`yq` não fazem: nenhum dos dois valida o documento contra um schema, nem verifica política de segurança, papéis que cabem a [kubeconform e conftest](kubeconform-e-conftest.md); `jq`/`yq` só entendem a estrutura sintática do documento (é um objeto, é um array, este campo existe), sem noção nenhuma do que o conteúdo deveria ser para ser considerado válido ou seguro.

## Continue por aqui

[Coreutils e documentação](coreutils-e-documentacao.md) cobre `grep` e `sed`, o processamento de texto plano que `jq`/`yq` substituem quando o alvo é um documento estruturado. [kubeconform e conftest](kubeconform-e-conftest.md) cobre a camada de validação que uma consulta estruturada, sozinha, não substitui.
