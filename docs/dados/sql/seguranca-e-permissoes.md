# Segurança SQL

Segurança de banco combina autenticação, autorização, isolamento, validação de entrada, proteção de segredos, auditoria e recuperação. Uma consulta correta pode ser insegura se qualquer usuário puder executá-la sobre qualquer tabela.

## Parâmetros preparados

Nunca concatene entrada do usuário em SQL:

```text
SELECT * FROM users WHERE email = '" + input + "'
```

Use parâmetros do driver ou da biblioteca:

```sql
SELECT id, name
FROM users
WHERE email = :email;
```

O marcador depende da biblioteca, mas a regra é universal: código SQL e valores devem ser enviados separadamente. Identificadores como nomes de tabela ou coluna não podem ser tratados como valores; quando precisarem ser dinâmicos, use uma lista permitida pelo código.

## Menor privilégio

Uma aplicação de leitura não precisa de `DROP TABLE`. Crie papéis conforme a responsabilidade:

```sql
GRANT SELECT ON users TO reporting_reader;
GRANT SELECT ON orders TO reporting_reader;

REVOKE INSERT, UPDATE, DELETE ON users FROM reporting_reader;
```

O nome, sintaxe e herança de roles variam. Revise privilégios sobre banco, schema, tabela, coluna, sequência, função e view. Não confunda o usuário usado pela migração com o usuário usado pela aplicação.

## Views como fronteira

Uma view pode expor somente as colunas necessárias:

```sql
CREATE VIEW public_user_directory AS
SELECT id, name
FROM users
WHERE active = true;

GRANT SELECT ON public_user_directory TO directory_reader;
```

Remover uma coluna da view não protege dados se o papel ainda possuir acesso direto à tabela. A view precisa fazer parte de um desenho de privilégios coerente.

## Row-Level Security

PostgreSQL oferece Row-Level Security para filtrar linhas conforme a identidade da sessão:

```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY own_orders
ON orders
USING (user_id = current_setting('app.user_id')::bigint);
```

Esse exemplo é apenas um modelo. A forma de definir a identidade de sessão, a possibilidade de bypass por administradores e a separação entre `USING` e `WITH CHECK` precisam ser desenhadas e testadas. Uma política incorreta pode vazar dados ou bloquear operações legítimas.

## Segredos

Não coloque senhas em consultas, arquivos versionados, logs ou mensagens de erro. Use secret managers, variáveis protegidas e rotação. Lembre que backups, réplicas, WAL, slow query logs e ferramentas de diagnóstico podem conter dados sensíveis.

## Funções e SQL dinâmico

SQL dinâmico dentro de uma procedure precisa separar identificadores e valores. Use as APIs de quoting do banco ou listas fechadas, nunca concatenação de entrada bruta. Funções com privilégios elevados aumentam o impacto de uma falha e exigem revisão específica.

## Auditoria

Registre autenticações, concessões de privilégios, alterações de schema, acessos administrativos e mutações sensíveis. Logs devem incluir quem, quando, de onde, qual objeto e qual resultado, sem registrar segredos ou dados pessoais além do necessário.

## Backup não é autorização

Um backup pode permitir recuperação e também ampliar o impacto de um vazamento. Cifre, restrinja, teste restauração e defina retenção. O papel que consulta produção não precisa necessariamente ler o backup bruto.

## Testes de segurança

Inclua casos de:

- tentativa de injeção em strings, filtros e ordenação;
- acesso de um papel de leitura a uma tabela administrativa;
- usuário tentando consultar a linha de outro usuário;
- mutação sem permissão;
- função com parâmetros inesperados;
- logs e mensagens que expõem valores sensíveis.

Segurança no banco é uma propriedade verificável por políticas, testes, auditoria e recuperação, não apenas uma promessa da aplicação.
