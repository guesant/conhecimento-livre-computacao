# sed

`sed` é um editor de fluxo. Ele lê a entrada, mantém um espaço de padrão, aplica um programa em ordem e escreve o resultado. Seu desenho favorece transformações lineares e repetíveis em pipelines, sem abrir um editor interativo.

## Substituição e seleção

```bash
sed 's/old/new/g' arquivo.txt
sed -n '1,20p' arquivo.txt
sed '/^#/d' config.txt
sed -E 's/[[:space:]]+$//' arquivo.txt
```

O comando `s` substitui texto, `-n` desativa a impressão implícita e `p` imprime somente as linhas selecionadas, enquanto `d` remove do fluxo de saída as linhas que correspondem. Expressões regulares, delimitadores e regras de escaping devem ser escolhidos considerando a entrada real.

## Edição in-place

`sed -i` altera o arquivo no lugar, mas sua sintaxe não é uniforme entre GNU sed e BSD sed. Em ambientes portáveis, prefira gerar um arquivo temporário, validar o resultado e só então substituir o original. Se usar `-i`, fixe a implementação e teste o comportamento do sufixo de backup.

Uma transformação destrutiva deve ser feita sobre um arquivo identificado de forma explícita. Antes de aplicá-la em massa, faça uma amostra, preserve o diff e interrompa se a quantidade de correspondências não for a esperada.

## Limites

`sed` não é um parser geral. É possível escrever programas complexos, mas a manutenção e a portabilidade se deterioram rapidamente. Para uma estrutura aninhada, use o parser correspondente; para uma agregação por campos, `awk` costuma expressar melhor a intenção.

## Fontes primárias

- [GNU sed](https://www.gnu.org/software/sed/)
- [Introdução ao GNU sed](https://www.gnu.org/software/sed/manual/html_node/Introduction.html)
- [Programas sed](https://www.gnu.org/software/sed/manual/html_node/sed-Programs.html)
- [Padrão POSIX para sed](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/sed.html)
