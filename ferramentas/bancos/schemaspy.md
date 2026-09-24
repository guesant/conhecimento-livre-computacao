# SchemaSpy

SchemaSpy é uma ferramenta de documentação de schemas que conecta a um banco, lê metadata e gera páginas HTML, diagramas e relações entre tabelas. O resultado é um artefato consultável e versionável, não uma interface para operar o banco em produção.

## Modelo de execução

O processo usa um driver JDBC e credenciais que devem ter somente o acesso de leitura necessário para metadata. A ferramenta observa tabelas, colunas, chaves, índices e relações que o driver e o banco conseguem expor. O resultado representa o estado observado no momento da execução.

## Quando usar

SchemaSpy é apropriado para publicar documentação técnica junto de uma versão do schema ou para comparar a evolução entre execuções. Ele não substitui a migration que criou uma tabela nem garante que o banco consultado corresponde ao ambiente que a aplicação usa.

## Limitações

Qualidade do diagrama depende da metadata declarada e do suporte do driver. Permissões insuficientes produzem documentação incompleta, enquanto uma credencial ampla aumenta o risco sem melhorar necessariamente o resultado.

## Relações

- [SchemaCrawler](schemacrawler.md) oferece descoberta por CLI e API com outras formas de relatório.
- [CloudBeaver](cloudbeaver.md) administra bancos interativamente, em vez de produzir somente documentação.

## Fonte primária

- [SchemaSpy documentation](https://schemaspy.readthedocs.io/)
