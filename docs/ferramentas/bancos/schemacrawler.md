# SchemaCrawler

SchemaCrawler é uma ferramenta e biblioteca para descobrir e documentar schemas de bancos relacionais. Ela pode ser executada pela linha de comando ou integrada a um programa para produzir diagramas, relatórios e validações baseados na metadata do banco.

## Modelo de execução

O processo conecta-se ao banco por JDBC, lê a estrutura que a conta consegue observar e transforma essa informação em uma saída escolhida. O resultado pode ser filtrado para concentrar tabelas, colunas e relações relevantes para uma equipe ou domínio.

## Quando usar

SchemaCrawler é útil quando a documentação precisa entrar em um pipeline, ser comparada entre ambientes ou ser gerada por código. Como qualquer ferramenta de introspecção, ele documenta o estado observado e não substitui a fonte de verdade das migrations.

## Limitações

A saída depende do driver, das permissões e das opções de inclusão ou exclusão. Uma comparação entre ambientes só é confiável quando as conexões, filtros e versões do gerador permanecem controlados.

## Relações

- [SchemaSpy](schemaspy.md) também gera documentação, mas prioriza um site HTML estático.
- [CloudBeaver](cloudbeaver.md) é uma interface interativa de administração.

## Fonte primária

- [SchemaCrawler](https://www.schemacrawler.com/)
