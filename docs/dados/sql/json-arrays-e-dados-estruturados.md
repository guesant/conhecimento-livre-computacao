# Dados estruturados em SQL

Dados estruturados em JSON ou arrays são úteis quando a forma varia, quando a aplicação recebe documentos externos ou quando um atributo opcional precisa evoluir sem uma migração imediata. Eles não devem substituir uma tabela relacional quando os dados possuem identidade, relacionamentos, restrições e consultas frequentes.

## JSON no PostgreSQL

PostgreSQL diferencia `json`, que preserva o texto, e `jsonb`, que armazena uma representação binária indexável:

```sql
CREATE TABLE events (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    payload jsonb NOT NULL
);
```

Operadores básicos:

```sql
SELECT
    payload->>'kind' AS kind,
    payload->'user'->>'email' AS email
FROM events
WHERE payload->>'kind' = 'signup';
```

`->` mantém JSON; `->>` extrai texto. Para filtrar uma estrutura:

```sql
SELECT *
FROM events
WHERE payload @> '{"kind": "signup"}';
```

Um índice GIN pode ajudar em consultas de contenção:

```sql
CREATE INDEX events_payload_gin
ON events USING gin (payload);
```

Também é possível criar um índice sobre uma expressão específica:

```sql
CREATE INDEX events_kind_idx
ON events ((payload->>'kind'));
```

## JSON no MySQL

MySQL oferece funções como `JSON_EXTRACT`, `JSON_VALUE`, `JSON_OBJECT` e `JSON_TABLE`:

```sql
SELECT JSON_VALUE(payload, '$.user.email') AS email
FROM events
WHERE JSON_VALUE(payload, '$.kind') = 'signup';
```

`JSON_TABLE` pode transformar elementos de um documento em linhas relacionais. A sintaxe de caminhos, operadores, índices e valores ausentes varia; marque o dialeto no código.

## Expandir documentos em linhas

No PostgreSQL, `jsonb_array_elements` expande uma lista:

```sql
SELECT
    event_id,
    item->>'sku' AS sku
FROM order_events
CROSS JOIN LATERAL jsonb_array_elements(payload->'items') AS item;
```

Esse padrão combina JSON com `LATERAL`. Se a lista for a parte principal do domínio, uma tabela relacionada costuma oferecer melhor integridade e consulta.

## Arrays no PostgreSQL

```sql
CREATE TABLE articles (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title text NOT NULL,
    tags text[] NOT NULL DEFAULT '{}'
);
```

Consultar pertencimento:

```sql
SELECT *
FROM articles
WHERE 'sql' = ANY(tags);
```

Expandir valores:

```sql
SELECT id, unnest(tags) AS tag
FROM articles;
```

Agregar valores:

```sql
SELECT user_id, array_agg(role ORDER BY role)
FROM user_roles
GROUP BY user_id;
```

Arrays são convenientes para valores pequenos e dependentes da linha. Para consultar, autorizar ou relacionar cada elemento individualmente, uma tabela de associação costuma ser mais clara.

## Dados estruturados e normalização

Perguntas que indicam uma tabela própria:

- o elemento tem identidade independente;
- existe uma relação com outra entidade;
- precisa de `FOREIGN KEY`, `UNIQUE` ou `CHECK` próprio;
- será filtrado ou ordenado com frequência;
- possui ciclo de vida ou permissões próprias;
- pode crescer sem limite previsível.

JSON e arrays são bons para extensões, payloads de integração, configurações e eventos. Eles dificultam integridade, descoberta de schema e otimização quando passam a carregar o núcleo do modelo.

## Atualização e concorrência

Atualizar um campo dentro de um documento pode substituir o valor inteiro, dependendo da função utilizada. Defina se a operação deve ser merge, substituição ou remoção de uma chave. Para concorrência, proteja a versão do documento ou use uma condição que detecte uma alteração intermediária.

## Segurança

Não trate JSON como uma forma de esconder segredo. Logs, índices, backups e consultas de diagnóstico podem expor os mesmos valores. Valide tamanho, profundidade e tipos de documentos recebidos, e não concatene caminhos ou expressões a partir de entrada não confiável.
