# Ferramentas de bancos

Ferramentas de banco ocupam fronteiras diferentes. Algumas administram dados por uma interface web, enquanto outras apenas descobrem metadata, geram documentação ou produzem diagramas do schema. Colocar todas sob o nome genérico de "administração" esconde diferenças de privilégio, exposição e finalidade.

## Administração interativa

[CloudBeaver](cloudbeaver.md) oferece uma interface web multiusuário baseada no ecossistema DBeaver. [Adminer](adminer.md) prioriza simplicidade e distribuição pequena. [phpMyAdmin](phpmyadmin.md) é especializado na administração de MySQL e MariaDB.

Essas interfaces devem ficar atrás de autenticação forte e de uma rede administrativa. Elas não devem ser expostas diretamente como parte da superfície pública de uma aplicação.

## Documentação e descoberta

[SchemaSpy](schemaspy.md) e [SchemaCrawler](schemacrawler.md) leem metadata por conexão JDBC ou por suas APIs para produzir documentação, diagramas e relatórios. Eles não substituem migrações nem devem ser confundidos com ferramentas de administração interativa.

## Critérios de escolha

Escolha pela operação necessária, pelo suporte ao banco, pelo modelo de autenticação, pela capacidade de executar alterações e pelo modo de publicação do resultado. Para somente documentar o schema, uma ferramenta de descoberta com acesso de leitura reduz o risco em comparação com uma interface capaz de alterar dados.
