# Mapa de extensões e recursos práticos

Extensão só é útil quando reduz trabalho real, melhora uma consulta recorrente ou oferece um tipo de dado que o modelo precisa. Esta página prioriza recursos que aparecem em aplicações, análises e manutenção cotidiana. Módulos experimentais, exemplos internos e recursos exclusivos de uma distribuição ficam fora da trilha principal.

## PostgreSQL

No PostgreSQL, uma extensão instala funções, operadores, tipos, índices ou objetos relacionados no banco atual. O servidor precisa ter os arquivos da extensão instalados antes de executar `CREATE EXTENSION`.

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

Consulte o que está disponível no servidor:

```sql
SELECT name, default_version, installed_version, comment
FROM pg_available_extensions
ORDER BY name;
```

### Extensões que valem conhecer primeiro

| Extensão | Para que serve | Exemplos de uso |
| --- | --- | --- |
| `pgcrypto` | hash, criptografia e dados aleatórios | `gen_random_uuid`, `digest`, `crypt` em versões compatíveis |
| `pg_trgm` | similaridade e busca aproximada de texto | `similarity`, índice trigram, busca por nome |
| `unaccent` | remover acentos em buscas | comparação e pesquisa textual |
| `citext` | texto com comparação sem distinção de caixa | emails e identificadores textuais |
| `uuid-ossp` | geração de UUIDs por diferentes algoritmos | UUID v1, v3, v4 e v5 em versões compatíveis |
| `pg_stat_statements` | estatísticas de consultas | localizar consultas caras e repetidas |
| `postgres_fdw` | consultar outro PostgreSQL | integração entre bancos |
| `tablefunc` | funções tabulares e relatórios | `crosstab` e pivôs |
| `ltree` | hierarquias armazenadas como caminhos | categorias, árvores e ancestralidade |
| `hstore` | pares chave-valor legados | sistemas antigos e migrações |
| `btree_gin` | classes GIN com comportamento B-tree | índices compostos especializados |
| `btree_gist` | classes GiST para tipos comuns | restrições `EXCLUDE` e intervalos |
| `fuzzystrmatch` | comparação aproximada de strings | Levenshtein, Soundex e buscas tolerantes |

### Exemplos úteis

Busca aproximada com `pg_trgm`:

```sql
CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE INDEX users_name_trgm_idx
ON users USING gin (name gin_trgm_ops);

SELECT id, name, similarity(name, 'Gabrial') AS score
FROM users
WHERE name % 'Gabrial'
ORDER BY score DESC;
```

UUID v4 e hash com `pgcrypto` em instalações que ainda não possuem `uuidv4()` nativo:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;

SELECT gen_random_uuid();
SELECT encode(digest('texto', 'sha256'), 'hex');
```

Em PostgreSQL 18 ou posterior, `uuidv4()` e `uuidv7()` são funções nativas. O v7 é ordenável por tempo e deve ser considerado quando o índice primário recebe muitas inserções distribuídas. Em versões anteriores, gere o v7 na aplicação ou use uma biblioteca compatível.

Não use hash rápido como `digest` para armazenar senhas. Para autenticação, use uma biblioteca de senha apropriada, com salt e custo configurável.

### Extensões externas populares

Estas não vêm necessariamente com a instalação padrão e precisam ser avaliadas por versão, licença, manutenção e compatibilidade:

- PostGIS, para dados geográficos e espaciais;
- pgvector, para vetores e busca por similaridade;
- TimescaleDB, para séries temporais;
- HypoPG, para testar índices hipotéticos;
- pg_partman, para manutenção de particionamento;
- pg_cron, para tarefas agendadas dentro do PostgreSQL;
- Citus, para distribuição horizontal;
- Apache AGE, para grafos;
- `pg_repack`, para reorganização com menor indisponibilidade.

Uma extensão externa não deve entrar em um tutorial básico apenas porque é popular. Primeiro explique o problema que ela resolve, os custos operacionais e a alternativa usando o PostgreSQL puro.

## MySQL

MySQL não possui um catálogo de extensões equivalente ao `CREATE EXTENSION` do PostgreSQL. Seus pontos de expansão são plugins, componentes, funções carregáveis, mecanismos de armazenamento, parsers e recursos integrados ao servidor.

### Recursos integrados que são mais úteis

| Recurso | Para que serve |
| --- | --- |
| InnoDB | transações, chaves estrangeiras, locks e recuperação |
| JSON | documentos semiestruturados e funções JSON |
| `FULLTEXT` | busca textual em colunas indexadas |
| Spatial | tipos e funções geométricas |
| Performance Schema | instrumentação de desempenho |
| schema `sys` | views práticas para diagnóstico |
| generated columns | materializar expressões para consulta e índice |
| índices funcionais | indexar expressões, conforme versão e formato |
| eventos | tarefas agendadas no servidor |
| plugins de autenticação | métodos de login e integração externa |
| componentes de keyring | armazenamento de chaves criptográficas |

### Plugins e componentes que merecem uma página própria

- autenticação, incluindo o método padrão da instalação e alternativas compatíveis;
- validação de senhas;
- auditoria;
- firewall e controle de consultas;
- keyring e gestão de chaves;
- parser `ngram` para busca textual;
- replicação semissíncrona e Group Replication;
- componentes de log e observabilidade;
- funções carregáveis escritas externamente.

A disponibilidade desses recursos depende da versão, edição, sistema operacional e distribuição do MySQL. A instalação deve ser documentada junto com as consequências de segurança e manutenção, não como uma função SQL universal.

## Como escolher

Antes de adicionar uma extensão, responda:

1. O problema aparece em mais de uma consulta ou aplicação?
2. Uma tabela, índice ou função nativa resolveria com menos dependências?
3. A extensão tem suporte para a versão usada?
4. Ela funciona em backup, réplica, migração e restauração?
5. Quem poderá instalar, atualizar e remover o recurso?
6. Existe impacto de licença, memória, CPU, segurança ou portabilidade?

Para uma base de conhecimento ampla, as primeiras páginas devem privilegiar `pgcrypto`, `pg_trgm`, `unaccent`, `pg_stat_statements`, PostGIS, pgvector, JSON, `FULLTEXT`, Performance Schema e `EXPLAIN`. Esses recursos resolvem problemas que aparecem com frequência para quem desenvolve, analisa ou mantém aplicações.
