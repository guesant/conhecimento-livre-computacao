# phpMyAdmin

phpMyAdmin é uma interface web em PHP para administrar MySQL e MariaDB. Ele permite explorar bancos, executar consultas, alterar objetos e importar ou exportar dados pela interface ou por recursos de automação suportados pelo projeto.

## Fronteira

O phpMyAdmin é especializado nesses bancos e não é um cliente universal. A aplicação acessa o servidor com uma conta própria, portanto a segurança efetiva depende da combinação entre privilégios do banco, autenticação web, rede e configuração do servidor.

## Quando usar

Ele é adequado quando a equipe já opera MySQL ou MariaDB e precisa de uma interface administrativa conhecida. Para apenas gerar documentação de schema, use uma ferramenta de leitura como [SchemaSpy](schemaspy.md) ou [SchemaCrawler](schemacrawler.md).

## Segurança

A interface deve ficar em rede administrativa, com autenticação forte, atualização regular e privilégios mínimos. O histórico de consultas e as exportações podem conter dados sensíveis; retenção e acesso a esses artefatos precisam fazer parte da política do banco.

## Fonte primária

- [phpMyAdmin documentation](https://docs.phpmyadmin.net/)
