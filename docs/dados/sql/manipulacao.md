# SQL: manipulação de dados

Manipular dados significa inserir, alterar e remover linhas. Essas operações parecem simples, mas podem afetar milhares de registros. O hábito central é testar o predicado com `SELECT` antes de executar uma mutação e controlar a transação quando o banco permitir.

## Inserir com `INSERT`

Sempre informe a lista de colunas quando possível. Isso evita que uma mudança na ordem ou na estrutura da tabela altere silenciosamente o significado dos valores.

```sql
INSERT INTO users (name, email)
VALUES ('Ana Maria', 'ana@example.com');
```

Várias linhas podem ser inseridas na mesma instrução:

```sql
INSERT INTO users (name, email)
VALUES
    ('José da Silva', 'jose@example.com'),
    ('Gustavo Silva', 'gustavo@example.com');
```

Colunas omitidas recebem `DEFAULT` ou `NULL`, se a definição permitir. Colunas `NOT NULL` sem valor padrão precisam ser preenchidas.

Datas, horários e textos usam literais apropriados ao dialeto. Números não precisam de aspas:

```sql
INSERT INTO orders (user_id, status, total)
VALUES (1, 'pending', 920.00);
```

Não use `INSERT INTO tabela VALUES (...)` em código de longa duração sem uma razão forte. A forma sem lista depende da ordem física da definição e é frágil durante migrações.

## Atualizar com `UPDATE`

`UPDATE` altera todas as linhas que satisfazem o `WHERE`. Sem `WHERE`, a alteração atinge a tabela inteira.

```sql
UPDATE orders
SET status = 'paid'
WHERE id = 42;
```

Antes da mutação, confira o conjunto:

```sql
SELECT id, status
FROM orders
WHERE status = 'pending'
  AND created_at < CURRENT_TIMESTAMP - INTERVAL '7 days';
```

A sintaxe de intervalos varia entre bancos. Em qualquer dialeto, a ideia é a mesma: validar o predicado e o número de linhas antes do `UPDATE`.

Uma atualização pode usar valores de outras colunas:

```sql
UPDATE products
SET price = price * 1.10
WHERE active = true;
```

Use uma transação quando a operação precisar ser revisada antes de ser confirmada.

## Remover com `DELETE`

```sql
DELETE FROM users
WHERE id = 42;
```

O `DELETE` pode falhar ou produzir efeitos em cascata quando existem chaves estrangeiras. O comportamento é definido pelas ações `ON DELETE`, como `RESTRICT`, `CASCADE`, `SET NULL` ou `SET DEFAULT`. Escolha a ação conforme o significado do relacionamento, não apenas para fazer o comando passar.

Para remover todas as linhas, `DELETE FROM tabela` respeita triggers e pode gerar uma operação por linha. `TRUNCATE` é uma operação de DDL ou de manutenção específica do banco, costuma ser mais rápida e pode ter regras diferentes para transações, identidade e dependências.

## Transações

Uma transação reúne operações que devem ser confirmadas ou desfeitas como uma unidade.

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;

COMMIT;
```

Se uma verificação falhar:

```sql
ROLLBACK;
```

Uma transferência não deve confirmar o débito sem o crédito. Isso é um caso clássico de atomicidade. [Transações de banco de dados](../modos-de-transacao.md) e [ACID](../transacoes-acid.md) aprofundam isolamento, durabilidade e concorrência.

## Savepoints

Savepoints permitem desfazer parte de uma transação sem abandonar tudo:

```sql
BEGIN;

UPDATE products
SET price = price * 0.95
WHERE active = true;

SAVEPOINT after_discount;

DELETE FROM products
WHERE active = false;

ROLLBACK TO SAVEPOINT after_discount;
COMMIT;
```

O savepoint não torna uma operação segura por si só. A transação ainda precisa ser pequena o bastante para não prender locks e recursos por tempo excessivo.

## Padrão de pré-visualização

Para uma mutação complexa, escreva primeiro um `SELECT` com as mesmas tabelas e predicados:

```sql
SELECT id, status
FROM orders
WHERE status = 'pending'
  AND total = 0;
```

Depois, transforme apenas a projeção em uma mutação:

```sql
UPDATE orders
SET status = 'cancelled'
WHERE status = 'pending'
  AND total = 0;
```

Em ambientes de produção, combine isso com limite de lote, logs, métricas, backup e uma estratégia de reversão. Um `WHERE` correto não impede que uma regra de negócio equivocada altere o conjunto errado.

## Inserir ou atualizar

O padrão de UPSERT depende do banco. PostgreSQL usa `ON CONFLICT`; MySQL possui `ON DUPLICATE KEY UPDATE`; alguns sistemas usam `MERGE`.

```sql
INSERT INTO users (email, name)
VALUES ('ana@example.com', 'Ana')
ON CONFLICT (email)
DO UPDATE SET name = EXCLUDED.name;
```

Essa operação precisa de uma chave ou restrição que defina o conflito. Sem uma identidade única, “atualizar se existir” fica ambíguo.

## DML e concorrência

Duas transações podem tentar alterar a mesma linha. O resultado depende do isolamento, dos locks, da ordem e do banco. Não esconda conflitos com retries infinitos: entenda se a operação é idempotente, se pode ser repetida e qual leitura deve ser protegida.

## Checklist antes de uma mutação

- execute o `SELECT` equivalente;
- confira o número e alguns exemplos de linhas;
- confirme o `WHERE` e as chaves de relacionamento;
- use transação quando houver mais de uma etapa;
- defina como detectar e desfazer um resultado incorreto;
- registre a mudança e observe duração, locks e número de linhas afetadas.
