# CloudBeaver

CloudBeaver é uma interface web para acessar e administrar bancos de dados, derivada do ecossistema DBeaver. O servidor concentra conexões, autenticação e recursos de colaboração, enquanto o navegador apresenta a exploração de schemas, consultas e resultados.

## Fronteira

CloudBeaver é uma ferramenta de acesso administrativo, não um proxy de banco para aplicações. As credenciais usadas pela interface devem ser separadas das credenciais de runtime, e permissões de escrita devem ser concedidas somente quando a tarefa realmente exige alteração.

## Quando usar

Ele faz sentido quando uma equipe precisa de uma interface web para múltiplos bancos, com usuários e conexões gerenciados centralmente. É mais pesado que uma ferramenta de arquivo único, mas oferece uma superfície mais próxima de um ambiente compartilhado de administração.

## Riscos operacionais

A interface pode executar SQL destrutivo com as permissões da conexão. Coloque-a em uma rede administrativa, exija autenticação e registre o acesso. Para documentação automática de schema, prefira [SchemaSpy](schemaspy.md) ou [SchemaCrawler](schemacrawler.md), que podem operar com credenciais somente leitura.

## Fonte primária

- [CloudBeaver documentation](https://dbeaver.com/docs/cloudbeaver/)
