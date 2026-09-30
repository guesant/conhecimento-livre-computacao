# Performance SQL

SQL rápido não é uma coleção de índices aplicados por intuição. É o resultado de uma pergunta bem definida, um modelo coerente, estatísticas confiáveis, um plano adequado e medição no volume real.

## Medir antes de otimizar

Registre a consulta, parâmetros, duração, número de linhas retornadas e contexto de concorrência. Uma consulta rápida para dez linhas pode ser inadequada para dez milhões. Uma consulta rápida em cache pode esconder um problema de I/O.

## `EXPLAIN`

```sql
EXPLAIN
SELECT id, name
FROM users
WHERE email = 'ana@example.com';
```

O plano pode mostrar:

- varredura sequencial ou por índice;
- estimativa e quantidade real de linhas;
- filtros aplicados em cada etapa;
- `Nested Loop`, `Hash Join` ou `Merge Join`;
- custo estimado, memória e ordenações.

PostgreSQL:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT id, name
FROM users
WHERE email = 'ana@example.com';
```

`ANALYZE` executa a consulta. Nunca use essa opção em uma mutação sem entender seus efeitos. MySQL possui `EXPLAIN` e formatos adicionais, mas a nomenclatura e as colunas diferem.

## Índices

Um índice ajuda quando reduz o trabalho necessário para encontrar ou ordenar as linhas. Ele também ocupa espaço e torna escritas mais caras.

```sql
CREATE INDEX orders_user_created_idx
ON orders (user_id, created_at DESC);
```

A ordem das colunas importa. Um índice em `(user_id, created_at)` ajuda diretamente consultas que começam por `user_id`; não é equivalente a dois índices independentes em todas as situações.

## Índices parciais e funcionais

PostgreSQL pode indexar apenas uma parte das linhas:

```sql
CREATE INDEX orders_pending_idx
ON orders (created_at)
WHERE status = 'pending';
```

Também pode indexar uma expressão:

```sql
CREATE INDEX users_lower_email_idx
ON users (LOWER(email));
```

A consulta precisa usar uma expressão compatível para aproveitar o índice. Outros bancos oferecem recursos equivalentes com sintaxe própria.

## Cardinalidade e estatísticas

O otimizador estima quantas linhas cada filtro produzirá. Estimativas ruins podem escolher um join ou índice inadequado. Causas comuns incluem estatísticas antigas, correlação entre colunas, distribuição muito desigual e predicados que o banco não consegue estimar.

Atualize estatísticas conforme o banco e investigue a diferença entre linhas estimadas e reais. Não transforme cada diferença em um índice: descubra primeiro se a consulta, o modelo ou a estatística está errada.

## Sargabilidade

Um predicado sargável permite que o banco use uma estrutura de busca:

```sql
WHERE created_at >= TIMESTAMP '2025-01-01'
```

Aplicar uma função à coluna pode impedir um índice comum:

```sql
WHERE DATE(created_at) = DATE '2025-01-01'
```

Uma alternativa é usar um intervalo:

```sql
WHERE created_at >= TIMESTAMP '2025-01-01'
  AND created_at < TIMESTAMP '2025-01-02'
```

Isso não significa que toda função na coluna seja errada. Um índice funcional ou uma coluna gerada pode ser a solução quando a transformação for parte recorrente do contrato.

## Joins e cardinalidade

Antes de adicionar `DISTINCT`, descubra se um join está multiplicando linhas. Relacione a cardinalidade esperada:

- um para um;
- um para muitos;
- muitos para muitos;
- relação opcional ou obrigatória.

Um join muitos-para-muitos sem uma agregação pode multiplicar resultados legitimamente. Se a tela espera uma linha por usuário, agregue pedidos antes ou use uma janela para escolher uma linha.

## Paginação

`OFFSET` fica mais caro à medida que a página avança porque o banco precisa localizar e descartar linhas anteriores. Keyset pagination usa a última chave observada:

```sql
SELECT id, created_at, name
FROM users
WHERE (created_at, id) < (TIMESTAMP '2025-01-01 10:00:00', 100)
ORDER BY created_at DESC, id DESC
LIMIT 50;
```

O índice e a ordenação precisam acompanhar a chave usada. A comparação de tuplas tem variações entre bancos.

## N+1 queries

Uma aplicação pode buscar uma lista e então executar uma consulta adicional para cada linha. Isso produz N+1 consultas e latência proporcional ao número de itens. Prefira joins, agregações, pré-carregamento ou uma consulta em lote quando a relação e o volume permitirem.

## Custo de índices

Um índice pode piorar escrita, vacuum, backup e espaço. Índices redundantes, índices pouco seletivos e índices em colunas que quase nunca são filtradas devem ser medidos antes de permanecerem.

## Plano não é contrato eterno

O plano pode mudar com estatísticas, volume, parâmetros, versão do banco e distribuição dos dados. Acompanhe consultas importantes com métricas, planos periódicos e testes representativos. Otimização sem medição transforma uma hipótese em configuração permanente.
