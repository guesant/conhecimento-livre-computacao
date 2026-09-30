# Adminer

Adminer é uma interface web pequena para administrar bancos de dados. A distribuição tradicional é um único arquivo PHP, o que reduz o custo de instalação e facilita colocar a ferramenta temporariamente em um ambiente controlado.

## Fronteira

Adminer é uma interface administrativa, não um componente de aplicação nem uma camada de compatibilidade entre bancos. O conjunto de recursos e a sintaxe disponível dependem do driver e do banco acessado.

## Quando usar

Ele é útil para uma inspeção ou operação pontual em um ambiente pequeno, especialmente quando a simplicidade de implantação importa mais que recursos colaborativos. A versão e a origem do arquivo devem ser controladas como qualquer outro artefato PHP.

## Segurança

Não exponha o endpoint publicamente. Restrinja a rede, use autenticação externa quando possível, conceda privilégios mínimos e remova a instância quando a tarefa terminar. Uma ferramenta simples continua tendo capacidade de alterar ou apagar dados.

## Fonte primária

- [Adminer](https://www.adminer.org/)
