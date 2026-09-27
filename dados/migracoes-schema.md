# Migrações de schema

Uma migração de schema altera a estrutura persistente enquanto outras conexões podem continuar lendo ou escrevendo. A dificuldade não está apenas no comando DDL, mas na compatibilidade entre versões do código, duração dos locks, tamanho do backfill e possibilidade de rollback.

## Colunas, defaults e constraints

Adicionar uma coluna simples costuma ser compatível quando o código antigo ignora o novo campo. O risco aumenta quando a alteração exige preencher milhões de linhas, validar uma constraint imediatamente ou instalar um default que force reescrita física.

No PostgreSQL, versões modernas conseguem registrar alguns defaults constantes sem reescrever toda a tabela, mas a validação e a aquisição do lock ainda precisam ser observadas. Uma constraint pode ser criada como `NOT VALID`, validada em etapa separada e só depois usada como contrato para o código. Índices podem exigir construção concorrente.

No MySQL e no MariaDB, o algoritmo efetivo depende da versão, do engine e da operação. `INSTANT`, `INPLACE` e `COPY` possuem custos e bloqueios diferentes. Em topologias Galera, uma alteração pesada também se propaga e pode afetar a capacidade do cluster.

## Expand and contract

Uma migração compatível normalmente segue estas fases:

1. expandir o schema com estruturas opcionais;
2. publicar código que entende o schema antigo e o novo;
3. fazer backfill em lotes pequenos e retomáveis;
4. medir locks, latência, replica lag e erros;
5. validar os dados sem bloquear a aplicação;
6. mudar leituras e escritas para o novo campo;
7. remover o caminho antigo depois da janela de compatibilidade;
8. contrair o schema em uma operação separada.

Esse desenho evita exigir que o deploy do código e a migração terminem no mesmo instante. Também permite interromper o backfill sem deixar uma versão antiga incapaz de operar.

## Alternativas para alterações grandes

Quando o DDL nativo não oferece risco aceitável, podem ser usadas uma tabela sombra, uma cópia incremental, uma ferramenta de online schema change ou uma janela de manutenção. A escolha deve considerar volume, escrita concorrente, chaves estrangeiras, triggers, replicação e tempo de recuperação.

Antes de executar, confirme o plano no ambiente compatível, estime o volume, verifique espaço temporário, observe o timeout de lock e defina o procedimento de interrupção. Depois da mudança, valide contagem, constraints, índices, planos de consulta e comportamento das réplicas.

## Fontes

- [PostgreSQL, ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)
- [PostgreSQL, criação concorrente de índices](https://www.postgresql.org/docs/current/sql-createindex.html)
- [MySQL, online DDL](https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-operations.html)
- [MariaDB, ALTER TABLE](https://mariadb.com/kb/en/alter-table/)
